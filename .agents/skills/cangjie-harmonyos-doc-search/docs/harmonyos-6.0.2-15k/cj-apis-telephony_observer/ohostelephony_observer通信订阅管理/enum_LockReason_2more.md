## enum LockReason

```cangjie
public enum LockReason {
    | SIM_NONE
    | SIM_PIN
    | SIM_PUK
    | SIM_PN_PIN
    | SIM_PN_PUK
    | SIM_PU_PIN
    | SIM_PU_PUK
    | SIM_PP_PIN
    | SIM_PP_PUK
    | SIM_PC_PIN
    | SIM_PC_PUK
    | SIM_SIM_PIN
    | SIM_SIM_PUK
    | ...
}
```

**功能：** SIM卡锁类型。

**系统能力：** SystemCapability.Telephony.StateRegistry

**起始版本：** 19

### SIM_NONE

```cangjie
SIM_NONE
```

**功能：** 无锁。

**起始版本：** 19

### SIM_PC_PIN

```cangjie
SIM_PC_PIN
```

**功能：** 组织PIN锁。

**起始版本：** 19

### SIM_PC_PUK

```cangjie
SIM_PC_PUK
```

**功能：** 组织PUK锁。

**起始版本：** 19

### SIM_PIN

```cangjie
SIM_PIN
```

**功能：** PIN锁。

**起始版本：** 19

### SIM_PN_PIN

```cangjie
SIM_PN_PIN
```

**功能：** 网络PIN锁。

**起始版本：** 19

### SIM_PN_PUK

```cangjie
SIM_PN_PUK
```

**功能：** 网络PUK锁。

**起始版本：** 19

### SIM_PP_PIN

```cangjie
SIM_PP_PIN
```

**功能：** 服务提供商PIN锁。

**起始版本：** 19

### SIM_PP_PUK

```cangjie
SIM_PP_PUK
```

**功能：** 服务提供商PUK锁。

**起始版本：** 19

### SIM_PUK

```cangjie
SIM_PUK
```

**功能：** PUK锁。

**起始版本：** 19

### SIM_PU_PIN

```cangjie
SIM_PU_PIN
```

**功能：** 子网PIN锁。

**起始版本：** 19

### SIM_PU_PUK

```cangjie
SIM_PU_PUK
```

**功能：** 子网PUK锁。

**起始版本：** 19

### SIM_SIM_PIN

```cangjie
SIM_SIM_PIN
```

**功能：** SIM PIN锁。

**起始版本：** 19

### SIM_SIM_PUK

```cangjie
SIM_SIM_PUK
```

**功能：** SIM PUK锁。

**起始版本：** 19

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取枚举类型对应的数值。

**系统能力：** SystemCapability.Telephony.StateRegistry

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|枚举类型对应的数值。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let i = LockReason.SIM_PU_PIN.getValue()
```

## enum ObserverEventType

```cangjie
public enum ObserverEventType <: ToString {
    | NetworkStateChange
    | SignalInfoChange
    | CallStateChange
    | CellularDataConnectionStateChange
    | CellularDataFlowChange
    | SimStateChange
    | IccAccountInfoChange
    | ...
}
```

**功能：** 事件类型。

**系统能力：** SystemCapability.Telephony.StateRegistry

**起始版本：** 19

**父类型：**

- ToString

### CallStateChange

```cangjie
CallStateChange
```

**功能：** 通话状态变化事件。

**起始版本：** 19

### CellularDataConnectionStateChange

```cangjie
CellularDataConnectionStateChange
```

**功能：** 蜂窝数据链路连接状态变化事件。

**起始版本：** 19

### CellularDataFlowChange

```cangjie
CellularDataFlowChange
```

**功能：** 蜂窝数据业务的上下行数据流状态变化事件。

**起始版本：** 19

### IccAccountInfoChange

```cangjie
IccAccountInfoChange
```

**功能：** 卡账户变化事件。

**起始版本：** 19

### NetworkStateChange

```cangjie
NetworkStateChange
```

**功能：** 网络状态变化事件。

**起始版本：** 19

### SignalInfoChange

```cangjie
SignalInfoChange
```

**功能：** 信号状态变化事件。

**起始版本：** 19

### SimStateChange

```cangjie
SimStateChange
```

**功能：** sim状态更改事件。

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回枚举类型对应的字符串。

**系统能力：** SystemCapability.Telephony.StateRegistry

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举类型对应的字符串。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let eventType = ObserverEventType.NetworkStateChange.toString()
```