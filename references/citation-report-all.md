# 引用检查报告（scripts/check_citations.py）

- 检查文件：21 个（含 research/，--all 模式）
- 引用总数：1461
- **ERROR（必须修）：0**
- EXPECTED（错误记录类文件在引用「已知的错误行号」）：3
- LOOSE（区间起点 / 「前后·附近」式模糊锚点）：13
- ANCHOR（指向章节标题，合法的「这一章从这里开始」写法）：133
- QUOTE（紧贴短引未命中，多为相邻引用的误配）：28
- VERBATIM（同行短引与所引原文逐字不符，需人工确认配对）：5

> **这个脚本只判断「机械可判定」的错，且宁可漏报不要误报。** 除 ERROR 外的四类都是合法的或有意的写法，列出来只为让人一眼看到全貌。三轮人工核对的经验是：真正的错几乎都发生在「这条结论对不对」这一层（因果、归属、统计量），而不是「行号指到哪一行」——所以 ERROR 为 0 不等于内容正确。

## ERROR（必须修）

- （无）

## EXPECTED（错误记录类文件，非缺陷）

- references\validation-canon.md: `安达与岛村9.md:790` 指向空行（报告在引用该错误本身）
- references\validation-canon.md: `安达与岛村9.md:790` 指向空行（报告在引用该错误本身）
- references\validation-canon.md: `安达与岛村9.md:790` 指向空行（报告在引用该错误本身）

## LOOSE（区间起点 / 模糊锚点，非缺陷）

