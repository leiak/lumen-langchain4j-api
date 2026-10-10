"""Build static HTML pages for translated LangChain4j tutorials."""
import os
import re
import html
from pathlib import Path

SRC_DIR = Path("D:/work-ai/0401-lumen-langchain4j-API/langchain4j-tutorials-zh")
OUT_DIR = Path("D:/work-ai/0401-lumen-langchain4j-API/site")

# Order & metadata of tutorials (from the official index page)
TUTORIALS = [
    ("chat-and-language-models", "对话与语言模型", "Chat and Language Models", "基础与核心 API"),
    ("chat-memory", "对话记忆", "Chat Memory", "基础与核心 API"),
    ("model-parameters", "模型参数", "Model Parameters", "基础与核心 API"),
    ("response-streaming", "响应流式输出", "Response Streaming", "基础与核心 API"),
    ("ai-services", "AI Services", "AI Services", "基础与核心 API"),
    ("agents", "智能体与智能体 AI", "Agents and Agentic AI", "基础与核心 API"),
    ("tools", "工具（函数调用）", "Tools (Function Calling)", "基础与核心 API"),
    ("rag", "检索增强生成（RAG）", "RAG (Retrieval-Augmented Generation)", "基础与核心 API"),
    ("structured-outputs", "结构化输出", "Structured Outputs", "基础与核心 API"),
    ("guardrails", "护栏", "Guardrails", "基础与核心 API"),
    ("classification", "分类", "Classification", "基础与核心 API"),
    ("embedding-stores", "向量存储", "Embedding (Vector) Stores", "基础与核心 API"),
    ("mcp-stdio-server", "构建 Java MCP 服务端", "Building a Java MCP server", "协议与扩展"),
    ("mcp", "模型上下文协议（MCP）", "Model Context Protocol (MCP)", "协议与扩展"),
    ("image-models", "图像模型", "Image Models", "协议与扩展"),
    ("spring-boot-integration", "Spring Boot 集成", "Spring Boot Integration", "框架集成"),
    ("quarkus-integration", "Quarkus 集成", "Quarkus Integration", "框架集成"),
    ("micronaut-integration", "Micronaut 集成", "Micronaut Integration", "框架集成"),
    ("helidon-integration", "Helidon 集成", "Helidon Integration", "框架集成"),
    ("payara-micro-integration", "Payara Micro 集成", "Payara Micro Integration", "框架集成"),
    ("kotlin", "Kotlin 支持", "Kotlin Support", "语言与工具链"),
    ("logging", "日志", "Logging", "语言与工具链"),
    ("json", "JSON 编码器", "JSON Codec", "语言与工具链"),
    ("jackson-3", "使用 Jackson 3", "Using Jackson 3", "语言与工具链"),
    ("observability", "可观测性", "Observability", "语言与工具链"),
    ("skills", "技能（Skills）", "Skills", "语言与工具链"),
    ("customizable-http-client", "可定制 HTTP 客户端", "Customizable HTTP Client", "语言与工具链"),
    ("testing-and-evaluation", "测试与评估", "Testing and Evaluation", "语言与工具链"),
    ("non-blocking", "非阻塞与响应式", "Non-blocking and Reactive", "实验性与高级特性"),
    ("decision-services", "决策服务", "Decision Services", "实验性与高级特性"),
    ("decision-models", "决策模型", "Decision Models", "实验性与高级特性"),
    ("model-routing", "模型路由", "Model Routing", "实验性与高级特性"),
]

