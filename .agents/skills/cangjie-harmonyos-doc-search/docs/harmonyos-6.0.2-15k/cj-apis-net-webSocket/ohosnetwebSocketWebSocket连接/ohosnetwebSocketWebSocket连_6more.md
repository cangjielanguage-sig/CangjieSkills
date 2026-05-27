# ohos.net.webSocket（WebSocket连接）

使用WebSocket建立服务器与客户端的双向连接，需要先通过[createWebSocket](#func-createwebsocket)方法创建[WebSocket](#class-websocket)对象，然后通过[connect](#func-connectstring-asynccallbackbool-websocketrequestoptions)方法连接到服务器。 当连接成功后，客户端会收到[open](#func-ononofftype-websocketasynccallbackhashmapuint32string)事件的回调，之后客户端就可以通过[send](#func-sendmessagedata-asynccallbackbool)方法与服务器进行通信。 当服务器发信息给客户端时，客户端会收到[message](#func-ononofftype-websocketasynccallbackmessagedata)事件的回调。当客户端不要此连接时，可以通过调用[close](#func-closeasynccallbackbool-websocketcloseoptions)方法主动断开连接，之后客户端会收到[close](#func-closeasynccallbackbool-websocketcloseoptions)事件的回调。

若在上述任一过程中发生错误，客户端会收到[error](#func-ononofftype-websocketerrorcallback)事件的回调。

## 导入模块

```cangjie
import kit.NetworkKit.*
```

## 权限列表

ohos.permission.INTERNET

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func createWebSocket()

```cangjie
public func createWebSocket(): WebSocket
```

**功能：** 创建一个WebSocket，里面包括建立连接、关闭连接、发送数据和订阅/取消订阅WebSocket连接的打开事件、接收到服务器消息事件、关闭事件和错误事件。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[WebSocket](#class-websocket)|返回一个WebSocket对象，里面包括connect、send、close、on和off方法。|

## class CloseResult

```cangjie
public class CloseResult {
    public CloseResult(
        public let code : UInt32,
        public let reason : String
    )
}
```

**功能：** 关闭WebSocket连接时，订阅close事件得到的关闭结果。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

### let code

```cangjie
public let code: UInt32
```

**功能：** 错误码，订阅close事件得到的关闭连接的错误码。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let reason

```cangjie
public let reason: String
```

**功能：** 原因值，订阅close事件得到的关闭连接的错误原因。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### CloseResult(UInt32, String)

```cangjie
public CloseResult(
    public let code : UInt32,
    public let reason : String
)
```

**功能：** CloseResult构造函数。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|code|UInt32|是|-|错误码，订阅close事件得到的关闭连接的错误码。|
|reason|String|是|-|原因值，订阅close事件得到的关闭连接的错误原因。|