#!/usr/bin/env python3
"""
从 DBLP 取一位研究者的全部发表记录（研究Skill · 全文深读 T3.1 发表列表的交叉核对来源）。

dblp.org 的 search / pid REST API 挂在 Anubis 反爬墙后面，脚本拿不到；这里改用 DBLP 官方 SPARQL 端点
https://sparql.dblp.org/sparql（POST query=…，Accept: application/sparql-results+json，curl 式 User-Agent）。
只用标准库 urllib；走环境里的 HTTPS 代理。

两步:
    1. 找人：--name "<姓名>"（或 --scholar <Google Scholar 用户ID> / --orcid <ORCID>）列出候选 DBLP 人物，
       带别名、单位、备注、ORCID、主页、记录数与年份范围、常发 venue、常合作者，供人工选定 pid。
       --name 按姓（最后一个词，整词匹配）+ 名的首字母在全部署名变体里找；与输入完全同名的排在前面。
    2. 取记录：--pid <pid>（如 12/3456，也接受 https://dblp.org/pid/12/3456.html）写出 JSON。

JSON 格式（--pid）:
    {"endpoint": "...", "fetched": "YYYY-MM-DD", "pid": "12/3456", "name": "...", "aliases": [...],
     "orcid": "...", "count": N,
     "records": [{"key": "journals/<venue>/<Key>", "url": "https://dblp.org/rec/journals/<venue>/<Key>",
                  "title": "...（去掉末尾句点）", "year": 2019, "venue": "<DBLP 简称>", "volume": "79",
                  "number": "2", "pages": "397-414", "types": ["Article"], "bibtex": "Article",
                  "role": "author"|"editor", "authors": ["<按署名顺序>", ...], "author_pids": ["12/3456", ...],
                  "editors": [...], "dois": ["10.xxxx/..."], "ee": ["https://doi.org/..."],
                  "arxiv": "1911.01234" 或 null, "isbn": [...]}, ...]}
    types 取 DBLP 类型：Article、Inproceedings、Informal（CoRR 预印本等）、Book、Incollection、Editorship、Reference…；
    arxiv 来自 ee 里的 arxiv.org/abs 链接、CoRR 的 "abs/…" 卷号或 10.48550/arXiv.… DOI。
    记录按 (year, title) 排序。发表列表的合并（与 Scholar 行对齐、补 DOI/arXiv）由 harvest 步骤完成。

用法:
    python3 dblp_works.py --name "<名 姓>" [--limit 15] [--json]
    python3 dblp_works.py --scholar <Google Scholar 用户ID 或 citations?user=… 链接>
    python3 dblp_works.py --orcid <0000-0000-0000-0000>
    python3 dblp_works.py --pid <pid> [--out FILE]      # 例如 team.json 里成员的 "dblp" 字段

输出:
    找人：每个候选一段（pid、姓名与别名、单位、记录数/年份、venue、合作者、下一步命令）；--json 输出候选列表。
    取记录：--out 写文件（否则 JSON 打到标准输出，汇总行打到标准错误）。
    最后一行汇总：✅/❌ …；没找到人、端点出错（会打印 HTTP 状态与端点的错误信息）时退出码为 1。
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ENDPOINT = "https://sparql.dblp.org/sparql"
HEADERS = {"Accept": "application/sparql-results+json", "User-Agent": "curl/8.5.0"}
PREFIX = ("PREFIX dblp: <https://dblp.org/rdf/schema#>\n"
          "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n")
PID_URI = "https://dblp.org/pid/"
REC_URI = "https://dblp.org/rec/"
RECORD_PREDICATES = [
    "rdf:type", "dblp:title", "dblp:yearOfPublication", "dblp:publishedIn", "dblp:publishedInJournal",
    "dblp:publishedInJournalVolume", "dblp:publishedInJournalVolumeIssue", "dblp:publishedInBook",
    "dblp:publishedInSeries", "dblp:publishedInSeriesVolume", "dblp:pagination", "dblp:doi",
    "dblp:documentPage", "dblp:primaryDocumentPage", "dblp:bibtexType", "dblp:isbn",
]
PERSON_PREDICATES = [
    "dblp:primaryCreatorName", "dblp:creatorName", "dblp:primaryAffiliation", "dblp:affiliation", "dblp:note",
    "dblp:orcid", "dblp:primaryHomepage", "dblp:homepage", "dblp:webpage", "dblp:wikipedia",
]
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/([a-z\-]+(?:\.[A-Z]{2})?/\d{7}|\d{4}\.\d{4,5})(?:v\d+)?", re.I)


class SparqlError(Exception):
    pass


def sparql(query: str, timeout: int = 180, tries: int = 3) -> list[dict]:
    """POST 查询，返回 bindings（每行 {变量: 值字符串}）。"""
    data = urllib.parse.urlencode({"query": PREFIX + query}).encode()
    req = urllib.request.Request(ENDPOINT, data=data, headers=HEADERS, method="POST")
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                body = json.loads(r.read().decode("utf-8"))
            return [{k: v.get("value", "") for k, v in b.items()} for b in body["results"]["bindings"]]
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")
            try:
                detail = json.loads(detail).get("exception") or detail
            except json.JSONDecodeError:
                m = re.search(r"<title>(.*?)</title>", detail, re.S | re.I)  # HTML 错误页只留标题
                detail = m.group(1) if m else re.sub(r"<[^>]+>", " ", detail)
            detail = re.sub(r"\s+", " ", str(detail)).strip()
            if e.code in (429, 500, 502, 503, 504) and attempt < tries - 1:
                time.sleep(10 * (attempt + 1))
                continue
            raise SparqlError(f"HTTP {e.code} from {ENDPOINT}: {str(detail)[:500]}") from None
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            if attempt < tries - 1:
                time.sleep(5 * (attempt + 1))
                continue
            raise SparqlError(f"cannot reach {ENDPOINT}: {e}") from None
        except (json.JSONDecodeError, KeyError) as e:
            raise SparqlError(f"unexpected response from {ENDPOINT}: {e}") from None
    return []


def lit(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def pid_of(s: str) -> str:
    """12/3456、https://dblp.org/pid/12/3456.html、dblp.org/pid/12/3456 → 12/3456。"""
    s = s.strip()
    m = re.search(r"pid/(.+?)(?:\.html|\.xml|\.rdf|\.nt|\.ttl)?/?$", s)
    return m.group(1) if m else s.strip("/")


