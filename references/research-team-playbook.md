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

`OPENALEX_API_KEY` 不是必需的。要用时，在同一处环境设置里加成环境变量，不要贴进对话。连通性自检（000 或 403 表示不通；Scholar 用 WebFetch 取一页试）：

```bash
for u in https://sparql.dblp.org/sparql https://api.crossref.org/works https://api.datacite.org/dois \
         https://arxiv.org/search/ https://api.unpaywall.org/; do
  printf '%s %s\n' "$(curl -s -o /dev/null -m 20 -w '%{http_code}' "$u")" "$u"; done
```

**依赖。** 写进环境设置里的 Setup script，新会话会自动装好：

```bash
pip install pypdfium2 pillow
apt-get install -y tesseract-ocr ghostscript     # OCR；ps2pdf 随 ghostscript 安装
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
| T0 定义 | `new_team.py --init` → 手填 → `new_team.py` | 选人结果 → `team.json`、团队目录骨架、README / 圆桌 / DEEP-READING 模板 | `.md` 里不剩 `{{`；`[TODO: …]` 就是待办 | 0 | — |
| T1 基础Skill | `team-base-skills.js` | 成员信息 → `<M>/SKILL.md`（含 Roundtable Card）、`research/01–06` | `quality_check.py` 12/12 | 17–20 agent（标准档；quick 档只跑调研 01–03） | 每人一个工作流 |
| T2 团队层 | `team-layer.js` | 各人的 Roundtable Card → README、圆桌 SKILL.md、各人 RESOURCES.md | `check_links.py` 0；每人都有 Roundtable Card | 2 agent，团队另加 5 | 团队一次 |
| T3.1 发表全表 | `team-harvest.js`（DBLP 走 `dblp_works.py`） | Scholar id、DBLP、Crossref → `works.json`、`scholar.md`；再做独立审计 | `validate_works.py` 0 errors；条目数与 Scholar 总数对得上 | 3 agent / 40 万 token | 每人一个 |
| T3.2 开放全文 | `acquire_fulltexts.py` | `works.json` → PDF、`txt/`、`INDEX.md`、`abstracts.json` | INDEX 行数 = `works.json` 条目数 | 0 agent；arXiv 请求间隔 3 秒 | 每人一个后台进程 |
| T3.3 补搜、合并 | `team-chase.js`（最后自动跑 `merge_chase.py`） | 仍为 no-oa 的作品（每块 20 篇）→ PDF、摘要 → 并入 `abstracts.json`、`abstract-sources.json`，重跑获取 | 只用合法开放来源；在首页核对作者；报告新增全文数 | 5 / 90 万 | 每人一个 |
| T3.4 切批 | `plan_reading_batches.py`，分轮跑 | INDEX → 角色（写回 INDEX）、批次计划 JSON（放 scratch） | 批次不超上限；后续轮次 `--exclude` 之前各轮的计划 | 0 | 每人一个 |
| T3.5 读卡 | `team-read.js`，每轮一次 | 批次计划与全文 → `cards/<bid>.md` + `.digest.json` | `verify_card_quotes.py` 全部通过；`mark_read_from_cards.py` 之后没有未读行 | 22 / 580 万 | 每人一个；各轮之间串行 |
| T3.6 汇总 | `team-synthesize.js` | 卡片 → 07、08、09、`technique-catalog.md`，SKILL.md 保守更新 | 质疑者复核；12/12；字数不超预算 | 6 / 240 万 | 每人一个 |
| T3.7 精简 | `team-tighten.js`（SKILL.md 仍超预算时才跑） | SKILL.md 精简到约 11.5k 词，长证据移入 `09-evidence-ledger.md` | `check_ledger.py` 通过；12/12 | 3 / 70 万 | 每人一个 |
| T3.8 团队整合 | `team-integrate.js` | 各人的 08 → README 诚实边界、DEEP-READING.md、圆桌 fault lines | 覆盖表与 `team_status.py --coverage` 一致；`check_links.py` 0 | 团队一次，4 / 100 万 | 团队一次 |
| T4 增量 | `team-increment.js` | 书的开放部分、新论文 → 新批次卡片，再保守更新 | 与 T3.5–T3.7 相同 | 每位书作者 4 / 100 万 | 每人一个 |

成本列里 T3 以后是 DFO 的实测（第六节）；T1、T2 是按工作流结构估的 agent 数，DFO 没有单独计量。

**工作流参数。** 九个工作流共用 5 个参数：
- `repo`：仓库的绝对路径；
- `team`：`product/<team>`；
- `scratch`：绝对路径，放批次计划、补搜分块和备份；
- `date`：`YYYY-MM-DD`；
- `members`：从 `team.json` 原样拷贝的成员对象数组。

按成员跑的工作流，`members` 只放一位，每人起一个工作流，在同一条消息里一起发出。T2 和 T3.8 要等所有人，`members` 放全体。一个完整的调用：

```js
Workflow({scriptPath: "<repo>/scripts/workflows/team-base-skills.js",
          args: {repo: "<repo>", team: "product/<team>", scratch: "<scratch>", date: "YYYY-MM-DD",
                 members: [/* team.json 里这一位成员的对象，原样拷贝 */], to: "review"}})
```

其余工作流只换 `scriptPath` 和下表的特有参数：

| 工作流 | `members` | 特有参数（默认值） | 工作流自己跑的闸门 |
|---|---|---|---|
| `team-base-skills.js` | 一位 | `from` / `to`（`research` … `refine`）；`tier`（`standard` / `quick`）；`word_budget`（8000）；`example_team` | `merge_research.py`、12/12、链接 |
| `team-layer.js` | 全体 | `deep_tier`（true：保留留给 T3.8 的 TODO）；`example_team` | 链接 0、不剩 `{{`、12/12 |
| `team-harvest.js` | 一位 | `audit`（true）；`acquire`（false；设为 true 时顺带跑 T3.2） | `validate_works.py` |
| `team-chase.js` | 一位 | `chunk_size`（20）；`max_searches`（4）；`skip_ids`；`only_chunks`；`merge`（true） | `merge_chase.py`、`validate_works.py` |
| `team-read.js` | 一位 | `round`（1）；`batchFiles`（默认 `<scratch>/batches-<slug>-r<round>.json`）；`only`；`overwrite`（false：已写完的批次跳过，可续跑）；`retry`（true） | 合并摘要、修正摘录、回填 Read 列 |
| `team-synthesize.js` | 一位 | `wordBudget`（11500，09 同时写）；`maxWords`；`notes` | 摘录没有全部通过的成员直接拦下，不改文件 |
| `team-tighten.js` | 一位 | `targetWords`（11500）；`maxWords`；`force` | `check_ledger.py`、12/12、字数 |
| `team-integrate.js` | 全体 | `rootReadme`（false）；`newFaultLines`（2） | 覆盖表、链接 0、fault line 双方都有卡片 |
| `team-increment.js` | 一位 | `label`；`find`（`book-parts` / `new-papers`）；`batchFiles`；`since`；`what`；`maxGrowth`（400 词） | 同 T3.5–T3.7 |

**人工检查点。** 对应主 `SKILL.md` 的 Phase 1.5 和 2.5：
1. T1 先用 `to: "review"` 跑，把调研摘要摆给用户看；
2. 再用 `from: "synthesis", to: "synthesis"` 跑，把提炼结果和 Roundtable Card 摆给用户看，确认视角没有重叠、座位表排得开；
3. 最后用 `from: "build"` 跑完。

T3.6 之后，把每人 08 里新增、降级的方法摆给用户看。

可以直接复制的命令如下。`<team>`、`<slug>` 换成实际值。

```bash
T=product/<team>; M=<slug>
S=${TMPDIR:-/tmp}/<team>-scratch; mkdir -p $S      # 即工作流的 scratch（绝对路径）

# T0 定义：起草 team.json，再照 team-templates/team.example.json 的说明补 scholar、hint、living、student_mode、chase_hints
python3 scripts/new_team.py --init <team> --field "<领域与传统>" --members "Name One;Name Two;Name Three"
python3 scripts/new_team.py $T/team.json          # 铺目录；已存在的文件保留
grep -rn --include='*.md' '{{' $T                 # 必须为空
grep -rn --include='*.md' '\[TODO' $T             # 待办清单
git add $T && git commit -m "feat(<team>): scaffold"

# T1 → T2 之后
python3 scripts/quality_check.py $T/$M/SKILL.md   # 每人 12/12
python3 scripts/check_links.py $T                 # 0 broken
git add $T && git commit -m "feat(<team>): base skills + roundtable"    # 轻量档到此完成

# T3.1 之后（harvest 带 acquire: true 时跳过 acquire 这一行）
python3 scripts/validate_works.py $T/$M           # 0 errors
python3 scripts/acquire_fulltexts.py $T/$M > $S/acq-$M.log 2>&1 &      # T3.2，每人一个后台进程

# T3.3 补搜之后（chase 带 merge: false 时才要手动合并）
python3 scripts/merge_chase.py $T/$M

# T3.4 切批：第 1 轮；之后每轮 --exclude 之前各轮的计划（含仍在读的），最后一轮去掉 --no-abstract
python3 scripts/plan_reading_batches.py $T/$M --no-abstract > $S/batches-$M-r1.json
python3 scripts/plan_reading_batches.py $T/$M --round 2 --no-abstract --exclude $S/batches-$M-r1.json > $S/batches-$M-r2.json

# T3.5 每轮 team-read.js（round: N）之后
python3 scripts/verify_card_quotes.py $T/$M       # NOT FOUND 必须为 0
python3 scripts/mark_read_from_cards.py $T/$M
git add $T/$M && git commit -m "cards($M): round N"

# T3.6 / T3.7 之后（精简前的备份由工作流存在 scratch 里）
python3 scripts/quality_check.py $T/$M/SKILL.md
python3 scripts/check_ledger.py $T/$M --before $S/$M-SKILL.before-tighten-<date>.md

# T3.8 之后
python3 scripts/team_status.py $T                 # 各人进度
python3 scripts/team_status.py $T --coverage      # 贴进 DEEP-READING.md 和 README 的诚实边界
python3 scripts/check_links.py $T
```

---

## 四、质量闸门

每道闸门都过了，才能进下一步。

| 闸门 | 命令 | 通过标准 | 什么时候跑 |
|---|---|---|---|
| 研究Skill自检 | `quality_check.py <M>/SKILL.md` | 12/12 | T1、T3.6、T3.7 之后；SKILL.md 每次改动之后 |
| 发表全表 | `validate_works.py <M>`（也可给团队目录） | 0 errors（结构、ID、dup_of）；警告（近似重复、没有 DOI/arXiv/链接）逐条人看 | T3.1 之后 |
| 摘录逐字 | `verify_card_quotes.py <M>` | 全部通过，NOT FOUND = 0 | 每轮读卡之后；汇总之前 |
| 精简无损 | `check_ledger.py <M> --before <scratch 里精简前的备份>` | 精简前的卡片 ID、「ID + 页码」引用和引文都还在 SKILL.md 或账本里；指向账本的锚点都能解析；激活规则、诚信规则、学生模式各节逐字不变 | T3.7 之后 |
| 链接 | `check_links.py <team>` | 0 broken | T2、T3.8 之后；交付之前 |
| 覆盖 | `team_status.py <team> --coverage` | 表格贴进 DEEP-READING 和 README；未读行 = 0 | T3.8 |
| 模板 | `grep -rn --include='*.md' -e '{{' -e '\[TODO' <team>` | 没有输出 | 交付之前 |
| 圆桌 | 人工检查 | 每人都有 Roundtable Card；每条 fault line 都有双方的卡片证据 | T2、T3.8 |

---

## 五、失败模式与降级

| 症状 | 原因 | 处理 |
|---|---|---|
| curl Scholar 得到 403 或空页 | Scholar 没有 API，拦 curl | 用 WebFetch 取 `citations?user=<id>&hl=en&cstart=N&pagesize=50`，prompt 要求逐字 “return every row as JSON lines + TOTAL=”；两次计数对不上，改用 `pagesize=20` 重取；再按 `sortby=pubdate` 做一次独立审计，补漏 |
| `dblp.org` 返回 Anubis 页面 | bot wall | 用 `sparql.dblp.org/sparql`（POST `query=`，`Accept: application/sparql-results+json`），即 `dblp_works.py` |
| OpenAlex 429 | 共享 IP 的免费额度 | 设 `OPENALEX_API_KEY`，或者不用它 |
| `export.arxiv.org` 406 | 云端 IP 被拒 | 用 `arxiv.org/search` 网页检索（脚本已内置） |
| 某个技术报告系列里匹配到别人的报告 | 只按标题词匹配 | 核对第 1 页上的作者 |
| `.ps` 文件、扫描件、文字层乱码 | 没有可用的文字层 | `.ps` 先用 `ps2pdf` 转成 PDF；扫描件和乱码文字层（英文停用词比例 < 0.01）由 `acquire_fulltexts.py` 自动 OCR；自己跑 tesseract 时设 `OMP_THREAD_LIMIT=1`，否则负载会爆掉；OCR 之后重读相关卡片 |
| `pkill -f` 把自己的 shell 也杀了 | shell 的命令行里含有同一个模式 | 按确切的 PID kill |
| 工作流慢，看上去只有 2 路在跑 | 并发 = min(16, CPU − 2) | 每人一个工作流，并行启动 |
| 读卡 agent 超时、同一篇被分派两次 | 批次太大；上一轮还在读 | core ≤110 页且 ≤5 篇；supplement ≤220 页且 ≤8 篇；>150 页的书单独一批；摘要 30 篇一批；第 2 轮 `--exclude` 仍在读的批次文件 |
| 摘录 NOT FOUND | 转述冒充原文，或者页码不对 | 每张卡片最多 2 条摘录；改成原文，或者去掉引号改成转述；全部通过再汇总 |
| 标题改了，txt 对不上 | 文件名 slug 由标题和年份生成 | 重命名文件或修正年份，再跑 `acquire_fulltexts.py --only <ID>` |
| INDEX 被重置成 no-oa | 旧版脚本在没有本地文件时覆盖 | `git checkout -- <M>/references/sources/papers/INDEX.md` |
| SKILL.md 膨胀到约 21k 词（DFO 当时） | 汇总时没有给字数预算 | `team-synthesize.js` 现在默认给 11,500 词预算并同时写 `09-evidence-ledger.md`；仍超预算再跑 T3.7 |
| 汇总提出的新方法站不住 | 排他性不过关 | 保留质疑复核；新的核心方法要有 ≥3 篇论文支撑，并过四重验证 |
| 容器重启，工作丢了 | 容器是临时的 | 每一步 commit |
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

合计：深读档每人约 45 个 agent、1,100 万 token；这 220 个 agent 共约 32 agent-小时（每人约 6.5）。轻量档按工作流结构估：T1 每人 17–20 个 agent，T2 每人 2 个、团队另加 5 个；DFO 这两步没有计量 token。实际耗时 ≈ agent-小时 ÷ 同时在跑的 agent 数，所以要按第二节的办法把并行开足。

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
2. **PDF 和 `txt/` 不进 git。** `.gitignore` 已经排除了它们。提交的只有索引、摘要、卡片和汇总。
3. **`private/` 不读。** 只有用户自己放进材料并提出要求时才读，且内容永远不进公开文件。
4. **摘录逐字**，每条带页码，必须过 `verify_card_quotes.py`。看不懂或没读到的，写「未读」。
5. **保守更新**，规则见卡片模板第三节：只追加；已有方法只补证据；新的核心方法要 ≥3 篇论文并过四重验证。
6. **语言。** 成员Skill和卡片用 `team.json` 的 `language`。英语研究者的卡片用英语写，这样摘录才能逐字核对。
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

**加一个成员**：
1. 在 `team.json` 里加上这个人，跑 `python3 scripts/new_team.py $T/team.json --add-member <slug>`。它只铺这个人的目录，在 README 成员表里插一行，不改圆桌和 DEEP-READING。
2. 只为这个人跑 T1（深读档还要跑 T3）。
3. 带全体成员重跑 `team-layer.js`（深读档重跑 `team-integrate.js`），把这个人写进座位表和 fault lines。

**减一个成员**：
1. 从 `team.json` 删掉，移走这个人的目录。
2. 带剩下的成员重跑 `team-layer.js` 或 `team-integrate.js`，删掉座位表、fault lines 和 README 里提到这个人的地方。
3. `check_links.py` 必须为 0。

---

## 九、完成检查清单

- [ ] 3–6 人，视角互补；座位表每行有 2 位主讲 + 1 位挑战者（只有一人有证据的行，挑战者写 —）；不在队里的学派写进了 `Outside the Team`
- [ ] 每位成员 `quality_check.py` 12/12，都有 `## Roundtable Card`
- [ ] 每条 fault line 都有双方的证据；深读档要有双方的卡片证据
- [ ] 历史人物和在世成员的时间边界、调研日期写进了诚实边界；`private/` 下只有 `README.md` 被 git 跟踪
- [ ] 深读档：`validate_works.py` 0 errors；`verify_card_quotes.py` 全部通过；`team_status.py` 显示没有未读行；跑过 T3.7 的成员 `check_ledger.py` 通过
- [ ] `team_status.py --coverage` 的表贴进了 DEEP-READING.md 和 README 的诚实边界，两处数字一致
- [ ] `check_links.py product/<team>` 0 broken；`grep -rn --include='*.md' -e '{{' -e '\[TODO' product/<team>` 没有输出
- [ ] `git status` 里没有 PDF、`txt/` 或 `private/` 下的文件；每一步都已 commit
- [ ] 用一个真实问题试一次圆桌：4 个检查点都出现，最终方案每条都有归属，并有 ✅ 签字或 ⚠️ 异议
