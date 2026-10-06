#!/usr/bin/env python3
"""验证 Shimamura-Skill 的 `文件名:行号` 引用。

背景：主文件有 1400+ 处行号引用；人工核对三轮都漏过错，而其中
「指向空行／图片占位行／越界」这类错误是**机械可判定**的，不该靠人眼。

设计原则：**宁可漏报，不要误报**。分三类输出：

  ERROR  一定是错，必须修
         * 行号越界
         * 指向空行或【图片内容】占位行
         * 引用的源文件不存在
  ANCHOR 指向章节标题行——**多数是有意为之**（把章标题当作"这一章从这里开始"的锚点），
         但需要人工确认；如果本意是引用正文，就是错。
  QUOTE  紧邻引用的短引（`「…」`（`file:line`）这种紧贴写法）在 ±5 行窗口里找不到。
         只在"紧贴"时才报，避免把邻接引用的短引错配过来。

用法：
    python scripts/check_citations.py [skill目录] [报告输出路径]

报告写成 UTF-8 markdown。退出码：有 ERROR 时为 1。
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CITE = re.compile(r"`(安达与岛村[^`]*?\.md):(\d+)(?:-(\d+))?`")
# 紧贴写法：短引后面 0–4 个字符内就跟上引用
TIGHT_AFTER = re.compile(r"[「『]([^「」『』]{2,40})[」』][`）)\s]{0,4}`?(安达与岛村[^`]*?\.md):(\d+)")
TIGHT_BEFORE = re.compile(r"`(安达与岛村[^`]*?\.md):(\d+)`[^`\n]{0,4}[「『]([^「」『』]{2,40})[」』]")
WINDOW = 5

DEFAULT_DOCS = ["SKILL.md", "README.md", "references/shimamura-blade.md"]


def load(p: Path) -> list[str]:
    return p.read_text(encoding="utf-8", errors="replace").splitlines()


def bad_line(s: str) -> str | None:
    t = s.strip()
    if t == "":
        return "空行"
    if t.startswith("【图片内容"):
        return "图片占位行"
    return None


def main() -> int:
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    scan_all = "--all" in sys.argv
    root = Path(argv[0]) if argv else Path(__file__).resolve().parent.parent
    out = Path(argv[1]) if len(argv) > 1 else root / "references" / "citation-report.md"
    src_dir = root / "references" / "source"
    if not src_dir.is_dir():
        print(f"找不到语料目录：{src_dir}", file=sys.stderr)
        return 2

    docs = [root / d for d in DEFAULT_DOCS if (root / d).is_file()]
    docs += [
        p
        for p in sorted((root / "references").glob("*.md"))
        if p not in docs
        and p.name not in {"citation-report.md", "citation-report-all.md"}
        and not p.name.startswith("citation-report")
    ]
    if scan_all:
        docs += sorted((root / "references" / "research").glob("*.md"))

    cache: dict[str, list[str]] = {}
    errors: list[str] = []
    expected: list[str] = []
    loose: list[str] = []
    anchors: list[str] = []
    quotes: list[str] = []
    verbatim: list[str] = []
    total = 0

    for doc in docs:
        text = doc.read_text(encoding="utf-8", errors="replace")
        lines_of_doc = text.splitlines()
        rel = doc.relative_to(root)
        n_doc = 0

        for m in CITE.finditer(text):
            total += 1
            n_doc += 1
            fname, line_no = m.group(1), int(m.group(2))
            src = src_dir / fname
            if not src.is_file():
                errors.append(f"{rel}: 源文件不存在 `{fname}`")
                continue
            if fname not in cache:
                cache[fname] = load(src)
            lines = cache[fname]
            if not (1 <= line_no <= len(lines)):
                errors.append(f"{rel}: `{fname}:{line_no}` 越界（该文件共 {len(lines)} 行）")
                continue
            raw = lines[line_no - 1]
            why = bad_line(raw)
            if why:
                # 三类"看起来像错、其实不是"的写法：
                #  LOOSE  —— 正文写的是"某某行 前后／附近／一带"，本来就是模糊锚点
                #  RANGE  —— 引用是一个区间 `:143-5507`，起点行恰好是空行，属排版边界
                #  REPORT —— validation-canon*.md 在描述"这个行号本身是错的"
                ctx = text[max(0, m.start() - 30) : m.end() + 30]
                is_range = m.group(3) is not None
                is_loose = any(k in ctx for k in ("前后", "附近", "一带", "左右"))
                if rel.name.startswith("validation-canon"):
                    expected.append(f"{rel}: `{fname}:{line_no}` 指向{why}（报告在引用该错误本身）")
                elif is_range or is_loose:
                    loose.append(
                        f"{rel}: `{fname}:{line_no}` 指向{why}"
                        f"（{'区间起点' if is_range else '模糊锚点'}，非缺陷）"
                    )
                else:
                    errors.append(f"{rel}: `{fname}:{line_no}` 指向{why}")
            elif raw.lstrip().startswith("#"):
                anchors.append(f"{rel}: `{fname}:{line_no}` → {raw.strip()[:40]}")

        # 紧贴短引核对
        for rx, qi, fi, li in (
            (TIGHT_AFTER, 1, 2, 3),
            (TIGHT_BEFORE, 3, 1, 2),
        ):
            for m in rx.finditer(text):
                fname, line_no = m.group(fi), int(m.group(li))
                quote = m.group(qi)
                src = src_dir / fname
                if not src.is_file():
                    continue
                if fname not in cache:
                    cache[fname] = load(src)
                lines = cache[fname]
                if not (1 <= line_no <= len(lines)):
                    continue
                win = re.sub(r"\s", "", "".join(lines[max(0, line_no - 1 - WINDOW) : line_no + WINDOW]))
                if re.sub(r"\s", "", quote) not in win:
                    quotes.append(f"{rel}: `{fname}:{line_no}` 找不到紧贴短引 `{quote}`")

        # 横向一致性：同一行里"反引号包住的短引"必须逐字出现在被引的那一行
        # （本轮加这道检查，是因为曾经出现「同一句在 README 里对、在 blade.md 里漏一个字」的情况）
        for i, ln in enumerate(lines_of_doc):
            cits = list(CITE.finditer(ln))
            if not cits:
                continue
            qs = re.findall(r"`[「『]([^「」『』]{4,40})[」』]`", ln)
            # 只在"一行一引用一短引"这种无歧义配对上判定，否则 N×M 组合会产生大量误报
            if len(qs) != 1 or len(cits) != 1:
                continue
            for mm in cits:
                fname, line_no = mm.group(1), int(mm.group(2))
                src = src_dir / fname
                if not src.is_file():
                    continue
                if fname not in cache:
                    cache[fname] = load(src)
                lines = cache[fname]
                if not (1 <= line_no <= len(lines)):
                    continue
                src_line = re.sub(r"\s", "", lines[line_no - 1])
                for q in qs:
                    if re.sub(r"\s", "", q) not in src_line:
                        verbatim.append(
                            f"{rel}:{i + 1} → `{fname}:{line_no}`：同行短引 `{q}` 不在该行原文里"
                        )

    report = [
        "# 引用检查报告（scripts/check_citations.py）",
        "",
        f"- 检查文件：{len(docs)} 个"
        + ("（含 research/，--all 模式）" if scan_all else "（主文件 + references 顶层 .md）"),
        f"- 引用总数：{total}",
        f"- **ERROR（必须修）：{len(errors)}**",
        f"- EXPECTED（错误记录类文件在引用「已知的错误行号」）：{len(expected)}",
        f"- LOOSE（区间起点 / 「前后·附近」式模糊锚点）：{len(loose)}",
        f"- ANCHOR（指向章节标题，合法的「这一章从这里开始」写法）：{len(anchors)}",
        f"- QUOTE（紧贴短引未命中，多为相邻引用的误配）：{len(quotes)}",
        f"- VERBATIM（同行短引与所引原文逐字不符，需人工确认配对）：{len(verbatim)}",
        "",
        "> **这个脚本只判断「机械可判定」的错，且宁可漏报不要误报。** 除 ERROR 外的四类"
        "都是合法的或有意的写法，列出来只为让人一眼看到全貌。三轮人工核对的经验是："
        "真正的错几乎都发生在「这条结论对不对」这一层（因果、归属、统计量），而不是"
        "「行号指到哪一行」——所以 ERROR 为 0 不等于内容正确。",
        "",
    ]
    for title, items in (
        ("## ERROR（必须修）", errors),
        ("## EXPECTED（错误记录类文件，非缺陷）", expected),
        ("## LOOSE（区间起点 / 模糊锚点，非缺陷）", loose),
        ("## ANCHOR（章标题锚点）", anchors),
        ("## QUOTE（短引未命中）", quotes),
        ("## VERBATIM（同行短引与原文逐字不符）", verbatim),
    ):
        report.append(title)
        report.append("")
        report.extend(f"- {i}" for i in (items or ["（无）"]))
        report.append("")

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(report), encoding="utf-8")

    print(f"report -> {out}")
    print(
        f"total={total} ERROR={len(errors)} EXPECTED={len(expected)} "
        f"LOOSE={len(loose)} ANCHOR={len(anchors)} QUOTE={len(quotes)}"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
