# 代码方案多审（codeplan-multireview）

开发需求时描述一个问题。扫过代码仓后发现要改代码或有 bug，就问要不要出一版升级方案。同意后再出具体方案，并按已确认的思路执行。出方案时由一个助手写方案，另两个助手基于同一批代码仓先自己扫一遍再审核，把审核补进方案末尾，可以多轮。

## 开发

本目录是 Skill **开发仓**。版本控制、基线、升级记录和打包都在 `governance/`（不进分发包）。改本 Skill 时让助手读 `governance/rules/skill-governance.md`，不必再调用 skill-devkit。

```
powershell -File governance/dev.ps1 pack
powershell -File governance/dev.ps1 release
```

## 许可证

[MIT](LICENSE) © 2026 qiusuo
