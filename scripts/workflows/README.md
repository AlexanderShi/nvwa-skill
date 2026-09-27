# 团队工作流（scripts/workflows/）

搭一支研究团队（多位研究者 × 研究Skill × 圆桌）要用的九个保存好的工作流，外加：从 `team.json` 生成启动参数的 `make_args.mjs`，不花 token 的预览器 `dry_run.mjs`，套件自检 `selftest.sh`，和一套虚构团队的示例参数 `examples/`。

- 端到端的做法（选人、环境、闸门、失败模式、成本、增删成员）见 [research-team-playbook.md](../../references/research-team-playbook.md)。本文只讲工作流本身：做什么、传什么参数、怎么启动、怎么预览。
- 实例是 `product/dfo-team/`（无导数优化，5 人）。成本数字都来自它；工作流里没有写死它的领域、成员或路径，一切从参数和 `team.json` 来。
- 工作流的 prompt 是英文的；agent 先读 `<repo>/<team>/team.json`，从里面拿 `language`、`field` 和各种线索，所以换领域、换语言都不用改脚本。

---

## 一、九个工作流

| 步 | 工作流 | 做什么 | `members` | 产出 | 工作流里跑的闸门 | 典型成本 |
|---|---|---|---|---|---|---|
| T1 | `team-base-skills.js` | 每人走女娲研究Skill的 Phase 1–5：6 个调研 agent（01–06）→ 1.5 复核 → 四重验证提炼 → 按 `research-skill-template.md` 写 SKILL.md（含 Roundtable Card）→ 盲测与修 → 双视角精修 | 一位 | `<M>/SKILL.md`、`references/research/01–06`、`RESOURCES.md` 行；学生模式另有 3 个文件；scratch 里的 Phase 2 记录 | `merge_research.py`、`quality_check.py` 12/12、`check_links.py` | 每人 16–20 个 agent（quick 档 13–17）；DFO 未计量 token |
| T2 | `team-layer.js` | 核对或补写每人的 Roundtable Card；按模板和各人的卡片写圆桌 SKILL.md 与团队 README（fault line 要两边都有证据）；核对各人 RESOURCES.md；两个只读核查员 + 修复。`deep_tier: false`（轻量档）时还把 DEEP-READING.md 换成模板开头的轻量档说明、RESOURCES.md 去掉深读档占位行；在已深读的团队上重跑（如加了成员）时保留 T3.8 写的卡片证据 | 全体（少了谁会记日志） | 团队 `README.md`、`<roundtable>/SKILL.md`、各人 Roundtable Card 与 `RESOURCES.md`、缺失的 `private/README.md`；轻量档另有 `DEEP-READING.md` | `check_links.py` 0、不剩 `{{`、只剩留给后续步骤的 TODO（轻量档一个不剩）、每位成员 12/12、`team_status.py`。圆桌不是研究Skill，不跑 `quality_check.py` | 每人 2 个 + 团队 4–5 个 |
| T3.1 | `team-harvest.js` | Google Scholar（WebFetch，逐字行 prompt + TOTAL）+ DBLP（SPARQL，`dblp_works.py`）+ Crossref/DataCite → 发表全表；再按年份排序独立审计一遍 | 一位 | `publications/works.json`、`scholar.md`、整行重写的 `RESOURCES.md` 第 1 行（没有 Scholar 主页时 Link 写 DBLP 个人页或主页列表）；`acquire: true` 时还有 `papers/INDEX.md` 等 | `validate_works.py` 0 errors；第 1 行不剩 `[TODO`、`{{` | DFO 实测每人 3 个 / 40 万 token |
| T3.3 | `team-chase.js` | 计划 agent 跑 `chase_chunks.py` 切块（算好每篇的目标路径）；获取脚本没拿到全文的作品，每 20 篇一个 agent，按 `chase_hints` → 通用开放来源去找合法全文和逐字摘要；最后合并、重建索引，书的开放部分线索记进 `book-leads.json` | 一位 | 放在精确目标路径的 PDF（不进 git）、`abstracts-chase-<date>-r<run>-<块>.json`（同一天重跑 run 加 1，不覆盖没合并的文件）→ `abstracts.json`；`works.json` 的 `urls`；`papers/book-leads.json` | `merge_chase.py`、`validate_works.py` | DFO 实测每人 5 个 / 90 万 |
| T3.5 | `team-read.js` | 按 `plan_reading_batches.py` 的批次文件，一批一个 agent 写 D1–D8 卡片（core / supplement / book / abstract 四种读法）；失败的批次重试一次；闸门 agent 合并摘要、修摘录、回填 Read 列 | 一位 | `cards/<bid>.md` + `<bid>.digest.json`；`INDEX.md` 的 Read 列 | `verify_card_quotes.py` 全部通过、`mark_read_from_cards.py`、`merge_chase.py`、`team_status.py` | DFO 实测每人 22 个 / 580 万（约 3.6 万 token 一张卡片） |
| T3.6 | `team-synthesize.js` | 卡片 → 07 卡片索引（`build_card_index.py` 生成）、08 深读汇总；在字数预算内保守更新 SKILL.md，同时写 `09-evidence-ledger.md` 和 technique catalog；三个质疑者复核（删改检测用 `check_ledger.py --before … --allow frontmatter,activation-disclaimer`）；修到闸门通过 | 一位 | `07`、`08`、`09`、`technique-catalog.md`、SKILL.md、`01`/`06`；`RESOURCES.md` 的深读档占位行（第 3 行）换成真实各行 | 摘录没全部通过就整人拦下；`quality_check.py` 12/12、`check_ledger.py`、`check_links.py`、字数；`RESOURCES.md` 不剩 `[TODO`、`{{` | DFO 实测每人 6 个 / 240 万 |
| T3.7 | `team-tighten.js` | SKILL.md 仍超预算时，把长证据无损移进 `09-evidence-ledger.md`；已在预算内的成员跳过 | 一位 | SKILL.md、`09-evidence-ledger.md`；scratch 里的精简前备份 | `check_ledger.py --before`（不加 `--allow`）、12/12、`check_links.py`、字数 | DFO 实测每人 3 个 / 70 万 |
| T3.8 | `team-integrate.js` | 用 `team_status.py` 的覆盖表和各人的 08 刷新团队 README、DEEP-READING.md 和圆桌 fault line（两边都要有卡片证据）；解决模板里写给 T3.8 的全部 TODO | 全体 | 团队 `README.md`、`DEEP-READING.md`、圆桌 SKILL.md（可选：根 README 的一行） | DEEP-READING 覆盖表 = `team_status.py --coverage`，README 五列摘要 = `--coverage --short`；`check_links.py` 0；fault line 双方卡片 ID 都存在；`grep -rn --include='*.md' -e '{{' -e '\[TODO' <team>` 没有输出（还没做完的成员自己文件夹里的除外）；圆桌不跑 `quality_check.py` | 团队一次 6–7 个；DFO 实测 4 个 / 100 万（旧版） |
| T4 | `team-increment.js` | 以后有新材料时：（可选）找书的开放部分和新论文并登记 → 写卡片 → 保守并入 07/08/09 和 SKILL.md（限制增长）→ 复核 → 修 | 一位 | 新的 `works.json` 行与文件、新卡片、08 的「Increment <label>」一节、SKILL.md 等 | 同 T3.5–T3.7；删改检测用 `check_ledger.py --before … --allow frontmatter-date,activation-numbers` | DFO 实测每位书作者 4 个 / 100 万（旧版；现在多一个复核，一批时每人 5–6 个） |

