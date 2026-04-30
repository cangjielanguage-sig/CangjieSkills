## enum CardType

```cangjie
public enum CardType {
    | UNKNOWN_CARD
    | SINGLE_MODE_SIM_CARD
    | SINGLE_MODE_USIM_CARD
    | SINGLE_MODE_RUIM_CARD
    | DUAL_MODE_CG_CARD
    | CT_NATIONAL_ROAMING_CARD
    | CU_DUAL_MODE_CARD
    | DUAL_MODE_TELECOM_LTE_CARD
    | DUAL_MODE_UG_CARD
    | SINGLE_MODE_ISIM_CARD
    | ...
}
```

**功能：** 卡类型。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

### CT_NATIONAL_ROAMING_CARD

```cangjie
CT_NATIONAL_ROAMING_CARD
```

**功能：** 中国电信内部漫游卡。

**起始版本：** 19

### CU_DUAL_MODE_CARD

```cangjie
CU_DUAL_MODE_CARD
```

**功能：** 中国联通双模卡。

**起始版本：** 19

### DUAL_MODE_CG_CARD

```cangjie
DUAL_MODE_CG_CARD
```

**功能：** 双卡模式C+G。

**起始版本：** 19

### DUAL_MODE_TELECOM_LTE_CARD

```cangjie
DUAL_MODE_TELECOM_LTE_CARD
```

**功能：** 双模式电信LTE卡。

**起始版本：** 19

### DUAL_MODE_UG_CARD

```cangjie
DUAL_MODE_UG_CARD
```

**功能：** 双模式UG卡。

**起始版本：** 19

### SINGLE_MODE_ISIM_CARD

```cangjie
SINGLE_MODE_ISIM_CARD
```

**功能：** 单一ISIM卡类型。

**起始版本：** 19

### SINGLE_MODE_RUIM_CARD

```cangjie
SINGLE_MODE_RUIM_CARD
```

**功能：** 单RUIM卡。

**起始版本：** 19

### SINGLE_MODE_SIM_CARD

```cangjie
SINGLE_MODE_SIM_CARD
```

**功能：** 单SIM卡。

**起始版本：** 19

### SINGLE_MODE_USIM_CARD

```cangjie
SINGLE_MODE_USIM_CARD
```

**功能：** 单USIM卡。

**起始版本：** 19

### UNKNOWN_CARD

```cangjie
UNKNOWN_CARD
```

**功能：** 未知类型。

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

let i = CardType.DUAL_MODE_UG_CARD.getValue()
```

## enum SimState

```cangjie
public enum SimState {
    | SIM_STATE_UNKNOWN
    | SIM_STATE_NOT_PRESENT
    | SIM_STATE_LOCKED
    | SIM_STATE_NOT_READY
    | SIM_STATE_READY
    | SIM_STATE_LOADED
    | ...
}
```

**功能：** SIM卡状态。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

### SIM_STATE_LOADED

```cangjie
SIM_STATE_LOADED
```

**功能：** 表示SIM卡处于loaded状态，即SIM卡在位且所有卡文件加载完毕。

**起始版本：** 19

### SIM_STATE_LOCKED

```cangjie
SIM_STATE_LOCKED
```

**功能：** 表示SIM卡处于locked状态，即SIM卡被PIN、PUK或网络锁锁定。

**起始版本：** 19

### SIM_STATE_NOT_PRESENT

```cangjie
SIM_STATE_NOT_PRESENT
```

**功能：** 表示SIM卡处于not present状态，即卡槽中没有插入SIM卡。

**起始版本：** 19

### SIM_STATE_NOT_READY

```cangjie
SIM_STATE_NOT_READY
```

**功能：** 表示SIM卡处于not ready状态，即SIM卡在位但无法正常工作。

**起始版本：** 19

### SIM_STATE_READY

```cangjie
SIM_STATE_READY
```

**功能：** 表示SIM卡处于ready状态，即SIM卡在位且工作正常。

**起始版本：** 19

### SIM_STATE_UNKNOWN

```cangjie
SIM_STATE_UNKNOWN
```

**功能：** SIM卡状态未知，即无法获取准确的状态。

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

let i = SimState.SIM_STATE_READY.getValue()
```