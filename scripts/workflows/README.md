# 团队工作流（scripts/workflows/）

搭一支研究团队（多位研究者 × 研究Skill × 圆桌）要用的九个保存好的工作流，外加一个不花 token 的预览器 `dry_run.mjs` 和一套虚构团队的示例参数 `examples/`。

- 端到端的做法（选人、环境、闸门、失败模式、成本、增删成员）见 [research-team-playbook.md](../../references/research-team-playbook.md)。本文只讲工作流本身：做什么、传什么参数、怎么启动、怎么预览。
- 实例是 `product/dfo-team/`（无导数优化，5 人）。成本数字都来自它；工作流里没有写死它的领域、成员或路径，一切从参数和 `team.json` 来。
- 工作流的 prompt 是英文的；agent 先读 `<repo>/<team>/team.json`，从里面拿 `language`、`field` 和各种线索，所以换领域、换语言都不用改脚本。

---

## 一、九个工作流

| 步 | 工作流 | 做什么 | `members` | 产出 | 工作流里跑的闸门 | 典型成本 |
|---|---|---|---|---|---|---|
| T1 | `team-base-skills.js` | 每人走女娲研究Skill的 Phase 1–5：6 个调研 agent（01–06）→ 1.5 复核 → 四重验证提炼 → 按 `research-skill-template.md` 写 SKILL.md（含 Roundtable Card）→ 盲测与修 → 双视角精修 | 一位 | `<M>/SKILL.md`、`references/research/01–06`、`RESOURCES.md` 行；学生模式另有 3 个文件；scratch 里的 Phase 2 记录 | `merge_research.py`、`quality_check.py` 12/12、`check_links.py` | 每人 16–20 个 agent（quick 档 13–17）；DFO 未计量 token |
| T2 | `team-layer.js` | 核对或补写每人的 Roundtable Card；按模板和各人的卡片写圆桌 SKILL.md 与团队 README（fault line 要两边都有证据）；核对各人 RESOURCES.md；两个只读核查员 + 修复 | 全体 | 团队 `README.md`、`<roundtable>/SKILL.md`、各人 Roundtable Card 与 `RESOURCES.md`、缺失的 `private/README.md` | `check_links.py` 0、不剩 `{{`、只剩留给后续步骤的 TODO、每人 12/12、`team_status.py` | 每人 2 个 + 团队 3–5 个 |
| T3.1 | `team-harvest.js` | Google Scholar（WebFetch，逐字行 prompt + TOTAL）+ DBLP（SPARQL，`dblp_works.py`）+ Crossref/DataCite → 发表全表；再按年份排序独立审计一遍 | 一位 | `publications/works.json`、`scholar.md`、`RESOURCES.md` 第 1 行；`acquire: true` 时还有 `papers/INDEX.md` 等 | `validate_works.py` 0 errors | DFO 实测每人 3 个 / 40 万 token |
| T3.3 | `team-chase.js` | 获取脚本没拿到全文的作品，每 20 篇一个 agent，按 `chase_hints` → 通用开放来源去找合法全文和逐字摘要；最后合并、重建索引 | 一位 | 放在精确目标路径的 PDF（不进 git）、`abstracts-chase-*.json` → `abstracts.json`；`works.json` 的 `urls` | `merge_chase.py`、`validate_works.py` | DFO 实测每人 5 个 / 90 万 |
| T3.5 | `team-read.js` | 按 `plan_reading_batches.py` 的批次文件，一批一个 agent 写 D1–D8 卡片（core / supplement / book / abstract 四种读法）；失败的批次重试一次；闸门 agent 合并摘要、修摘录、回填 Read 列 | 一位 | `cards/<bid>.md` + `<bid>.digest.json`；`INDEX.md` 的 Read 列 | `verify_card_quotes.py` 全部通过、`mark_read_from_cards.py`、`merge_chase.py`、`team_status.py` | DFO 实测每人 22 个 / 580 万（约 3.6 万 token 一张卡片） |
| T3.6 | `team-synthesize.js` | 卡片 → 07 卡片索引、08 深读汇总；在字数预算内保守更新 SKILL.md，同时写 `09-evidence-ledger.md` 和 technique catalog；三个质疑者复核；修到闸门通过 | 一位 | `07`、`08`、`09`、`technique-catalog.md`、SKILL.md、`01`/`06`/`RESOURCES.md` | 摘录没全部通过就整人拦下；`quality_check.py` 12/12、`check_ledger.py`、`check_links.py`、字数 | DFO 实测每人 6 个 / 240 万 |
| T3.7 | `team-tighten.js` | SKILL.md 仍超预算时，把长证据无损移进 `09-evidence-ledger.md`；已在预算内的成员跳过 | 一位 | SKILL.md、`09-evidence-ledger.md`；scratch 里的精简前备份 | `check_ledger.py --before`、12/12、`check_links.py`、字数 | DFO 实测每人 3 个 / 70 万 |
| T3.8 | `team-integrate.js` | 用 `team_status.py` 的覆盖表和各人的 08 刷新团队 README、DEEP-READING.md 和圆桌 fault line（两边都要有卡片证据） | 全体 | 团队 `README.md`、`DEEP-READING.md`、圆桌 SKILL.md（可选：根 README 的一行） | 覆盖表与 `team_status.py --coverage` 一致、`check_links.py` 0、fault line 双方卡片 ID 都存在 | 团队一次 6–7 个；DFO 实测 4 个 / 100 万（旧版） |
| T4 | `team-increment.js` | 以后有新材料时：（可选）找书的开放部分和新论文并登记 → 写卡片 → 保守并入 07/08/09 和 SKILL.md（限制增长）→ 复核 → 修 | 一位 | 新的 `works.json` 行与文件、新卡片、08 的「Increment <label>」一节、SKILL.md 等 | 同 T3.5–T3.7 | DFO 实测每位书作者 4 个 / 100 万 |