T3.2（`acquire_fulltexts.py`）和 T3.4（`plan_reading_batches.py --out-dir <scratch>`）是脚本，不是工作流。DFO 深读档合计每人约 45 个 agent、1,100 万 token；详见手册第六节。

每个工作流的返回值里都有 `next`：该 commit 什么（`bash scripts/team_commit.sh …`）、下一步跑什么，能写成命令的都写成了命令（例如 T3.1 找到的 Scholar id / DBLP pid 用 `new_team.py --set-member` 记进 `team.json`，T3.5 读卡报的 REOCR / WRONG-TEXT 用 `acquire_fulltexts.py --reocr / --drop` 和 `plan_reading_batches.py --reread`）。

## 二、参数约定

九个工作流共用 5 个参数，全部必填。**不用手写**：`make_args.mjs` 从 `team.json` 生成（见第三节）。

| 参数 | 含义 |
|---|---|
| `repo` | nuwa 仓库的绝对路径（含 `scripts/`、`references/`） |
| `team` | 团队目录，相对 `repo`，如 `"product/bandit-team"`（里面有 `team.json`） |
| `scratch` | scratch 目录的绝对路径，放批次计划、补搜分块、备份和中间记录（agent 可写）。放在仓库外；`make_args.mjs` 默认用固定的 `${TMPDIR:-/tmp}/<team>-scratch`，**所有阶段必须用同一个**：T3.5 默认的批次文件、补搜分块、T3.6/T3.7/T4 的 SKILL.md 备份都在里面，换了目录工作流就找不到，会跳过这位成员。一个阶段没做完前别删 |
| `date` | `"YYYY-MM-DD"`。工作流脚本不能调 `Date.now()`，日期只能传进来 |
| `members` | 从 `team.json` 原样拷贝的成员对象数组（slug、name、surname、living、hint、scholar、dblp、orcid、homepage、chase_hints、student_mode，可选 family_name）。按成员跑的工作流一般只放一位；T2、T3.8 放全体 |

