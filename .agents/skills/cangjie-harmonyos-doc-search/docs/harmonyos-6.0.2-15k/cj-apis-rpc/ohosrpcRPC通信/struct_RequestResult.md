## struct RequestResult

```cangjie
public struct RequestResult {
    public RequestResult(
        public let errCode: Int32,
        public let code: UInt32,
        public let data: MessageSequence,
        public let reply: MessageSequence
    )
}
```

**功能：** 发送请求的响应结果。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

### let code

```cangjie
public let code: UInt32
```

**功能：** 消息代码。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let data

```cangjie
public let data: MessageSequence
```

**功能：** 发送给对端进程的MessageSequence对象。

**类型：** [MessageSequence](#class-messagesequence)

**读写能力：** 只读

**起始版本：** 19

### let errCode

```cangjie
public let errCode: Int32
```

**功能：** 错误码。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let reply

```cangjie
public let reply: MessageSequence
```

**功能：** 对端进程返回的MessageSequence对象。

**类型：** [MessageSequence](#class-messagesequence)

**读写能力：** 只读

**起始版本：** 19

### RequestResult(Int32, UInt32, MessageSequence, MessageSequence)

```cangjie
public RequestResult(
    public let errCode: Int32,
    public let code: UInt32,
    public let data: MessageSequence,
    public let reply: MessageSequence
)
```

**功能：** 构建发送请求的响应结果的对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|errCode|Int32|是|-|错误码。|
|code|UInt32|是|-|消息代码。|
|data|[MessageSequence](#class-messagesequence)|是|-|发送给对端进程的MessageSequence对象。|
|reply|[MessageSequence](#class-messagesequence)|是|-|对端进程返回的MessageSequence对象。|