def short(uri: str, base: str) -> str:
    return uri[len(base):] if uri.startswith(base) else uri


def local(uri: str) -> str:
    return re.split(r"[#/]", uri)[-1]


def fold(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).casefold()


def clean_name(name: str) -> str:
    return re.sub(r"\s+\d{4}$", "", name)  # DBLP 同名消歧后缀 "Wei Wang 0001"


def values(pids: list[str]) -> str:
    return "VALUES ?p { " + " ".join(f"<{PID_URI}{p}>" for p in pids) + " }"


# ---------- 找人 ----------

def find_by_name(name: str) -> tuple[list[str], set[str]]:
    """→ (候选 pid, 其中与输入完全同名的 pid)。"""
    tokens = [t for t in re.split(r"[\s\-]+", name.strip()) if t.strip(".")]
    if not tokens:
        return [], set()
    surname = tokens[-1].strip(".").lower()
    initial = tokens[0][0].lower() if len(tokens) > 1 else ""
    flt = f"CONTAINS(LCASE(?n), {lit(surname)})"
    if initial:
        flt += f" && STRSTARTS(LCASE(?n), {lit(initial)})"
    rows = sparql(f"SELECT DISTINCT ?p ?n WHERE {{ ?p dblp:creatorName ?n . FILTER({flt}) }} LIMIT 2000")
    word = re.compile(r"(?<!\w)" + re.escape(fold(surname)) + r"(?!\w)")
    target = fold(re.sub(r"\s+", " ", name.strip()))
    whole: dict[str, bool] = {}
    loose: set[str] = set()
    for r in rows:
        pid = short(r["p"], PID_URI)
        n = fold(clean_name(r["n"]))
        if word.search(n):
            whole[pid] = whole.get(pid, False) or n == target
        else:
            loose.add(pid)
    if whole:  # 整词匹配到了就不要子串匹配（Lee ≠ Leeds）
        return sorted(whole), {p for p, exact in whole.items() if exact}
    return sorted(loose), set()


def find_by_scholar(user: str) -> list[str]:
    m = re.search(r"user=([\w-]+)", user)
    user = m.group(1) if m else user.strip()
    rows = sparql(f"SELECT DISTINCT ?p WHERE {{ ?p dblp:webpage ?w . FILTER(CONTAINS(STR(?w), {lit('user=' + user)})) }}")
    return [short(r["p"], PID_URI) for r in rows]


