# LangChain4j 教程中文翻译

[![Source](https://img.shields.io/badge/source-docs.langchain4j.dev-blue)](https://docs.langchain4j.dev/category/tutorials)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Last Sync](https://img.shields.io/badge/last_sync-2026--10--10-orange)]()

将 [LangChain4j 官方文档](https://docs.langchain4j.dev/) 中 **Tutorials** 分类下的全部 **32 篇教程** 翻译为简体中文，并提供本地预览站点。

---

## 📚 项目简介

LangChain4j 是 Java 生态主流的大语言模型（LLM）集成框架。本项目是对其官方文档 Tutorials 板块的完整中文翻译，方便中文开发者：

- 🚀 **快速入门**：从 LLM 基础调用到 Spring Boot 全栈集成
- 🛠️ **常用能力**：对话记忆、工具调用、RAG、结构化输出、护栏
- 🔌 **框架集成**：Spring Boot / Quarkus / Micronaut / Helidon / Payara Micro
- 📊 **生产化**：日志、可观测性、测试与评估
- 🧪 **实验特性**：智能体、MCP、技能、模型路由、决策模型

---

## 📁 目录结构

```
.
├── langchain4j-tutorials-zh/           翻译源文件（Markdown/纯文本）
│   ├── 00-index-zh.md                  中文总览与学习路线
│   ├── <slug>.txt                      各教程英文原文（爬取自官网）
│   └── <slug>-zh.txt                   各教程中文译文
├── site/                               静态预览站点（直接浏览器打开）
│   ├── index.html                      首页
│   └── <slug>.html                     各教程页面（含侧边栏、搜索、代码高亮）
├── build_site.py                       站点生成脚本
├── README.md                           本文件
└── LICENSE                             许可证
```

---

## 🚀 快速使用

### 方式一：浏览器直接打开（推荐）

不需要任何 HTTP 服务，直接在浏览器打开首页：

```
file:///D:/work-ai/0401-lumen-langchain4j-API/site/index.html
```

或 Windows 资源管理器中双击 `site/index.html`。

### 方式二：本地启动 HTTP 服务

如果更喜欢 HTTP 访问：

```bash
cd site
python -m http.server 12321 --bind 127.0.0.1
```

然后浏览器访问：<http://127.0.0.1:12321/>

### 方式三：重新生成站点

源文件更新后，重新构建：

```bash
python build_site.py
```

依赖：仅 Python 3.8+ 标准库（无第三方依赖）。

---

## 🗂️ 教程目录

### 一、基础与核心 API（12 篇）

| 原文链接 | 中文标题 |
|---|---|
| [Chat and Language Models](https://docs.langchain4j.dev/tutorials/chat-and-language-models) | 对话与语言模型 |
| [Chat Memory](https://docs.langchain4j.dev/tutorials/chat-memory) | 对话记忆 |
| [Model Parameters](https://docs.langchain4j.dev/tutorials/model-parameters) | 模型参数 |
| [Response Streaming](https://docs.langchain4j.dev/tutorials/response-streaming) | 响应流式输出 |
| [AI Services](https://docs.langchain4j.dev/tutorials/ai-services) | AI Services |
| [Agents and Agentic AI](https://docs.langchain4j.dev/tutorials/agents) | 智能体与智能体 AI |
| [Tools (Function Calling)](https://docs.langchain4j.dev/tutorials/tools) | 工具（函数调用） |
| [RAG](https://docs.langchain4j.dev/tutorials/rag) | 检索增强生成 |
| [Structured Outputs](https://docs.langchain4j.dev/tutorials/structured-outputs) | 结构化输出 |
| [Guardrails](https://docs.langchain4j.dev/tutorials/guardrails) | 护栏 |
| [Classification](https://docs.langchain4j.dev/tutorials/classification) | 分类 |
| [Embedding (Vector) Stores](https://docs.langchain4j.dev/tutorials/embedding-stores) | 向量存储 |

### 二、协议与扩展（3 篇）

| 原文链接 | 中文标题 |
|---|---|
| [Building a Java MCP server](https://docs.langchain4j.dev/tutorials/mcp-stdio-server) | 构建 Java MCP 服务端 |
| [Model Context Protocol (MCP)](https://docs.langchain4j.dev/tutorials/mcp) | 模型上下文协议（MCP） |
| [Image Models](https://docs.langchain4j.dev/tutorials/image-models) | 图像模型 |

### 三、框架集成（5 篇）

| 原文链接 | 中文标题 |
|---|---|
| [Spring Boot Integration](https://docs.langchain4j.dev/tutorials/spring-boot-integration) | Spring Boot 集成 |
| [Quarkus Integration](https://docs.langchain4j.dev/tutorials/quarkus-integration) | Quarkus 集成 |
| [Micronaut Integration](https://docs.langchain4j.dev/tutorials/micronaut-integration) | Micronaut 集成 |
| [Helidon Integration](https://docs.langchain4j.dev/tutorials/helidon-integration) | Helidon 集成 |
| [Payara Micro Integration](https://docs.langchain4j.dev/tutorials/payara-micro-integration) | Payara Micro 集成 |

### 四、语言与工具链（8 篇）

| 原文链接 | 中文标题 |
|---|---|
| [Kotlin Support](https://docs.langchain4j.dev/tutorials/kotlin) | Kotlin 支持 |
| [Logging](https://docs.langchain4j.dev/tutorials/logging) | 日志 |
| [JSON Codec](https://docs.langchain4j.dev/tutorials/json) | JSON 编码器 |
| [Using Jackson 3](https://docs.langchain4j.dev/tutorials/jackson-3) | 使用 Jackson 3 |
| [Observability](https://docs.langchain4j.dev/tutorials/observability) | 可观测性 |
| [Skills](https://docs.langchain4j.dev/tutorials/skills) | 技能（Skills） |
| [Customizable HTTP Client](https://docs.langchain4j.dev/tutorials/customizable-http-client) | 可定制 HTTP 客户端 |
| [Testing and Evaluation](https://docs.langchain4j.dev/tutorials/testing-and-evaluation) | 测试与评估 |

### 五、实验性与高级特性（4 篇）

| 原文链接 | 中文标题 |
|---|---|
| [Non-blocking and Reactive](https://docs.langchain4j.dev/tutorials/non-blocking) | 非阻塞与响应式 |
| [Decision Services](https://docs.langchain4j.dev/tutorials/decision-services) | 决策服务 |
| [Decision Models](https://docs.langchain4j.dev/tutorials/decision-models) | 决策模型 |
| [Model Routing](https://docs.langchain4j.dev/tutorials/model-routing) | 模型路由 |

---

## 🛣️ 学习路线建议

1. **入门**：先读「对话与语言模型」与「AI Services」，理解 LangChain4j 的两层抽象。
2. **常用能力**：再学「对话记忆」、「工具」、「RAG」、「结构化输出」，覆盖对话系统主要功能。
3. **框架集成**：根据项目框架选择「Spring Boot / Quarkus / Micronaut / Helidon / Payara Micro」集成。
4. **生产化**：阅读「日志」、「可观测性」、「测试与评估」，关注可观测性与可测试性。
5. **进阶探索**：根据需要了解「智能体」、「护栏」、「MCP」、「技能」、「模型路由」等实验性模块。

---

## 📝 翻译约定

- ✅ **代码块完整保留**（Java/JSON/YAML/Maven/SQL 等所有代码原样）
- ✅ **代码注释翻译**（如 `// Load a single document` → `// 加载单个文档`）
- ✅ **Java 类名/包名/方法名/注解保留英文**（如 `@AiService`、`@Tool`、`ChatModel`）
- ✅ **规范术语**（大语言模型 LLM、提示词 prompt、向量存储 embedding store、检索增强生成 RAG 等）
- ✅ **结构保留**（标题层级、列表、表格、代码块、注释块）

---

## 🔄 同步与更新

源文档可能持续更新。如需同步最新版：

```bash
# 1. 爬取最新页面（参考 build_site.py 的爬取流程）
# 2. 调用翻译脚本生成 -zh.txt 文件
# 3. 重新运行 python build_site.py 重建站点
```

爬取/翻译流程封装在 `build_site.py`，可参考其目录结构自行扩展。

---

## 📜 许可证与版权声明

本项目为**翻译衍生作品**，内容来源：

- **原文版权**：© LangChain4j 项目贡献者，遵循 [LangChain4j 仓库](https://github.com/langchain4j/langchain4j) 的开源协议
- **译文版权**：本翻译作品以 MIT 协议发布
- **使用规范**：
  - ✅ 允许学习、参考、转发
  - ✅ 允许在此基础上二次翻译与校对
  - ⚠️ 请保留对原文及 LangChain4j 项目署名的引用
  - ❌ 请勿声称为官方翻译或用于商业转售

详见 [LICENSE](LICENSE) 文件。

---

## 🙏 致谢

- [LangChain4j](https://github.com/langchain4j/langchain4j) —— Java 生态的优秀 LLM 框架
- 所有为 LangChain4j 文档做出贡献的贡献者
- 本翻译项目仅供学习参考，**最终以英文官方文档为准**

---

## 📮 反馈

欢迎通过 [Issues](../../issues) 提交：

- 🐛 翻译错误或不准确
- 💡 术语建议
- 📚 内容补充
- 🔄 同步请求

---

<p align="center">
  Made with ❤️ for the Chinese LangChain4j community
</p>