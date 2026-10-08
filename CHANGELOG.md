# Changelog

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
