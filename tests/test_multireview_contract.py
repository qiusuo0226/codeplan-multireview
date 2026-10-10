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
    "修改空间是允许修改的文件，每一项必须落在代码仓内。",
    "Agent B 不要求安装本技能。",
    "不要写总体评价，不要用 A/B/C/D 分节。",
    "修改空间之外的文件不得写成要改的对象。",
    "没有写入",
    "格式样例里的「可以执行」不算一轮。",
    "人没有指出任何一轮时，不改代码。",
    "方案「验收」必须有「回归验证」和「bug修复验证」。",
    "简洁直译。",
    "按方案改完代码后，按验收逐条验证再结束。",
    "每一行已有注释都要核对。",
    "注释的修改和补充写进执行，算代码改造。",
    "链路以外的行不加注释，也不改它们已有的注释。",
    "不写口令、密钥、令牌、完整报文。",
    "自审必须写出安全评估：这么改行不行、符不符合安全。",
    "不照抄方案「自审」里的安全评估。",
    "为什么这么写，有没有问题，有没有更好的实现方式。",
    "反问的任一子项写了「无」",
    "只是另一种写法、结果相同、安全性相同，不因此不可执行。",
    "### 覆盖",
    "五格有一格空着不算一轮。",
    "只写「没有」不算填实。",
    "只写「通过」不算填实。",
    "发现必须逐条列出，漏一条不算一轮。",
    "硬闸 13 的注释要求适用于执行里每一行要落地的代码，包括链路以内改写或补上的注释。",
    "完整报文指包含请求或响应全部字段的原始文本。",
    "现状没有把链路写到函数或语句块时，自审不通过，不交给 B。",
    "这一次修订要处理该轮发现里的全部问题，不要只改其中一条。",
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
    "## 修改空间",
    "## 自审",
    "## 交给审核",
    "不要求安装本技能",
    "不要写总体评价，不要用 A/B/C/D 分节",
    "修改空间之外的文件不得写成要改的对象",
    "没有写入",
    "格式样例里的「可以执行」不算一轮。",
    "人没有指出任何一轮时，不改代码。",
    "### 回归验证",
    "### bug修复验证",
    "怎样确认它仍正常运转且逻辑没有改变。",
    "问题链路从哪到哪",
    "每一行要落地的代码，正上方一行中文注释",
    "改完后按「验收」逐条做，再结束。",
    "链路以外的行不加注释，也不改它们已有的注释。",
    "### 安全评估",
    "### 反问",
    "这么改行不行",
    "符不符合安全",
    "不写口令、密钥、令牌、完整报文。",
    "不照抄方案「自审」里的安全评估。",
    "为什么这么写，有没有问题，有没有更好的实现方式。",
    "反问的任一子项写了「无」",
    "只是另一种写法、结果相同、安全性相同，不因此不可执行。",
    "### 覆盖",
    "五格有一格空着不算一轮。",
    "只写「没有」不算填实。",
    "只写「通过」不算填实。",
    "发现必须逐条列出，漏一条不算一轮。",
    "硬闸 13 的注释要求适用于执行里每一行要落地的代码，包括链路以内改写或补上的注释。",
    "完整报文指包含请求或响应全部字段的原始文本。",
    "现状没有把链路写到函数或语句块时，自审不通过，不交给 B。",
    "这一次修订要处理该轮发现里的全部问题，不要只改其中一条。",
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
        self.assertNotIn("本次不改的行不加，也不改它们已有的注释。", self.skill)

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
        self.assertNotIn("本次不改的行不加，也不改它们已有的注释。", self.procedure)

    def test_gap_capture_unchanged_and_routed(self):
        live = (REPO / "references" / "gap-capture.md").read_bytes()
        base = (
            REPO / "governance" / "baselines" / "0.1.0" / "references" / "gap-capture.md"
        ).read_bytes()
        self.assertEqual(live, base)
        for item in GAP_ROUTES:
            self.assertIn(item, self.skill, item)
        self.assertIn("references/gap-capture.md", self.skill)

    def test_readme_names_both_checks(self):
        self.assertIn("回归验证", self.readme)
        self.assertIn("bug修复验证", self.readme)
        self.assertIn("安全评估", self.readme)
        self.assertIn("反问", self.readme)


if __name__ == "__main__":
    unittest.main()
