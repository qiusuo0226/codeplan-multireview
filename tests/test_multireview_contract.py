#!/usr/bin/env python3
"""Lock the multireview contract text.

Reads only SKILL.md, README.md, skill.json, references/01-plan-review.md,
references/gap-capture.md, and the baseline copy of gap-capture.md.
Does not scan CHANGELOG.md or governance/planning/.
"""
from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

PHRASES = {
    "出一版升级方案",
    "你是 Agent A",
    "你是 Agent B",
    "审核这份方案",
    "开始按方案执行",
}

GATES = (
    "不得自行定成 2，也不得自行定成任何人数。",
    "Agent B 不改方案正文，不写代码。",
    "不看其他 B 的审核结果。",
    "都不能当审核依据。",
    "开始按方案执行",
    "references/01-plan-review.md",
    "references/gap-capture.md",
    "outputs/codeplan/",
    "把这一轮已经能发现的问题一次写进「发现」。",
)

CLAUSES = (
    "a-body.md",
    "plan.md",
    "隔离被打破",
    "对照修订",
    "本轮实读",
    "不把 B 的原话",
    "独立 git worktree",
    "开始按方案执行",
    "## 第1轮",
    "不要把这一轮已经能看到的问题留到后面几轮。",
    "由此新出现的问题可以在下一轮再写。",
)

GAP_ROUTES = (
    "技能做不到",
    "记成升级需求",
    "这是 skill 的问题",
    "技能缺口",
)


def _load_validate():
    path = REPO / "governance" / "scripts" / "validate_skill.py"
    spec = importlib.util.spec_from_file_location("validate_skill_for_contract", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class MultireviewContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = _load_validate()
        cls.skill = (REPO / "SKILL.md").read_text(encoding="utf-8")
        cls.readme = (REPO / "README.md").read_text(encoding="utf-8")
        cls.skill_json = json.loads((REPO / "skill.json").read_text(encoding="utf-8"))
        cls.procedure = (REPO / "references" / "01-plan-review.md").read_text(encoding="utf-8")
        fm = cls.mod.parse_frontmatter(cls.skill)
        cls.desc = fm["description"]
        cls.sj_desc = cls.skill_json["description"]

    def test_triggers_match_across_three_descriptions(self):
        skill_phrases = self.mod._trigger_segment(self.desc)
        readme_phrases = self.mod._readme_triggers(self.readme)
        json_phrases = self.mod._trigger_segment(self.sj_desc)
        self.assertEqual(skill_phrases, PHRASES)
        self.assertEqual(readme_phrases, PHRASES)
        self.assertEqual(json_phrases, PHRASES)

    def test_gates_present(self):
        for item in GATES:
            self.assertIn(item, self.skill, item)

    def test_no_fixed_two_reviewers(self):
        for label, text in (
            ("SKILL description", self.desc),
            ("README", self.readme),
            ("skill.json", self.sj_desc),
        ):
            self.assertNotIn("另两个助手", text, label)
        self.assertIn("不得自行定成 2，也不得自行定成任何人数。", self.skill)

    def test_procedure_clauses(self):
        for item in CLAUSES:
            self.assertIn(item, self.procedure, item)
        self.assertNotIn("0.1.0", self.procedure)
        self.assertIn("不把 B 的原话或复述写进", self.procedure)

    def test_gap_capture_unchanged_and_routed(self):
        live = (REPO / "references" / "gap-capture.md").read_bytes()
        base = (
            REPO / "governance" / "baselines" / "0.1.0" / "references" / "gap-capture.md"
        ).read_bytes()
        self.assertEqual(live, base)
        for item in GAP_ROUTES:
            self.assertIn(item, self.skill, item)
        self.assertIn("references/gap-capture.md", self.skill)


if __name__ == "__main__":
    unittest.main()
