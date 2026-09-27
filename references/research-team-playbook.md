# 研究团队搭建手册（多位研究者 × 研究Skill × 圆桌）

> 为任意领域搭一支「研究顾问团」：3–6 位研究者，每人一个研究Skill，再加一个圆桌Skill，把他们请到用户的问题上。目标是让下一支团队的工作只剩三件事：填 `team.json`，跑脚本和保存好的工作流，过闸门。
>
> 实例是 `product/dfo-team/`（无导数优化，5 人，2026-09）。这支团队用了约 60 次工作流、220 个 agent、5,500 万 token、32 agent-小时，编排大多写在一次性脚本里。本手册和 `scripts/workflows/` 把这些编排整理成了可复用的部件。
>
> 相关文件（本文只讲怎么串起来，不重复内容）：
> - 单个研究Skill的提炼：[research-extraction-framework.md](research-extraction-framework.md)
> - 卡片格式与保守更新：[paper-reading-card.md](paper-reading-card.md)
> - 工作流参数：[scripts/workflows/README.md](../scripts/workflows/README.md)
> - 团队文件模板：[team-templates/](team-templates/)
> - 实例记录：[DFO README](../product/dfo-team/README.md)、[DEEP-READING](../product/dfo-team/DEEP-READING.md)

---

## 〇、什么时候用团队模式

| 用户要的 | 走哪条路 | 产出 |
|---|---|---|
| 学一个人怎么做研究 | 研究Skill（主 `SKILL.md` 的研究路径） | 1 个研究Skill |
| 一个主题的共识与分歧，不需要每个人都能单独调用 | 多研究者研究Skill（框架第十节） | 1 个Skill，方法标注归属，不模拟个人口吻 |
| 几位研究者**各自能单独调用**，也能坐到一起，就用户的问题会诊、争论、出方案 | **团队模式（本文）** | N 个成员Skill、1 个圆桌、1 份 README |

判断依据：用户会不会说「用 X 的视角看我的证明」或「让 A 和 B 辩一下」？会，就用团队模式。只要一份领域方法论，用第十节。

**团队交付物**（目录结构由 `new_team.py` 按 `team-templates/` 生成）：

1. **成员研究Skill**，每人一个。每个包括：
   - `SKILL.md`，末尾有 `## Roundtable Card`（Lens / Leads when / First questions asked / Default recommendation / Will push back on / Likely disagreements / Blind spots）；
   - `references/research/01–06`；
   - `references/sources/RESOURCES.md`。
2. **圆桌Skill**：
   - 主持人加每位成员各一个独立 agent；
   - 座位表：问题信号 → 2 位主讲 + 1 位挑战者；
   - 有据可查的分歧（fault lines）；
   - 4 个用户检查点。
3. **团队 README**：成员表、安装、用法，以及带覆盖表的诚实边界。
4. **深读档（可选）**：
   - 发表全表、开放全文索引、论文卡片；
   - 每位成员的 `07/08/09` 和 `technique-catalog.md`；
   - 团队的 `DEEP-READING.md`。

分两档：
- **轻量档** = T0–T2，每人一个研究Skill，加圆桌。
- **深读档** = 轻量档再加 T3，以后按需加 T4。深读档每人约多花 45 个 agent、1,100 万 token（见第六节），开跑前让用户选档。

---

## 一、选人

1. **3–6 人。** 少于 3 人争不起来（圆桌默认坐 3 人）。多于 6 人，座位表难排，成本也按人数线性增长。
2. **视角互补。** 开始调研前，先给每人写一行 lens，再按问题信号草拟座位表（每行 2 位主讲 + 1 位挑战者）。有人哪一行都不主讲，或者每一行都主讲，就换人或重新划分视角。
3. **分歧有据。** 挑在论文里真正意见不同的人。立队时列出预计的 3–5 条 fault line，每条写明双方是谁。T3 之后，每条都要有双方各自的卡片证据（写法如 `[<member> card S093 pp. 3–4]`）；找不到证据的，标为「推断」或删掉。证据强弱依次是：成员之间在论文里的直接交锋，已发表方法的对照，推断。
4. **先写清边界。** 不在队里的学派（DFO 的例子是贝叶斯优化和进化方法）写进 README 第一段和圆桌的 `Outside the Team`。
5. **看证据量。** 立队前，先看每人的 Google Scholar 条目数和方法论自述（访谈、讲义、学生回忆）。来源太少的人，提炼出的方法会很薄：要么换人，要么在诚实边界里写明。
   - **没有 Scholar 主页的人**（历史人物常见，尤其是在 Scholar 个人主页出现以前就去世的人）：用 `python3 scripts/dblp_works.py --name "<Name>"` 看 DBLP 记录数和年份范围，再看主页或 CV 的发表列表。`team.json` 的 `scholar` 留空；harvest 会先在 Scholar 上按姓名搜一次主页，找不到就以 DBLP + 主页为主列表（ID 用 `D`、`H`），T3.1 闸门改为与 DBLP 记录数和 CV 对账（见第三节）。
6. **姓氏在队内唯一。** 圆桌的 `[Surname lens]`、`@<Surname>`、`add/drop <Surname>` 都靠 `surname` 区分成员。撞姓时（例如数值线性代数的 Nicholas Higham 和 Desmond Higham）写成 `"N. Higham"`、`"D. Higham"`。`new_team.py` 不检查这一点，填 `team.json` 时自己核对。

