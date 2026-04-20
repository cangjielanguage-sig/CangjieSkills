## enum NetworkSelectionMode

```cangjie
public enum NetworkSelectionMode {
    | NETWORK_SELECTION_UNKNOWN
    | NETWORK_SELECTION_AUTOMATIC
    | NETWORK_SELECTION_MANUAL
    | ...
}
```

**功能：** 选网模式。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

### NETWORK_SELECTION_AUTOMATIC

```cangjie
NETWORK_SELECTION_AUTOMATIC
```

**功能：** 自动选网模式。

**起始版本：** 19

### NETWORK_SELECTION_MANUAL

```cangjie
NETWORK_SELECTION_MANUAL
```

**功能：** 手动选网模式。

**起始版本：** 19

### NETWORK_SELECTION_UNKNOWN

```cangjie
NETWORK_SELECTION_UNKNOWN
```

**功能：** 未知选网模式。

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

let i = NetworkSelectionMode.NETWORK_SELECTION_AUTOMATIC.getValue()
```

## enum NetworkType

```cangjie
public enum NetworkType {
    | NETWORK_TYPE_UNKNOWN
    | NETWORK_TYPE_GSM
    | NETWORK_TYPE_CDMA
    | NETWORK_TYPE_WCDMA
    | NETWORK_TYPE_TDSCDMA
    | NETWORK_TYPE_LTE
    | NETWORK_TYPE_NR
    | ...
}
```

**功能：** 网络类型。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

### NETWORK_TYPE_CDMA

```cangjie
NETWORK_TYPE_CDMA
```

**功能：** 网络类型为CDMA（Code Division Multiple Access）。

**起始版本：** 19

### NETWORK_TYPE_GSM

```cangjie
NETWORK_TYPE_GSM
```

**功能：** 网络类型为GSM（Global System For Mobile Communication）。

**起始版本：** 19

### NETWORK_TYPE_LTE

```cangjie
NETWORK_TYPE_LTE
```

**功能：** 网络类型为LTE（Long Term Evolution）。

**起始版本：** 19

### NETWORK_TYPE_NR

```cangjie
NETWORK_TYPE_NR
```

**功能：** 网络类型为NR（New Radio）。

**起始版本：** 19

### NETWORK_TYPE_TDSCDMA

```cangjie
NETWORK_TYPE_TDSCDMA
```

**功能：** 网络类型为TDSCDMA（TimeDivision-Synchronous Code Division Multiple Access）。

**起始版本：** 19

### NETWORK_TYPE_UNKNOWN

```cangjie
NETWORK_TYPE_UNKNOWN
```

**功能：** 未知网络类型。

**起始版本：** 19

### NETWORK_TYPE_WCDMA

```cangjie
NETWORK_TYPE_WCDMA
```

**功能：** 网络类型为WCDMA（Wideband Code Division Multiple Access）。

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

let i = NetworkType.NETWORK_TYPE_TDSCDMA.getValue()
```