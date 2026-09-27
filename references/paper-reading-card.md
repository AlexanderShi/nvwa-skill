# 论文卡片（研究Skill · 全文深读用）

> 研究Skill深读阶段：每读一篇论文写一张卡片，追加到 `references/research/07-paper-cards.md`。卡片是「他怎么做研究」的逐篇证据，最后汇总回 SKILL.md 的研究方法。
>
> 结构改编自 [AppleCG/academic-research-workflow](https://github.com/AppleCG/academic-research-workflow) 的 `research-distiller`（MIT License）：借用了「先声明意图」「材料角色」「每个维度都写可迁移手法」「只追加、冲突标为变体」「保守更新」五个做法。原版的8个维度面向社科人文并明确排除数学推导；这里换成数学/计算类研究（优化、数值分析、理论CS等）的维度。
>
> **实际布局**（`product/dfo-team` 五个研究Skill的深读，2026-09，795张卡片）：卡片按阅读批次写在 `references/research/cards/<批次>.md`，旁边配一个机读的 `<批次>.digest.json`；`07-paper-cards.md` 只做索引。见第四节。

---

## 一、开读前：声明意图（必做）

每一批深读开始前写三行，写在该批次文件（`cards/<批次>.md`，见第四节）的开头：

```
本批目标：[想从这批论文里看清什么？例：Scheinberg 如何把确定性方法改造成随机oracle版本]
聚焦维度：[从下方 D1–D8 选；或自定义维度]
材料角色：[每篇论文的角色，见下表]
```

| 角色 | 读法 | 卡片 |
|------|------|------|
| **core** | 全文精读 | 完整卡片（所选维度全写） |
| **contrast** | 精读与核心样本不同的部分 | 只写差异 |
| **supplement** | 读摘要、引言、贡献段、结论 | 简版卡片（D1、D7、D8 + 一句话方法关联） |
| **background** | 不单独写 | 只在其他卡片里被引用 |

角色记录在 `references/sources/papers/INDEX.md` 的 Role 列（`scripts/fetch_fulltexts.py` 默认被引前20篇为 core，其余 supplement，可手改）。

用 `scripts/acquire_fulltexts.py` 建索引时，core 与 supplement 由 `scripts/plan_reading_batches.py` 写入：被引前25篇、SKILL.md 已提到的、近年的、访谈/回忆录/随笔为 core；其余有全文的为 supplement。skip（不写卡片）不由它判断：专利、talk 由 acquire_fulltexts.py 按 works.json 的 kind 设为 skip；非本人作品用 plan_reading_batches.py --skip-ids 或手改 INDEX 的 Role 列；已有的 skip 会保留。它同时把论文切成阅读批次，一批交给一个深读 agent。

---

## 二、卡片维度（D1–D8）

每个维度最后一行都是 **可迁移手法**：这篇论文里，哪个做法是学生可以照着做的？写不出可迁移手法的维度，宁可留空。

| 维度 | 要提取的 | 证据位置 |
|------|---------|---------|
| **D1 问题与切口** | 从哪里切进来：旧方法的哪个假设太强？哪个现象没解释？哪个应用逼出来的？问题陈述的形式 | 摘要、引言前两段 |
| **D2 核心想法与算法设计** | 一句话关键洞察；相对最近的经典方法**改了什么、没改什么**；为什么是这个改法 | 引言末、算法章节 |
| **D3 假设与模型** | 光滑性、噪声/oracle 模型、约束类型；哪些假设是为了证明方便（作者承认的） | 假设段、定理前 |
| **D4 分析与证明技巧** | 证明骨架（势函数、随机过程、计数论证、反例构造……）；关键引理的模式；复杂度的形式与常数依赖 | 分析章节、附录 |
| **D5 数值实验** | 测试集、基线、比较口径（按函数评估数还是迭代数）、噪声设置、画什么图、是否报告失败案例 | 实验章节 |
| **D6 文献定位** | 自称延续/修正/推翻谁；如何评价前人（直接批评还是重新表述）；引谁不引谁 | 引言、相关工作 |
| **D7 写作与修辞** | 贡献句的典型句式；核心论点首次出现的位置；hedging 的密度；定理与直觉解释的配比 | 全文 |
| **D8 贡献与局限** | 贡献层次（理论/算法/软件/应用）；局限怎么写（具体还是套话）；给出的未来方向 | 贡献段、结论 |

**换领域时改维度。** D1–D8 是按数学/计算类研究定的。别的领域（看 `team.json` 的 `field`）按下面的办法换，把换法写进每批开头的「聚焦维度」；`cards/` 里已有批次的，先照已有批次开头的换法，让同一个人的各批口径一致。研究团队在 T0 就把换法写进 `team.json` 的 `card_dimensions`（如 `{"D3": "材料与史料批判", "D4": "论证结构", "D5": "反例与对话者"}`），所有读卡 agent 照同一份用，不必各自换、事后再抽查。不用改这份文件：
- D1、D2、D6、D7、D8 基本通用，照用。
- D3–D5 换成这个领域里「证据怎么来」的环节。例如实验科学：D3 实验系统与对照、D4 测量与统计分析、D5 实验与复现；社会科学：D3 理论与假设、D4 识别策略或研究设计、D5 数据与实证结果；人文或史学：D3 材料与史料批判、D4 论证结构、D5 反例与对话者；工程与系统：D3 需求与约束、D4 设计取舍、D5 评测口径与基线。
- 某一维度对某篇作品没有意义（例如没有证明），写 `n/a`，不硬凑。团队工作流 `team-read.js` 的 prompt 已允许这样写。
- digest 的字段名不变（改的是含义，不是键）：比如社会科学团队的 `proof_devices` 放识别策略、`experiments` 放数据与实证结果。`verify_card_quotes.py`、`mark_read_from_cards.py` 和汇总工作流按字段名读 digest，改了键它们就读不到。

### 卡片格式

```markdown
### [序号] 标题（venue 年份，arXiv/DOI）
**角色**: core / contrast / supplement · **合作者**: … · **在研究轨迹中的位置**: …

- **D1 问题与切口**: …（页码/章节）
  - 可迁移手法: …
- **D2 核心想法**: …
  - 可迁移手法: …
- …（只写本批意图选中的维度）

**方法关联**: 佐证 SKILL.md 的 Method N（实践证据 ✅）/ 与 Method M 矛盾（变体 ⚠）/ 新模式候选（记入候选池）
**原文摘录**（≤2句，带页码）: "…"
```

规则：
- 每条都带页码或章节号；摘录只用原文，不转述成引号
- 看不懂或没读到的部分写「未读」，不猜

---

## 三、汇总回 SKILL.md：保守更新

深读几十上百篇论文，最大的风险不是漏读，而是把SKILL.md写肿、写散。汇总时守住以下规则：

1. **只追加、不覆盖**：卡片只往 `07-paper-cards.md` 追加。新卡片与旧结论矛盾 → 标为「变体」，不删旧的
2. **已有方法只补证据**：卡片佐证了已有的 Method N → 更新它的「实践」证据和言行一致标注，不新增方法
3. **新方法的门槛**：同一模式在 **≥3篇** 不同论文的卡片里出现、且通过四重验证（见 `research-extraction-framework.md` 第三节），才进核心研究方法；否则留在候选池
4. **拒绝无增益的更新**：如果现有方法已经覆盖、或解释力更强，就拒绝更新，哪怕新材料很多。判断标准是框架的融贯性和解释力，不是新旧
5. **来源可追溯**：SKILL.md 里每条新增证据都指向卡片序号

汇总完成后重跑 `python3 scripts/quality_check.py <SKILL.md>`，并更新 `references/sources/RESOURCES.md`。

---

## 四、卡片文件布局（实际采用）

`product/dfo-team` 五个研究Skill的深读（2026-09）用的是下面的布局，后续深读照此执行：

```
references/research/
├── cards/
│   ├── <批次>.md                 # 一个阅读批次的全部卡片（给人读）
│   └── <批次>.digest.json        # 同一批卡片的机读版（给脚本读）
├── 07-paper-cards.md             # 卡片索引：每篇作品一行（阅读深度、所在批次文件、方法关联、一句话贡献）
└── 08-deep-reading-synthesis.md  # 汇总：第三节的保守更新先在这里写成提案，再改 SKILL.md
```

- **批次名**由 `plan_reading_batches.py` 生成，首字母是批次类型：
  - `c`：core
  - `s`：supplement
  - `b`：book，超过150页，按章读
  - `a`：abstract，没有全文，只写摘要级或元数据级卡片

  第1轮的批次名形如 `c01`，之后各轮形如 `c2-01`、`a2-03`、`s4-01`……（`--round N` 决定中间的数字）。
  - **增量**（`team-increment.js`，T4）接着已有的轮次编号：成员已有卡片最高到第4轮，增量就是第5轮，批次名形如 `c5-01`、`a5-01`。增量工作流用 `--core-ids` 把新条目定为 core，所以有文本、不到150页的书的开放部分（`B` 条目）落进 `c` 批次，没有文本的落进 `a` 批次。
  - **手工命名的批次**也可以，只要批次文件开头写清是什么。DFO 团队的书的开放部分是在有增量工作流之前手工读的，四位书作者各有一个 `k01`；`team-synthesize.js` 按批次文件开头识别它们。
  - 每轮用新的 `--round` 编号，否则批次名会和已有的卡片文件撞名（`team-read.js` 默认跳过已有卡片的批次）；还在读的轮次的计划要 `--exclude`，同一篇作品才不会被派两次（见 `research-extraction-framework.md` 第十二节）。用 `plan_reading_batches.py … --out-dir <scratch>` 时这两件事都自动做：轮次取已有计划和已有卡片批次的最大轮次加 1，scratch 里其他轮的计划自动排除。
- **作品 ID**（`works.json` 与 INDEX.md 里的 ID，卡片按它引用；`scripts/validate_works.py` 只认下面这些字母，别的字母要加 `--extra-id-letters`）：
  - `S`：Google Scholar 条目，按 Scholar 引用排序编号
  - `D`：Scholar 上没有、只在 DBLP / Crossref 等书目库里的作品
  - `H`：只在作者主页或简历上的作品
  - `R`：机构报告系列里对不上 Scholar 条目的报告
  - `X`：关于本人的外部文献：访谈、口述史、回忆录
  - `B`：书的开放部分，见下一条
- **`B` 条目只收合法开放的部分**：出版社或作者公开的目录、前言等前页、样章、勘误、增补，以及能公开读到的已发表书评。书的正文不开放就不读，不用影子图书馆。每条在 `works.json` 里带一个 `note`，写明是什么、是谁的话、怎么读：
  - **书评是书评人的话**，卡片按书评人的视角写（「书评人认为……」），不当作者本人的方法证据；它进同行批评（`05-peer-critique.md`）。
  - **目录只读标题**：可以推断全书结构（先讲什么、什么单独成章、什么没写），推断要标明；不编章节内容。
  - `team_status.py` 把 `B` 条目单独计入 Book material 列，不算进研究作品。
- **批次文件开头**写第一节的三行意图，再加一行「文件页码与印刷页码的对应」。页码一律用抽取文本里的 `[[page N]]` 标记。
- **卡片**按第二节的格式写，一篇一张。标题行后注明这篇读到什么深度：全文、部分、摘要、元数据，或无法读取。
- **`07-paper-cards.md`** 只做索引，每张卡片一行，内容取自 digest 字段（id、year、title、read_level、批次文件、method_links、contribution）。团队模式里由 `team-synthesize.js`（T3.6）用 python 从全部 digest 生成，`team-increment.js`（T4）给新卡片按原格式加行；手动深读时照相邻行的格式按 digest 写一行，卡片改了就同步改这一行。第三节的「只追加」在这种布局下，指的是往 `cards/` 追加新的批次文件，不改旧卡片。

### digest.json 字段

每个 `<批次>.digest.json` 是一个数组，每张卡片对应一个对象：

| 字段 | 类型 | 含义 |
|------|------|------|
| `id` | 字符串 | INDEX.md 里的 ID（如 `S012`） |
| `year`、`title` | 字符串 | 年份、标题 |
| `read_level` | 字符串 | `full` / `partial` / `abstract` / `metadata` / `unreadable` |
| `contribution` | 字符串 | 一句话贡献（07索引用） |
| `problem_entry` | 字符串 | D1 问题与切口 |
| `key_idea` | 字符串 | D2 核心想法 |
| `assumptions` | 字符串 | D3 假设与模型 |
| `proof_devices` | 字符串数组 | D4 证明手法，每条带页码 |
| `experiments` | 字符串 | D5 数值实验 |
| `positioning` | 字符串 | D6 文献定位 |
| `writing` | 字符串 | D7 写作与修辞 |
| `limits_future` | 字符串 | D8 局限与未来方向 |
| `method_links` | 对象数组 | `{method, relation, note, pages}`。relation 为 `evidence`（佐证）、`variant`（变体）或 `contradiction`（矛盾） |
| `new_pattern_candidates` | 对象数组 | `{pattern, evidence, pages}`，进候选池 |
| `transferable` | 字符串数组 | 可迁移手法 |
| `coauthors` | 字符串 | 合作者 |
| `quotes` | 对象数组 | `{text, page}`，原文摘录，最多2条 |

没读到的维度留空字符串或空数组，不猜。

`python3 scripts/mark_read_from_cards.py <skill目录>` 按 `read_level` 回填 INDEX.md 的 Read 列。同一篇有多张卡片时，取读得最深的一张。对应关系：

| `read_level` | Read 列 |
|---|---|
| `full` | `carded` |
| `partial` | `skimmed` |
| `abstract` | `abstract` |
| `metadata` | `metadata` |
| `unreadable` | `unreadable` |

### 摘录规则（硬性）

- `quotes[].text` 必须逐字取自抽取文本 `references/sources/papers/txt/<ID>-*.txt` 或 `abstracts.json`。`page` 用 `[[page N]]` 的页码。
- 每写完一批，就跑 `python3 scripts/verify_card_quotes.py <skill目录>`。脚本比较前会统一 Unicode、连字、行末断词、引号、破折号和空白。
- 报 `NOT FOUND` 的摘录，要么改成原文，要么去掉引号改为转述。
- **全部通过才进入第三节的汇总。** DFO团队的1,139条摘录全部逐字通过。
