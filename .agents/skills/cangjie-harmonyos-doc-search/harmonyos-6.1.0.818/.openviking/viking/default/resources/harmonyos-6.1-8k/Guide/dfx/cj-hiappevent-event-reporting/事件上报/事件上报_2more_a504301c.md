# 事件上报

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

HiAppEvent提供用于处理并上报事件的接口。

## 接口说明

API接口的具体使用说明（参数使用限制、具体取值范围等）请参见[应用事件打点API文档](../reference/PerformanceAnalysisKit/cj-apis-hiappevent.md)。

**数据处理者接口功能介绍：**

| 接口名 | 描述 |
| --------------- | ---------------- |
| addProcessor(processor: Processor): Int64 | 添加数据处理者，通过预置处理者进行事件上报。     |
| removeProcessor(id: Int64): Unit          | 移除数据处理者，取消预置处理者。                 |

**用户ID接口功能介绍：**

| 接口名 | 描述  |
| ---------- | --------------- |
| setUserId(name: String, value: String): Unit | 设置用户ID，数据处理者上报事件时可携带用户ID。 |
| getUserId(name: String): String              | 获取已设置的用户ID。 |

**用户属性接口功能介绍：**

| 接口名 | 描述  |
| ------------ | ----------------- |
| setUserProperty(name: String, value: String): Unit | 设置用户属性，数据处理者上报事件时可携带用户属性。   |
| getUserProperty(name: String): String              | 获取已设置的用户属性。 |