CSS = """
* { box-sizing: border-box; }
body {
  margin: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC',
    'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
  background: #f8fafc; color: #1e293b; line-height: 1.65;
}
.layout { display: flex; min-height: 100vh; }
aside {
  width: 280px; background: #0f172a; color: #cbd5e1;
  padding: 24px 16px; overflow-y: auto;
  position: sticky; top: 0; height: 100vh;
}
aside h2 {
  font-size: 14px; color: #94a3b8; text-transform: uppercase;
  letter-spacing: 0.05em; margin: 24px 0 8px;
}
aside h2:first-child { margin-top: 0; }
aside a {
  display: block; color: #cbd5e1; text-decoration: none;
  padding: 6px 12px; border-radius: 6px; font-size: 13px;
  transition: background 0.15s;
}
aside a:hover, aside a.active { background: #1e293b; color: #fff; }
main {
  flex: 1; padding: 32px 48px; max-width: 1000px; margin: 0 auto;
  background: white; min-height: 100vh;
}
nav.breadcrumb {
  font-size: 13px; color: #64748b; margin-bottom: 16px;
}
nav.breadcrumb a { color: #2563eb; text-decoration: none; }
h1 {
  font-size: 28px; color: #0f172a; border-bottom: 2px solid #e2e8f0;
  padding-bottom: 12px; margin-top: 0;
}
h2 {
  font-size: 22px; color: #1e293b; margin-top: 32px;
  border-left: 4px solid #3b82f6; padding-left: 12px;
}
h3 {
  font-size: 18px; color: #334155; margin-top: 24px;
}
h4 { font-size: 16px; color: #475569; margin-top: 20px; }
p { margin: 12px 0; }
ul, ol { padding-left: 28px; }
li { margin: 4px 0; }
code {
  font-family: 'SF Mono', Consolas, 'Courier New', monospace;
  background: #f1f5f9; padding: 2px 6px; border-radius: 4px;
  font-size: 0.9em; color: #be185d;
}
pre {
  background: #0f172a; color: #e2e8f0; padding: 16px;
  border-radius: 8px; overflow-x: auto; line-height: 1.5;
  font-family: 'SF Mono', Consolas, monospace; font-size: 13px;
}
pre code { background: transparent; color: inherit; padding: 0; }
blockquote {
  border-left: 4px solid #94a3b8; padding: 8px 16px;
  color: #475569; background: #f8fafc; margin: 16px 0;
}
table {
  border-collapse: collapse; width: 100%; margin: 16px 0;
  font-size: 14px;
}
th, td {
  border: 1px solid #cbd5e1; padding: 8px 12px; text-align: left;
}
th { background: #f1f5f9; font-weight: 600; }
tr:nth-child(even) { background: #f8fafc; }
hr { border: 0; border-top: 1px solid #e2e8f0; margin: 32px 0; }
.search-box {
  width: 100%; padding: 8px 12px; border-radius: 6px;
  border: 1px solid #334155; background: #1e293b; color: white;
  font-size: 13px; margin-bottom: 16px;
}
.search-box::placeholder { color: #64748b; }
.meta-card {
  background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
  color: white; padding: 32px; border-radius: 12px;
  margin-bottom: 24px;
}
.meta-card h1 { color: white; border: 0; margin: 0 0 8px; }
.meta-card p { margin: 0; opacity: 0.9; }
.lesson-card {
  display: block; padding: 16px 20px; border: 1px solid #e2e8f0;
  border-radius: 8px; margin: 8px 0; text-decoration: none;
  color: #1e293b; transition: all 0.15s;
}
.lesson-card:hover {
  border-color: #3b82f6; box-shadow: 0 4px 12px rgba(59,130,246,0.1);
  transform: translateY(-1px);
}
.lesson-card .title { font-weight: 600; font-size: 16px; }
.lesson-card .en { color: #64748b; font-size: 13px; margin-top: 4px; }
.lesson-card .cat {
  display: inline-block; background: #eff6ff; color: #2563eb;
  padding: 2px 8px; border-radius: 4px; font-size: 12px;
  margin-top: 8px;
}
.tag-experimental {
  background: #fef3c7; color: #92400e; padding: 2px 8px;
  border-radius: 4px; font-size: 12px; margin-left: 8px;
}
.prev-next {
  display: flex; justify-content: space-between;
  margin-top: 48px; padding-top: 24px;
  border-top: 1px solid #e2e8f0; gap: 16px;
}
.prev-next a {
  padding: 12px 20px; border: 1px solid #e2e8f0;
  border-radius: 8px; text-decoration: none; color: #2563eb;
  flex: 1; max-width: 45%;
}
.prev-next a:hover { background: #eff6ff; border-color: #3b82f6; }
.prev-next .label { font-size: 12px; color: #64748b; }
"""

