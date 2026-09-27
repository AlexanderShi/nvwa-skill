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

确定只做轻量档时：T0 铺目录加 `--base-tier`（`DEEP-READING.md` 直接写成轻量档说明；各人 `RESOURCES.md` 去掉深读档占位行，第 1 行记 `not harvested (base tier)`），T2 用 `deep_tier: false`。之后想加深读：删掉轻量档的 `DEEP-READING.md`，再跑一次 `new_team.py <team.json>`（不带 `--base-tier`；已有文件保留，只补缺的），然后从 T3.1 跑起。各人的 `RESOURCES.md` 这时还是轻量档的样子（没有深读档占位行，第 1 行记 `not harvested (base tier)`），不用手改：T3.1 的审计整行重写第 1 行，T3.6 发现没有占位行就把深读档各行接在最后。README 和圆桌里轻量档的写法（「without full-text reading」「No deep reading was done (base tier)」「have not been checked against full texts」）由 T3.8 换掉；之后 `team_check.py` 通过即可。

---

## 一、选人

1. **3–6 人。** 少于 3 人争不起来（圆桌默认坐 3 人）。多于 6 人，座位表难排，成本也按人数线性增长。
2. **视角互补。** 开始调研前，先给每人写一行 lens，再按问题信号草拟座位表（每行 2 位主讲 + 1 位挑战者）。有人哪一行都不主讲，或者每一行都主讲，就换人或重新划分视角。
3. **分歧有据。** 挑在论文里真正意见不同的人。立队时列出预计的 3–5 条 fault line，每条写明双方是谁。T3 之后，每条都要有双方各自的卡片证据（写法如 `[<member> card S093 pp. 3–4]`）；找不到证据的，标为「推断」或删掉。证据强弱依次是：成员之间在论文里的直接交锋，已发表方法的对照，推断。
4. **先写清边界。** 不在队里的学派（DFO 的例子是贝叶斯优化和进化方法）写进 README 第一段和圆桌的 `Outside the Team`。
5. **看证据量。** 立队前，先看每人的 Google Scholar 条目数和方法论自述（访谈、讲义、学生回忆）。来源太少的人，提炼出的方法会很薄：要么换人，要么在诚实边界里写明。
   - **没有 Scholar 主页的人**（历史人物常见，尤其是在 Scholar 个人主页出现以前就去世的人）：用 `python3 scripts/dblp_works.py --name "<Name>"` 看 DBLP 记录数和年份范围，再看主页或 CV 的发表列表。`team.json` 的 `scholar` 留空；harvest 会先在 Scholar 上按姓名搜一次主页，找不到就以 DBLP + 主页为主列表（ID 用 `D`、`H`），T3.1 闸门改为与 DBLP 记录数和 CV 对账（见第三节）。`python3 scripts/new_team.py $T/team.json --lookup` 从 DBLP 补空着的 `dblp`、`orcid`、`homepage`（按 Scholar 链接或 ORCID 匹配到的可靠；只按姓名匹配到的会提示对照 hint 核对）；harvest 找到的 Scholar id、DBLP pid，照它返回的 `next` 用 `--set-member <slug> scholar=… dblp=…` 记回去，不用手改 JSON。`new_team.py` 先把这人 `RESOURCES.md` 第 1 行的 Link 写成 `— (no Scholar profile in team.json; list from DBLP/homepage)`（轻量档是 `—`），harvest 的审计再把整行改写成实际用的 DBLP 个人页或主页列表。
