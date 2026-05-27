## class Task

```cangjie
public class Task {
    public Task(
        public let tid: String,
        public let config: Config
    )
}
```

**功能：** 上传或下载任务。使用该方法前需要先获取Task对象，通过create获取。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

### let config

```cangjie
public let config: Config
```

**功能：** 任务的配置信息。

**类型：** [Config](#class-config)

**读写能力：** 只读

**起始版本：** 12

### let tid

```cangjie
public let tid: String
```

**功能：** 任务id，在系统上是唯一的，由系统自动生成。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### Task(String, Config)

```cangjie
public Task(
    public let tid: String,
    public let config: Config
)
```

**功能：** 创建Task对象。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|tid|String|是|-|任务id，在系统上是唯一的，由系统自动生成。|
|config|[Config](#class-config)|是|-|任务的配置信息。|

### func off(String, ?CallbackObject)

```cangjie
public func off(event: String, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消订阅任务事件。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|String|是|-|订阅的事件类型。<br>- 取值为'progress'，表示任务进度。<br>- 取值为'completed'，表示任务完成。<br>- 取值为'failed'，表示任务失败。<br>- 取值为'pause'，表示任务暂停。<br>- 取值为'resume'，表示任务恢复。<br>- 取值为'remove'，表示任务删除。<br>- 取值为'response'，表示任务响应。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 需要取消订阅的回调函数。若无此参数，则取消订阅当前类型的所有回调函数。|