T3.2（`acquire_fulltexts.py`）和 T3.4（`plan_reading_batches.py`）是脚本，不是工作流。DFO 深读档合计每人约 45 个 agent、1,100 万 token；详见手册第六节。

## 二、参数约定

九个工作流共用 5 个参数，全部必填：

| 参数 | 含义 |
|---|---|
| `repo` | nuwa 仓库的绝对路径（含 `scripts/`、`references/`） |
| `team` | 团队目录，相对 `repo`，如 `"product/bandit-team"`（里面有 `team.json`） |
| `scratch` | scratch 目录的绝对路径，放批次计划、补搜分块、备份和中间记录（agent 可写）。放在仓库外，如 `${TMPDIR:-/tmp}/<team>-scratch`；一个阶段没做完前别删，分段运行和续跑都要读它 |
| `date` | `"YYYY-MM-DD"`。工作流脚本不能调 `Date.now()`，日期只能传进来 |
| `members` | 从 `team.json` 原样拷贝的成员对象数组（slug、name、surname、living、hint、scholar、dblp、orcid、homepage、chase_hints、student_mode）。按成员跑的工作流一般只放一位；T2、T3.8 放全体 |

各工作流的特有参数（都可省略，括号里是默认值）。注意命名：前四个用 `snake_case`，后五个用 `camelCase`，照抄下表。写错的键不会报错，只会在运行开头记一行 `ignores args key(s)` 的日志，`dry_run.mjs` 也会警告。