6. **姓氏在队内唯一。** 圆桌的 `[Surname lens]`、`@<Surname>`、`add/drop <Surname>` 都靠 `surname` 区分成员。撞姓时（例如数值线性代数的 Nicholas Higham 和 Desmond Higham）写成 `"N. Higham"`、`"D. Higham"`。`new_team.py` 起草、铺目录和 `--add-member` 时都会检查，撞姓就警告，照提示改 `team.json` 的 `surname`。`surname` 只是标签：工作流核对作者、拼检索词用的是姓（`name` 的最后一个词，如 "Higham"；姓不在最后的名字写可选的 `family_name`），所以 "N. Higham" 不会让核对第 1 页作者的 agent 把正确的文本当成错的。

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
# 成员有非英文的扫描件时再装语言包，如 tesseract-ocr-deu、tesseract-ocr-chi-sim（配合 acquire_fulltexts.py --ocr-lang）
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
| T0 定义 | `new_team.py --init` → 补 `team.json`（`--lookup` 从 DBLP 补 id，`--set-member` 改字段）→ `new_team.py`（只做轻量档加 `--base-tier`） | 选人结果 → `team.json`、团队目录骨架、README / 圆桌 / DEEP-READING 模板 | `.md` 里不剩 `{{`；`[TODO: …]` 就是待办，每条都写明由哪一步填；没有撞姓警告；`check_links.py` 0 broken（README 指向各人 SKILL.md 的链接记为 pending，T1 写） | 0 | — |
| T1 基础Skill | `team-base-skills.js`（`to` / `from` 分段，见下方人工检查点；`tier: "quick"` 只跑调研 01–03） | 成员信息 → `<M>/SKILL.md`（含 Roundtable Card）、`research/01–06` | `quality_check.py` 12/12 | 16–20 agent（quick 档 13–17） | 每人一个工作流 |
| T2 团队层 | `team-layer.js`（`members` 放**全体**；只做轻量档时 `deep_tier: false`） | 各人的 Roundtable Card → README、圆桌 SKILL.md、各人 RESOURCES.md | `check_links.py` 0；每人都有 Roundtable Card；每条 fault line 双方都有证据；模板闸门：轻量档没有输出，深读档只剩标给 T3 各步的 TODO。圆桌不跑 `quality_check.py` | 每人 2 个，团队另加 4–5 个 | 团队一次 |
| T3.1 发表全表 | `team-harvest.js`（DBLP 走 `dblp_works.py`；`acquire` 默认 false，T3.2 在主会话里跑） | Scholar id、DBLP、Crossref → `works.json`、`scholar.md`；再做独立审计 | `validate_works.py` 0 errors；`S` 行数与 Scholar 总数对得上。没有 Scholar 主页时，改为与 `dblp_works.py --pid` 的记录数对账（`D` 行；差额要逐条说得清，例如并进正式版的 CoRR 预印本、重复、编辑的文集），`H` 行与主页 CV 对账 | 3 agent / 40 万 token | 每人一个 |
| T3.2 开放全文 | `acquire_fulltexts.py` | `works.json` → PDF、`txt/`、`INDEX.md`、`abstracts.json` | INDEX 行数 = `works.json` 里不是重复（`dup_of` 为空）的条目数（`team_status.py` 的 Indexed 列打 ✓；书的开放部分 B### 另计） | 0 agent；arXiv 请求间隔 3 秒 | 每人一个后台进程 |
| T3.3 补搜、合并 | `team-chase.js`（最后自动跑 `merge_chase.py`） | 仍为 no-oa 的作品（每块 20 篇）→ PDF、`abstracts-chase-<date>-r<run>-<块>.json` → 并入 `abstracts.json`、`abstract-sources.json`，重跑获取 | 只用合法开放来源；在首页核对作者；报告新增全文数 | 5 / 90 万 | 每人一个 |
| T3.4 切批 | `plan_reading_batches.py <team> --out-dir <scratch>`，分轮跑 | INDEX → 角色（写回 INDEX）、`<scratch>/batches-<slug>-r<N>.json`（team-read 默认读的文件名；轮次自动取下一轮，scratch 里其他轮的计划自动排除） | 批次不超上限；打印的轮次 N 就是 team-read 的 `round` | 0 | 一条命令规划全体 |
| T3.5 读卡 | `team-read.js`（`round: N`），每轮一次 | 批次计划与全文 → `cards/<bid>.md` + `.digest.json` | 每轮：本轮每个批次都有卡片，`verify_card_quotes.py` 的 NOT FOUND = 0。最后一轮（不带 `--no-abstract`）之后，`mark_read_from_cards.py` 跑完没有未读行。中间轮次留下的 no-oa 行本来就是未读，要等最后一轮 | 22 / 580 万 | 每人一个；各轮之间串行 |
| T3.6 汇总 | `team-synthesize.js` | 卡片 → 07、08、09、`technique-catalog.md`，SKILL.md 保守更新 | 三位质疑者复核（删改检测：`check_ledger.py <M> --before <汇总前备份> --allow frontmatter,activation-disclaimer`，没有 ✗）；12/12；`check_ledger.py <M>`（不带 `--before`：指向账本的锚点都能解析）；字数不超预算 | 6 / 240 万 | 每人一个 |
| T3.7 精简 | `team-tighten.js`（SKILL.md 仍超预算时才跑） | SKILL.md 精简到约 11.5k 词，长证据移入 `09-evidence-ledger.md` | `check_ledger.py <M> --before <精简前的备份>`（不加 `--allow`）通过；12/12 | 3 / 70 万 | 每人一个 |
| T3.8 团队整合 | `team-integrate.js` | 各人的 08 → README 诚实边界、DEEP-READING.md、圆桌 fault lines | `team_check.py <team>` 退出码 0：DEEP-READING 的覆盖表原样是 `team_status.py --coverage`，README 的 5 列摘要原样是 `team_status.py --coverage --short`；`check_links.py` 0；fault line 双方都有卡片证据且卡片 ID 存在；模板闸门没有输出；每人 12/12、摘录、账本、发表全表 | 团队一次，6–7 agent（DFO 用旧版时 4 / 100 万） | 团队一次 |
| T4 增量 | `team-increment.js`（`find: ["book-parts"]` 或 `["new-papers"]`） | 书的开放部分、新论文 → 新批次卡片（批次名接着轮次，如 `c5-01`），再保守更新 | 与 T3.5–T3.7 相同；删改检测 `check_ledger.py <M> --before <增量前备份> --allow frontmatter-date,activation-numbers` | 每位书作者 4 / 100 万（旧版实测；现版多一位复核员，一批时每人 5–6 个） | 每人一个 |

成本列里 T3.1–T3.7 和 T4 是 DFO 的实测（第六节）；T1、T2、T3.8 的 agent 数，以及现版 T4 的数字，按现在的工作流结构估算，DFO 没有单独计量这几步。

