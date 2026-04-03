## enum RegState

```cangjie
public enum RegState {
    | REG_STATE_NO_SERVICE
    | REG_STATE_IN_SERVICE
    | REG_STATE_EMERGENCY_CALL_ONLY
    | REG_STATE_POWER_OFF
    | ...
}
```

**功能：** 网络注册状态。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

### REG_STATE_EMERGENCY_CALL_ONLY

```cangjie
REG_STATE_EMERGENCY_CALL_ONLY
```

**功能：** 设备只能使用紧急呼叫业务。

**起始版本：** 19

### REG_STATE_IN_SERVICE

```cangjie
REG_STATE_IN_SERVICE
```

**功能：** 设备可以正常使用服务，包括数据业务、短信、通话等。

**起始版本：** 19

### REG_STATE_NO_SERVICE

```cangjie
REG_STATE_NO_SERVICE
```

**功能：** 设备不能使用任何服务，包括数据业务、短信、通话等。

**起始版本：** 19

### REG_STATE_POWER_OFF

```cangjie
REG_STATE_POWER_OFF
```

**功能：** 蜂窝无线电已关闭，modem下电，无法和网侧进行通信。

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

let i = RegState.REG_STATE_EMERGENCY_CALL_ONLY.getValue()
```