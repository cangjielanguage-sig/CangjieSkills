## enum NsaState

```cangjie
public enum NsaState {
    | NSA_STATE_NOT_SUPPORT
    | NSA_STATE_NO_DETECT
    | NSA_STATE_CONNECTED_DETECT
    | NSA_STATE_IDLE_DETECT
    | NSA_STATE_DUAL_CONNECTED
    | NSA_STATE_SA_ATTACHED
    | ...
}
```

**功能：** 非独立组网状态。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

### NSA_STATE_CONNECTED_DETECT

```cangjie
NSA_STATE_CONNECTED_DETECT
```

**功能：** 设备在LTE小区下连接到LTE网络支持NSA和NR覆盖检测。

**起始版本：** 19

### NSA_STATE_DUAL_CONNECTED

```cangjie
NSA_STATE_DUAL_CONNECTED
```

**功能：** 设备在支持NSA的LTE小区下连接到LTE + NR网络。

**起始版本：** 19

### NSA_STATE_IDLE_DETECT

```cangjie
NSA_STATE_IDLE_DETECT
```

**功能：** 支持NSA和NR覆盖检测的LTE小区下设备处于空闲状态。

**起始版本：** 19

### NSA_STATE_NOT_SUPPORT

```cangjie
NSA_STATE_NOT_SUPPORT
```

**功能：** 设备在不支持NSA的LTE小区下处于空闲状态或连接状态。

**起始版本：** 19

### NSA_STATE_NO_DETECT

```cangjie
NSA_STATE_NO_DETECT
```

**功能：** 在支持NSA但不支持NR覆盖检测的LTE小区下，设备处于空闲状态。

**起始版本：** 19

### NSA_STATE_SA_ATTACHED

```cangjie
NSA_STATE_SA_ATTACHED
```

**功能：** 设备在5GC附着时在NG-RAN小区下空闲或连接到NG-RAN小区。

**起始版本：** 19

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取枚举类型对应的数值。

**系统能力：** SystemCapability.Telephony.CoreService

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

let i = NsaState.NSA_STATE_IDLE_DETECT.getValue()
```