# 引用检查报告（scripts/check_citations.py）

- 检查文件：12 个（主文件 + references 顶层 .md）
- 引用总数：423
- **ERROR（必须修）：0**
- EXPECTED（错误记录类文件在引用「已知的错误行号」）：3
- LOOSE（区间起点 / 「前后·附近」式模糊锚点）：0
- ANCHOR（指向章节标题，合法的「这一章从这里开始」写法）：22
- QUOTE（紧贴短引未命中，多为相邻引用的误配）：5
- VERBATIM（同行短引与所引原文逐字不符，需人工确认配对）：2

> **这个脚本只判断「机械可判定」的错，且宁可漏报不要误报。** 除 ERROR 外的四类都是合法的或有意的写法，列出来只为让人一眼看到全貌。三轮人工核对的经验是：真正的错几乎都发生在「这条结论对不对」这一层（因果、归属、统计量），而不是「行号指到哪一行」——所以 ERROR 为 0 不等于内容正确。

## ERROR（必须修）

- （无）

## EXPECTED（错误记录类文件，非缺陷）

- references\validation-canon.md: `安达与岛村9.md:790` 指向空行（报告在引用该错误本身）
- references\validation-canon.md: `安达与岛村9.md:790` 指向空行（报告在引用该错误本身）
- references\validation-canon.md: `安达与岛村9.md:790` 指向空行（报告在引用该错误本身）

## LOOSE（区间起点 / 模糊锚点，非缺陷）

- （无）

## ANCHOR（章标题锚点）

- SKILL.md: `安达与岛村8.md:20` → # 「远游」
- SKILL.md: `安达与岛村 99.9.md:13` → # Chito
- SKILL.md: `安达与岛村11.md:3907` → # 『Remember22』
- SKILL.md: `安达与岛村5.md:24` → # if「如果大家很年幼」
- SKILL.md: `安达与岛村7.md:21` → # 「如果没有在体育馆二楼相遇」
- SKILL.md: `安达与岛村7.md:835` → # 「如果安达贯彻最初的风格」
- SKILL.md: `安达与岛村 12.md:3653` → # 如果一切一如既往
- SKILL.md: `安达与岛村2.md:1491` → # 附录「肉店来访者」
- SKILL.md: `安达与岛村8.md:3636` → # 「日野与永藤」
- SKILL.md: `安达与岛村9.md:957` → # 第二章「晶」
- README.md: `安达与岛村5.md:2470` → # 第二话　「岛村之刃」
- references\validation-canon-round2.md: `安达与岛村 SS.md:949` → # 效果永存
- references\validation-canon-round2.md: `安达与岛村8.md:20` → # 「远游」
- references\validation-canon.md: `安达与岛村8.md:20` → # 「远游」
- references\validation-canon.md: `安达与岛村 SS.md:949` → # 效果永存
- references\validation-canon.md: `安达与岛村 SS.md:949` → # 效果永存
- references\validation-canon.md: `安达与岛村 SS.md:949` → # 效果永存
- references\validation-canon.md: `安达与岛村 12.md:3653` → # 如果一切一如既往
- references\validation-citation-audit.md: `安达与岛村8.md:20` → # 「远游」
- references\validation-citation-audit.md: `安达与岛村8.md:20` → # 「远游」
- references\validation-edge-voice.md: `安达与岛村7.md:1031` → # 第二章　「仅需要片刻的安宁」
- references\validation.md: `安达与岛村 12.md:3653` → # 如果一切一如既往

## QUOTE（短引未命中）

- SKILL.md: `安达与岛村10.md:699` 找不到紧贴短引 `岛村并不温柔`
- SKILL.md: `安达与岛村10.md:2783` 找不到紧贴短引 `我想不到自己以前有做错什么决定`
- references\refine-creator.md: `安达与岛村4.md:3316` 找不到紧贴短引 `安达儿～`
- references\validation-canon-round2.md: `安达与岛村5.md:2658` 找不到紧贴短引 `我！讨厌岛村在我不知道的地方露出笑容！……`
- references\validation-canon.md: `安达与岛村9.md:790` 找不到紧贴短引 `算了，无所谓`

## VERBATIM（同行短引与原文逐字不符）

- SKILL.md:31 → `安达与岛村8.md:1638`：同行短引 `她的爱太沉重啦……` 不在该行原文里
- references\validation-canon-round2.md:49 → `安达与岛村5.md:2658`：同行短引 `等一下，安达──` 不在该行原文里