| 工作流 | 特有参数 |
|---|---|
| `team-base-skills.js` | `from` / `to`：`research`、`review`、`synthesis`、`build`、`test`、`refine` 中的一段（全部）；`tier`：`standard` / `quick`（只跑调研 01–03）；`dims`：如 `["02","06"]`，只跑这几个调研 agent，覆盖 `tier`；`user_context`：用户自己的领域和阶段；`word_budget`（8000）；`example_team`：一支已完成团队的目录，只学形状 |
| `team-layer.js` | `roundtable`（`team.json` 的 `roundtable`）；`deep_tier`（true：保留留给 T3.8 的 TODO；false：删掉深读档专用的部分）；`example_team` |
| `team-harvest.js` | `audit`（true）；`acquire`（false；true 时每人再跑一次 `acquire_fulltexts.py`，很慢） |
| `team-chase.js` | `chunk_size`（20）；`max_searches`（每篇最多搜几次，4）；`skip_ids`：`{"<slug>": ["S012", …]}`；`only_chunks`：`{"<slug>": [1, 3]}`，只（重）跑这几块；`merge`（true） |
| `team-read.js` | `round`（1）；`batchFiles`：`{"<slug>": "<绝对路径>"}`（默认 `<scratch>/batches-<slug>-r<round>.json`）；`batches`：`{"<slug>": [{"bid","mode"}]}`，跳过计划 agent；`only`：`{"<slug>": ["c01", …]}`；`overwrite`（false：已有卡片的批次跳过，可续跑）；`retry`（true） |
| `team-synthesize.js` | `wordBudget`（11500，09 同时写）；`maxWords`（预算 + 1500）；`notes`：`{"<slug>": "给汇总 agent 的提醒"}` |
| `team-tighten.js` | `targetWords`（11500）；`maxWords`（目标 + 1500）；`force`（false） |
| `team-increment.js` | `label`（`inc-<date>`）；`find`：`["book-parts", "new-papers"]` 的子集（`[]`：不搜，只读手工准备的批次文件）；`batchFiles`（默认 `<scratch>/batches-<slug>-<label>.json`；给了就不搜）；`round`；`since`（默认 `works.json` 的 `harvested`）；`what`：`{"<slug>": "新材料是什么"}`；`maxGrowth`（400 词） |
| `team-integrate.js` | `rootReadme`（false）；`newFaultLines`（2） |

每个脚本开头的注释里有同样的说明，以脚本为准。

## 三、启动

工作流只能在有 Workflow 工具的会话里启动，而且要用户同意。一次调用：

```js
Workflow({
  scriptPath: "<repo>/scripts/workflows/team-read.js",
  args: {
    repo: "<repo>", team: "product/<team>", scratch: "<scratch>", date: "2026-01-15",
    members: [ /* team.json 里这一位成员的对象，原样拷贝 */ ],
    round: 1
  }
})
```

- **`args` 传 JSON 对象。** 传字符串脚本也能解析，但一不小心就会变成整段字符串。
- **每人一个工作流，并行启动。** 每个工作流的并发上限是 min(16, CPU 数 − 2)，4 核容器只有 2。按成员的工作流（T1、T3.1–T3.7、T4）给每人各起一个，`members` 只放这一位，在同一条消息里一起发出。T2 和 T3.8 要等全体，只起一个。
- **续跑。** 工作流中断、被停或改了脚本以后，用同样的 `scriptPath` 和 `args` 加上一次结果里的 `runId`：`Workflow({scriptPath, args, resumeFromRunId: "<runId>"})`。没改过的 agent 调用直接返回缓存结果，从第一个改动过的调用开始重新跑。脚本自己也有续跑的办法：T1 的 `from`/`to`，T3.5 的 `overwrite: false` 与 `only`，T3.3 的 `only_chunks`。
- **人工检查点。** T1 先用 `to: "review"` 跑，把调研摘要给用户看；再用 `from: "synthesis", to: "synthesis"`，看提炼结果和 Roundtable Card；最后 `from: "build"` 跑完。
- **每一步做完就 commit。** 容器是临时的。PDF、`txt/` 和 `private/` 永远不进 git。每个工作流的返回值里有 `next`，写着该 commit 什么、下一步跑什么。

