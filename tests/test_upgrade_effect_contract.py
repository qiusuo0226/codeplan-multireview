#!/usr/bin/env python3
"""Lock the nine-section upgrade-effect checklist and the phrases that load it."""
from __future__ import annotations

import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

REQUIRED = (
    "## 1. 预期解决的问题",
    "## 2. 已经解决的",
    "## 3. 回归用例",
    "## 4. 回归结果",
    "## 5. 版本是否对齐",
    "## 6. 改动范围",
    "## 7. 说好不改的",
    "## 8. 打包",
    "## 9. 发布记录",
    "审核一下升级结果",
    "核对交给同一会话里的另一个助手。",
    "查完之前不向人发文字。",
    "## 核对用预期",
    "## 核对用范围",
    "## 核对用不改",
    "## 核对用回归",
    "## 核对用结果",
)

SOURCES = (
    "governance/templates/upgrade-effect.md",
    "governance/templates/CR-template.md",
    "governance/templates/RR-template.md",
    "governance/rules/upgrade-dual-agent.md",
    "governance/rules/skill-governance.md",
)


def _read(rel: str) -> str:
    return (REPO / rel).read_text(encoding="utf-8")


class UpgradeEffectContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.effect = _read("governance/templates/upgrade-effect.md")
        cls.dual = _read("governance/rules/upgrade-dual-agent.md")
        cls.gov = _read("governance/rules/skill-governance.md")
        cls.combined = "\n".join(_read(rel) for rel in SOURCES)

    def test_required_strings_present(self):
        for text in REQUIRED:
            self.assertIn(text, self.combined, text)

    def test_new_phrases_in_both_rules(self):
        for phrase in ("审核一下升级结果", "审核升级结果", "已经升级完了"):
            self.assertIn(phrase, self.dual, phrase)
            self.assertIn(phrase, self.gov, phrase)

    def test_old_effect_headings_gone(self):
        for text in ("## 满足", "## 未满足", "## 方案外"):
            self.assertNotIn(text, self.effect, text)
