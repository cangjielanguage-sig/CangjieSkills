## enum Action

```cangjie
public enum Action <: ToString {
    | DOWNLOAD
    | UPLOAD
    | ...
}
```

**功能：** 定义操作选项。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

**父类型：**

- ToString

### DOWNLOAD

```cangjie
DOWNLOAD
```

**功能：** 表示下载任务。

**起始版本：** 12

### UPLOAD

```cangjie
UPLOAD
```

**功能：** 表示上传任务。

**起始版本：** 12

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|

## enum BroadcastEvent

```cangjie
public enum BroadcastEvent {
    | COMPLETE
    | ...
}
```

**功能：** 定义自定义系统事件。用户可以使用公共事件接口获取该事件。上传下载SA具有'ohos.permission.SEND_TASK_COMPLETE_EVENT' 该权限，用户可以配置事件的metadata 指向的二级配置文件来拦截其他事件发送者。使用CommonEventData 类型传输公共事件相关数据。成员的内容填写和[CommonEventData介绍](./cj-apis-common_event_manager.md) 介绍的有所区别，其中CommonEventData.code 表示任务的状态，目前为0x40 COMPLETE或0x41 FAILED; CommonEventData.data 表示任务的taskId。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

### COMPLETE

```cangjie
COMPLETE
```

**功能：** 表示任务完成事件。

**起始版本：** 12

### prop value

```cangjie
public prop value: String
```

**功能：** 返回该BroadcastEvent的字符串形式。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

## enum ConfigDataType

```cangjie
public enum ConfigDataType {
    | STR(String)
    | FORMITEMS(Array<FormItem>)
    | ...
}
```

**功能：** 上传/下载任务的data配置枚举类型。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

### FORMITEMS(Array\<FormItem>)

```cangjie
FORMITEMS(Array<FormItem>)
```

**功能：** 表示上传时，data是表单项数组Array&lt;FormItem&gt;，默认为空。

**起始版本：** 12

### STR(String)

```cangjie
STR(String)
```

**功能：** 下载时，data为字符串类型，通常使用json(object将被转换为json文本)，默认为空。

**起始版本：** 12

## enum Faults

```cangjie
public enum Faults <: ToString {
    | OTHERS
    | DISCONNECTED
    | TIMEOUT
    | PROTOCOL
    | FSIO
    | ...
}
```

**功能：** 定义任务失败的原因。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

**父类型：**

- ToString

### DISCONNECTED

```cangjie
DISCONNECTED
```

**功能：** 表示网络断开连接。

**起始版本：** 12

### FSIO

```cangjie
FSIO
```

**功能：** 表示文件系统io错误，例如打开/查找/读取/写入/关闭。

**起始版本：** 12

### OTHERS

```cangjie
OTHERS
```

**功能：** 表示其他故障。

**起始版本：** 12

### PROTOCOL

```cangjie
PROTOCOL
```

**功能：** 表示协议错误，例如：服务器内部错误（500）、无法处理的数据区间（416）等。

**起始版本：** 12

### TIMEOUT

```cangjie
TIMEOUT
```

**功能：** 表示任务超时。

**起始版本：** 12

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|