## 四、先预览：`dry_run.mjs`

`dry_run.mjs` 用 Node（≥ 18）在沙箱里跑工作流，行为和 Workflow 运行时一致，但 `agent()` 不派 agent，而是按 `opts.schema` 造一个假结果。它不花 token，不碰仓库，除了 `--out` 什么都不写。用来在花钱之前看清每个 agent 会收到什么 prompt、会不会走到每个阶段。

```bash
# 示例团队：每个阶段都会走到
node scripts/workflows/dry_run.mjs scripts/workflows/team-read.js scripts/workflows/examples/team-read.args.json \
  --answers scripts/workflows/examples/team-read.answers.json

# 自己的团队：成员从 team.json 读，把全部 prompt 写进一个目录慢慢看
node scripts/workflows/dry_run.mjs scripts/workflows/team-read.js scripts/workflows/examples/team-read.args.json \
  --team product/<team> --member <slug> --out /tmp/<team>-prompts
```

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
| `--team DIR` / `--member a,b` | 从 `<repo>/DIR/team.json` 读成员并设置 `args.team`；`--member` 只留这几位 |
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
T3.4 切批      plan_reading_batches.py（每轮；后续轮次 --exclude 之前的批次文件）
T3.5 读卡      team-read.js（每人，每轮一次）             闸门：verify_card_quotes 全部通过
T3.6 汇总      team-synthesize.js（每人）                 闸门：12/12、字数、check_ledger
T3.7 精简      team-tighten.js（只给仍超预算的人）        闸门：check_ledger --before
T3.8 整合      team-integrate.js（全体）                  闸门：覆盖表一致、check_links 0
T4 增量        team-increment.js（以后有新材料时），之后再跑一次 team-integrate.js
```

每一步之间要跑的命令（包括上面的闸门）见[手册第三、四节](../../references/research-team-playbook.md#三流水线-t0t4)。

## 六、`examples/`

一支虚构的两人团队 `product/example-team`，领域写的是 "multi-armed bandits"。两位成员 Ada Example、Bo Sample 是占位人物，不是真人。这支团队的目录并不存在，示例只给 `dry_run.mjs` 用。两人故意设得不一样（一位已故、没有 Scholar id；一位在世、有全部 id、开了学生模式），好让 prompt 的各个分支都显示出来。

- `team-<name>.args.json`：该工作流的参数。路径写成 `$REPO`、`$SCRATCH`，由 `dry_run.mjs` 替换；真正启动时换成绝对路径。
- `team-<name>.answers.json`：让预览走到每个阶段的假结果。比如 `team-read` 的计划里四种读法各有一批，其中一批第一次失败、重试成功；`team-integrate` 里一人已汇总、一人还在读。

## 七、改工作流之后

改完任何一个工作流，先把九个示例都预览一遍，全部 `✓` 且没有警告再提交：

```bash
for w in base-skills layer harvest chase read synthesize tighten increment integrate; do
  printf '%-14s ' $w
  node scripts/workflows/dry_run.mjs scripts/workflows/team-$w.js scripts/workflows/examples/team-$w.args.json \
    --answers scripts/workflows/examples/team-$w.answers.json --quiet --strict --forbid 'dfo|DFO|[Pp]owell' \
    | grep -E '^(warnings|result)' | tr '\n' ' '; echo
done
```

写工作流的规矩：
- 用纯 JavaScript，开头是纯字面量的 `export const meta = {...}`；
- 每个 agent 调用都经过 `A()`，带 `opts.phase` 和 `opts.label`，都用 schema；
- 跳过或丢掉的东西都要 `log()`；
- 不用 `Date.now()`、`Math.random()`、`new Date()`，不用文件系统 API；
- 不写死路径、团队、研究者或领域；
- prompt 用英文，让 agent 先读 `team.json`；
- 新参数写进脚本开头的注释、`KNOWN_ARGS` 和本文第二节。
