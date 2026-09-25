# WaytoAGI Visual Style Library

A reusable visual-language reference library for WaytoAGI skills. It contains the seven styles from `daily-comic-report` plus 23 new Pinterest-based references, for 30 styles total.

## Use from a skill

1. Read [`catalog.json`](catalog.json).
2. Choose a style by `id` or `tags`.
3. Read the matching file under [`prompts/`](prompts/).
4. Replace `{variables}` with the current task's subject, copy, scene, and layout requirements.
5. Keep source-specific names, logos, signatures, QR codes, and unrelated copy out of the generated image.

The prompts describe visual language only. A skill can reuse them for comics, posters, slides, web visuals, and social content.

查看全部 30 个条目的配图、来源与提示词：[`GALLERY.md`](GALLERY.md)。

## Styles

| ID | Name | Best for |
|---|---|---|
| 01 | 像素梦境 | 复古网页、成长旅程、游戏感叙事 |
| 02 | 黑白日历拼格 | 日记、时间线、单日复盘 |
| 03 | 蜡笔拼贴 | 轻松手帐、情绪拼贴、亲子内容 |
| 04 | 荧光双色涂鸦 | 活动海报、贴纸、潮流社媒 |
| 05 | 童趣粗线 | 生活漫画、轻量品牌故事 |
| 06 | 黑黄实验排版 | 编辑海报、观点卡、复杂信息 |
| 07 | 波普立体书 | 项目回顾、知识卡、空间化叙事 |
| 08 | 软体字角色海报 | 品牌角色、餐饮与生活方式 |
| 09 | 城市荧光剪影 | 城市观察、摄影活动、文化海报 |
| 10 | 透明证件卡档案 | 个人介绍、职业卡、设计档案 |
| 11 | 青春物件环形拼贴 | 音乐企划、主题策展、青年文化 |
| 12 | 复古照片荧光涂鸦 | 艺术拼贴、社交内容、复古叙事 |
| 13 | 橙色生活分镜 | 居住故事、生活记录、活动分镜 |

## CLI lookup

```bash
python3 select_style.py 08
python3 select_style.py storyboard
```

The command prints the selected style metadata and the full prompt as JSON, so another skill can call it without knowing the directory layout.

## Batch 2: styles 14—30

| ID | Name | Best for |
|---|---|---|
| 14 | 粉色实物杂货目录 | 杂货目录、物件收藏、产品海报 |
| 15 | 金属磁贴记忆拼贴 | 人物情绪板、旅行记忆、个人档案 |
| 16 | 博物馆撕纸胶带清单 | 展览导览、收藏清单、知识卡 |
| 17 | 复古桌面物件拼贴 | 数字日记、创作者主页、音乐与活动海报 |
| 18 | 像素柔焦选框研究板 | 视觉研究、物件档案、实验海报 |
| 19 | 黑色软体角色绘本提案 | 儿童绘本、概念教学、IP提案 |
| 20 | 随手画品牌物件板 | hand-drawn, brand board |
| 21 | 建筑色块叠印书封 | 建筑书封、城市主题、展览封面 |
| 22 | 蓝色水彩票券套装 | 活动票券、联名物料、品牌包装 |
| 23 | 春日童趣九宫格 | children, spring |
| 24 | 黄黑伙伴关系信息图 | infographic, yellow black |
| 25 | 粉彩颗粒动作分镜 | 创作理念、读书卡、过程说明 |
| 26 | 黑底极简新闻图 | news graphic, black |
| 27 | 手写涂鸦品牌延展 | 品牌延展、活动物料、生活方式海报 |
| 28 | 黑白猫咪贴纸格 | stickers, monochrome |
| 29 | 红框漫画方法卡 | comic, method |
| 30 | 人物连线照片墙 | 信息关系、自我观察、概念摄影 |