def find_by_orcid(orcid: str) -> list[str]:
    m = re.search(r"\d{4}-\d{4}-\d{4}-\d{3}[\dX]", orcid)
    if not m:
        raise SparqlError(f"not an ORCID: {orcid}")
    rows = sparql(f"SELECT DISTINCT ?p WHERE {{ ?p dblp:orcid <https://orcid.org/{m.group(0)}> }}")
    return [short(r["p"], PID_URI) for r in rows]


def person_info(pids: list[str]) -> dict[str, dict]:
    info = {p: collections.defaultdict(list) for p in pids}
    for part in range(0, len(pids), 100):
        chunk = pids[part:part + 100]
        rows = sparql(f"SELECT ?p ?pr ?o WHERE {{ {values(chunk)} ?p ?pr ?o . "
                      f"VALUES ?pr {{ {' '.join(PERSON_PREDICATES)} }} }}")
        for r in rows:
            vals = info[short(r["p"], PID_URI)][local(r["pr"])]
            if r["o"] not in vals:
                vals.append(r["o"])
    return info


def person_stats(pids: list[str]) -> dict[str, dict]:
    stats: dict[str, dict] = {p: {"records": 0, "first": None, "last": None, "venues": [], "coauthors": []} for p in pids}
    rows = []
    for part in range(0, len(pids), 100):
        rows += sparql(f"SELECT ?p (COUNT(DISTINCT ?pub) AS ?n) (MIN(?y) AS ?y0) (MAX(?y) AS ?y1) WHERE {{ "
                       f"{values(pids[part:part + 100])} ?pub dblp:createdBy ?p . "
                       f"OPTIONAL {{ ?pub dblp:yearOfPublication ?y }} }} GROUP BY ?p")
    for r in rows:
        s = stats[short(r["p"], PID_URI)]
        s["records"] = int(r.get("n") or 0)
        s["first"], s["last"] = r.get("y0"), r.get("y1")
    return stats


def person_context(pids: list[str], stats: dict[str, dict], top: int = 3) -> None:
    """常发 venue 与常合作者（区分同名的人最有用）。"""
    rows = sparql(f"SELECT ?p ?v (COUNT(DISTINCT ?pub) AS ?c) WHERE {{ {values(pids)} "
                  f"?pub dblp:createdBy ?p ; dblp:publishedIn ?v }} GROUP BY ?p ?v")
    by = collections.defaultdict(list)
    for r in rows:
        by[short(r["p"], PID_URI)].append((int(r["c"]), r["v"]))
    for p, lst in by.items():
        stats[p]["venues"] = [f"{v} ({c})" for c, v in sorted(lst, key=lambda x: (-x[0], x[1]))[:top]]
    rows = sparql(f"SELECT ?p ?qn (COUNT(DISTINCT ?pub) AS ?c) WHERE {{ {values(pids)} "
                  f"?pub dblp:authoredBy ?p , ?q . FILTER(?q != ?p) ?q dblp:primaryCreatorName ?qn }} GROUP BY ?p ?qn")
    by = collections.defaultdict(list)
    for r in rows:
        by[short(r["p"], PID_URI)].append((int(r["c"]), clean_name(r["qn"])))
    for p, lst in by.items():
        stats[p]["coauthors"] = [f"{n} ({c})" for c, n in sorted(lst, key=lambda x: (-x[0], x[1]))[:top]]


def candidates(pids: list[str], exact: set[str], limit: int) -> list[dict]:
    if not pids:
        return []
    stats = person_stats(pids)
    shown = sorted(pids, key=lambda p: (p not in exact, -stats[p]["records"], p))[:limit]  # 完全同名在前，再按记录数
    info = person_info(shown)
    person_context(shown, stats)
    out = []
    for p in shown:
        i, s = info[p], stats[p]
        name = clean_name((i.get("primaryCreatorName") or [p])[0])
        out.append({
            "pid": p, "name": name,
            "aliases": sorted({clean_name(n) for n in i.get("creatorName", [])} - {name}),
            "affiliation": list(dict.fromkeys(i.get("primaryAffiliation", []) + i.get("affiliation", []))),
            "note": i.get("note", []), "orcid": [short(o, "https://orcid.org/") for o in i.get("orcid", [])],
            "homepage": list(dict.fromkeys(i.get("primaryHomepage", []) + i.get("homepage", []))),
            "webpage": i.get("webpage", []) + i.get("wikipedia", []),
            **s,
        })
    return out


