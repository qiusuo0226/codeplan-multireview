# 发布核对

目标版本：0.2.0

## 变更控制

- [x] 有 AP，用户已同意执行（人说「按照方案执行升级」；AP 随后按步骤删除）
- [x] 有 CR，目标可验证，没有混入无关改动（CR-20261003-001）
- [x] 有 IA（IA-20261003-001）
- [x] 有 RR（正 / 反 / 旧能力）（RR-20261003-001）
- [x] RR 含固定四问（装得上 / 唤得起 / 答得对 / 说得清），填了上一版结果（上一版写「无（首次）」）
- [x] AP 结论与 B 节发现都带可信度标签（已验证 / 推断 / 参考）；推断只在 AP-5 当待验证项（删除前已核对；B1 结语为修订-需再审，执行授权是人覆盖）

## 版本与记录

- [x] 根目录 `VERSION`、`skill.json` 的 `version`、`CHANGELOG.md` 该版本段一致（0.2.0）
- [x] 已跑 `python governance/scripts/sync_version.py`
- [x] 已写 `governance/migrations/upgrade-to-0.2.0.md`
- [x] 该版本 AP 已删除（思路在 CR / CHANGELOG / upgrade-to / 基线）

## 基线与打包

- [x] `python governance/scripts/snapshot_baseline.py` 已生成且未改历史基线（新增 `baselines/0.2.0/`，12 个文件）
- [x] `python governance/pack/pack.py --skill-root . --dry-run` 不含 `governance/`、`.git/`、`AGENTS.md`（12 个文件，也不含 `tests/`、`outputs/`）
- [x] `python governance/scripts/audit_release.py` 退出码 0

## Git

- [x] 已提交（人要求收尾并推远程）
- [x] tag 为 `v0.1.0`（`1df4a70`，远程上的 0.1.0）和 `v0.2.0`（本提交）。推 origin（Gitee）与 github。zip 不进 git，作为 Release 附件