**DFO 的例子。** 这五人可以看成「两个学派 × 理论 / 实践，外加一个新方向」。五条 fault line 各至少涉及 2 人，每人至少出现在 2 条里，这是可以参照的形状：

| 成员 | 在世 | Lens | 给团队补上的 | 参与的 fault line |
|---|---|---|---|---|
| Powell | 否（1936–2015） | 用插值模型驱动的实用求解器；用最小的决定性例子了结争论 | 模型法的实践、求解器默认值 | 1 模型法 vs 直接搜索 · 2 模型需要多少几何控制 · 5 保证 vs 性能 |
| Conn | 否（1946–2019） | 信赖域框架；样本集的几何让收敛可证 | 模型质量的理论 | 1 · 2 · 3 模型质量：确定性 vs 概率 |
| Scheinberg | 是，有学生模式 | 随机与概率模型 | 噪声、随机 oracle、ML 目标函数 | 2 · 3 · 5 |
| Vicente | 是 | 直接搜索理论：充分下降、最坏情况复杂度 | 复杂度保证 | 1 · 3 · 4 直接搜索的全局化 · 5 |
| Audet | 是 | 黑箱工程：MADS/NOMAD、约束分类、同预算比较 | 约束、仿真崩溃、基准测试 | 1 · 4 |

**在世 vs 历史人物**（`team.json` 的 `living` 字段）：
- **历史人物**：
  - Skill 只反映到其去世为止的工作；
  - Agent 6 不找「最近12个月」；
  - 后人的延续工作不算在他名下（例如 PRIMA 维护 Powell 的求解器）。

  这几点都写进诚实边界。
- **在世**：
  - Agent 6 必须覆盖最近 12 个月；
  - 新论文走 T4 增量；
  - 诚实边界写明调研日期。

**学生模式**（`student_mode: true`）：用户就在这位成员的组里时打开。这时 Skill 多出一个 Student Mode 段，以及三个文件：`proof-playbook.md`、`open-problems.md`、`reading-path.md`。可参照 Scheinberg 的 Workflow F（证明脚手架）和 Workflow G（组会前自查）。用户自己的导师反馈放在 `references/sources/private/`，这个目录不进 git；只有用户自己放进材料并提出要求时才读。

---

## 二、环境准备

**网络。** 云环境默认可能不放行下面的主机。被拒时，到环境设置里放行：会话标题栏的云环境菜单 → Edit → Network access，提高访问级别，或把域名加进允许列表。各访问级别的说明见 https://code.claude.com/docs/en/claude-code-on-the-web。

| 主机 | 用途 | 注意 |
|---|---|---|
| `scholar.google.com` | 发表全表 | 只能用 WebFetch：没有 API，也拦 curl |
| `sparql.dblp.org` | DBLP 记录（`dblp_works.py`） | `dblp.org` 的 REST 接口在 bot wall 后面 |
| `api.crossref.org` | 补 DOI、摘要 | 请求里不带邮箱 |
| `api.datacite.org` | arXiv 的 DOI（`10.48550/…`） | — |
| `arxiv.org` | 全文与标题检索 | `export.arxiv.org` 对云端 IP 返回 406，脚本改走 `arxiv.org/search` |
| `api.unpaywall.org` | 开放获取位置 | 必须带 email 参数：用 noreply 地址，**不用用户的邮箱** |
| `api.openalex.org` | 可选 | 共享 IP 很快 429；要用就设 `OPENALEX_API_KEY` |
| 领域仓库、作者主页、机构技术报告 | 补搜 | 写进 `team.json` 的 `chase_hints` |

`OPENALEX_API_KEY` 不是必需的。要用时，在同一处环境设置里加成环境变量，不要贴进对话。连通性自检：每行都应是 200。只有 `000`（连不上）或 `403`（被代理拒绝）表示不通，其他状态码说明主机可达。DBLP 的端点只接受查询，所以要用 POST 发一条查询来测；直接 GET 会得到 404，这不代表不通。Scholar 用 WebFetch 取一页来试。

```bash
printf '%s %s\n' "$(curl -s -o /dev/null -m 20 -w '%{http_code}' -X POST -H 'Accept: application/sparql-results+json' \
  --data-urlencode 'query=SELECT * WHERE {?s ?p ?o} LIMIT 1' https://sparql.dblp.org/sparql)" https://sparql.dblp.org/sparql
for u in https://api.crossref.org/works https://api.datacite.org/dois https://arxiv.org/search/ https://api.unpaywall.org/; do
  printf '%s %s\n' "$(curl -s -o /dev/null -m 20 -w '%{http_code}' "$u")" "$u"; done
```

**依赖。** 写进环境设置里的 Setup script，新会话会自动装好：

```bash
pip install pypdfium2 pillow
apt-get update && apt-get install -y tesseract-ocr ghostscript     # OCR；ps2pdf 随 ghostscript 安装
```

**磁盘。** PDF 与 `txt/` 每人约 20–300 MB。DFO 五人的 421 篇开放全文合计约 620 MB。

**CPU。** 每个工作流的并发上限是 min(16, CPU 数 − 2)，4 核容器只有 2（用 `nproc` 查）。所以要给每位成员各起一个工作流，并行跑。

**容器是临时的。**
- 每一步做完就 commit。
- PDF 与 `txt/` 不进 git，容器没了它们也就没了。写卡片和 `verify_card_quotes.py` 要在同一个容器的生命周期内做完。
- 换了容器，重跑 `acquire_fulltexts.py` 能重新下载脚本自己找得到的全文；补搜时手工找到的文件（`Source = manual`）要重新找。