- references\research\01-writings.md: `安达与岛村1.md:4370` 指向空行（区间起点，非缺陷）
- references\research\02-conversations.md: `安达与岛村1.md:1900` 指向空行（区间起点，非缺陷）
- references\research\02-conversations.md: `安达与岛村1.md:3630` 指向空行（区间起点，非缺陷）
- references\research\02-conversations.md: `安达与岛村2.md:3700` 指向空行（区间起点，非缺陷）
- references\research\02-conversations.md: `安达与岛村6.md:3555` 指向空行（区间起点，非缺陷）
- references\research\02-conversations.md: `安达与岛村8.md:2055` 指向空行（区间起点，非缺陷）
- references\research\02-conversations.md: `安达与岛村8.md:3415` 指向空行（区间起点，非缺陷）
- references\research\02-conversations.md: `安达与岛村 SS.md:960` 指向空行（区间起点，非缺陷）
- references\research\02-conversations.md: `安达与岛村 99.9.md:4060` 指向空行（区间起点，非缺陷）
- references\research\02-conversations.md: `安达与岛村8.md:5495` 指向空行（区间起点，非缺陷）
- references\research\05-decisions.md: `安达与岛村10.md:1602` 指向空行（模糊锚点，非缺陷）
- references\research\05-decisions.md: `安达与岛村10.md:2690` 指向空行（模糊锚点，非缺陷）
- references\research\06-timeline.md: `安达与岛村5.md:143` 指向空行（区间起点，非缺陷）

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
- references\research\00-lead-review.md: `安达与岛村10.md:2923` → # 『The Moon Cradle』
- references\research\00-verified-anchors.md: `安达与岛村7.md:1031` → # 第二章　「仅需要片刻的安宁」
- references\research\00-verified-anchors.md: `安达与岛村2.md:2241` → # 安达思考中圣诞节进行中
- references\research\00-verified-anchors.md: `安达与岛村6.md:2754` → # 第三话　「爱情错综」
- references\research\01-writings.md: `安达与岛村1.md:19` → # 制服PINPON
- references\research\01-writings.md: `安达与岛村2.md:25` → # 岛村 前往健身房
- references\research\01-writings.md: `安达与岛村2.md:961` → # 安达Ｑ
- references\research\01-writings.md: `安达与岛村9.md:21` → # 第一章「YOUNG岛抱月」
- references\research\01-writings.md: `安达与岛村1.md:19` → # 制服PINPON
- references\research\01-writings.md: `安达与岛村2.md:25` → # 岛村 前往健身房
- references\research\01-writings.md: `安达与岛村2.md:2947` → # 岛村思考中圣诞节进行中
- references\research\01-writings.md: `安达与岛村3.md:33` → # 第一章「请挑选一个适合我的巧克力」
- references\research\01-writings.md: `安达与岛村4.md:768` → # 第二章「春与月」
- references\research\01-writings.md: `安达与岛村4.md:2888` → # 第四章「决心与友人」
- references\research\01-writings.md: `安达与岛村5.md:504` → # 第一话　「来自蔚蓝」
- references\research\01-writings.md: `安达与岛村6.md:2754` → # 第三话　「爱情错综」
- references\research\01-writings.md: `安达与岛村6.md:4162` → # 第四话　「飞翔」
- references\research\01-writings.md: `安达与岛村7.md:1031` → # 第二章　「仅需要片刻的安宁」
- references\research\01-writings.md: `安达与岛村7.md:2675` → # 第三章　「平凡至极的话语」
- references\research\01-writings.md: `安达与岛村7.md:4069` → # 第四章　「许下小小愿望」
- references\research\01-writings.md: `安达与岛村8.md:20` → # 「远游」
- references\research\01-writings.md: `安达与岛村8.md:4216` → # 「第一次旅行的一角②」
- references\research\01-writings.md: `安达与岛村9.md:21` → # 第一章「YOUNG岛抱月」
- references\research\01-writings.md: `安达与岛村9.md:4572` → # 第五章「因为是难以割舍的关系」
- references\research\01-writings.md: `安达与岛村10.md:189` → # 『Astray from the Sentiment』
- references\research\01-writings.md: `安达与岛村10.md:2923` → # 『The Moon Cradle』
- references\research\01-writings.md: `安达与岛村10.md:4028` → # 『Stay of Hope』
- references\research\01-writings.md: `安达与岛村11.md:26` → # 『黑色夜幕里的白色星辰』
- references\research\01-writings.md: `安达与岛村11.md:2881` → # 『Summer18』
- references\research\01-writings.md: `安达与岛村11.md:3907` → # 『Remember22』
- references\research\01-writings.md: `安达与岛村 SS.md:13` → # 第几次的开始
- references\research\01-writings.md: `安达与岛村 SS.md:949` → # 效果永存
- references\research\01-writings.md: `安达与岛村 SS2.md:1123` → # 『纯真无邪』
- references\research\01-writings.md: `安达与岛村7.md:21` → # 「如果没有在体育馆二楼相遇」
- references\research\01-writings.md: `安达与岛村7.md:835` → # 「如果安达贯彻最初的风格」
- references\research\01-writings.md: `安达与岛村5.md:24` → # if「如果大家很年幼」
- references\research\01-writings.md: `安达与岛村 12.md:51` → # 如果安达是老师
- references\research\01-writings.md: `安达与岛村 99.9.md:13` → # Chito
- references\research\01-writings.md: `安达与岛村7.md:4985` → # 后记
- references\research\02-conversations.md: `安达与岛村5.md:2470` → # 第二话　「岛村之刃」
- references\research\02-conversations.md: `安达与岛村5.md:24` → # if「如果大家很年幼」
- references\research\02-conversations.md: `安达与岛村7.md:201` → # 第一章　「感受着你的笑容」
- references\research\02-conversations.md: `安达与岛村7.md:1031` → # 第二章　「仅需要片刻的安宁」
- references\research\02-conversations.md: `安达与岛村7.md:2675` → # 第三章　「平凡至极的话语」
- references\research\02-conversations.md: `安达与岛村9.md:21` → # 第一章「YOUNG岛抱月」
- references\research\02-conversations.md: `安达与岛村9.md:4572` → # 第五章「因为是难以割舍的关系」
- references\research\02-conversations.md: `安达与岛村10.md:1059` → # 『Be Your Self』
- references\research\02-conversations.md: `安达与岛村10.md:4028` → # 『Stay of Hope』
- references\research\02-conversations.md: `安达与岛村11.md:124` → # 『Never8』
- references\research\02-conversations.md: `安达与岛村 SS2.md:2641` → # 『快来吧』
- references\research\02-conversations.md: `安达与岛村5.md:2470` → # 第二话　「岛村之刃」
- references\research\02-conversations.md: `安达与岛村 SS2.md:2597` → # 『无论在哪里都是岛村抱月』
- references\research\02-conversations.md: `安达与岛村5.md:24` → # if「如果大家很年幼」
- references\research\02-conversations.md: `安达与岛村5.md:2470` → # 第二话　「岛村之刃」
- references\research\04-external-views.md: `安达与岛村2.md:961` → # 安达Ｑ
- references\research\04-external-views.md: `安达与岛村9.md:957` → # 第二章「晶」
- references\research\04-external-views.md: `安达与岛村9.md:2591` → # 第三章「妙子」
- references\research\04-external-views.md: `安达与岛村7.md:21` → # 「如果没有在体育馆二楼相遇」
- references\research\04-external-views.md: `安达与岛村5.md:24` → # if「如果大家很年幼」
- references\research\04-external-views.md: `安达与岛村7.md:2479` → # 附录 「日野与永藤」
- references\research\04-external-views.md: `安达与岛村9.md:4326` → # 附录「安达与岛村与圣诞节」
- references\research\05-decisions.md: `安达与岛村7.md:21` → # 「如果没有在体育馆二楼相遇」
- references\research\05-decisions.md: `安达与岛村5.md:24` → # if「如果大家很年幼」
- references\research\05-decisions.md: `安达与岛村7.md:21` → # 「如果没有在体育馆二楼相遇」
- references\research\05-decisions.md: `安达与岛村7.md:835` → # 「如果安达贯彻最初的风格」
- references\research\05-decisions.md: `安达与岛村5.md:24` → # if「如果大家很年幼」
- references\research\06-timeline.md: `安达与岛村8.md:20` → # 「远游」
- references\research\06-timeline.md: `安达与岛村11.md:2881` → # 『Summer18』
- references\research\06-timeline.md: `安达与岛村 12.md:5081` → # 相伴夏天
- references\research\06-timeline.md: `安达与岛村11.md:3907` → # 『Remember22』
- references\research\06-timeline.md: `安达与岛村3.md:17` → # 「今天的安达同学」
- references\research\06-timeline.md: `安达与岛村6.md:5170` → # 后记
- references\research\06-timeline.md: `安达与岛村8.md:5576` → # 后记
- references\research\06-timeline.md: `安达与岛村 12.md:5169` → # 愉快的问答大会
- references\research\06-timeline.md: `安达与岛村11.md:124` → # 『Never8』
- references\research\06-timeline.md: `安达与岛村9.md:21` → # 第一章「YOUNG岛抱月」
- references\research\06-timeline.md: `安达与岛村1.md:19` → # 制服PINPON
- references\research\06-timeline.md: `安达与岛村3.md:4355` → # 第五章「樱─愿望闪耀之时─」
- references\research\06-timeline.md: `安达与岛村8.md:1080` → # 「第一次旅行的一角①」
- references\research\06-timeline.md: `安达与岛村5.md:258` → # 「就算你不求我，我也会去见你」
- references\research\06-timeline.md: `安达与岛村6.md:4162` → # 第四话　「飞翔」
- references\research\06-timeline.md: `安达与岛村11.md:2881` → # 『Summer18』
- references\research\06-timeline.md: `安达与岛村 12.md:5081` → # 相伴夏天
- references\research\06-timeline.md: `安达与岛村11.md:3907` → # 『Remember22』
- references\research\06-timeline.md: `安达与岛村10.md:189` → # 『Astray from the Sentiment』
- references\research\06-timeline.md: `安达与岛村11.md:124` → # 『Never8』
- references\research\06-timeline.md: `安达与岛村9.md:21` → # 第一章「YOUNG岛抱月」
- references\research\06-timeline.md: `安达与岛村1.md:19` → # 制服PINPON
- references\research\06-timeline.md: `安达与岛村2.md:25` → # 岛村 前往健身房
- references\research\06-timeline.md: `安达与岛村2.md:2241` → # 安达思考中圣诞节进行中
- references\research\06-timeline.md: `安达与岛村3.md:33` → # 第一章「请挑选一个适合我的巧克力」
- references\research\06-timeline.md: `安达与岛村4.md:22` → # 第一章「樱与春」
- references\research\06-timeline.md: `安达与岛村8.md:1080` → # 「第一次旅行的一角①」
- references\research\06-timeline.md: `安达与岛村7.md:191` → # 「今天的安达同学」
- references\research\06-timeline.md: `安达与岛村9.md:21` → # 第一章「YOUNG岛抱月」
- references\research\06-timeline.md: `安达与岛村10.md:1189` → # 『The Sakura's Ark』
- references\research\06-timeline.md: `安达与岛村11.md:2881` → # 『Summer18』
- references\research\06-timeline.md: `安达与岛村 12.md:5081` → # 相伴夏天
- references\research\06-timeline.md: `安达与岛村11.md:3907` → # 『Remember22』
- references\research\06-timeline.md: `安达与岛村10.md:189` → # 『Astray from the Sentiment』
- references\research\06-timeline.md: `安达与岛村8.md:20` → # 「远游」
- references\research\06-timeline.md: `安达与岛村 99.9.md:13` → # Chito
- references\research\06-timeline.md: `安达与岛村1.md:4451` → # 女高中生HOLIDAY
- references\research\06-timeline.md: `安达与岛村10.md:2923` → # 『The Moon Cradle』
- references\research\_method.md: `安达与岛村2.md:25` → # 岛村 前往健身房
- references\research\_method.md: `安达与岛村7.md:1019` → # 「今天的岛村同学」
- references\research\_method.md: `安达与岛村1.md:2173` → # 安达QUESTION
- references\research\_method.md: `安达与岛村2.md:961` → # 安达Ｑ
- references\research\_method.md: `安达与岛村7.md:21` → # 「如果没有在体育馆二楼相遇」
- references\research\_method.md: `安达与岛村7.md:835` → # 「如果安达贯彻最初的风格」
- references\research\_method.md: `安达与岛村5.md:24` → # if「如果大家很年幼」

