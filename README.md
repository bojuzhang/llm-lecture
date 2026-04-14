# 大模型推理 & Inference-Time Scaling — 课程课件

《大语言模型》课程 45 分钟讲课课件，基于 [reveal.js](https://revealjs.com/) 构建。

## 课件内容

| Part | 内容 | 时长 |
|------|------|------|
| Part 1 | 推理基础 — Transformer → 自回归生成 → KV Cache → 瓶颈分析 | ~15 min |
| Part 2 | 推理加速技术 — Speculative Decoding、量化、Flash Attention、PagedAttention | ~15 min |
| Part 3 | Inference-Time Scaling — CoT、Self-Consistency、Tree of Thoughts、MCTS、Scaling Laws | ~15 min |

## 快速开始

直接用浏览器打开 `index.html` 即可播放课件，无需安装任何依赖或启动服务器。

快捷键：
- **方向键 / 空格** — 翻页
- **S** — 演讲者模式（显示备注 + 预览）
- **F** — 全屏模式
- **?** — 查看所有快捷键

## 如何修改课件

### 目录结构

```
llm-lecture/
├── build.py                        # 构建脚本
├── index.html                      # 构建产物（勿直接编辑）
├── slides/
│   ├── part1-fundamentals.html     # Part 1 内容
│   ├── part2-optimization.html     # Part 2 内容
│   ├── part3-scaling.html          # Part 3 内容
│   └── shared-style.css            # 全局样式主题
├── demos/
│   ├── kv_cache_demo.ipynb         # 图表生成脚本
│   ├── speculative_decode_demo.ipynb
│   └── self_consistency_demo.ipynb
└── assets/
    ├── p1-rnn-vs-attention.png     # 插图与图表
    └── ...
```

### 修改流程

**重要**：`index.html` 是构建脚本自动生成的，直接编辑它不会被保留。请按以下流程操作：

1. **编辑源文件**（任选其一）：
   - `slides/part1-fundamentals.html` — Part 1 的幻灯片
   - `slides/part2-optimization.html` — Part 2 的幻灯片
   - `slides/part3-scaling.html` — Part 3 的幻灯片
   - `slides/shared-style.css` — 全局样式（颜色、字体、布局等）

2. **重新构建**：
   ```bash
   python build.py
   ```
   脚本会读取上述源文件，组装生成 `index.html`。

3. **刷新浏览器**查看效果。

### 源文件格式

每个 part HTML 文件包含若干 `<section>` 标签，每个 `<section>` 就是一张幻灯片。示例：

```html
<section>
  <h2>标题</h2>
  <p>正文内容</p>
  <ul>
    <li>要点一</li>
    <li>要点二</li>
  </ul>
  <aside class="notes">
    演讲者备注（在演讲者模式中可见）
  </aside>
</section>
```

### 数学公式

使用 KaTeX 语法：
- 行内公式：`$E = mc^2$`
- 独立行公式：`$$P(y_t \mid y_{<t}) = \text{softmax}(W \cdot h_t)$$`

### CSS 主题

`slides/shared-style.css` 定义了所有视觉样式。主要 CSS 变量：

| 变量 | 用途 | 当前值 |
|------|------|--------|
| `--ocean-deep` | 背景色 | `#1a2332` |
| `--ocean-teal` | 主强调色 | `#2d8b8b` |
| `--ocean-seafoam` | 标题/高亮色 | `#a8dadc` |
| `--ocean-cream` | 正文文字色 | `#f1faee` |

常用 CSS 类：
- `.two-column` — 双栏布局
- `.callout` — 提示框
- `.diagram` — SVG 图表容器
- `.dim` — 次要文字
- `.fragment` — 逐步显示动画

### 图片资源

`assets/` 目录包含两类图片：

- **PNG 插图**（`p1-*`、`p2-*`、`p3-*`）：氛围/过渡页大图，在幻灯片中通过 `<img src="assets/xxx.png">` 引用。
- **数据图表**（`chart-*`）：由 `demos/` 目录下的 Jupyter notebook 生成。如需更新数据，运行对应 notebook 后将输出的 PNG 替换到 `assets/` 目录。

## 技术依赖

课件通过 CDN 加载以下库，播放时需要网络连接：

- [reveal.js 5.x](https://revealjs.com/) — 幻灯片框架
- [KaTeX](https://katex.org/) — 数学公式渲染
- [highlight.js](https://highlightjs.org/) — 代码高亮（reveal.js 内置插件）