`team.json` 里还有几个工作流会用到的可选键：`card_dimensions`（非数学领域里 D1–D8 各指什么，读卡 agent 照用）、成员的 `family_name`（作者核对和检索用的姓；默认取 `name` 的最后一个词，`surname` 只作圆桌的视角标签，撞姓时可以写成 "N. Higham"）、`source_labels`（`acquire_fulltexts.py` 给手工补来的全文标来源）。见 [team.example.json](../../references/team-templates/team.example.json)。

各工作流的特有参数（都可省略，括号里是默认值）。参数名一律 `snake_case`。早期版本里有五个工作流用过 `camelCase`（`batchFiles`、`wordBudget`、`maxWords`、`targetWords`、`maxGrowth`、`rootReadme`、`newFaultLines`），这些旧名仍然当别名接受，运行开头会记一行日志提醒改名；新旧两个名字都给时用新名。写错的键不会报错，只会在运行开头记一行 `ignores args key(s)` 的日志，`dry_run.mjs` 也会警告（`make_args.mjs --set` 直接拒绝）。

**按成员的映射参数**（`only`、`only_chunks`、`skip_ids`、`batch_files`、`batches`、`notes`、`what`）以成员 slug 为键。键不是这次运行里的成员时记一行日志；`only`、`only_chunks` 还会在「这次运行里有成员没有对应的键」时直接停下：slug 拼错会让 `only` 失效、把这位成员的所有批次（或块）重跑一遍，加上 `overwrite: true` 还会覆盖已有卡片。

**WebSearch 预算**（`search_budget`，T1、T3.1、T3.3、T3.5、T4）：这次运行一共能用多少次 WebSearch（所有成员合计），工作流按人、按 agent 均分，写进每个 prompt（「at most N calls」），agent 在 `searches_used` 里报用量，结尾记一行合计。会话的 WebSearch 约 200 次、所有 agent 共用，默认值按 5 人团队分好了（手册第六节）；curl、WebFetch 不算。

