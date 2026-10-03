# pack/

把 Skill 打成分发包 zip。排除名单以 `governance/pack.ini` 为准（与 snapshot / audit 同读）。默认排除 `.git`、`governance/`、`tests/`、`AGENTS.md`、缓存和压缩包。

```
python governance/pack/pack.py --skill-root .
python governance/pack/pack.py --skill-root . --dry-run
python governance/pack/pack.py --skill-root . --output-dir <目录>
```

zip 名：`{name}-Skill-v{VERSION}.zip`。`name` 取 `skill.json` 的英文名（小写字母、数字、连字符），不用中文显示名。版本优先读根目录 `VERSION`。

发布包打在开发仓根目录，只留本地。任何时候都不提交、不推远程。不要 `git add -f` 这个 zip。