def md_to_html(text):
    """Lightweight Markdown -> HTML converter that handles headings, code, lists, paragraphs."""
    lines = text.split('\n')
    out = []
    i = 0
    in_code = False
    code_buf = []
    code_lang = ''

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Code block fence
        if stripped.startswith('```'):
            if not in_code:
                in_code = True
                code_lang = stripped[3:].strip()
                code_buf = []
            else:
                in_code = False
                lang_class = f' class="language-{code_lang}"' if code_lang else ''
                code_text = '\n'.join(code_buf)
                out.append(f'<pre><code{lang_class}>{html.escape(code_text)}</code></pre>')
                code_buf = []
                code_lang = ''
            i += 1
            continue

        if in_code:
            code_buf.append(line)
            i += 1
            continue

        # Blank line
        if not stripped:
            out.append('')
            i += 1
            continue

        # Headings
        m = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if m:
            level = len(m.group(1))
            content = m.group(2).strip()
            out.append(f'<h{level}>{inline_md(content)}</h{level}>')
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^-{3,}$|^\*{3,}$', stripped):
            out.append('<hr>')
            i += 1
            continue

        # Lists
        if re.match(r'^[-*]\s+', stripped):
            list_buf = []
            while i < len(lines):
                l = lines[i].strip()
                if re.match(r'^[-*]\s+', l):
                    item = re.sub(r'^[-*]\s+', '', l)
                    list_buf.append(inline_md(item))
                    i += 1
                elif not l:
                    break
                else:
                    # continuation
                    list_buf[-1] += ' ' + inline_md(l)
                    i += 1
            out.append('<ul>' + ''.join(f'<li>{x}</li>' for x in list_buf) + '</ul>')
            continue

        if re.match(r'^\d+\.\s+', stripped):
            list_buf = []
            while i < len(lines):
                l = lines[i].strip()
                if re.match(r'^\d+\.\s+', l):
                    item = re.sub(r'^\d+\.\s+', '', l)
                    list_buf.append(inline_md(item))
                    i += 1
                elif not l:
                    break
                else:
                    list_buf[-1] += ' ' + inline_md(l)
                    i += 1
            out.append('<ol>' + ''.join(f'<li>{x}</li>' for x in list_buf) + '</ol>')
            continue

        # Tables (very basic)
        if '|' in stripped and i + 1 < len(lines) and re.match(r'^\|?[\s\-:|]+\|?$', lines[i+1].strip()):
            tbl = []
            while i < len(lines):
                l = lines[i].strip()
                if '|' not in l:
                    break
                if re.match(r'^\|?[\s\-:|]+\|?$', l):
                    i += 1
                    continue
                cells = [c.strip() for c in l.strip('|').split('|')]
                tbl.append(cells)
                i += 1
            if tbl:
                rows = []
                rows.append('<thead><tr>' + ''.join(f'<th>{inline_md(c)}</th>' for c in tbl[0]) + '</tr></thead>')
                body_rows = ''.join('<tr>' + ''.join(f'<td>{inline_md(c)}</td>' for c in r) + '</tr>' for r in tbl[1:])
                rows.append(f'<tbody>{body_rows}</tbody>')
                out.append('<table>' + ''.join(rows) + '</table>')
            continue

        # Paragraph (collect consecutive non-empty non-special lines)
        para_buf = []
        while i < len(lines):
            l = lines[i].strip()
            if not l or re.match(r'^(#{1,6}\s|[-*]\s|```|---+|\d+\.\s)', l) or ('|' in l and i+1 < len(lines) and re.match(r'^\|?[\s\-:|]+\|?$', lines[i+1].strip())):
                break
            para_buf.append(l)
            i += 1
        if para_buf:
            out.append(f'<p>{inline_md(" ".join(para_buf))}</p>')

    return '\n'.join(out)


def inline_md(text):
    """Apply inline markdown: **bold**, *italic*, `code`, [link](url)."""
    text = html.escape(text)
    # code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # bold
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    # italic
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    # link
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    return text


def base_html(title, body, active_slug=None):
    """Wrap content in the site chrome."""
    sidebar_groups = {}
    for slug, zh, en, cat in TUTORIALS:
        sidebar_groups.setdefault(cat, []).append((slug, zh))

    sidebar = ['<h2>🏠 首页</h2>', '<a href="index.html">教程总览</a>']
    for cat, items in sidebar_groups.items():
        sidebar.append(f'<h2>{html.escape(cat)}</h2>')
        for slug, zh in items:
            cls = ' class="active"' if slug == active_slug else ''
            sidebar.append(f'<a href="{slug}.html"{cls}>{html.escape(zh)}</a>')

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | LangChain4j 教程（中文）</title>
<style>{CSS}</style>
</head>
<body>
<div class="layout">
<aside>
<input class="search-box" type="text" placeholder="🔍 搜索..." oninput="
  const q = this.value.toLowerCase();
  this.parentElement.querySelectorAll('a').forEach(a => {{
    a.style.display = (!q || a.textContent.toLowerCase().includes(q)) ? '' : 'none';
  }});