| 工作流 | 特有参数 |
|---|---|
| `team-base-skills.js` | `from` / `to`：`research`、`review`、`synthesis`、`build`、`test`、`refine` 中的一段（全部）；`tier`：`standard` / `quick`（只跑调研 01–03）；`dims`：如 `["02","06"]`，只跑这几个调研 agent，覆盖 `tier`；`user_context`：用户自己的领域和阶段；`word_budget`（8000）；`example_team`：一支已完成团队的目录，只学形状；`search_budget`（每人 36：复核 3、资源表 1、每轮评分 1，其余均分给调研 agent，标准档每个 5） |
| `team-layer.js` | `roundtable`（`team.json` 的 `roundtable`）；`deep_tier`（true：保留留给 T3.1、T3.6、T3.8 的 TODO；false：轻量档，DEEP-READING.md 换成轻量档说明、RESOURCES.md 第 1 行记 not harvested (base tier) 并删掉深读档占位行、README 删掉深读档专用部分，一个 TODO 都不留）；`example_team` |
| `team-harvest.js` | `audit`（true）；`acquire`（false；true 时每人再跑一次 `acquire_fulltexts.py`，很慢）；`search_budget`（每人 2） |
| `team-chase.js` | `chunk_size`（20）；`max_searches`（每篇最多搜几次，4）；`skip_ids`：`{"<slug>": ["S012", …]}`；`only_chunks`：`{"<slug>": [1, 3]}`，只（重）跑这几块；`merge`（true）；`search_budget`（每人 24，按块均分） |
| `team-read.js` | `round`（1；`plan_reading_batches.py --out-dir` 打印的轮次）；`batch_files`：`{"<slug>": "<绝对路径>"}`（默认 `<scratch>/batches-<slug>-r<round>.json`）；`batches`：`{"<slug>": [{"bid","mode"}]}`，跳过计划 agent；`only`：`{"<slug>": ["c01", …]}`；`overwrite`（false：已有卡片的批次跳过，可续跑）；`retry`（true）；`search_budget`（每人 8，只给摘要批次） |
| `team-synthesize.js` | `word_budget`（11500，09 同时写）；`max_words`（预算 + 1500）；`notes`：`{"<slug>": "给汇总 agent 的提醒"}`；`from`：`mine`（默认）、`edit`、`verify`（别名 `review`：人工改过 SKILL.md 之后只重跑三位复核员和修复，不重新挖卡片）、`fix`（只跑闸门和修复） |
| `team-tighten.js` | `target_words`（11500）；`max_words`（目标 + 1500）；`force`（false） |
| `team-increment.js` | `label`（`inc-<date>`）；`find`：`["book-parts", "new-papers"]` 的子集（`[]`：不搜，只读手工准备的批次文件；`book-parts` 先看补搜留下的 `papers/book-leads.json`）；`batch_files`（默认 `<scratch>/batches-<slug>-<label>.json`；给了就不搜）；`round`；`since`（默认 `works.json` 的 `harvested`）；`what`：`{"<slug>": "新材料是什么"}`；`max_growth`（400 词）；`search_budget`（每人 10，给找材料的 agent）；`from`：`prepare`（默认）、`read`、`integrate`、`verify`（别名 `review`）、`fix`，同一个 `label` 续跑 |
| `team-integrate.js` | `root_readme`（false）；`new_fault_lines`（2） |

每个脚本开头的注释里有同样的说明，以脚本为准。

## 三、启动

工作流只能在有 Workflow 工具的会话里启动，而且要用户同意。**参数用 `make_args.mjs` 生成**，不要手抄 `team.json`：

```bash
node scripts/workflows/make_args.mjs team-read --team product/<team> --set round=1        # 每人一个调用
node scripts/workflows/make_args.mjs team-layer --team product/<team>                     # 团队级：一个调用，全体成员
node scripts/workflows/make_args.mjs team-base-skills --team product/<team> --member a,b --set to=review
```

