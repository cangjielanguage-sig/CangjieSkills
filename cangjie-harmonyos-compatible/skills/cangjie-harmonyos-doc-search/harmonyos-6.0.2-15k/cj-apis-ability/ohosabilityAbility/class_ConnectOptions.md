## class ConnectOptions

```cangjie
public class ConnectOptions <: FFIData {
    public var onConnect: (ElementName, IRemoteObject) -> Unit
    public var onDisconnect: (ElementName) -> Unit
    public var onFailed: (Int32) -> Unit

    public init(
        onDisconnect: (ElementName) -> Unit,
        onFailed: (Int32) -> Unit
    )

    public init(
        onConnect: (ElementName, IRemoteObject) -> Unit,
        onDisconnect: (ElementName) -> Unit,
        onFailed: (Int32) -> Unit
    )
}
```

**功能：** 在连接指定的后台服务时作为入参用于接收连接过程中的状态变化。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 12

### var onConnect

```cangjie
public var onConnect: (ElementName, IRemoteObject) -> Unit
```

**功能：** 建立连接时的回调函数。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ([ElementName](#class-elementname), [IRemoteObject](../IPCKit/cj-apis-rpc.md#interface-iremoteobject)) -> Unit

**读写能力：** 可读写

**起始版本：** 19

### var onDisconnect

```cangjie
public var onDisconnect: (ElementName) -> Unit
```

**功能：** 断开连接时的回调函数。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ([ElementName](#class-elementname)) -> Unit

**读写能力：** 可读写

**起始版本：** 12

### var onFailed

```cangjie
public var onFailed: (Int32) -> Unit
```

**功能：** 连接失败时的回调函数。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** (Int32)->Unit

**读写能力：** 可读写

**起始版本：** 12

### init((ElementName) -> Unit, (Int32) -> Unit)

```cangjie
public init(
    onDisconnect: (ElementName) -> Unit,
    onFailed: (Int32) -> Unit
)
```

**功能：** ConnectOptions的构造器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onDisconnect|([ElementName](#class-elementname))->Unit|是|-|断开连接时的回调函数。|
|onFailed|(Int32)->Unit|是|-|连接失败时的回调函数。|

### init((ElementName,IRemoteObject) -> Unit, (ElementName) -> Unit, (Int32) -> Unit)

```cangjie
public init(
    onConnect: (ElementName, IRemoteObject) -> Unit,
    onDisconnect: (ElementName) -> Unit,
    onFailed: (Int32) -> Unit
)
```

**功能：** ConnectOptions的构造器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onConnect|([ElementName](#class-elementname),[IRemoteObject](../IPCKit/cj-apis-rpc.md#interface-iremoteobject))->Unit|是|-|建立连接时的回调函数。|
|onDisconnect|([ElementName](#class-elementname))->Unit|是|-|断开连接时的回调函数。|
|onFailed|(Int32)->Unit|是|-|连接失败时的回调函数。|