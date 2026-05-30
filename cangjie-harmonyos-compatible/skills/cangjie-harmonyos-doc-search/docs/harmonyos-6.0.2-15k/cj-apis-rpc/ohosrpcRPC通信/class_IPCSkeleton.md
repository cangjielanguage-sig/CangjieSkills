## class IPCSkeleton

```cangjie
public class IPCSkeleton {}
```

**功能：** 用于获取IPC上下文信息，包括获取UID和PID、获取本端和对端设备ID、检查接口调用是否在同一设备上。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

### static func flushCmdBuffer(IRemoteObject)

```cangjie
public static func flushCmdBuffer(object: IRemoteObject): Unit
```

**功能：** 静态方法，将所有挂起的命令从指定的RemoteProxy刷新到相应的RemoteObject。建议在任何时间执行敏感操作之前调用此方法。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|object|[IRemoteObject](#interface-iremoteobject)|是|-|返回系统能力管理者。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The number of parameters is incorrect;<br>2.The parameter type does not match;<br>3.The passed mapType exceeds the maximum protection level.|

### static func getCallingDeviceID()

```cangjie
public static func getCallingDeviceID(): String
```

**功能：** 静态方法，获取调用者进程所在的设备ID。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回调用者进程所在的设备ID。|

### static func getCallingPid()

```cangjie
public static func getCallingPid(): Int32
```

**功能：** 静态方法，获取调用者的PID。此方法由[RemoteObject](#class-remoteobject)对象在onRemoteRequest方法中调用，不在IPC上下文环境（onRemoteRequest）中调用则返回本进程的PID。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回调用者的PID。|

### static func getCallingTokenId()

```cangjie
public static func getCallingTokenId(): UInt32
```

**功能：** 静态方法，获取调用者的TokenId，用于被调用方对调用方的身份校验。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回调用者的TokenId。|

### static func getCallingUid()

```cangjie
public static func getCallingUid(): Int32
```

**功能：** 静态方法，获取调用者的UID。此方法由RemoteObject对象在onRemoteRequest方法中调用，不在IPC上下文环境（onRemoteRequest）中调用则返回本进程的UID。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回调用者的UID。|

### static func getContextObject()

```cangjie
public static func getContextObject(): IRemoteObject
```

**功能：** 静态方法，获取系统能力的管理者。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[IRemoteObject](#interface-iremoteobject)|返回系统能力管理者。|

### static func getLocalDeviceID()

```cangjie
public static func getLocalDeviceID(): String
```

**功能：** 静态方法，获取本端设备ID。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回本地设备的ID。|

### static func isLocalCalling()

```cangjie
public static func isLocalCalling(): Bool
```

**功能：** 静态方法，检查当前通信对端是否是本设备的进程。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true：调用在同一台设备，false：调用未在同一台设备。|