它打印 `[{scriptPath, args}, …]`：按成员的工作流每人一个，`team-layer.js`、`team-integrate.js` 一个（给 `--member` 会报错）。`args` 里是 `repo`、`team`、`scratch`（默认固定的 `${TMPDIR:-/tmp}/<team>-scratch`，没有就建）、`date`（默认今天）、从 `team.json` 原样拷来的 `members`，`team-layer.js` 还有 `team.json` 的 `roundtable`；`--set KEY=JSON` 加特有参数（键必须是这个工作流读的；按成员的映射只能用本队的 slug，每个调用只带自己那一项）。`--args-only` 只打印一个 `args`（配合 `dry_run.mjs`），`--out DIR` 另存成文件。把打印出来的每个对象原样交给 Workflow 工具：

```js
Workflow({ scriptPath: "<repo>/scripts/workflows/team-read.js", args: { /* make_args.mjs 打印的 args */ } })
```

- **`args` 传 JSON 对象。** 传字符串脚本也能解析，但一不小心就会变成整段字符串。
- **每人一个工作流，并行启动。** 每个工作流的并发上限是 min(16, CPU 数 − 2)，4 核容器只有 2。按成员的工作流（T1、T3.1–T3.7、T4）给每人各起一个，`members` 只放这一位，在同一条消息里一起发出。T2 和 T3.8 要等全体，只起一个。
- **续跑。** 工作流中断、被停或改了脚本以后，用同样的 `scriptPath` 和 `args` 加上一次结果里的 `runId`：`Workflow({scriptPath, args, resumeFromRunId: "<runId>"})`。没改过的 agent 调用直接返回缓存结果，从第一个改动过的调用开始重新跑。脚本自己也有续跑的办法：T1 的 `from`/`to`，T3.5 的 `overwrite: false` 与 `only`，T3.3 的 `only_chunks`，T3.6 和 T4 的 `from`（人工修好 SKILL.md 后用 `from: "verify"` 只重跑复核和修复，每人省下约 240 万 token 的重新挖卡片）。
- **人工检查点。** T1 先用 `to: "review"` 跑，把调研摘要给用户看；再用 `from: "synthesis", to: "synthesis"`，看提炼结果和 Roundtable Card；最后 `from: "build"` 跑完。
- **每一步做完就 commit，长阶段中途也 commit。** 容器是临时的：`bash scripts/team_commit.sh <路径> "<说明>"`（先暂存，暂存区里有 PDF、PostScript、DjVu、EPUB、`txt/` 或 `private/` 下的文件就停下，退出码 3）。T3.2、T3.5、T3.6 这种一跑几小时的阶段，每 30–60 分钟提交一次检查点（已完成批次的卡片可以先提交）。每个工作流的返回值里有 `next`，写着该 commit 什么、下一步跑什么。

## 四、先预览：`dry_run.mjs`

`dry_run.mjs` 用 Node（≥ 18）在沙箱里跑工作流，行为和 Workflow 运行时一致，但 `agent()` 不派 agent，而是按 `opts.schema` 造一个假结果。它不花 token，不碰仓库，除了 `--out` 什么都不写。用来在花钱之前看清每个 agent 会收到什么 prompt、会不会走到每个阶段。

```bash
# 示例团队：每个阶段都会走到
node scripts/workflows/dry_run.mjs scripts/workflows/team-read.js scripts/workflows/examples/team-read.args.json \
  --answers scripts/workflows/examples/team-read.answers.json

# 自己的团队：不给参数文件，参数和真正启动时 make_args.mjs 生成的一样；全部 prompt 写进一个目录慢慢看
node scripts/workflows/dry_run.mjs scripts/workflows/team-read.js --team product/<team> --member <slug> \
  --set round=1 --out /tmp/<team>-prompts --strict --forbid 'bandit|Ada Example|Bo Sample'
# team-layer.js / team-integrate.js 预览时不给 --member：它们要全体成员（给了会警告，少了人 team-layer 连圆桌都不写）
```

别拿 `examples/` 的参数文件加 `--team` 当真预览：那些参数描述的是虚构的示例团队。真这么用时，`--team` 会把 `roundtable` 换成 `team.json` 的、删掉示例专用的值（`user_context`、`notes`、`what`、`skip_ids`、`batch_files`、`batches`、`only`、`only_chunks`、`since`、`label`）、把日期换成今天，每一处都打印一行 `note`；但真正启动一定用 `make_args.mjs` 生成的参数。