">
{''.join(sidebar)}
</aside>
<main>
{body}
</main>
</div>
</body>
</html>"""


def build_index():
    """Build the index page."""
    body_parts = ['''<div class="meta-card">
<h1>LangChain4j 教程（中文）</h1>
<p>官方文档 32 篇核心教程的中文翻译 · 爬取自 docs.langchain4j.dev</p>
</div>

<p>欢迎使用 LangChain4j 中文教程。本站点收录了官方文档 Tutorials 分类下的全部 32 篇文章，按官方推荐的学习顺序整理，方便中文开发者快速查阅。</p>

<h2>学习路线</h2>
<ul>
<li><strong>入门</strong>：先读「对话与语言模型」与「AI Services」，理解 LangChain4j 的两层抽象。</li>
<li><strong>常用能力</strong>：再学「对话记忆」、「工具」、「RAG」、「结构化输出」，覆盖对话系统主要功能。</li>
<li><strong>框架集成</strong>：根据项目框架选择「Spring Boot / Quarkus / Micronaut / Helidon / Payara Micro」集成。</li>
<li><strong>生产化</strong>：阅读「日志」、「可观测性」、「测试与评估」，关注可观测性与可测试性。</li>
<li><strong>进阶探索</strong>：根据需要了解「智能体」、「护栏」、「MCP」、「技能」、「模型路由」等实验性模块。</li>
</ul>

<h2>教程目录</h2>''']

    # Group tutorials by category
    groups = {}
    for slug, zh, en, cat in TUTORIALS:
        groups.setdefault(cat, []).append((slug, zh, en))

    for cat, items in groups.items():
        body_parts.append(f'<h2>{html.escape(cat)}</h2>')
        for slug, zh, en in items:
            body_parts.append(f'<a class="lesson-card" href="{slug}.html">')
            body_parts.append(f'  <div class="title">{html.escape(zh)}</div>')
            body_parts.append(f'  <div class="en">{html.escape(en)}</div>')
            body_parts.append(f'</a>')

    body_parts.append('<hr>')
    body_parts.append('<p><em>📚 翻译日期：2026-10-10 · 来源：<a href="https://docs.langchain4j.dev/category/tutorials">docs.langchain4j.dev/category/tutorials</a></em></p>')

    return base_html("教程总览", '\n'.join(body_parts))


def build_tutorial(slug, zh_title):
    """Build a single tutorial page."""
    src = SRC_DIR / f'{slug}-zh.txt'
    if not src.exists():
        print(f"  Missing: {src}")
        return None

    text = src.read_text(encoding='utf-8')
    body = md_to_html(text)

    # Find prev/next
    idx = next((i for i, t in enumerate(TUTORIALS) if t[0] == slug), None)
    prev_link = ''
    next_link = ''
    if idx is not None:
        if idx > 0:
            p_slug, p_zh, _, _ = TUTORIALS[idx-1]
            prev_link = f'<a href="{p_slug}.html"><div class="label">← 上一篇</div><div>{html.escape(p_zh)}</div></a>'
        else:
            prev_link = '<a href="index.html"><div class="label">← 返回</div><div>教程总览</div></a>'
        if idx < len(TUTORIALS) - 1:
            n_slug, n_zh, _, _ = TUTORIALS[idx+1]
            next_link = f'<a href="{n_slug}.html"><div class="label">下一篇 →</div><div>{html.escape(n_zh)}</div></a>'
        else:
            next_link = '<a href="index.html"><div class="label">→ 返回</div><div>教程总览</div></a>'

    content = f'''<nav class="breadcrumb"><a href="index.html">首页</a> / {html.escape(zh_title)}</nav>
<h1>{html.escape(zh_title)}</h1>
{body}
<div class="prev-next">
  {prev_link}
  {next_link}
</div>'''

    return base_html(zh_title, content, active_slug=slug)


# Main
OUT_DIR.mkdir(parents=True, exist_ok=True)

print("Building index...")
(OUT_DIR / 'index.html').write_text(build_index(), encoding='utf-8')

print("Building tutorial pages...")
for slug, zh, en, cat in TUTORIALS:
    html_content = build_tutorial(slug, zh)
    if html_content:
        (OUT_DIR / f'{slug}.html').write_text(html_content, encoding='utf-8')
        size = (OUT_DIR / f'{slug}.html').stat().st_size
        print(f"  OK {slug}.html ({size} bytes)")

print(f"\nSite built at: {OUT_DIR}")
print(f"  Total files: {len(list(OUT_DIR.glob('*.html')))}")