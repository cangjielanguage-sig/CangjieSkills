## class RemoteProxy

```cangjie
public class RemoteProxy <: IRemoteObject {
    public static const PING_TRANSACTION: Int32 = 0x5f504e47
    public static const DUMP_TRANSACTION: Int32 = 0x5f444d50
    public static const INTERFACE_TRANSACTION: Int32 = 0x5f4e5446
    public static const MIN_TRANSACTION_ID: Int32 = 0x00000001
    public static const MAX_TRANSACTION_ID: Int32 = 0x00FFFFFF
}
```

**功能：** 实现IRemoteObject代理对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**父类型：**

- [IRemoteObject](#interface-iremoteobject)

### static const DUMP_TRANSACTION

```cangjie
public static const DUMP_TRANSACTION: Int32 = 0x5f444d50
```

**功能：** 内部指令码，获取Binder内部状态。

**类型：** Int32

**起始版本：** 19

### static const INTERFACE_TRANSACTION

```cangjie
public static const INTERFACE_TRANSACTION: Int32 = 0x5f4e5446
```

**功能：** 内部指令码，获取对端接口描述符。

**类型：** Int32

**起始版本：** 19

### static const MAX_TRANSACTION_ID

```cangjie
public static const MAX_TRANSACTION_ID: Int32 = 0x00FFFFFF
```

**功能：** 最大有效指令码。

**类型：** Int32

**起始版本：** 19

### static const MIN_TRANSACTION_ID

```cangjie
public static const MIN_TRANSACTION_ID: Int32 = 0x00000001
```

**功能：** 最小有效指令码。

**类型：** Int32

**起始版本：** 19

### static const PING_TRANSACTION

```cangjie
public static const PING_TRANSACTION: Int32 = 0x5f504e47
```

**功能：** 内部指令码，用于测试IPC服务正常。

**类型：** Int32

**起始版本：** 19

### func getDescriptor()

```cangjie
public func getDescriptor(): String
```

**功能：** 获取对象的接口描述符，接口描述符为字符串。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回接口描述符。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1900007|communication failed.|
  |1900008|The proxy or remote object is invalid.|

### func getLocalInterface(String)

```cangjie
public func getLocalInterface(descriptor: String): IRemoteBroker
```

**功能：** 查询并获取当前接口描述符对应的本地接口对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|descriptor|String|是|-|需要查询的接口描述符。|

**返回值：**

|类型|说明|
|:----|:----|
|[IRemoteBroker](#interface-iremotebroker)|默认返回Null，标识该接口是一个代理侧接口。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|check param failed.|
  |1900006|Operation allowed only for the remote object.|

### func isObjectDead()

```cangjie
public func isObjectDead(): Bool
```

**功能：** 指示对应的RemoteObject是否死亡。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true：对应的对象已经死亡，false：对应的对象未死亡。|