输出依次是：`meta`（名称、说明、阶段）；每个 agent 调用的编号、阶段、label、schema 字段和 prompt 开头（和前面某个 prompt 相同的前缀，比如共同的规矩，缩成一行）；`log()` 的每一行；返回值；最后是汇总（agent 数、按阶段分布、prompt 总长、没走到的阶段、警告）。

| 选项 | 作用 |
|---|---|
| `--full` | 打印完整 prompt |
| `--out DIR` | 每个 prompt 写成 `DIR/NNN-<label>.md`，另有 `calls.json`、`return.json` |
| `--chars N` | 每个 prompt 显示多少字符（500） |
| `--quiet` | 不显示 prompt，只看日志和汇总 |
| `--items N` | 假结果里每个数组放 N 项，字符串换成 `<字段>` 占位符（默认数组为空、字符串为空） |
| `--bools MODE` | `happy`（默认：布尔值为 true，但 blocked、skipped、failed、missing 这类字段为 false，走正常路径）、`true`、`false`（走「没通过」「没准备好」的分支） |
| `--answers FILE` | 按 label 指定假结果：`{"<label 正则>": 值}`，第一个匹配的键生效。值是对象时按 schema 合并进假结果（没给的字段自动补齐）；`null` 表示 agent 死了；数组表示依次调用的结果（最后一个重复用）。以 `_` 开头的键是注释 |
| `--team DIR` / `--member a,b` | 从 `<repo>/DIR/team.json` 读成员并设置 `args.team`；`--member` 只留这几位。不给参数文件时参数由 `make_args.mjs` 生成（可加 `--set KEY=JSON`） |
| `--repo PATH` / `--scratch PATH` | args 里字符串 `$REPO`、`$SCRATCH` 替换成什么（默认：本仓库，以及 `<tmpdir>/nuwa-dry-run/<team>`） |
| `--forbid RE` | prompt 匹配这个正则就警告，如 `--forbid 'dfo\|powell\|/home/'`，查有没有漏掉的旧团队内容 |
| `--strict` | 有警告时退出码为 2（工作流抛错或语法错误是 1） |

它会检查：
- 脚本能否按运行时的方式解析（运行时把整个脚本包进一个 async 函数，所以脚本末尾有顶层 `return`；别用 `node --check file.js` 检查，一定会报 "Illegal return statement"）；
- `meta` 是不是纯字面量，`phase()` 和 `opts.phase` 是否都在 `meta.phases` 里；
- 每个 agent 调用有没有 label 和 phase，schema 能否满足；
- prompt 和日志里有没有 `undefined`、`[object Object]`、`NaN`；
- 用没用 `Date.now()`、`Math.random()`、`new Date()`（沙箱里和运行时一样会抛错）；
- args 里有没有脚本从没读过的键（多半是拼错了）；
- 按成员的映射参数有没有用了不在 `members` 里的 slug（拼错会让 `only` 这类选项悄悄失效）；
- 团队级工作流是不是只给了部分成员；
- `pipeline()`、`parallel()` 里抛错被丢掉的项。

`pipeline()` 和 `parallel()` 的语义与运行时相同：抛错的项变成 `null` 并记一行；`pipeline` 的第一个阶段收到成员本身，每个阶段收到 `(上一步结果, 成员, 下标)`，某个阶段返回 `null` 时，这一项后面的阶段不再执行。

它**不**检查文件是否存在、脚本能否跑通、agent 能否完成任务，也估不了真实成本。第一次在真团队上跑，先拿一位成员小规模试。

## 五、顺序

