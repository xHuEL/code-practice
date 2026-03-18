## 🦌 DeerFlow 是什么？
[DeerFlow](https://github.com/bytedance/deer-flow)（ D eep E xploration and E fficient R esearch Flow ）是一个开源的智能体编排框架，它能够：

### 核心功能
1. 智能体编排 - 协调多个子智能体（sub-agents）协同工作
2. 记忆管理 - 提供长期记忆存储和检索功能
3. 沙箱环境 - 提供安全的代码执行环境
4. 技能扩展 - 支持可扩展的技能和工具系统

## **Long-horizon Agent**(长程智能体)



## 详细流程

主agent

```
prompt的实现如下：

```



### Middleware实现

```python
middlewares = [
    ThreadDataMiddleware(),      # 线程数据管理
    UploadsMiddleware(),         # 文件上传处理
    SandboxMiddleware(),         # 沙箱环境管理
    SummarizationMiddleware(),   # 上下文摘要
    TitleMiddleware(),           # 标题自动生成
    MemoryMiddleware(),          # 长期记忆管理
    ToolErrorHandlingMiddleware(), # 工具错误处理
    ClarificationMiddleware(),     # 澄清请求处理
]
```

问题：其中middleware是在什么时候被执行的？



## 沙箱工具