def print_candidates(cands: list[dict], total: int) -> None:
    for k, c in enumerate(cands, 1):
        years = f"{c['first']}–{c['last']}" if c["first"] else "no years"
        print(f"{k}. {c['pid']}  {c['name']}  · {c['records']} records, {years}  (https://dblp.org/pid/{c['pid']}.html)")
        for label, key in (("aliases", "aliases"), ("affiliation", "affiliation"), ("note", "note"),
                           ("orcid", "orcid"), ("homepage", "homepage"), ("webpages", "webpage"),
                           ("venues", "venues"), ("coauthors", "coauthors")):
            if c.get(key):
                print(f"     {label}: " + "; ".join(c[key][:6]) + (" …" if len(c[key]) > 6 else ""))
    if total > len(cands):
        print(f"   … {total - len(cands)} more candidates (raise --limit to see them)")
    if cands:
        print("next: python3 scripts/dblp_works.py --pid <the matching pid, e.g. "
              f"{cands[0]['pid']}> --out dblp.json   (check affiliation, venues, coauthors against the person)")


# ---------- 取记录 ----------

def fetch_records(pid: str) -> list[dict]:
    uri = f"<{PID_URI}{pid}>"
    rows = sparql(f"SELECT ?pub ?p ?o WHERE {{ ?pub dblp:createdBy {uri} . ?pub ?p ?o . "
                  f"VALUES ?p {{ {' '.join(RECORD_PREDICATES)} }} }}")
    recs: dict[str, dict[str, list[str]]] = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in rows:
        vals = recs[r["pub"]][local(r["p"])]
        if r["o"] not in vals:
            vals.append(r["o"])
    sigs = sparql(f"SELECT ?pub ?kind ?ord ?name ?creator WHERE {{ ?pub dblp:createdBy {uri} ; dblp:hasSignature ?sig . "
                  f"?sig dblp:signatureOrdinal ?ord ; dblp:signatureDblpName ?name ; rdf:type ?kind . "
                  f"OPTIONAL {{ ?sig dblp:signatureCreator ?creator }} "
                  f"FILTER(?kind IN (dblp:AuthorSignature, dblp:EditorSignature)) }}")
    people: dict[str, dict[str, list]] = collections.defaultdict(lambda: {"author": [], "editor": []})
    for s in sigs:
        role = "editor" if s["kind"].endswith("EditorSignature") else "author"
        people[s["pub"]][role].append((int(s["ord"]), clean_name(s["name"]), short(s.get("creator", ""), PID_URI)))

    out = []
    for key, r in recs.items():
        first = lambda k: (r.get(k) or [None])[0]  # noqa: E731
        types = [local(t) for t in r.get("type", []) if local(t) != "Publication"]
        authors = sorted(set(people[key]["author"]))
        editors = sorted(set(people[key]["editor"]))
        ee = list(dict.fromkeys(r.get("primaryDocumentPage", []) + r.get("documentPage", [])))
        dois = sorted({re.sub(r"^https?://(dx\.)?doi\.org/", "", d) for d in r.get("doi", [])})
        volume = first("publishedInJournalVolume") or first("publishedInSeriesVolume")
        arxiv = None
        for u in ee:
            m = ARXIV_RE.search(u)
            if m:
                arxiv = m.group(1)
                break
        if not arxiv and first("publishedInJournal") == "CoRR" and volume and volume.startswith("abs/"):
            arxiv = volume[4:]
        if not arxiv:
            arxiv = next((d.split("arXiv.", 1)[1] for d in dois if d.lower().startswith("10.48550/arxiv.")), None)
        title = first("title") or ""
        year = first("yearOfPublication")
        out.append({
            "key": short(key, REC_URI), "url": key,
            "title": title[:-1] if title.endswith(".") else title,
            "year": int(year) if year and year.isdigit() else None,
            "venue": (first("publishedIn") or first("publishedInJournal") or first("publishedInBook")
                      or first("publishedInSeries")),
            "volume": volume, "number": first("publishedInJournalVolumeIssue"), "pages": first("pagination"),
            "types": types, "bibtex": local(first("bibtexType") or "") or None,
            "role": "editor" if pid in {e[2] for e in editors} and pid not in {a[2] for a in authors} else "author",
            "authors": [a[1] for a in authors], "author_pids": [a[2] for a in authors],
            "editors": [e[1] for e in editors],
            "dois": dois, "ee": ee, "arxiv": arxiv,
            "isbn": [re.sub(r"^urn:isbn:", "", i) for i in r.get("isbn", [])],
        })
    out.sort(key=lambda x: (x["year"] or 0, x["title"].lower()))
    return out


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--name", help="按姓名找候选人物（姓整词匹配 + 名的首字母）")
    g.add_argument("--scholar", help="按 Google Scholar 用户ID找人（DBLP 人物页登记的 Scholar 链接）")
    g.add_argument("--orcid", help="按 ORCID 找人")
    g.add_argument("--pid", help="取这个 DBLP pid 的全部记录（如 12/3456）")
    ap.add_argument("--out", default="", help="--pid 时写到这个 JSON 文件（默认打到标准输出）")
    ap.add_argument("--limit", type=int, default=15, help="找人时最多详细列出几个候选（默认15）")
    ap.add_argument("--json", action="store_true", help="找人时输出 JSON")
    a = ap.parse_args()

    try:
        if a.pid:
            pid = pid_of(a.pid)
            if not re.fullmatch(r"[A-Za-z0-9_\-]+(?:/[A-Za-z0-9_\-]+)*", pid):
                print(f"❌ not a DBLP pid: {a.pid} (expected something like 12/3456)")
                sys.exit(1)
            info = person_info([pid])[pid]
            name = clean_name((info.get("primaryCreatorName") or [""])[0])
            if not name:
                print(f"❌ no DBLP person with pid {pid} ({PID_URI}{pid})")
                sys.exit(1)
            recs = fetch_records(pid)
            doc = {
                "endpoint": ENDPOINT, "fetched": dt.date.today().isoformat(), "pid": pid, "name": name,
                "aliases": sorted({clean_name(n) for n in info.get("creatorName", [])} - {name}),
                "orcid": [short(o, "https://orcid.org/") for o in info.get("orcid", [])],
                "count": len(recs), "records": recs,
            }
            text = json.dumps(doc, ensure_ascii=False, indent=1)
            types = collections.Counter(t for r in recs for t in (r["types"] or ["?"]))
            years = [r["year"] for r in recs if r["year"]]
            summary = (f"✅ {pid} {name}: {len(recs)} records"
                       + (f", {min(years)}–{max(years)}" if years else "")
                       + f" ({', '.join(f'{t} {n}' for t, n in types.most_common())})"
                       + f" · DOI {sum(1 for r in recs if r['dois'])} · arXiv {sum(1 for r in recs if r['arxiv'])}"
                       + f" · as editor {sum(1 for r in recs if r['role'] == 'editor')}")
            if a.out:
                Path(a.out).parent.mkdir(parents=True, exist_ok=True)
                Path(a.out).write_text(text + "\n", encoding="utf-8")
                print(summary + f" → {a.out}")
            else:
                print(text)
                print(summary, file=sys.stderr)
            return

        exact: set[str] = set()
        if a.name:
            (pids, exact), what = find_by_name(a.name), f'name "{a.name}"'
        elif a.scholar:
            pids, what = find_by_scholar(a.scholar), f"Google Scholar user {a.scholar}"
        else:
            pids, what = find_by_orcid(a.orcid), f"ORCID {a.orcid}"
        cands = candidates(pids, exact, a.limit)
        if a.json:
            print(json.dumps({"query": what, "total": len(pids), "candidates": cands}, ensure_ascii=False, indent=1))
        else:
            print_candidates(cands, len(pids))
        if not pids:
            print(f"❌ no DBLP person matches {what} (try another spelling or name variant, --name / --scholar / --orcid; "
                  "DBLP registers Scholar links and ORCIDs for some people only; some fields have little DBLP coverage)")
            sys.exit(1)
        print(f"✅ {len(pids)} DBLP candidates for {what}" + (f" (showing {len(cands)})" if len(cands) < len(pids) else ""),
              file=sys.stderr if a.json else sys.stdout)
    except SparqlError as e:
        print(f"❌ {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