---

## 三、流水线 T0–T4

工作流要在有 Workflow 工具的会话里、经用户同意后启动；启动方法见 [scripts/workflows/README.md](../scripts/workflows/README.md)。没有 Workflow 工具时，把工作流里的 prompt 当作 agent 简报手动派发；串行也能跑完，只是慢。

| 步 | 命令 / 工作流 | 输入 → 输出 | 闸门（通过标准） | 成本（每人） | 并行 |
|---|---|---|---|---|---|
| T0 定义 | `new_team.py --init` → 手填 → `new_team.py` | 选人结果 → `team.json`、团队目录骨架、README / 圆桌 / DEEP-READING 模板 | `.md` 里不剩 `{{`；`[TODO: …]` 就是待办，每条都写明由哪一步填 | 0 | — |
| T1 基础Skill | `team-base-skills.js`（`to` / `from` 分段，见下方人工检查点；`tier: "quick"` 只跑调研 01–03） | 成员信息 → `<M>/SKILL.md`（含 Roundtable Card）、`research/01–06` | `quality_check.py` 12/12 | 16–20 agent（quick 档 13–17） | 每人一个工作流 |
| T2 团队层 | `team-layer.js`（只做轻量档时 `deep_tier: false`） | 各人的 Roundtable Card → README、圆桌 SKILL.md、各人 RESOURCES.md | `check_links.py` 0；每人都有 Roundtable Card；模板闸门：轻量档没有输出，深读档只剩标给 T3 各步的 TODO | 2 agent，团队另加 3–5 | 团队一次 |
| T3.1 发表全表 | `team-harvest.js`（DBLP 走 `dblp_works.py`；`acquire: true` 顺带做 T3.2） | Scholar id、DBLP、Crossref → `works.json`、`scholar.md`；再做独立审计 | `validate_works.py` 0 errors；`S` 行数与 Scholar 总数对得上。没有 Scholar 主页时，改为与 `dblp_works.py --pid` 的记录数对账（`D` 行；差额要逐条说得清，例如并进正式版的 CoRR 预印本、重复、编辑的文集），`H` 行与主页 CV 对账 | 3 agent / 40 万 token | 每人一个 |
| T3.2 开放全文 | `acquire_fulltexts.py` | `works.json` → PDF、`txt/`、`INDEX.md`、`abstracts.json` | INDEX 行数 = `works.json` 里不是重复（`dup_of` 为空）的条目数 | 0 agent；arXiv 请求间隔 3 秒 | 每人一个后台进程 |
| T3.3 补搜、合并 | `team-chase.js`（最后自动跑 `merge_chase.py`） | 仍为 no-oa 的作品（每块 20 篇）→ PDF、摘要 → 并入 `abstracts.json`、`abstract-sources.json`，重跑获取 | 只用合法开放来源；在首页核对作者；报告新增全文数 | 5 / 90 万 | 每人一个 |
| T3.4 切批 | `plan_reading_batches.py`，分轮跑 | INDEX → 角色（写回 INDEX）、批次计划 JSON（放 scratch） | 批次不超上限；后续轮次 `--exclude` 之前各轮的计划 | 0 | 每人一个 |
| T3.5 读卡 | `team-read.js`（`round: N`），每轮一次 | 批次计划与全文 → `cards/<bid>.md` + `.digest.json` | 每轮：本轮每个批次都有卡片，`verify_card_quotes.py` 的 NOT FOUND = 0。最后一轮（不带 `--no-abstract`）之后，`mark_read_from_cards.py` 跑完没有未读行。中间轮次留下的 no-oa 行本来就是未读，要等最后一轮 | 22 / 580 万 | 每人一个；各轮之间串行 |
| T3.6 汇总 | `team-synthesize.js` | 卡片 → 07、08、09、`technique-catalog.md`，SKILL.md 保守更新 | 三位质疑者复核；12/12；`check_ledger.py <M>`（不带 `--before`，只查指向账本的锚点）；字数不超预算 | 6 / 240 万 | 每人一个 |
| T3.7 精简 | `team-tighten.js`（SKILL.md 仍超预算时才跑） | SKILL.md 精简到约 11.5k 词，长证据移入 `09-evidence-ledger.md` | `check_ledger.py <M> --before <精简前的备份>` 通过；12/12 | 3 / 70 万 | 每人一个 |
| T3.8 团队整合 | `team-integrate.js` | 各人的 08 → README 诚实边界、DEEP-READING.md、圆桌 fault lines | DEEP-READING 的覆盖表与 `team_status.py --coverage` 逐格一致，README 的 5 列摘要由它相加得到；`check_links.py` 0；模板闸门没有输出 | 团队一次，6–7 agent（DFO 用旧版时 4 / 100 万） | 团队一次 |
| T4 增量 | `team-increment.js`（`find: ["book-parts"]` 或 `["new-papers"]`） | 书的开放部分、新论文 → 新批次卡片，再保守更新 | 与 T3.5–T3.7 相同 | 每位书作者 4 / 100 万 | 每人一个 |

成本列里 T3.1–T3.7 和 T4 是 DFO 的实测（第六节）；T1、T2、T3.8 的 agent 数按现在的工作流结构估算，DFO 没有单独计量这几步。