**工作流参数。** 五个共用参数（`repo`、`team`、`scratch`、`date`、`members`）和各工作流的特有参数，见 [README 第二节](../scripts/workflows/README.md#二参数约定)。**不要手抄**：`node scripts/workflows/make_args.mjs <工作流> --team $T [--member a,b] [--set KEY=JSON]` 从 `team.json` 生成现成的 `{scriptPath, args}`，每人一个（T2、T3.8 一个），scratch 固定为 `${TMPDIR:-/tmp}/<team>-scratch`，所有阶段都用这一个。参数名一律 `snake_case`（如 `batch_files`、`word_budget`、`max_words`、`target_words`、`max_growth`、`root_readme`、`new_fault_lines`）；早期版本用过的 camelCase 旧名（`batchFiles`、`maxGrowth` 等）仍当别名接受，运行开头记一行日志提醒改名，新旧都给时用新名。按成员跑的工作流，`members` 只放一位（从 `team.json` 原样拷贝），每人起一个，在同一条消息里一起发出。T2 和 T3.8 放**全体**：圆桌要读每个人的卡片；`team-layer.js` 少了谁，圆桌 agent 会在返回值里报 `NOT-IN-RUN <slug>`，日志记一行 `team.json members missing from this run: …`；那人在圆桌里原有的行不删也不更新，要带全体重跑。一个完整的调用：

```bash
node scripts/workflows/make_args.mjs team-base-skills --team product/<team> --set to=review
# → [{"scriptPath": ".../team-base-skills.js", "args": {"repo": …, "team": …, "scratch": …, "date": …, "members": [<一位>], "to": "review"}}, …]
```

把每个对象原样交给 Workflow 工具（`Workflow({scriptPath, args})`），同一条消息里一起发出。其余工作流只换名字，再用 `--set` 加上表里括号中的参数。

**续跑与预览。**
- 中断以后续跑：同样的调用加上 `resumeFromRunId: "<上次的 runId>"`。
- 第一次在真团队上跑之前，先用 `dry_run.mjs`（Node ≥ 18）预览每个 agent 会收到的 prompt，不花 token：`node scripts/workflows/dry_run.mjs scripts/workflows/team-<name>.js --team product/<team> --member <slug> --set KEY=JSON --out /tmp/<team>-prompts --strict --forbid 'bandit|Ada Example|Bo Sample'`。不给参数文件，参数就和 `make_args.mjs` 为真启动生成的一样；别拿 `examples/` 的参数文件预览自己的团队（那是虚构示例团队的值）。`team-layer.js`、`team-integrate.js` 预览时不给 `--member`：它们要全体成员。
- 改过工作流脚本或套件脚本，闸门是 `bash scripts/workflows/selftest.sh product/<一支已完成的团队>`（九个示例的 `--strict` 预览、已完成团队上的 `make_args.mjs` 与 `dry_run.mjs --team`、脚本编译、`team_check.py`；见 [README 第七节](../scripts/workflows/README.md#七改工作流之后)）。**别用 `node --check`**：运行时把脚本包进一个 async 函数，脚本末尾的顶层 `return` 是合法的，`node --check` 却一定报 "Illegal return statement"。

**人工检查点。** 对应主 `SKILL.md` 的 Phase 1.5 和 2.5：
1. T1 先用 `to: "review"` 跑，把调研摘要摆给用户看。这时就 commit 调研笔记 01–06（`bash scripts/team_commit.sh $T/$M "research($M): notes 01–06"`），用户看摘要期间容器可能被回收；
2. 再用 `from: "synthesis", to: "synthesis"` 跑，把提炼结果和 Roundtable Card 摆给用户看，确认视角没有重叠、座位表排得开；
3. 最后用 `from: "build"` 跑完。

第 2 步的提炼记录放在 `<scratch>/base-skills/<slug>/`，不在 git 里。scratch 丢了，第 3 步就没有输入：重跑 `from: "synthesis"`（每人约 1 个 agent），不用从调研重来。

T3.6 之后，把每人 08 里新增、降级的方法摆给用户看。

可以直接复制的命令如下。`<team>`、`<slug>`、`<date>`（工作流的 `date` 参数）换成实际值。变量在每个新 shell 里都要重新设一次：Bash 工具的每次调用都是新 shell。

提交一律用 `bash scripts/team_commit.sh <路径> "<说明>"`：先暂存，再查整个暂存区，有受版权保护的文件（任何文件夹里的 PDF、PostScript、DjVu、EPUB，抽出的 `txt/`）或 `private/` 下的文件（`README.md` 除外）就停下（退出码 3），不提交。一跑几小时的阶段（T3.2 获取、T3.5 读卡、T3.6 汇总）中途每 30–60 分钟提交一次检查点，如 `bash scripts/team_commit.sh $T "wip(<team>): T3.5 checkpoint"`：已完成批次的卡片可以先提交，其余由这一轮的闸门 agent 补齐。

```bash
T=product/<team>; M=<slug>
S=${TMPDIR:-/tmp}/<team>-scratch; mkdir -p $S      # 即工作流的 scratch（make_args.mjs 的默认值；所有阶段同一个）

# T0 定义：起草 team.json，再照 team-templates/team.example.json 的说明补 scholar、hint、living、student_mode、chase_hints
python3 scripts/new_team.py --init <team> --field "<领域与传统>" --members "Name One;Name Two;Name Three"
python3 scripts/new_team.py $T/team.json --lookup # 可选：从 DBLP 补 dblp / orcid / homepage（只补空的）
python3 scripts/new_team.py $T/team.json          # 铺目录；已存在的文件保留。确定只做轻量档加 --base-tier；有撞姓警告先改 surname
grep -rn --include='*.md' '{{' $T                 # 必须为空
grep -rn --include='*.md' '\[TODO' $T             # 待办清单：每条写明由哪一步填
python3 scripts/check_links.py $T                 # 0 broken；README 成员表指向各人 SKILL.md 的链接记为 pending（T1 写，T1 开始后仍缺就算坏链）
bash scripts/team_commit.sh $T "feat(<team>): scaffold"
node scripts/workflows/make_args.mjs team-base-skills --team $T --set to=review   # T1 的启动参数，每人一个

# T1 → T2 之后
python3 scripts/quality_check.py $T/$M/SKILL.md   # 每人 12/12（只给成员；圆桌不是研究Skill，不跑它）
python3 scripts/check_links.py $T                 # 0 broken
#   圆桌的闸门：每位成员都在 Team 表和座位表里、都有 Roundtable Card；每条 fault line 双方都有证据
grep -rn --include='*.md' -e '{{' -e '\[TODO' $T  # 模板闸门，见下面两行
#   深读档：只剩标给 T3 各步的项（DEEP-READING.md、各人 RESOURCES.md 的第 1 行和深读档占位行、README 和圆桌里标 T3.8 的项）
#   轻量档：必须为空。还有 DEEP-READING.md 或 RESOURCES.md 里留给深读档的项，就照模板里写的轻量档（base tier）写法改掉
python3 scripts/team_check.py $T --tier base      # 轻量档：上面这些一次查完（每人 12/12 和 Roundtable Card、链接、模板、git、座位表与 fault line），退出码 0
bash scripts/team_commit.sh $T "feat(<team>): base skills + roundtable"    # 轻量档到此完成

# T3.1 之后
python3 scripts/validate_works.py $T/$M           # 0 errors
python3 scripts/new_team.py $T/team.json --set-member $M scholar=<id> dblp=<pid>   # harvest 的 next 里给出的 id（team.json 缺的才有）
# T3.2 在主会话里跑，每人一个后台进程（推荐；harvest 的 acquire 默认 false。设成 true 时由 agent 起进程再轮询，不如这里稳）。
# 下面这条自己记 PID（bash -c 里的 $$ 就是 exec 之后的 python 进程），用 Bash 工具的 run_in_background 跑或末尾加 & 都行，
# 查进度的命令两种方式都适用。非英文的扫描件：加 --ocr-lang <语言>（如 deu、chi_sim），或先 export NUWA_OCR_LANG=<语言>
nohup bash -c 'echo $$ > "$1"; exec python3 scripts/acquire_fulltexts.py "$2"' _ $S/acq-$M.pid $T/$M > $S/acq-$M.log 2>&1 < /dev/null &
tail -n 3 $S/acq-$M.log; kill -0 $(cat $S/acq-$M.pid) 2>/dev/null && echo running || echo finished    # 查进度
# kill $(cat $S/acq-$M.pid)                       # 要中途停下时才用：按 PID 停，别用 pkill -f
bash scripts/team_commit.sh $T/$M "sources($M): publication list + open full texts"      # 等获取进程跑完再提交（中途可提交检查点）

# T3.3 补搜之后（chase 带 merge: false 时才要手动合并）。摘要文件是 papers/abstracts-chase-<date>-r<run>-<块>.json，
# 同一天重跑 run 加 1，不会覆盖没合并的文件；含 works.json 里没有的 ID 的文件会被整份留下、报出来（退出码 1）
python3 scripts/merge_chase.py $T/$M
bash scripts/team_commit.sh $T/$M "chase($M): open copies and abstracts"
# 想先看补搜范围：python3 scripts/chase_chunks.py $T/$M --out $S/chase/$M.json --date <date>（team-chase.js 的计划阶段跑的就是它）

# T3.4 切批：每轮一条命令，给全体成员各写 $S/batches-<slug>-r<N>.json（N = 下一轮，自动排除 $S 里其他轮的计划），打印 N
python3 scripts/plan_reading_batches.py $T --out-dir $S --no-abstract
#   某位成员打印「no full-text batches left」时，给他跑最后一轮：不带 --no-abstract，剩下的作品进摘要、元数据批次
python3 scripts/plan_reading_batches.py $T --out-dir $S --member $M
#   然后 team-read.js 每人一个：node scripts/workflows/make_args.mjs team-read --team $T --set round=<打印的 N>

# T3.5 每轮 team-read.js（round: N）之后
python3 scripts/verify_card_quotes.py $T/$M       # NOT FOUND 必须为 0
python3 scripts/mark_read_from_cards.py $T/$M
python3 scripts/team_status.py $T                 # Next 列写着每人下一步；最后一轮之后：未读行 = 0（中间轮次的 no-oa 行本来就未读）
bash scripts/team_commit.sh $T/$M "cards($M): round N"
# 读卡报的 REOCR（文字层乱码）/ WRONG-TEXT（文件是别的作品）：team-read 的 next 给出现成命令，形如
python3 scripts/acquire_fulltexts.py $T/$M --reocr S028 --drop S011   # 强制 OCR / 删掉错文件、行改回 no-oa
python3 scripts/plan_reading_batches.py $T/$M --out-dir $S --no-abstract --reread S028,S011   # 重新排进下一轮

# T3.6 之后
python3 scripts/quality_check.py $T/$M/SKILL.md   # 12/12
python3 scripts/check_ledger.py $T/$M             # 不带 --before：只查 SKILL.md 指向账本的锚点，必须 ✅
# 和汇总前对比（工作流的复核员已跑过，人工复核时再跑）：汇总按设计会改 front matter（researched 日期、description 里的数字）
# 和首次激活的免责声明，--allow 放行这两处，打印成「~ allowed」；剩下的每一行 ✗ 都是问题
python3 scripts/check_ledger.py $T/$M --before $S/$M-SKILL.before-synth-<date>.md --allow frontmatter,activation-disclaimer
bash scripts/team_commit.sh $T/$M "synth($M): deep-reading synthesis"
# 闸门两轮修复后仍不过：人工改好 SKILL.md，再用 team-synthesize.js 的 from: "verify"（只重跑复核和修复）或 "fix"（只跑闸门）

# T3.7：只给 SKILL.md 仍超预算的成员。开跑前从 git 存一份精简前的副本（工作流看到已有的副本会保留它，scratch 丢了也能再取）
git show HEAD:$T/$M/SKILL.md > $S/$M-SKILL.before-tighten-<date>.md
# T3.7 之后
python3 scripts/quality_check.py $T/$M/SKILL.md
python3 scripts/check_ledger.py $T/$M --before $S/$M-SKILL.before-tighten-<date>.md   # 不加 --allow，必须 ✅（无损）
bash scripts/team_commit.sh $T/$M "tighten($M): evidence to 09-evidence-ledger.md"

# T3.8 之后
python3 scripts/team_status.py $T                 # 各人进度
python3 scripts/team_status.py $T --coverage          # 11 列全表，原样是 DEEP-READING.md 的 Coverage
python3 scripts/team_status.py $T --coverage --short  # 5 列摘要，原样是 README 诚实边界里的表（由全表相加，不手算）
python3 scripts/check_links.py $T                 # 0 broken
grep -rn --include='*.md' -e '{{' -e '\[TODO' $T  # 必须为空；还有输出就照每条 TODO 写的来源补上（数字只取脚本输出）
python3 scripts/team_check.py $T                  # 交付闸门：第四节的检查一次跑完（含 fault line 两边的卡片 ID），退出码 0
bash scripts/team_commit.sh $T "docs(<team>): integrate the deep reading"

# T4 每次 team-increment.js 之后（工作流自己跑过这些闸门；人工复核时再跑）。备份名里的 <label> 是工作流的 label（默认 inc-<date>）
python3 scripts/verify_card_quotes.py $T/$M       # NOT FOUND 必须为 0
python3 scripts/check_ledger.py $T/$M --before $S/$M-SKILL.before-<label>.md --allow frontmatter-date,activation-numbers
bash scripts/team_commit.sh $T/$M "increment($M): <label>"   # 之后带全体成员跑 team-integrate.js，再跑 team_check.py
```

---

## 四、质量闸门

每道闸门都过了，才能进下一步。

| 闸门 | 命令 | 通过标准 | 什么时候跑 |
|---|---|---|---|
| 研究Skill自检 | `quality_check.py <M>/SKILL.md` | 12/12 | T1、T3.6、T3.7、T4 之后；SKILL.md 每次改动之后。只给成员：圆桌不是研究Skill（它会按人物Skill模式打分，只有 2/6），它的闸门见最后一行 |
| 发表全表 | `validate_works.py <M>`（也可给团队目录） | 0 errors（结构、ID、dup_of）；警告（近似重复、没有 DOI/arXiv/链接）逐条人看；条目数与 Scholar 总数对得上（没有 Scholar 主页时与 DBLP 记录数和主页 CV 对账，见第三节 T3.1） | T3.1 之后 |
| 摘录逐字 | `verify_card_quotes.py <M>` | 全部通过，NOT FOUND = 0 | 每轮读卡之后；汇总之前 |
| 读完 | `mark_read_from_cards.py <M>`，再 `team_status.py <team>` | 未读行 = 0 | 最后一轮（不带 `--no-abstract`）读卡之后；中间轮次不查 |
| 账本锚点 | `check_ledger.py <M>`（不带 `--before`） | SKILL.md 指向 `09-evidence-ledger.md` 的锚点都能解析 | T3.6 之后 |
| 精简无损 | `check_ledger.py <M> --before <scratch>/<slug>-SKILL.before-tighten-<date>.md`（不加 `--allow`） | 精简前的卡片 ID、「ID + 页码」引用和引文都还在 SKILL.md 或账本里；指向账本的锚点都能解析；front matter 和激活规则、诚信规则、学生模式各节逐字不变 | T3.7 之后（只有跑了 T3.7 的成员）。备份不在了就用 `git show <精简前的提交>:<M>/SKILL.md` 取回 |
| 汇总、增量没删东西 | T3.6：`check_ledger.py <M> --before <scratch>/<slug>-SKILL.before-synth-<date>.md --allow frontmatter,activation-disclaimer`；T4：`… --before <scratch>/<slug>-SKILL.before-<label>.md --allow frontmatter-date,activation-numbers` | 按设计会变的地方（front matter、免责声明或其中的数字）打印成 `~ allowed`；没有任何 ✗ 行 | T3.6、T4 之后（工作流的复核员已跑；人工复核时再跑） |
| 链接 | `check_links.py <team>` | 0 broken | T2、T3.8 之后；交付之前 |
| 覆盖 | `team_status.py <team> --coverage`，`team_status.py <team> --coverage --short` | DEEP-READING 的 Coverage 原样是 11 列全表；README 诚实边界原样是 5 列摘要（成员；作品数；全读 / 部分读；摘要 + 元数据；跳过），由脚本从全表相加，不手算 | T3.8；T4 之后的 T3.8 |
| 模板 | `grep -rn --include='*.md' -e '{{' -e '\[TODO' <team>` | 没有输出 | 轻量档 T2 之后；深读档 T3.8 之后；交付之前 |
| 提交 | `bash scripts/team_commit.sh <路径> "<说明>"`（查整个暂存区，退出码 3 = 停下） | 没有任何文件夹里的 PDF、PostScript、DjVu、EPUB，没有 `txt/`，`private/` 下只有 `README.md` | 每次 commit |
| 工作流脚本 | `node scripts/workflows/dry_run.mjs <工作流> <参数> --strict` | 退出码 0，没有警告。不用 `node --check`（顶层 `return` 在运行时合法，它一定报错） | 改过任何工作流之后 |
| 圆桌 | `team_check.py <team>` 的 roundtable 一项（加 `check_links.py`）；不跑 `quality_check.py` | 每位成员都在 Team 表里、在座位表里至少主讲一行、都有 7 项齐全的 Roundtable Card；3–6 条 fault line，每条都引用两位以上成员（深读档：两边都是 `[<slug> card <ID> p. N]`，卡片 ID 在该成员的卡片里都存在，不剩 "card evidence pending"）；不剩 `{{`，`[TODO` 只剩标给后续步骤的。能否真正辩起来仍要人看一眼 | T2、T3.8 |
| **交付（全部）** | `python3 scripts/team_check.py <team> [--tier base\|deep]` | 退出码 0：上面各行一次查完（team.json、链接、模板、git、README、圆桌、覆盖表；每人 12/12 与 Roundtable Card；深读档每人发表全表与索引、未读行、07–09 与 technique catalog、摘录、账本）。新容器里没有 `txt/` 时摘录一项跳过（—），先重跑 `acquire_fulltexts.py` | 轻量档 T2 之后；深读档 T3.8 之后；交付之前 |

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
| 非英文的扫描件 OCR 出来是乱码 | OCR 默认用 tesseract 的英文模型。（乱码检测只对拉丁字母的文字层看英文停用词比例；中文、俄文等文字的正常文字层不会再被当成乱码去 OCR） | 装语言包（`apt-get install tesseract-ocr-<语言>`，如 `deu`、`chi-sim`），再 `acquire_fulltexts.py <M> --ocr-lang <语言> --only <ID>`（如 `deu`、`chi_sim`、`eng+deu`）；整位成员都是这种语言就先 `export NUWA_OCR_LANG=<语言>`，`merge_chase.py` 重跑获取时也用它。非英文的 `txt/` 仍逐篇抽查，改过文本就重读相关卡片 |
| `pkill -f` 把自己的 shell 也杀了 | shell 的命令行里含有同一个模式 | 按确切的 PID kill |
| 后台的 `acquire_fulltexts.py` 没跑完就没了 | 在 Bash 工具调用里用 `&` 起的进程，可能随这次调用结束被收掉 | 用 Bash 工具的 run_in_background，或 `nohup … &`；两种都用第三节那条自己记 PID 的命令（`bash -c 'echo $$ > …; exec python3 …'`）。在新 shell 里写 `echo $! > pid` 只会写进空行，查进度就永远显示「已结束」 |
| 工作流慢，看上去只有 2 路在跑 | 并发 = min(16, CPU − 2) | 每人一个工作流，并行启动 |
| 读卡 agent 超时、同一篇被分派两次 | 批次太大；上一轮还在读 | core ≤110 页且 ≤5 篇；supplement ≤220 页且 ≤8 篇；>150 页的书单独一批；摘要 30 篇一批；后续轮次用 `plan_reading_batches.py --out-dir`（自动排除 scratch 里其他轮的计划，包括仍在读的） |
| 摘录 NOT FOUND | 转述冒充原文，或者页码不对 | 每张卡片最多 2 条摘录；改成原文，或者去掉引号改成转述；全部通过再汇总 |
| 标题改了，txt 对不上 | 文件名 slug 由标题和年份生成 | 重命名文件或修正年份，再跑 `acquire_fulltexts.py --only <ID>` |
| INDEX 被重置成 no-oa | 旧版脚本在没有本地文件时覆盖 | `git checkout -- <M>/references/sources/papers/INDEX.md` |
| 读卡轮次停不下来 | 每轮都只剩没有开放全文的作品 | `plan_reading_batches.py --out-dir` 会提示「no full-text batches left」：给这位成员跑最后一轮，不带 `--no-abstract`，剩下的作品进摘要、元数据批次 |
| 读卡 agent 报 REOCR（文字层乱码）或 WRONG-TEXT（文件是别的作品），之后没人管 | 获取脚本不会重抽已有的 txt，切批脚本把 unreadable 的卡片当作读完 | 照 team-read 的 `next`：`acquire_fulltexts.py <M> --reocr <ID,…>`（删 txt、强制 OCR）、`--drop <ID,…>`（删错文件、行改回 no-oa），再 `plan_reading_batches.py <M> --out-dir <scratch> --reread <ID,…>` 排进下一轮。乱码检测现在也看控制字符（占非空白字符三成以上就 OCR），DFO 的 S028 这类不会再漏 |
| 工作流日志说批次文件不存在、成员被跳过；T3.6/T4 找不到备份 | 各阶段用了不同的 scratch 目录 | 所有阶段用同一个 scratch：`make_args.mjs` 默认固定为 `${TMPDIR:-/tmp}/<team>-scratch` |
| 重跑获取后，旧团队的 INDEX.md 最后一行（汇总行）变了 | 旧版脚本写的汇总行格式不同（如 DFO 的 Conn、Scheinberg、Audet） | 正常：只有这一行变，内容不变，跟着这一次的提交一起提交即可 |
| `check_ledger.py` 退出码 2 | `--before` 的备份不存在：没跑 T3.7，或 scratch 丢了 | 没跑 T3.7 的成员只跑不带 `--before` 的锚点检查；scratch 丢了，用 `git show <精简前的提交>:<M>/SKILL.md` 取回 |
| `check_ledger.py --before` 报 front matter、Activation Rules 不同 | 拿汇总前（`before-synth`）或增量前（`before-<label>`）的备份对比，没加 `--allow`：这两步按设计会改 researched 日期、description 和免责声明里的覆盖数字 | 用 `--allow` 放行：T3.6 `frontmatter,activation-disclaimer`，T4 `frontmatter-date,activation-numbers`；T3.7 不放行。放行后剩下的每一行 ✗ 都是问题，不凭眼睛判断「是不是故意的」 |
| SKILL.md 膨胀到约 21k 词（DFO 当时） | 汇总时没有给字数预算 | `team-synthesize.js` 现在默认给 11,500 词预算并同时写 `09-evidence-ledger.md`；仍超预算再跑 T3.7 |
| 汇总提出的新方法站不住 | 排他性不过关 | 保留质疑复核；新的核心方法要有 ≥3 篇论文支撑，并过四重验证 |
| 容器重启，工作丢了 | 容器是临时的 | 每一步 commit；T1 在 `to: "review"` 之后就 commit 调研笔记；scratch 里的提炼记录丢了，重跑 T1 的 `from: "synthesis"` |
| 交付前模板闸门还有 `[TODO` | 某一步没清掉模板里标给它的项；轻量档留下了给深读档的项（DEEP-READING.md、RESOURCES.md 第 1 行和深读档占位行） | 每条 TODO 都写明由哪一步、按什么来源填：照它补上，数字只取脚本输出；轻量档照模板里的轻量档（base tier）写法改 |
| 暂存区里出现 PDF、`.ps`、`.djvu`、`.epub`、幻灯片 | `.gitignore` 排除 `product/` 下成员 `references/sources/` 里任何文件夹的 PDF、PostScript、DjVu、EPUB（不分大小写）和 `papers/txt/`，但幻灯片（`.ppt`、`.pptx`、`.key`）等其他格式不在内，团队目录不在 `product/` 下时也管不到（`new_team.py` 会检查并打印要加的规则） | 用 `scripts/team_commit.sh` 提交（它查整个暂存区）；漏掉的模式补进 `.gitignore` |
| `@<Surname>` 分不清是谁 | 队里有人同姓 | `surname` 写成 `"N. Higham"`、`"D. Higham"` 这样，队内唯一 |
| 工作流中断、被停，或者改了脚本 | — | 用同样的 `scriptPath` 和 `args`，加 `resumeFromRunId` 续跑，没改过的 agent 调用直接取缓存；也可以用 T1 的 `from`、T3.5 的 `overwrite: false` / `only`、T3.3 的 `only_chunks`、T3.6 和 T4 的 `from`（`verify`：人工修好之后只重跑复核和修复） |
| 改了 `only` / `only_chunks` 却把所有批次都重跑了 | 映射的键（成员 slug）拼错，这一位成员等于没有 `only` | 现在工作流发现键不是这次运行的成员、且有成员没对应的键时直接停下；`dry_run.mjs` 也警告。用 `make_args.mjs --set` 生成参数，slug 不对当场报错 |
| 书的正文读不到 | 正文不开放 | 读合法开放的部分（目录、勘误、增补、前言、已发表书评），作为 `B###` 条目，用 `team-increment.js`（`find: ["book-parts"]`）；批次名接着已有轮次编（如 `c5-01`；DFO 当时是手工读的，批次叫 `k01`）。书评按书评人的话写。不用影子图书馆 |
| WebSearch 突然全部失败 | 每个会话约 200 次的预算用完了（所有 agent 共用） | 工作流的 `search_budget` 把次数分到每个 agent 的 prompt 里（默认值见第六节的分配）；按第六节分会话跑：T1 一个会话，T3 另一个；补搜先用 curl 查 `chase_hints` 里的已知仓库，WebSearch 留给难找的。已经用完就在新会话里接着跑（工作流可续跑） |
| fault line 只有一方的证据 | 圆桌从成员简介拼出来 | 每条都要双方的卡片证据；成员简介指向各人的 technique catalog 和 08 |
| `merge_chase.py` 退出码 1，留下了一个补搜文件 | 文件里有 `works.json` / INDEX.md 里没有的 ID（例如写了 DOI、标题或自造的 ID），或者值不是字符串 | 整份文件留下、其余文件照常并入。把键改成这一块里的作品 ID 后重跑 `merge_chase.py` |
| 担心同一天重跑 chase 覆盖没合并的摘要 | — | 不会：文件名是 `abstracts-chase-<date>-r<run>-<块>.json`，计划 agent 取当天已有的最大 run 加 1，名字已存在时再加 `-b`、`-c` |
| 圆桌上 `quality_check.py` 只有 2/6 | 圆桌不是研究Skill，被按人物Skill模式打分 | 别拿它当闸门；圆桌的闸门见第四节最后一行 |
| `team-layer.js` 的日志里有 `team.json members missing from this run`（返回值里是 `NOT-IN-RUN <slug>`） | `members` 没放全体 | 带 `team.json` 里的全体成员重跑 |
| `node --check` 报 "Illegal return statement" | 工作流脚本末尾有顶层 `return`，运行时合法 | 用 `dry_run.mjs … --strict` 检查 |
| harvest 带 `acquire: true` 时拖很久、获取没跑完 | 由 agent 起后台获取进程再轮询 | 保持默认的 `acquire: false`，按第三节在主会话里跑 `acquire_fulltexts.py` |
| 非数学领域的卡片维度对不上（没有证明、没有数值实验） | D1–D8 按数学/计算类研究定 | T0 就在 `team.json` 里写 `card_dimensions`（如 `{"D3": "…", "D4": "…", "D5": "…"}`，按 [paper-reading-card.md](paper-reading-card.md) 第二节把 D3–D5 换成这个领域「证据怎么来」的环节），每个读卡 agent 照用，digest 字段名不变；仍不适用的维度写 `n/a`。只有没写 `card_dimensions` 又发现口径不一时，才用 `team-read.js` 的 `only` + `overwrite: true` 重读（最贵的阶段，能免则免） |

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

合计：深读档每人约 45 个 agent、1,100 万 token；这 220 个 agent 共约 32 agent-小时（每人约 6.5）。轻量档按工作流结构估：T1 每人 16–20 个 agent（quick 档 13–17），T2 每人 2 个、团队另加 4–5 个（圆桌、README、两位核查员，有问题时再加一位修复）；DFO 这两步没有计量 token。T3.8 现版每次 6–7 个；T4 现版多一位复核员，一批时每人 5–6 个。实际耗时 ≈ agent-小时 ÷ 同时在跑的 agent 数，所以要按第二节的办法把并行开足。

**WebSearch 的分配。** 每个会话约 200 次，所有 agent 共用，用完为止（DFO 在后期用完过）。工作流的 `search_budget` 默认按下面分（5 人团队）；按阶段分会话跑，每个会话都在预算内：

| 会话 | 阶段 | 每人 | 5 人合计 |
|---|---|---|---|
| 1 | T1 基础Skill（调研 agent 每个 5，复核 3，资源表 1，每轮评分 1） | 36 | 180 |
| 2 | T3.1 发表全表（Scholar 用 WebFetch，不算） | 2 | 10 |
| 2 | T3.3 补搜（按块均分） | 24 | 120 |
| 2 | T3.5 读卡（只给摘要批次） | 8 | 40 |
| 以后 | T4 增量（找材料的 agent） | 10 | 50 |

人少或某阶段要多搜，就调 `search_budget`；合计超过 200 的就拆到下一个会话（每一步都已 commit，工作流也能续跑）。

**怎么省：**

- **只做轻量档。** 不做 T3，省掉每人约 1,100 万 token。T0 就加 `--base-tier`，T2 用 `deep_tier: false`。
- **少精读。** 用 `plan_reading_batches.py --core-top 10`（默认 25），让精读的 core 变少；其余有全文的作品走 supplement 略读，每批页数上限是 core 的两倍。`--recent` 定哪一年起的作品一律精读（默认今年减 2），研究者近年很高产时往后挪。读卡占一半以上的成本。
- **跳过补搜。** 获取脚本没拿到全文的作品直接走摘要批次，30 篇一批，便宜得多。代价是证据变弱，要在诚实边界里写明。
- **不做书的增量。** 除非成员有核心著作。
- **T1 用 quick 档**（`tier: "quick"`，只跑调研 01–03）。代价是少了学生回忆、同行批评和研究轨迹，要在诚实边界里写明。
- **不跑 T3.7。** `team-synthesize.js` 已按预算同时写 ledger，SKILL.md 没超预算就不用精简。

---

## 七、规矩

1. **只用合法的开放获取来源**：arXiv、Unpaywall、作者主页、机构报告、开放仓库。不用 Sci-Hub 等影子图书馆，不绕付费墙。
2. **受版权保护的文件不进 git。** 任何文件夹里的 PDF、PostScript、DjVu、EPUB，以及抽出的 `txt/`，都只留在本地；`talks/`、`essays/` 里存的幻灯片和文章也一样。`.gitignore` 排除 `product/` 下成员 `references/sources/` 里任何文件夹的 PDF、PostScript、DjVu、EPUB 和 `papers/txt/`，但不管幻灯片等其他格式，不能全靠它：提交一律用 `bash scripts/team_commit.sh <路径> "<说明>"`，它会先查暂存区。提交的只有索引、摘要、卡片和汇总。
3. **`private/` 不读。** 只有用户自己放进材料并提出要求时才读，且内容永远不进公开文件。
4. **摘录逐字**，每条带页码，必须过 `verify_card_quotes.py`。看不懂或没读到的，写「未读」。
5. **保守更新**，规则见卡片模板第三节：只追加；已有方法只补证据；新的核心方法要 ≥3 篇论文并过四重验证。
6. **语言。** 成员Skill和卡片用 `team.json` 的 `language`。英语研究者的卡片用英语写，这样摘录才能逐字核对。
   - 团队文件的模板（README、圆桌、DEEP-READING、RESOURCES）是英文的。`team-layer.js` 按 `language` 写团队层，`team-integrate.js` 沿用文件已有的语言；模板里固定的英文段落（圆桌的协议、成员简报等）不一定会被翻译。非英文团队在 T2 之后检查这几个文件的语言是否统一。
   - OCR 默认用英文模型：非英文的扫描件用 `acquire_fulltexts.py --ocr-lang <语言>` 或环境变量 `NUWA_OCR_LANG`，`txt/` 仍逐篇抽查（见第五节）。
   - 卡片维度 D1–D8 按数学/计算类研究定。别的领域按 [paper-reading-card.md](paper-reading-card.md) 第二节换 D3–D5 的含义，T0 写进 `team.json` 的 `card_dimensions`，每个读卡 agent 照用（digest 字段名不变）；不适用的写 `n/a`。
7. **API 请求里不放用户的邮箱。** Unpaywall 用 noreply 地址，Crossref 不带邮箱。
8. **成员是基于公开作品模拟的视角，不代表本人观点。** README 和每个 Skill 的诚实边界都写明这一点。

---

## 八、增量更新与增删成员

**有新论文、新书时**，用 `team-increment.js`：

- **让工作流自己找**：`find: ["new-papers"]`（在世成员，`since` 默认取 `works.json` 的 harvested 日期）或 `find: ["book-parts"]`（书的开放部分，作为 `B###` 条目）。Prepare agent 会做这几件事：
  - 把新材料登记进 `works.json`；
  - 跑 `validate_works.py`、`acquire_fulltexts.py --only <新ID>` 和 `plan_reading_batches.py`；
  - 读卡（批次名接着已有轮次编，如 `c5-01`），保守并入（SKILL.md 净增不超过 `max_growth`，默认 400 词，细节进 09），再复核、修。
- **用户手里有合法副本时**：
  1. 按 DEEP-READING 的「How to extend」命名（`<ID>-<年份>-<标题前8词>.pdf`），放进 `papers/`；
  2. 在 `works.json` 加一行，带 note；
  3. 跑 `acquire_fulltexts.py <M> --only <ID>`；
  4. 用 `plan_reading_batches.py <M> --round <下一轮> --no-abstract --core-ids <ID> > $S/batches-<slug>-<label>.json` 写批次文件。读完的轮次不用 `--exclude`（有全文卡片的作品本来就跳过）；只有别的轮次还在读时才 `--exclude` 它们的计划（文件不在了只会警告）；
  5. 用 `team-increment.js` 的 `batch_files`（`{"<slug>": "<绝对路径>"}`）跑。旧名 `batchFiles`、`maxGrowth` 仍能用，运行开头会记一行日志提醒改名。
- 书的开放部分：补搜（T3.3）找到的目录、勘误、书评链接记在 `papers/book-leads.json`，`find: ["book-parts"]` 从它开始，只去搜它没覆盖的书。
- 增量闸门两轮修复后仍不过：人工改好，再用同一个 `label` 加 `from: "verify"`（只重跑复核和修复）或 `from: "fix"`。

两种做法之后都要跑 `team-integrate.js`，让 README、DEEP-READING 和圆桌显示新的覆盖。在世的成员每年跑一次 `new-papers`。

**加一个成员**（按这个顺序）：
1. 在 `team.json` 里加上这个人（`surname` 不能和队里已有的人重复，撞了脚本会警告），跑 `python3 scripts/new_team.py $T/team.json --add-member <slug>`（轻量档团队加 `--base-tier`）。它只铺这个人的目录，在 README 成员表里最后一位成员之后插一行，不改圆桌和 DEEP-READING。
2. 只为这个人跑 T1。
3. 带全体成员重跑 `team-layer.js`，把这个人写进圆桌的成员表、座位表和 fault lines。`team-integrate.js` 不会给新成员排座，所以这一步不能省。
   - 深读档团队：`team-layer.js` 看到已有卡片的成员，会保留 T3.8 写的带卡片证据的 fault lines、「Papers behind…」和深读档的诚实边界，只为新成员补内容；新成员那一方写「(card evidence pending for <slug>)」。跑完仍用 `git diff` 核对一遍，被误改的从 git 里恢复。
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
- [ ] 每位成员 `quality_check.py` 12/12，都有 `## Roundtable Card`（圆桌不跑 `quality_check.py`，按第四节最后一行检查）
- [ ] 每条 fault line 都有双方的证据；深读档要有双方的卡片证据
- [ ] 历史人物和在世成员的时间边界、调研日期写进了诚实边界；`private/` 下只有 `README.md` 被 git 跟踪
- [ ] 深读档：`validate_works.py` 0 errors，条目数与 Scholar 总数（没有主页时与 DBLP 记录数和 CV）对得上；`verify_card_quotes.py` 全部通过；最后一轮读卡之后 `team_status.py` 显示没有未读行；每人 `check_ledger.py` 锚点通过，跑过 T3.7 的成员 `check_ledger.py --before <精简前的备份>`（不加 `--allow`）通过
- [ ] `team_status.py --coverage` 的表原样贴进了 DEEP-READING.md；README 诚实边界的 5 列摘要原样是 `team_status.py --coverage --short` 的输出
- [ ] `check_links.py product/<team>` 0 broken；`grep -rn --include='*.md' -e '{{' -e '\[TODO' product/<team>` 没有输出（轻量档也一样：DEEP-READING.md 和 RESOURCES.md 里给深读档留的项按模板的轻量档写法改掉了）
- [ ] 每次提交都用了 `scripts/team_commit.sh`：git 里没有任何文件夹下的 PDF、PostScript、DjVu、EPUB，没有 `txt/`，`private/` 下只有 `README.md`（`git ls-files product/<team> | grep -Ei '\.(pdf|ps|ps\.gz|djvu|epub)$|/txt/|/private/'` 只列出 `private/README.md`）；每一步都已 commit
- [ ] `python3 scripts/team_check.py product/<team>` 退出码 0（上面能自动查的都在里面；摘录一项显示 — 时先重跑 `acquire_fulltexts.py` 恢复 `txt/`）
- [ ] 用一个真实问题试一次圆桌：4 个检查点都出现，最终方案每条都有归属，并有 ✅ 签字或 ⚠️ 异议
