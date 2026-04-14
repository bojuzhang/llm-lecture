# 大模型推理 & Inference Time Scaling — 课件项目

## 项目概述

为《大语言模型》课程制作 45 分钟讲课课件（reveal.js HTML），三人各 ~15 min。

## 听众背景

中高年级本科生，了解神经网络基础（RNN、CNN），对 Transformer/Attention 了解较少。内容需适度深入数学本质，但需详细解释每个概念。

## 三人分工

| Part | 主讲人 | 内容 | 时长 | Slides 数 |
|------|--------|------|------|-----------|
| Part 1 | A | 推理基础 — 从 Transformer 到自回归生成 | ~15 min | 11 |
| Part 2 | B | 推理加速技术 | ~15 min | 10 |
| Part 3 | C | Inference-Time Scaling | ~15 min | 10 |

过渡衔接：
- Part 1 → Part 2: "了解了推理流程和瓶颈，接下来看如何加速"
- Part 2 → Part 3: "单次推理变快后，能否用更多推理计算提升效果？"

## 技术栈

- **框架**: reveal.js 5.x (CDN)
- **数学**: KaTeX (reveal.js 插件)
- **代码高亮**: highlight.js (内置)
- **演讲者模式**: 按 `S` 键，每张 slide 附 `<aside class="notes">` 备注

## 视觉内容策略

| 类型 | 用途 | 制作方式 |
|------|------|---------|
| PNG 大图 (5张) | 过渡/引入/总结页，视觉冲击力 | `nano-banana-pro` skill |
| Inline SVG (~12张) | 技术原理图解，精确可控 | 直接在 HTML 中手写 |
| 代码生成图表 (6张) | 数据驱动的图表 | Python/Matplotlib → 导出嵌入 |
| HTML/CSS 排版 | 文字对比（如 CoT 示例） | 无需图片 |

## 构建流程

**源文件**（编辑这些文件）：
- `slides/part1-fundamentals.html` / `part2-optimization.html` / `part3-scaling.html`
- `slides/shared-style.css`

**构建**：
```bash
python build.py
```
读取上述源文件，组装为单文件 `index.html`（内联 CSS + HTML，无需 HTTP 服务器）。

**重要**：修改 part 文件或 CSS 后必须运行 `python build.py` 才能在 index.html 中生效。

## 文件结构

```
llm-lecture/
├── CLAUDE.md
├── build.py                      # 构建脚本（源文件 → index.html）
├── index.html                    # 构建产物（单文件，可直接用浏览器打开）
├── slides/
│   ├── part1-fundamentals.html   # Part 1 源文件
│   ├── part2-optimization.html   # Part 2 源文件
│   ├── part3-scaling.html        # Part 3 源文件
│   └── shared-style.css          # CSS 主题源文件
├── demos/
│   ├── kv_cache_demo.ipynb           # 图表生成脚本（非实时 demo）
│   ├── speculative_decode_demo.ipynb
│   └── self_consistency_demo.ipynb
└── assets/
    ├── p1-rnn-vs-attention.png
    ├── p2-optimization-landscape.png
    ├── p3-two-scaling.png
    ├── p3-tot-mcts.png
    ├── p3-summary.png
    ├── chart-kv-memory.png
    ├── chart-latency-breakdown.png
    ├── chart-roofline.png
    ├── chart-spec-decode.png
    ├── chart-self-consistency-voting.png
    └── chart-scaling-law.png
```

## CSS 主题

使用 `frontend-design` + `theme-factory` skill 生成。
风格：深色背景（深蓝/深灰），浅色文字，适合投影，代码块 monokai 风格。

## 注意事项

- 计划文件位于 `/home/zhangboju/.claude/plans/smooth-rolling-pebble.md`
- 后续需求变动时需同步更新此文件
- 数学公式使用 KaTeX 语法（`$...$` 行内，`$$...$$` 独立行）
- SVG 图解配色需与 CSS 主题一致
