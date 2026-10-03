# Changelog

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
