# LangChain4j 教程（中文翻译）

> 来源：https://docs.langchain4j.dev/category/tutorials
> 爬取日期：2026-10-10

LangChain4j 官方文档中的教程目录收录了 32 篇核心教程，按主题划分覆盖了从基础 LLM 接入到企业级集成的完整能力。本目录为中文翻译版本，方便中文开发者快速查阅。

## 教程目录（按官方推荐顺序）

### 基础与核心 API

| # | 中文标题 | 英文原标题 | 原文链接 | 简介 |
|---|---|---|---|---|
| 1 | 对话与语言模型 | Chat and Language Models | [/tutorials/chat-and-language-models](https://docs.langchain4j.dev/tutorials/chat-and-language-models) | 介绍低级别 LLM API。 |
| 2 | 对话记忆 | Chat Memory | [/tutorials/chat-memory](https://docs.langchain4j.dev/tutorials/chat-memory) | 介绍 ChatMessage 的管理与维护机制。 |
| 3 | 模型参数 | Model Parameters | [/tutorials/model-parameters](https://docs.langchain4j.dev/tutorials/model-parameters) | 介绍 temperature、top-p 等可调参数。 |
| 4 | 响应流式输出 | Response Streaming | [/tutorials/response-streaming](https://docs.langchain4j.dev/tutorials/response-streaming) | 介绍低级别 API 的响应流式输出。 |
| 5 | AI Services | AI Services | [/tutorials/ai-services](https://docs.langchain4j.dev/tutorials/ai-services) | 高级 API，基于声明式接口简化 LLM 调用。 |
| 6 | 智能体与智能体 AI | Agents and Agentic AI | [/tutorials/agents](https://docs.langchain4j.dev/tutorials/agents) | 介绍 langchain4j-agentic 模块（实验性）。 |
| 7 | 工具（函数调用） | Tools (Function Calling) | [/tutorials/tools](https://docs.langchain4j.dev/tutorials/tools) | 让 LLM 触发外部动作。 |
| 8 | 检索增强生成（RAG） | RAG (Retrieval-Augmented Generation) | [/tutorials/rag](https://docs.langchain4j.dev/tutorials/rag) | 用外部知识扩展 LLM 知识范围。 |
| 9 | 结构化输出 | Structured Outputs | [/tutorials/structured-outputs](https://docs.langchain4j.dev/tutorials/structured-outputs) | 让 LLM 输出符合 JSON Schema 的结果。 |
| 10 | 护栏 | Guardrails | [/tutorials/guardrails](https://docs.langchain4j.dev/tutorials/guardrails) | 实验性功能，对输入/输出进行校验。 |
| 11 | 分类 | Classification | [/tutorials/classification](https://docs.langchain4j.dev/tutorials/classification) | 用 LLM 做文本分类。 |
| 12 | 向量存储 | Embedding (Vector) Stores | [/tutorials/embedding-stores](https://docs.langchain4j.dev/tutorials/embedding-stores) | 支持同步与异步搜索的向量数据库抽象。 |

### 协议与扩展

| # | 中文标题 | 英文原标题 | 原文链接 | 简介 |
|---|---|---|---|---|
| 13 | 构建 Java MCP 服务端 | Building a Java MCP server | [/tutorials/mcp-stdio-server](https://docs.langchain4j.dev/tutorials/mcp-stdio-server) | 介绍 langchain4j-mcp 客户端与 Java MCP 服务端构建。 |
| 14 | 模型上下文协议（MCP） | Model Context Protocol (MCP) | [/tutorials/mcp](https://docs.langchain4j.dev/tutorials/mcp) | 通过 executeToolAsync(...) 异步执行 MCP 工具。 |
| 15 | 图像模型 | Image Models | [/tutorials/image-models](https://docs.langchain4j.dev/tutorials/image-models) | 文生图模型接入（文档待完善）。 |

### 框架集成

| # | 中文标题 | 英文原标题 | 原文链接 | 简介 |
|---|---|---|---|---|
| 16 | Spring Boot 集成 | Spring Boot Integration | [/tutorials/spring-boot-integration](https://docs.langchain4j.dev/tutorials/spring-boot-integration) | 提供 Spring Boot Starter，简化依赖注入与配置。 |
| 17 | Quarkus 集成 | Quarkus Integration | [/tutorials/quarkus-integration](https://docs.langchain4j.dev/tutorials/quarkus-integration) | Quarkus 提供的官方扩展模块。 |
| 18 | Micronaut 集成 | Micronaut Integration | [/tutorials/micronaut-integration](https://docs.langchain4j.dev/tutorials/micronaut-integration) | Micronaut 官方模块。 |
| 19 | Helidon 集成 | Helidon Integration | [/tutorials/helidon-integration](https://docs.langchain4j.dev/tutorials/helidon-integration) | 结合 Helidon 编程模型的集成模块。 |
| 20 | Payara Micro 集成 | Payara Micro Integration | [/tutorials/payara-micro-integration](https://docs.langchain4j.dev/tutorials/payara-micro-integration) | 基于 Jakarta EE 与 MicroProfile 的依赖注入与配置。 |

### 语言与工具链

| # | 中文标题 | 英文原标题 | 原文链接 | 简介 |
|---|---|---|---|---|
| 21 | Kotlin 支持 | Kotlin Support | [/tutorials/kotlin](https://docs.langchain4j.dev/tutorials/kotlin) | Kotlin 用户的兼容性与破坏性变更说明。 |
| 22 | 日志 | Logging | [/tutorials/logging](https://docs.langchain4j.dev/tutorials/logging) | 基于 SLF4J 的日志配置。 |
| 23 | JSON 编码器 | JSON Codec | [/tutorials/json](https://docs.langchain4j.dev/tutorials/json) | 内部 JSON 序列化器（默认 Jackson）。 |
| 24 | 使用 Jackson 3 | Using Jackson 3 | [/tutorials/jackson-3](https://docs.langchain4j.dev/tutorials/jackson-3) | 升级到 Jackson 3 的迁移指南。 |
| 25 | 可观测性 | Observability | [/tutorials/observability](https://docs.langchain4j.dev/tutorials/observability) | AI Service 的可观测性接入。 |
| 26 | 技能（Skills） | Skills | [/tutorials/skills](https://docs.langchain4j.dev/tutorials/skills) | 实验性 API，封装可复用工具。 |
| 27 | 可定制 HTTP 客户端 | Customizable HTTP Client | [/tutorials/customizable-http-client](https://docs.langchain4j.dev/tutorials/customizable-http-client) | 自定义 OpenAI/Ollama 模块的 HTTP 客户端。 |
| 28 | 测试与评估 | Testing and Evaluation | [/tutorials/testing-and-evaluation](https://docs.langchain4j.dev/tutorials/testing-and-evaluation) | 测试样例与评估样例。 |

### 实验性与高级特性

| # | 中文标题 | 英文原标题 | 原文链接 | 简介 |
|---|---|---|---|---|
| 29 | 非阻塞与响应式 | Non-blocking and Reactive | [/tutorials/non-blocking](https://docs.langchain4j.dev/tutorials/non-blocking) | 实验性异步/响应式 API。 |
| 30 | 决策服务 | Decision Services | [/tutorials/decision-services](https://docs.langchain4j.dev/tutorials/decision-services) | 实验性 API，未来可能变化。 |
| 31 | 决策模型 | Decision Models | [/tutorials/decision-models](https://docs.langchain4j.dev/tutorials/decision-models) | 实验性 API，未来可能变化。 |
| 32 | 模型路由 | Model Routing | [/tutorials/model-routing](https://docs.langchain4j.dev/tutorials/model-routing) | 实验性 API，按规则路由到不同模型。 |

## 学习路线建议

- **入门**：先读 *Chat and Language Models* 与 *AI Services*，理解 LangChain4j 的两层抽象。
- **常用能力**：再学 *Chat Memory*、*Tools*、*RAG*、*Structured Outputs*，覆盖对话系统主要功能。
- **框架集成**：根据项目框架选择 *Spring Boot / Quarkus / Micronaut / Helidon / Payara Micro*。
- **生产化**：阅读 *Logging*、*Observability*、*Testing and Evaluation*，关注可观测性与可测试性。
- **进阶探索**：根据需要了解 *Agents*、*Guardrails*、*MCP*、*Skills*、*Model Routing* 等实验性模块。

## 文件清单

本目录下的中文翻译文件命名规则为 `<原文件名>-zh.txt`，与英文原文一一对应：

```
00-index-zh.md                              本索引
chat-and-language-models-zh.txt
chat-memory-zh.txt
ai-services-zh.txt
tools-zh.txt
model-parameters-zh.txt
response-streaming-zh.txt
rag-zh.txt
structured-outputs-zh.txt
agents-zh.txt
guardrails-zh.txt
classification-zh.txt
embedding-stores-zh.txt
mcp-zh.txt
mcp-stdio-server-zh.txt
image-models-zh.txt
spring-boot-integration-zh.txt
quarkus-integration-zh.txt
micronaut-integration-zh.txt
helidon-integration-zh.txt
payara-micro-integration-zh.txt
kotlin-zh.txt
logging-zh.txt
json-zh.txt
jackson-3-zh.txt
observability-zh.txt
skills-zh.txt
customizable-http-client-zh.txt
testing-and-evaluation-zh.txt
non-blocking-zh.txt
decision-services-zh.txt
decision-models-zh.txt
model-routing-zh.txt
```