**工作流参数。** 五个共用参数（`repo`、`team`、`scratch`、`date`、`members`）和各工作流的特有参数，见 [README 第二节](../scripts/workflows/README.md#二参数约定)。按成员跑的工作流，`members` 只放一位（从 `team.json` 原样拷贝），每人起一个，在同一条消息里一起发出；T2 和 T3.8 放全体。一个完整的调用：

```js
Workflow({scriptPath: "<repo>/scripts/workflows/team-base-skills.js",
          args: {repo: "<repo>", team: "product/<team>", scratch: "<scratch>", date: "YYYY-MM-DD",
                 members: [/* team.json 里这一位成员的对象 */], to: "review"}})
```

其余工作流只换 `scriptPath`，再加上表里括号中的参数。

**续跑与预览。**
- 中断以后续跑：同样的调用加上 `resumeFromRunId: "<上次的 runId>"`。
- 第一次在真团队上跑之前，先用 `dry_run.mjs`（Node ≥ 18）预览每个 agent 会收到的 prompt，不花 token：`node scripts/workflows/dry_run.mjs scripts/workflows/team-<name>.js scripts/workflows/examples/team-<name>.args.json --team product/<team> --member <slug>`。

**人工检查点。** 对应主 `SKILL.md` 的 Phase 1.5 和 2.5：
1. T1 先用 `to: "review"` 跑，把调研摘要摆给用户看。这时就 commit 调研笔记 01–06（`commit $T/$M "research($M): notes 01–06"`，`commit` 函数见下面的命令块），用户看摘要期间容器可能被回收；
2. 再用 `from: "synthesis", to: "synthesis"` 跑，把提炼结果和 Roundtable Card 摆给用户看，确认视角没有重叠、座位表排得开；
3. 最后用 `from: "build"` 跑完。

第 2 步的提炼记录放在 `<scratch>/base-skills/<slug>/`，不在 git 里。scratch 丢了，第 3 步就没有输入：重跑 `from: "synthesis"`（每人约 1 个 agent），不用从调研重来。

T3.6 之后，把每人 08 里新增、降级的方法摆给用户看。

可以直接复制的命令如下。`<team>`、`<slug>`、`<date>`（工作流的 `date` 参数）换成实际值。变量和 `commit` 函数在每个新 shell 里都要重新设一次：Bash 工具的每次调用都是新 shell。

```bash
T=product/<team>; M=<slug>
S=${TMPDIR:-/tmp}/<team>-scratch; mkdir -p $S      # 即工作流的 scratch（绝对路径）
# 提交一律用 commit：先暂存，再查暂存区。有受版权保护的文件（任何文件夹里的 PDF、PostScript、DjVu、EPUB，
# 抽出的 txt/）或 private/ 下的文件（README.md 除外）就停下，不提交。
commit() { git add "$1" && if git diff --cached --name-only | grep -Ei '\.(pdf|ps|ps\.gz|djvu|epub)$|/txt/|/private/' | grep -v '/private/README\.md$'
  then echo "STOP: 上面这些文件不能提交。git restore --staged 它们，把它们的模式加进 .gitignore（或把文件移出仓库），再重跑"
  else git commit -m "$2"; fi; }

# T0 定义：起草 team.json，再照 team-templates/team.example.json 的说明补 scholar、hint、living、student_mode、chase_hints
python3 scripts/new_team.py --init <team> --field "<领域与传统>" --members "Name One;Name Two;Name Three"
python3 scripts/new_team.py $T/team.json          # 铺目录；已存在的文件保留
grep -rn --include='*.md' '{{' $T                 # 必须为空
grep -rn --include='*.md' '\[TODO' $T             # 待办清单：每条写明由哪一步填
commit $T "feat(<team>): scaffold"

# T1 → T2 之后
python3 scripts/quality_check.py $T/$M/SKILL.md   # 每人 12/12
python3 scripts/check_links.py $T                 # 0 broken
grep -rn --include='*.md' -e '{{' -e '\[TODO' $T  # 模板闸门，见下面两行
#   深读档：只剩标给 T3 各步的项（DEEP-READING.md、各人 RESOURCES.md 的第 1 行和深读档占位行、README 和圆桌里标 T3.8 的项）
#   轻量档：必须为空。还有 DEEP-READING.md 或 RESOURCES.md 里留给深读档的项，就照模板里写的轻量档（base tier）写法改掉
commit $T "feat(<team>): base skills + roundtable"    # 轻量档到此完成

# T3.1 之后
python3 scripts/validate_works.py $T/$M           # 0 errors
# T3.2，每人一个后台进程（harvest 带 acquire: true 时跳过）。首选 Bash 工具的 run_in_background 跑下面这条（去掉末尾的 &）；
# 否则用 nohup 单独一行起，记下 PID。别在同一行用 && 串别的命令，否则 $! 不是这个进程
nohup python3 scripts/acquire_fulltexts.py $T/$M > $S/acq-$M.log 2>&1 < /dev/null &
echo $! > $S/acq-$M.pid
tail -n 3 $S/acq-$M.log; kill -0 $(cat $S/acq-$M.pid) 2>/dev/null && echo running    # 查进度
# kill $(cat $S/acq-$M.pid)                       # 要中途停下时才用：按 PID 停，别用 pkill -f
commit $T/$M "sources($M): publication list + open full texts"      # 等获取进程跑完再提交

# T3.3 补搜之后（chase 带 merge: false 时才要手动合并）
python3 scripts/merge_chase.py $T/$M
commit $T/$M "chase($M): open copies and abstracts"

# T3.4 切批：每轮 --exclude 之前各轮的计划（含仍在读的）
python3 scripts/plan_reading_batches.py $T/$M --no-abstract > $S/batches-$M-r1.json
python3 scripts/plan_reading_batches.py $T/$M --round 2 --no-abstract --exclude $S/batches-$M-r1.json > $S/batches-$M-r2.json
#   某一轮计划出 0 个全文批次（剩下的都没有开放全文）时，就跑最后一轮：不带 --no-abstract，剩下的作品进摘要、元数据批次
python3 scripts/plan_reading_batches.py $T/$M --round 3 --exclude $S/batches-$M-r1.json,$S/batches-$M-r2.json > $S/batches-$M-r3.json

# T3.5 每轮 team-read.js（round: N）之后
python3 scripts/verify_card_quotes.py $T/$M       # NOT FOUND 必须为 0
python3 scripts/mark_read_from_cards.py $T/$M
python3 scripts/team_status.py $T                 # 最后一轮之后：未读行 = 0（中间轮次的 no-oa 行本来就未读）
commit $T/$M "cards($M): round N"

# T3.6 之后
python3 scripts/quality_check.py $T/$M/SKILL.md   # 12/12
python3 scripts/check_ledger.py $T/$M             # 不带 --before：只查 SKILL.md 指向账本的锚点，必须 ✅
#   可选：和汇总前对比。front matter（researched 日期）和 Activation Rules（免责声明里的覆盖数字）有差异是预期的，其余 ✗ 逐条看
python3 scripts/check_ledger.py $T/$M --before $S/$M-SKILL.before-synth-<date>.md
commit $T/$M "synth($M): deep-reading synthesis"

# T3.7：只给 SKILL.md 仍超预算的成员。开跑前从 git 存一份精简前的副本（工作流看到已有的副本会保留它，scratch 丢了也能再取）
git show HEAD:$T/$M/SKILL.md > $S/$M-SKILL.before-tighten-<date>.md
# T3.7 之后
python3 scripts/quality_check.py $T/$M/SKILL.md
python3 scripts/check_ledger.py $T/$M --before $S/$M-SKILL.before-tighten-<date>.md   # 必须 ✅（无损）
commit $T/$M "tighten($M): evidence to 09-evidence-ledger.md"

# T3.8 之后
python3 scripts/team_status.py $T                 # 各人进度
python3 scripts/team_status.py $T --coverage      # 这张 11 列表原样贴进 DEEP-READING.md 的 Coverage；README 诚实边界是 5 列摘要，逐格由它相加
python3 scripts/check_links.py $T                 # 0 broken
grep -rn --include='*.md' -e '{{' -e '\[TODO' $T  # 必须为空；还有输出就照每条 TODO 写的来源补上（数字只取脚本输出）
commit $T "docs(<team>): integrate the deep reading"
```

---

## 四、质量闸门

每道闸门都过了，才能进下一步。

| 闸门 | 命令 | 通过标准 | 什么时候跑 |
|---|---|---|---|
| 研究Skill自检 | `quality_check.py <M>/SKILL.md` | 12/12 | T1、T3.6、T3.7 之后；SKILL.md 每次改动之后 |
| 发表全表 | `validate_works.py <M>`（也可给团队目录） | 0 errors（结构、ID、dup_of）；警告（近似重复、没有 DOI/arXiv/链接）逐条人看；条目数与 Scholar 总数对得上（没有 Scholar 主页时与 DBLP 记录数和主页 CV 对账，见第三节 T3.1） | T3.1 之后 |
| 摘录逐字 | `verify_card_quotes.py <M>` | 全部通过，NOT FOUND = 0 | 每轮读卡之后；汇总之前 |
| 读完 | `mark_read_from_cards.py <M>`，再 `team_status.py <team>` | 未读行 = 0 | 最后一轮（不带 `--no-abstract`）读卡之后；中间轮次不查 |
| 账本锚点 | `check_ledger.py <M>`（不带 `--before`） | SKILL.md 指向 `09-evidence-ledger.md` 的锚点都能解析 | T3.6 之后 |
| 精简无损 | `check_ledger.py <M> --before <scratch>/<slug>-SKILL.before-tighten-<date>.md` | 精简前的卡片 ID、「ID + 页码」引用和引文都还在 SKILL.md 或账本里；指向账本的锚点都能解析；front matter 和激活规则、诚信规则、学生模式各节逐字不变 | T3.7 之后（只有跑了 T3.7 的成员）。备份不在了就用 `git show <精简前的提交>:<M>/SKILL.md` 取回。别拿汇总前的备份（`before-synth`）当通过标准：汇总本来就会改 front matter 的日期和激活规则里的覆盖数字 |
| 链接 | `check_links.py <team>` | 0 broken | T2、T3.8 之后；交付之前 |
| 覆盖 | `team_status.py <team> --coverage` | DEEP-READING 的 Coverage 原样是这张 11 列表；README 诚实边界是 5 列摘要（成员；作品数；全读 / 部分读；摘要 + 元数据；跳过），逐格由这张表相加，两处数字一致 | T3.8 |
| 模板 | `grep -rn --include='*.md' -e '{{' -e '\[TODO' <team>` | 没有输出 | 轻量档 T2 之后；深读档 T3.8 之后；交付之前 |
| 提交 | 第三节的 `commit` 函数（查暂存区） | 没有任何文件夹里的 PDF、PostScript、DjVu、EPUB，没有 `txt/`，`private/` 下只有 `README.md` | 每次 commit |
| 圆桌 | 人工检查 | 每人都有 Roundtable Card；每条 fault line 都有双方的卡片证据 | T2、T3.8 |

---

## 五、失败模式与降级

| 症状 | 原因 | 处理 |
|---|---|---|
| curl Scholar 得到 403 或空页 | Scholar 没有 API，拦 curl | 用 WebFetch 取 `citations?user=<id>&hl=en&cstart=N&pagesize=50`，prompt 要求逐字 “return every row as JSON lines + TOTAL=”；两次计数对不上，改用 `pagesize=20` 重取；再按 `sortby=pubdate` 做一次独立审计，补漏 |
| `dblp.org` 返回 Anubis 页面 | bot wall | 用 `sparql.dblp.org/sparql`（POST `query=`，`Accept: application/sparql-results+json`），即 `dblp_works.py` |
| 连通性自检里 `sparql.dblp.org` 返回 404 | 端点只接受查询；直接 GET 就是 404 | 404 说明主机可达。用第二节的 POST 自检，应为 200 |
| 成员没有 Google Scholar 主页 | 历史人物常见 | `scholar` 留空；harvest 先在 Scholar 上按姓名搜一次主页，找不到就以 DBLP + 主页（设了 `OPENALEX_API_KEY` 时再加 OpenAlex）为主列表，ID 用 `D`、`H`；T3.1 闸门改为与 DBLP 记录数和主页 CV 对账 |
| OpenAlex 429 | 共享 IP 的免费额度 | 设 `OPENALEX_API_KEY`，或者不用它 |
| `export.arxiv.org` 406 | 云端 IP 被拒 | 用 `arxiv.org/search` 网页检索（脚本已内置） |
| 某个技术报告系列里匹配到别人的报告 | 只按标题词匹配 | 核对第 1 页上的作者 |
| `.ps` 文件、扫描件、文字层乱码 | 没有可用的文字层 | `.ps` 先用 `ps2pdf` 转成 PDF；扫描件和乱码文字层（英文停用词比例 < 0.01）由 `acquire_fulltexts.py` 自动 OCR；自己跑 tesseract 时设 `OMP_THREAD_LIMIT=1`，否则负载会爆掉；OCR 之后重读相关卡片 |
| 非英文论文的全文不对，或获取很慢 | 乱码检测和 OCR 都按英文调：检测看英文停用词比例，OCR 用 tesseract 的英文模型。拉丁字母的其他语言一般不会误判；中文、俄文等文字的论文容易被当成乱码去 OCR，英文模型的识别结果可能替换掉本来正常的文字层，扫描件则会被识别成乱码 | 非英文的全文逐篇抽查 `txt/`；抽错的，用对应语言重新抽取或 OCR（`tesseract <页图> - -l <语言>`），写回同名的 txt 文件并保留 `[[page N]]` 标记，再写卡片 |
| `pkill -f` 把自己的 shell 也杀了 | shell 的命令行里含有同一个模式 | 按确切的 PID kill |
| 后台的 `acquire_fulltexts.py` 没跑完就没了 | 在 Bash 工具调用里用 `&` 起的进程，可能随这次调用结束被收掉 | 用 Bash 工具的 run_in_background；或按第三节用 `nohup … &` 单独一行起，PID 写进 `$S/acq-<slug>.pid` |
| 工作流慢，看上去只有 2 路在跑 | 并发 = min(16, CPU − 2) | 每人一个工作流，并行启动 |
| 读卡 agent 超时、同一篇被分派两次 | 批次太大；上一轮还在读 | core ≤110 页且 ≤5 篇；supplement ≤220 页且 ≤8 篇；>150 页的书单独一批；摘要 30 篇一批；第 2 轮 `--exclude` 仍在读的批次文件 |
| 摘录 NOT FOUND | 转述冒充原文，或者页码不对 | 每张卡片最多 2 条摘录；改成原文，或者去掉引号改成转述；全部通过再汇总 |
| 标题改了，txt 对不上 | 文件名 slug 由标题和年份生成 | 重命名文件或修正年份，再跑 `acquire_fulltexts.py --only <ID>` |
| INDEX 被重置成 no-oa | 旧版脚本在没有本地文件时覆盖 | `git checkout -- <M>/references/sources/papers/INDEX.md` |
| 读卡轮次停不下来 | 每轮都只剩没有开放全文的作品 | 某一轮计划出 0 个全文批次时，跑最后一轮：不带 `--no-abstract`，剩下的作品进摘要、元数据批次 |
| `check_ledger.py` 退出码 2 | `--before` 的备份不存在：没跑 T3.7，或 scratch 丢了 | 没跑 T3.7 的成员只跑不带 `--before` 的锚点检查；scratch 丢了，用 `git show <精简前的提交>:<M>/SKILL.md` 取回 |
| `check_ledger.py --before` 报 front matter、Activation Rules 不同 | 拿了汇总前的备份（`before-synth`）：汇总本来就会改 researched 日期和免责声明里的覆盖数字 | 这两处差异是预期的，其余 ✗ 逐条看；无损的通过标准只用精简前的备份（`before-tighten`） |
| SKILL.md 膨胀到约 21k 词（DFO 当时） | 汇总时没有给字数预算 | `team-synthesize.js` 现在默认给 11,500 词预算并同时写 `09-evidence-ledger.md`；仍超预算再跑 T3.7 |
| 汇总提出的新方法站不住 | 排他性不过关 | 保留质疑复核；新的核心方法要有 ≥3 篇论文支撑，并过四重验证 |
| 容器重启，工作丢了 | 容器是临时的 | 每一步 commit；T1 在 `to: "review"` 之后就 commit 调研笔记；scratch 里的提炼记录丢了，重跑 T1 的 `from: "synthesis"` |
| 交付前模板闸门还有 `[TODO` | 某一步没清掉模板里标给它的项；轻量档留下了给深读档的项（DEEP-READING.md、RESOURCES.md 第 1 行和深读档占位行） | 每条 TODO 都写明由哪一步、按什么来源填：照它补上，数字只取脚本输出；轻量档照模板里的轻量档（base tier）写法改 |
| 暂存区里出现 PDF、`.ps`、`.djvu`、`.epub` | `.gitignore` 只按已知的路径和扩展名排除（例如 `papers/*.pdf`），`talks/`、`essays/` 里的文件、大写的 `.PDF` 可能漏掉 | 用第三节的 `commit` 函数提交；漏掉的模式补进 `.gitignore` |
| `@<Surname>` 分不清是谁 | 队里有人同姓 | `surname` 写成 `"N. Higham"`、`"D. Higham"` 这样，队内唯一 |
| 工作流中断、被停，或者改了脚本 | — | 用同样的 `scriptPath` 和 `args`，加 `resumeFromRunId` 续跑，没改过的 agent 调用直接取缓存；也可以用 T1 的 `from`、T3.5 的 `overwrite: false` / `only`、T3.3 的 `only_chunks` |
| 书的正文读不到 | 正文不开放 | 读合法开放的部分（目录、勘误、增补、前言、已发表书评），作为 `B###` 条目、批次 `k01`；不用影子图书馆 |
| WebSearch 突然全部失败 | 每个会话约 200 次的预算用完了 | 补搜先用 curl 查 `chase_hints` 里的已知仓库，WebSearch 留给难找的 |
| fault line 只有一方的证据 | 圆桌从成员简介拼出来 | 每条都要双方的卡片证据；成员简介指向各人的 technique catalog 和 08 |

---

## 六、成本与时间

DFO 深读档的实测：5 人，Scholar 935 行，421 篇开放全文，795 张卡片。

| 阶段 | DFO 合计 | 每人约 | 占比 |
|---|---|---|---|
| 读卡 T3.5 | 112 agent / 2,880 万 token | 22 / 580 万（约 3.6 万 token 一张卡片） | 52% |
| 汇总 T3.6 | 30 / 1,180 万 | 6 / 240 万 | 21% |
| 补搜 T3.3 | 27 / 430 万 | 5 / 90 万 | 8% |
| 书的增量 T4 | 16 / 390 万（4 位书作者） | 4 / 100 万 | 7% |
| 精简 T3.7 | 15 / 340 万 | 3 / 70 万 | 6% |
| 发表全表 T3.1 | 15 / 190 万 | 3 / 40 万 | 3% |
| 团队整合 T3.8 | 4 / 100 万 | 团队一次 | 2% |

合计：深读档每人约 45 个 agent、1,100 万 token；这 220 个 agent 共约 32 agent-小时（每人约 6.5）。轻量档按工作流结构估：T1 每人 16–20 个 agent，T2 每人 2 个、团队另加 3–5 个；DFO 这两步没有计量 token。实际耗时 ≈ agent-小时 ÷ 同时在跑的 agent 数，所以要按第二节的办法把并行开足。

**怎么省：**

- **只做轻量档。** 不做 T3，省掉每人约 1,100 万 token。
- **少精读。** 用 `plan_reading_batches.py --core-top 10`（默认 25），让精读的 core 变少；其余有全文的作品走 supplement 略读，每批页数上限是 core 的两倍。读卡占一半以上的成本。
- **跳过补搜。** 获取脚本没拿到全文的作品直接走摘要批次，30 篇一批，便宜得多。代价是证据变弱，要在诚实边界里写明。
- **不做书的增量。** 除非成员有核心著作。
- **T1 用 quick 档**（`tier: "quick"`，只跑调研 01–03）。代价是少了学生回忆、同行批评和研究轨迹，要在诚实边界里写明。
- **不跑 T3.7。** `team-synthesize.js` 已按预算同时写 ledger，SKILL.md 没超预算就不用精简。

---

## 七、规矩

1. **只用合法的开放获取来源**：arXiv、Unpaywall、作者主页、机构报告、开放仓库。不用 Sci-Hub 等影子图书馆，不绕付费墙。
2. **受版权保护的文件不进 git。** 任何文件夹里的 PDF、PostScript、DjVu、EPUB，以及抽出的 `txt/`，都只留在本地；`talks/`、`essays/` 里存的幻灯片和文章也一样。`.gitignore` 只按已知的路径和扩展名排除，不能全靠它：提交一律用第三节的 `commit` 函数，它会先查暂存区。提交的只有索引、摘要、卡片和汇总。
3. **`private/` 不读。** 只有用户自己放进材料并提出要求时才读，且内容永远不进公开文件。
4. **摘录逐字**，每条带页码，必须过 `verify_card_quotes.py`。看不懂或没读到的，写「未读」。
5. **保守更新**，规则见卡片模板第三节：只追加；已有方法只补证据；新的核心方法要 ≥3 篇论文并过四重验证。
6. **语言。** 成员Skill和卡片用 `team.json` 的 `language`。英语研究者的卡片用英语写，这样摘录才能逐字核对。
   - 团队文件的模板（README、圆桌、DEEP-READING、RESOURCES）是英文的。`team-layer.js` 按 `language` 写团队层，`team-integrate.js` 沿用文件已有的语言；模板里固定的英文段落（圆桌的协议、成员简报等）不一定会被翻译。非英文团队在 T2 之后检查这几个文件的语言是否统一。
   - 全文获取的乱码检测和 OCR 按英文调好，非英文论文的 `txt/` 要逐篇抽查（见第五节）。
7. **API 请求里不放用户的邮箱。** Unpaywall 用 noreply 地址，Crossref 不带邮箱。
8. **成员是基于公开作品模拟的视角，不代表本人观点。** README 和每个 Skill 的诚实边界都写明这一点。

---

## 八、增量更新与增删成员

**有新论文、新书时**，用 `team-increment.js`：

- **让工作流自己找**：`find: ["new-papers"]`（在世成员，`since` 默认取 `works.json` 的 harvested 日期）或 `find: ["book-parts"]`（书的开放部分，作为 `B###` 条目）。Prepare agent 会做这几件事：
  - 把新材料登记进 `works.json`；
  - 跑 `validate_works.py`、`acquire_fulltexts.py --only <新ID>` 和 `plan_reading_batches.py`；
  - 读卡，保守并入（SKILL.md 净增不超过 `maxGrowth`，默认 400 词，细节进 09）。
- **用户手里有合法副本时**：
  1. 按 DEEP-READING 的「How to extend」命名（`<ID>-<年份>-<标题前8词>.pdf`），放进 `papers/`；
  2. 在 `works.json` 加一行，带 note；
  3. 跑 `acquire_fulltexts.py <M> --only <ID>`；
  4. 用 `plan_reading_batches.py --round <下一轮> --no-abstract --exclude <之前各轮的计划>` 写 `$S/batches-<slug>-<label>.json`；
  5. 用 `team-increment.js` 的 `batchFiles` 跑。

两种做法之后都要跑 `team-integrate.js`，让 README、DEEP-READING 和圆桌显示新的覆盖。在世的成员每年跑一次 `new-papers`。

**加一个成员**（按这个顺序）：
1. 在 `team.json` 里加上这个人（`surname` 不能和队里已有的人重复），跑 `python3 scripts/new_team.py $T/team.json --add-member <slug>`。它只铺这个人的目录，在 README 成员表里插一行，不改圆桌和 DEEP-READING。
2. 只为这个人跑 T1。
3. 带全体成员重跑 `team-layer.js`，把这个人写进圆桌的成员表、座位表和 fault lines。`team-integrate.js` 不会给新成员排座，所以这一步不能省。
   - 深读档团队：`team-layer.js` 的诚实边界按 T3 之前的写法（「fault lines 还没对照全文核对」），新 fault line 也带「(card evidence pending)」。跑完用 `git diff` 核对：已有的、带卡片证据的 fault lines 和深读档的诚实边界要保留下来，被改掉的从 git 里恢复。
4. 深读档：为这个人跑 T3.1–T3.7。
5. 深读档：带全体成员跑 `team-integrate.js`，补上新成员的卡片证据和覆盖数字。
6. 跑第四节的链接和模板闸门。

**减一个成员**：
1. 从 `team.json` 删掉，移走这个人的目录。
2. 带剩下的成员重跑 `team-layer.js`，删掉圆桌和 README 里提到这个人的地方（座位表、fault lines、成员表）；深读档接着跑 `team-integrate.js`，更新 DEEP-READING 和覆盖表，同样用 `git diff` 核对留下的卡片证据没被改掉。
3. `check_links.py` 必须为 0。

---

## 九、完成检查清单

- [ ] 3–6 人，视角互补，`surname` 队内唯一；座位表每行有 2 位主讲 + 1 位挑战者（只有一人有证据的行，挑战者写 —）；不在队里的学派写进了 `Outside the Team`
- [ ] 每位成员 `quality_check.py` 12/12，都有 `## Roundtable Card`
- [ ] 每条 fault line 都有双方的证据；深读档要有双方的卡片证据
- [ ] 历史人物和在世成员的时间边界、调研日期写进了诚实边界；`private/` 下只有 `README.md` 被 git 跟踪
- [ ] 深读档：`validate_works.py` 0 errors，条目数与 Scholar 总数（没有主页时与 DBLP 记录数和 CV）对得上；`verify_card_quotes.py` 全部通过；最后一轮读卡之后 `team_status.py` 显示没有未读行；每人 `check_ledger.py` 锚点通过，跑过 T3.7 的成员 `check_ledger.py --before <精简前的备份>` 通过
- [ ] `team_status.py --coverage` 的表原样贴进了 DEEP-READING.md；README 诚实边界的 5 列摘要逐格由它相加，两处数字一致
- [ ] `check_links.py product/<team>` 0 broken；`grep -rn --include='*.md' -e '{{' -e '\[TODO' product/<team>` 没有输出（轻量档也一样：DEEP-READING.md 和 RESOURCES.md 里给深读档留的项按模板的轻量档写法改掉了）
- [ ] 每次提交都用了 `commit` 函数：git 里没有任何文件夹下的 PDF、PostScript、DjVu、EPUB，没有 `txt/`，`private/` 下只有 `README.md`（`git ls-files product/<team> | grep -Ei '\.(pdf|ps|ps\.gz|djvu|epub)$|/txt/|/private/'` 只列出 `private/README.md`）；每一步都已 commit
- [ ] 用一个真实问题试一次圆桌：4 个检查点都出现，最终方案每条都有归属，并有 ✅ 签字或 ⚠️ 异议
