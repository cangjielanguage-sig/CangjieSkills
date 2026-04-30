## class RemoteObject

```cangjie
public open class RemoteObject <: IRemoteObject {
    public init(descriptor: String)
}
```

**功能：** 实现远程对象。服务提供者必须继承此类。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**父类型：**

- [IRemoteObject](#interface-iremoteobject)

### init(String)

```cangjie
public init(descriptor: String)
```

**功能：** RemoteObject构造函数。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|descriptor|String|是|-|接口描述符。|

### func getCallingPid()

```cangjie
public func getCallingPid(): Int32
```

**功能：** 获取通信对端的进程Pid。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回通信对端的进程Pid。|

### func getCallingUid()

```cangjie
public func getCallingUid(): Int32
```

**功能：** 获取通信对端的进程Uid。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回通信对端的进程Uid。|

### func getDescriptor()

```cangjie
public func getDescriptor(): String
```

**功能：** 获取对象的接口描述符。接口描述符为字符串。

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
  |1900008|The proxy or remote object is invalid.|

### func getLocalInterface(String)

```cangjie
public func getLocalInterface(descriptor: String): IRemoteBroker
```

**功能：** 查询接口描述符的字符串。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|descriptor|String|是|-|接口描述符的字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|[IRemoteBroker](#interface-iremotebroker)|返回绑定到指定接口描述符的IRemoteBroker对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: <br/> 1.The number of parameters is incorrect; <br/> 2.The parameter type does not match; <br/> 3.The string length exceeds 40960 bytes; <br/> 4.The number of bytes copied to the buffer is different from the length of the obtained string.|

### func isObjectDead()

```cangjie
public func isObjectDead(): Bool
```

**功能：** 检查当前对象是否死亡。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true：对象死亡，false：对象未死亡。|