```
T0 定义  new_team.py → team.json、目录骨架、模板
T1 基础Skill  team-base-skills.js（每人）                 闸门：quality_check 12/12
T2 团队层    team-layer.js（全体）                        闸门：check_links 0、每人有 Roundtable Card
―― 轻量档到此完成；深读档继续 ――
T3.1 发表全表  team-harvest.js（每人）                    闸门：validate_works 0 errors
T3.2 开放全文  acquire_fulltexts.py（每人一个后台进程）
T3.3 补搜      team-chase.js（每人）
T3.4 切批      plan_reading_batches.py <team> --out-dir <scratch> --no-abstract（每轮一行：自动定轮次、自动排除其他轮的计划）
T3.5 读卡      team-read.js（每人，每轮一次）             闸门：verify_card_quotes 全部通过
T3.6 汇总      team-synthesize.js（每人）                 闸门：12/12、字数、check_ledger
T3.7 精简      team-tighten.js（只给仍超预算的人）        闸门：check_ledger --before
T3.8 整合      team-integrate.js（全体）                  闸门：team_check.py <team> 退出码 0
T4 增量        team-increment.js（以后有新材料时），之后再跑一次 team-integrate.js
```

每一步之间要跑的命令（包括上面的闸门）见[手册第三、四节](../../references/research-team-playbook.md#三流水线-t0t4)。

## 六、`examples/`

一支虚构的团队 `product/example-team`，领域写的是 "multi-armed bandits"。示例参数里放了两位成员 Ada Example、Bo Sample，都是占位人物，不是真人。这支团队的目录并不存在，示例只给 `dry_run.mjs` 用。两人故意设得不一样（一位已故、没有 Scholar id；一位在世、有全部 id、开了学生模式），好让 prompt 的各个分支都显示出来。[`references/team-templates/team.example.json`](../../references/team-templates/team.example.json) 是同一支团队：这两位原样照抄，另加第三位 Cleo Placeholder（3 人才凑得起一张圆桌）。拿它试 `new_team.py` 时是三个人，预览工作流时仍是两个人。

- `team-<name>.args.json`：该工作流的参数。路径写成 `$REPO`、`$SCRATCH`，由 `dry_run.mjs` 替换；真正启动时换成绝对路径。
- `team-<name>.answers.json`：让预览走到每个阶段的假结果。比如 `team-read` 的计划里四种读法各有一批，其中一批第一次失败、重试成功；`team-chase` 里一人是当天第一次补搜、一人是同一天重跑（摘要文件名里的 run 变成 r2）；`team-integrate` 里一人已汇总、一人还在读。
- 看其他分支不用改示例，直接给行内参数，例如轻量档的 T2：`node scripts/workflows/dry_run.mjs scripts/workflows/team-layer.js "$(jq -c '.deep_tier=false' scripts/workflows/examples/team-layer.args.json)" --answers scripts/workflows/examples/team-layer.answers.json`。

## 七、改工作流之后

改完任何一个工作流或套件脚本，先跑自检，全部 `✓` 再提交：

```bash
bash scripts/workflows/selftest.sh product/dfo-team    # 参数是一支已完成的团队（这里用实例）；不给就只跑示例预览和脚本检查
```

它做三件事：九个示例和几个分支变体（轻量档 T2、T3.6/T4 的 `from`）的 `--strict` 预览，`--forbid` 由已完成团队的 `team.json` 生成（团队、圆桌 slug 和成员的姓，不许漏进通用工作流）；对已完成团队的每个工作流跑 `make_args.mjs` 和 `dry_run.mjs --team`；所有脚本能编译、能 `--help`，`team_check.py <team>` 退出码 0。退出码是失败项数。

写工作流的规矩：
- 用纯 JavaScript，开头是纯字面量的 `export const meta = {...}`；
- 每个 agent 调用都经过 `A()`，带 `opts.phase` 和 `opts.label`，都用 schema；
- 跳过或丢掉的东西都要 `log()`；
- 不用 `Date.now()`、`Math.random()`、`new Date()`，不用文件系统 API；
- 不写死路径、团队、研究者或领域；
- prompt 用英文，让 agent 先读 `team.json`；
- 新参数写进脚本开头的注释、`KNOWN_ARGS` 和本文第二节。