## QUOTE（短引未命中）

- SKILL.md: `安达与岛村10.md:699` 找不到紧贴短引 `岛村并不温柔`
- SKILL.md: `安达与岛村10.md:2783` 找不到紧贴短引 `我想不到自己以前有做错什么决定`
- references\refine-creator.md: `安达与岛村4.md:3316` 找不到紧贴短引 `安达儿～`
- references\validation-canon-round2.md: `安达与岛村5.md:2658` 找不到紧贴短引 `我！讨厌岛村在我不知道的地方露出笑容！……`
- references\validation-canon.md: `安达与岛村9.md:790` 找不到紧贴短引 `算了，无所谓`
- references\research\00-verified-anchors.md: `安达与岛村 SS.md:1281` 找不到紧贴短引 `上瘾`
- references\research\00-verified-anchors.md: `安达与岛村10.md:4469` 找不到紧贴短引 `告白`
- references\research\02-conversations.md: `安达与岛村7.md:1543` 找不到紧贴短引 `更重要的问题是，我该用什么态度面对安达？`
- references\research\02-conversations.md: `安达与岛村10.md:4999` 找不到紧贴短引 `跟安达交往以后，就不能再去找樽见了。`
- references\research\02-conversations.md: `安达与岛村10.md:4483` 找不到紧贴短引 `安达现在一样是我最看重的那个人。`
- references\research\02-conversations.md: `安达与岛村11.md:4085` 找不到紧贴短引 `反而安达比我还要容易吸引其他人的目光，害我总是心惊胆跳的……其实也没有啦`
- references\research\02-conversations.md: `安达与岛村10.md:4573` 找不到紧贴短引 `每个人对我的称呼大多会用岛村当作基础……我几乎只有姓氏会被当绰号，名字就不会。`
- references\research\02-conversations.md: `安达与岛村6.md:5110` 找不到紧贴短引 `我是第一次交到女朋友`
- references\research\02-conversations.md: `安达与岛村5.md:2682` 找不到紧贴短引 `**用身体动作代替语言**`
- references\research\04-external-views.md: `安达与岛村1.md:2999` 找不到紧贴短引 `但是岛村不会继续追究。她个性就是这样`
- references\research\04-external-views.md: `安达与岛村5.md:5114` 找不到紧贴短引 `感觉好像被布下了防线`
- references\research\04-external-views.md: `安达与岛村4.md:2106` 找不到紧贴短引 `对安达破例`
- references\research\05-decisions.md: `安达与岛村2.md:239` 找不到紧贴短引 `只是麻烦`
- references\research\05-decisions.md: `安达与岛村1.md:45` 找不到紧贴短引 `是不讨厌啊`
- references\research\05-decisions.md: `安达与岛村6.md:3772` 找不到紧贴短引 `还好啦～`
- references\research\05-decisions.md: `安达与岛村2.md:4439` 找不到紧贴短引 `应该不用回复，直接由我打电话给她就好了吧……我马上就找到她的电话号码`
- references\research\05-decisions.md: `安达与岛村6.md:5160` 找不到紧贴短引 `而剩下的问题，明天的我会想办法解决。`
- references\research\05-decisions.md: `安达与岛村10.md:2783` 找不到紧贴短引 `我无法给她超乎友情的情感，所以这次是真的只能选择不采取任何行动。`
- references\research\05-decisions.md: `安达与岛村8.md:1800` 找不到紧贴短引 `朋友跟情人都只要有一个就够了`
- references\research\05-decisions.md: `安达与岛村6.md:5038` 找不到紧贴短引 `跟现在有什么不一样`
- references\research\06-timeline.md: `安达与岛村 99.9.md:5857` 找不到紧贴短引 `保洁员`
- references\research\06-timeline.md: `安达与岛村 99.9.md:267` 找不到紧贴短引 `我跟安达在不同的地方工作`
- references\research\06-timeline.md: `安达与岛村 SS.md:979` 找不到紧贴短引 `变成了从出生到死亡`

## VERBATIM（同行短引与原文逐字不符）

- SKILL.md:31 → `安达与岛村8.md:1638`：同行短引 `她的爱太沉重啦……` 不在该行原文里
- references\validation-canon-round2.md:49 → `安达与岛村5.md:2658`：同行短引 `等一下，安达──` 不在该行原文里
- references\research\00-lead-review.md:16 → `安达与岛村7.md:1783`：同行短引 `你的标准会不会有点太严格了～？` 不在该行原文里
- references\research\00-verified-anchors.md:206 → `安达与岛村10.md:2693`：同行短引 `是是是。` 不在该行原文里
- references\research\02-conversations.md:218 → `安达与岛村10.md:4815`：同行短引 `抱……夜？` 不在该行原文里
