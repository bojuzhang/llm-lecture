#!/usr/bin/env python3
"""
构建脚本：将分模块的 slides 组装为单文件 index.html
用法: python build.py
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def read(path):
    with open(os.path.join(BASE, path), 'r', encoding='utf-8') as f:
        return f.read()

# 读取各部分
css = read('slides/shared-style.css')
part1 = read('slides/part1-fundamentals.html')
part2 = read('slides/part2-optimization.html')
part3 = read('slides/part3-scaling.html')

# 生成 index.html
html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>大模型推理 &amp; Inference-Time Scaling</title>

  <!-- Reveal.js Core CSS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.css">

  <!-- KaTeX CSS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">

  <!-- Embedded Theme -->
  <style>
{css}

    /* Inline SVG colors — fallback values for speaker-view iframe context */
    .svg-diagram text {{ fill: var(--ocean-cream, #f1faee); font-family: "Source Sans 3", "Noto Sans SC", sans-serif; }}
    .svg-diagram .box {{ fill: var(--ocean-mid, #223044); stroke: var(--ocean-teal, #2d8b8b); stroke-width: 1.5; }}
    .svg-diagram .box-highlight {{ fill: var(--ocean-teal, #2d8b8b); }}
    .svg-diagram .box-highlight text {{ fill: var(--ocean-deep, #1a2332); font-weight: 700; }}
    .svg-diagram .arrow {{ stroke: var(--ocean-seafoam, #a8dadc); stroke-width: 2; fill: none; marker-end: url(#arrowhead); }}
    .svg-diagram .arrow-muted {{ stroke: var(--ocean-mist, #8faab0); stroke-width: 1.5; fill: none; opacity: 0.5; }}
  </style>
</head>
<body>

  <div class="reveal">
    <div class="slides">

      <!-- ═══════════════════════════════════════════════════════════
           Title Slide
           ═══════════════════════════════════════════════════════════ -->
      <section class="title-slide">
        <h1>大模型推理 &amp; Inference-Time Scaling</h1>
        <div class="subtitle">Large Model Inference &amp; Inference-Time Compute Scaling</div>
        <div class="authors">黄烨威 &nbsp;·&nbsp; 冯启豫 &nbsp;·&nbsp; 丁宣铭 &nbsp;·&nbsp; 张博钜</div>
        <div class="date">2026 春 · 《大语言模型》课程</div>
        <aside class="notes">
          开场：介绍课题 — 大模型推理是 LLM 应用的核心环节，本次课分三部分：
          Part 1 推理基础、Part 2 推理加速、Part 3 推理时扩展。
          每部分约 15 分钟，中间自然过渡。
        </aside>
      </section>

      <!-- ═══════════════════════════════════════════════════════════
           Roadmap
           ═══════════════════════════════════════════════════════════ -->
      <section>
        <h2>今日路线图</h2>
        <div style="display:flex; gap:1em; margin-top:1em;">
          <div style="flex:1; background:var(--ocean-mid); border-top:3px solid var(--ocean-teal); border-radius:8px; padding:1em;">
            <div style="color:var(--ocean-teal); font-weight:700; font-size:0.85em;">Part 1 · ~15 min</div>
            <div style="font-weight:700; margin:0.3em 0;">推理基础</div>
            <div class="dim" style="font-size:0.8em;">Transformer → 自回归生成 → KV Cache → 瓶颈分析</div>
          </div>
          <div style="flex:1; background:var(--ocean-mid); border-top:3px solid #5ec4c4; border-radius:8px; padding:1em;">
            <div style="color:#5ec4c4; font-weight:700; font-size:0.85em;">Part 2 · ~15 min</div>
            <div style="font-weight:700; margin:0.3em 0;">推理加速技术</div>
            <div class="dim" style="font-size:0.8em;">Speculative Decoding · 量化 · Flash Attention · PagedAttention</div>
          </div>
          <div style="flex:1; background:var(--ocean-mid); border-top:3px solid var(--ocean-seafoam); border-radius:8px; padding:1em;">
            <div style="color:var(--ocean-seafoam); font-weight:700; font-size:0.85em;">Part 3 · ~15 min</div>
            <div style="font-weight:700; margin:0.3em 0;">Inference-Time Scaling</div>
            <div class="dim" style="font-size:0.8em;">CoT · Self-Consistency · Tree of Thoughts · MCTS · Scaling Laws</div>
          </div>
        </div>
        <aside class="notes">
          总览三部分。强调这是一条从"理解推理"到"加速推理"再到"用更多推理换更好结果"的逻辑链。
        </aside>
      </section>

      <!-- ═══════════════════════════════════════════════════════════
           Part 1: 推理基础
           ═══════════════════════════════════════════════════════════ -->
      <section data-part="1" class="section-slide">
        <div class="section-number">01</div>
        <h2>推理基础</h2>
        <div class="dim">从 Transformer 到自回归生成</div>
        <aside class="notes">
          Part 1 开始。主讲人 A 接力。
        </aside>
      </section>

{part1}

      <!-- ═══════════════════════════════════════════════════════════
           Part 2: 推理加速技术
           ═══════════════════════════════════════════════════════════ -->
      <section data-part="2" class="section-slide">
        <div class="section-number">02</div>
        <h2>推理加速技术</h2>
        <div class="dim">从瓶颈分析到系统优化</div>
        <aside class="notes">
          Part 1 结束，过渡到 Part 2。主讲人 B 接力。
          过渡语：了解了推理流程和瓶颈，接下来看如何加速这个过程。
        </aside>
      </section>

{part2}

      <!-- ═══════════════════════════════════════════════════════════
           Part 3: Inference-Time Scaling
           ═══════════════════════════════════════════════════════════ -->
      <section data-part="3" class="section-slide">
        <div class="section-number">03</div>
        <h2>Inference-Time Scaling</h2>
        <div class="dim">用更多推理计算换更好结果</div>
        <aside class="notes">
          Part 2 结束，过渡到 Part 3。主讲人 C 接力。
          过渡语：单次推理变快后，能否用更多推理计算提升效果？
        </aside>
      </section>

{part3}

    </div> <!-- .slides -->
  </div> <!-- .reveal -->

  <!-- Reveal.js Core JS -->
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.js"></script>

  <!-- Reveal.js Plugins -->
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/math/math.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/highlight.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/notes/notes.js"></script>

  <!-- KaTeX -->
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

  <script>
    // Mark reveal.js receiver iframes (used by speaker notes previews)
    // so responsive rules can avoid mobile-style restacking there.
    if (/(?:^|[?&])receiver(?:[=&]|$)/i.test(window.location.search)) {{
      document.documentElement.classList.add('receiver-mode');
    }}

    Reveal.initialize({{
      width: 1280,
      height: 720,
      margin: 0.06,
      minScale: 0.2,
      maxScale: 2.0,
      transition: 'fade',
      transitionSpeed: 'default',
      backgroundTransition: 'fade',
      hash: true,
      history: true,
      center: true,
      controls: true,
      progress: true,
      slideNumber: 'c/t',
      plugins: [
        RevealMath.KaTeX,
        RevealHighlight,
        RevealNotes
      ],
      math: {{
        katexScript: 'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js',
        config: 'default'
      }},
      keyboard: true
    }});

    // === KaTeX rendering in speaker notes popup ===
    // Keep this strictly scoped to notes math rendering.
    // Do NOT inject deck/theme CSS into the speaker popup or its iframes:
    // reveal-notes already loads slide previews from the same URL, and extra
    // global CSS injection can break popup layout and preview alignment.
    (function() {{
      var KATEX_BASE = 'https://cdn.jsdelivr.net/npm/katex@0.16.9';
      var NOTES_SELECTOR = '.speaker-controls-notes .value';
      var _injected = false;

      var KATEX_CONFIG = {{
        delimiters: [
          {{left: '$$', right: '$$', display: true}},
          {{left: '$', right: '$', display: false}},
          {{left: '\\\\(', right: '\\\\)', display: false}},
          {{left: '\\\\[', right: '\\\\]', display: true}}
        ],
        throwOnError: false
      }};

      function renderNotes(doc) {{
        var el = doc.querySelector(NOTES_SELECTOR);
        if (!el || el.querySelector('.katex')) return;
        var win = doc.defaultView;
        if (!win || !win.renderMathInElement) return;
        win.renderMathInElement(el, KATEX_CONFIG);
      }}

      function setupObserver(doc) {{
        var el = doc.querySelector(NOTES_SELECTOR);
        if (!el) return;
        renderNotes(doc);
        try {{
          var observer = new doc.defaultView.MutationObserver(function() {{
            setTimeout(function() {{ renderNotes(doc); }}, 50);
          }});
          observer.observe(el, {{ childList: true, subtree: true, characterData: true }});
        }} catch(e) {{}}
      }}

      function injectKatex(popup) {{
        if (_injected || !popup || popup.closed) return;
        var doc;
        try {{
          doc = popup.document;
        }} catch(e) {{
          return;
        }}
        if (!doc || !doc.head) return;

        _injected = true;

        // KaTeX CSS (needed for already-rendered KaTeX HTML from main document)
        if (!doc.querySelector('link[data-katex-notes="1"]')) {{
          var link = doc.createElement('link');
          link.rel = 'stylesheet';
          link.href = KATEX_BASE + '/dist/katex.min.css';
          link.setAttribute('data-katex-notes', '1');
          doc.head.appendChild(link);
        }}

        // If scripts are already available in the popup, just observe and render.
        var win = doc.defaultView;
        if (win && win.katex && win.renderMathInElement) {{
          setupObserver(doc);
          return;
        }}

        // KaTeX JS + auto-render (fallback for unrendered notes)
        var s1 = doc.createElement('script');
        s1.src = KATEX_BASE + '/dist/katex.min.js';
        s1.onload = function() {{
          var s2 = doc.createElement('script');
          s2.src = KATEX_BASE + '/dist/contrib/auto-render.min.js';
          s2.onload = function() {{ setupObserver(doc); }};
          doc.head.appendChild(s2);
        }};
        doc.head.appendChild(s1);
      }}

      // Detect popup via postMessage — no window.open monkey-patch needed.
      // The popup sends 'connected' when it's ready, and 'state' on slide changes.
      // event.source gives us the popup window reference.
      window.addEventListener('message', function(event) {{
        try {{
          var data = JSON.parse(event.data);
          if (data && data.namespace === 'reveal-notes') {{
            if (data.type === 'connected' || data.type === 'state') {{
              injectKatex(event.source);
            }}
          }}
        }} catch(e) {{}}
      }});
    }})();
  </script>

</body>
</html>'''

output = os.path.join(BASE, 'index.html')
with open(output, 'w', encoding='utf-8') as f:
    f.write(html)

# Stats
section_count = html.count('<section')
print(f'✓ Built index.html ({len(html)//1024} KB, ~{section_count} slides)')
print(f'  Sources: slides/shared-style.css + part1/2/3 HTML')
print(f'  Output:  index.html (single file, works with file://)')
