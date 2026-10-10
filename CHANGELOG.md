# Changelog

## 0.5.0 — 2026-10-10

目标：业务方案必须核对链路注释，逻辑变化时补日志，自审写出安全评估。B 每一轮用覆盖五格填实链路、注释、日志、安全和更好实现，空着不算一轮。

- 改了 `SKILL.md`、`references/01-plan-review.md`、`README.md`、`examples/03-你是AgentA.md`、`examples/04-你是AgentB.md`、`examples/06-开始按方案执行.md`、`examples/README.md`、`tests/test_multireview_contract.py`、`VERSION`、`skill.json`
- 没改 `references/gap-capture.md`、`governance/rules/`、触发短语、`examples/08-完整方案-登录与返参解密.md`
- 链路以内对不上或不清楚的注释写进执行。逻辑有变化时补日志，不写口令、密钥、令牌、完整报文。自审要有安全评估。B 的一轮要有安全评估、反问和覆盖五格
- 测了 `validate_skill.py`、`tests/run_smoke.py`、`pack.py --dry-run`。固定四问的当次结果在 `governance/regression-reports/RR-20261010-001.md`
- 回滚：分发包回到 `governance/baselines/0.4.0/`，版本回到 0.4.0。基线一旦生成就不改、不删。发布包不提交

## 0.4.0 — 2026-10-09

目标：业务方案必须写出回归验证和 bug修复验证。改完代码后按验收验证。执行里的代码一行一中文注释。

- 改了 `SKILL.md`、`references/01-plan-review.md`、`README.md`、`examples/03-你是AgentA.md`、`examples/06-开始按方案执行.md`、`examples/README.md`、`tests/test_multireview_contract.py`、`VERSION`、`skill.json`
- 没改 `references/gap-capture.md`、`governance/rules/`、触发短语、`examples/08-完整方案-登录与返参解密.md`
- 验收固定两节。升级改造写本次结果和关联业务。报错或 bug 只写问题链路。执行里每一行要落地的代码上一行中文注释。改完按验收逐条验证
- 测了 `validate_skill.py`、`tests/run_smoke.py`、`pack.py --dry-run`。固定四问的当次结果在 `governance/regression-reports/RR-20261009-001.md`
- 回滚：分发包回到 `governance/baselines/0.3.1/`，版本回到 0.3.1。基线一旦生成就不改、不删。发布包不提交

## 0.3.1 — 2026-10-08

目标：审核写不进指定文件时必须声明没落盘；人指出有效一轮并拍板后，Agent A 按方案改代码。

- 改了 `SKILL.md`、`references/01-plan-review.md`、`README.md`、`examples/04-你是AgentB.md`、`examples/06-开始按方案执行.md`、`tests/test_multireview_contract.py`、`VERSION`、`skill.json`
- 没改 `references/gap-capture.md`、`governance/rules/`、触发短语
- 指定文件末尾没有本轮时，回复第一句是「没有写入」。格式样例里的「可以执行」不算一轮。没有可核对的一轮，或结论是「不可执行」时，不改代码
- 测了 `validate_skill.py`、`tests/run_smoke.py`、`pack.py --dry-run`。固定四问的当次结果在 `governance/regression-reports/RR-20261008-001.md`
- 回滚：分发包回到 `governance/baselines/0.3.0/`，版本回到 0.3.0。基线一旦生成就不改、不删。发布包不提交

## 0.3.0 — 2026-10-05

目标：标准业务方案必须自带问题语境、修改空间和执行顺序。Agent B 不要求安装本技能，只按方案文末的骨架追加一轮。

- 改了 `SKILL.md`、`references/01-plan-review.md`、`README.md`、`tests/test_multireview_contract.py`、`VERSION`、`skill.json`
- 没改 `references/gap-capture.md`、`governance/rules/`
- 代码仓只授权阅读。修改空间只授权修改，且必须落在代码仓内
- 测了 `validate_skill.py`、`tests/run_smoke.py`、`pack.py --dry-run`。固定四问的当次结果在 `governance/regression-reports/RR-20261005-001.md`
- 回滚：分发包回到 `governance/baselines/0.2.1/`，版本回到 0.2.1。基线一旦生成就不改、不删。发布包不提交

## 0.2.1 — 2026-10-03

目标：Agent B 每一轮把当时已经能发现的问题一次写完；Agent A 改过方案或点名代码变了之后，新出现的问题可以在下一轮再提。

- 改了 `SKILL.md`、`references/01-plan-review.md`、`tests/test_multireview_contract.py`、`VERSION`、`skill.json`
- 没改 `README.md`、`references/gap-capture.md`、`governance/rules/`
- 测了 `validate_skill.py`、`tests/run_smoke.py`、`pack.py --dry-run`。固定四问的当次结果在 `governance/regression-reports/RR-20261003-002.md`
- 回滚：`baselines/0.2.1/` 还没生成时，分发包回到 `governance/baselines/0.2.0/`，版本回到 0.2.0。基线一旦生成就不改、不删。发布包不提交

## 0.2.0 — 2026-10-03

目标：审核人数由人指定；每个 B 分章独立、每轮重读磁盘最新代码；全部最新一轮为可以执行且人说开始按方案执行后，只由 A 改代码。

- 改了 `SKILL.md`、`README.md`、`skill.json`、`VERSION`、`references/01-plan-review.md`、`references/README.md`、`tests/README.md`、`tests/test_multireview_contract.py`
- 没改 `references/gap-capture.md`，也没改 `governance/rules/`
- 测了 `validate_skill.py`、`tests/run_smoke.py`、`pack.py --dry-run`。固定四问的当次结果在 `governance/regression-reports/RR-20261003-001.md`
- 回滚：`baselines/0.2.0/` 还没生成时，分发包回到 `governance/baselines/0.1.0/`，版本回到 0.1.0。基线一旦生成就不改、不删。发布包不提交

## 0.1.0 — 2026-10-03

脚手架诞生（初始化）。本版无业务能力，只建立开发仓。

- 版本控制：根目录 `VERSION` + git
- 基线：`governance/baselines/0.1.0/`
- 升级记录：`CR-000-init`、`upgrade-to-0.1.0.md`
- 变更门禁与打包：见 `governance/`
