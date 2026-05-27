## enum RadioTechnology

```cangjie
public enum RadioTechnology {
    | RADIO_TECHNOLOGY_UNKNOWN
    | RADIO_TECHNOLOGY_GSM
    | RADIO_TECHNOLOGY_1XRTT
    | RADIO_TECHNOLOGY_WCDMA
    | RADIO_TECHNOLOGY_HSPA
    | RADIO_TECHNOLOGY_HSPAP
    | RADIO_TECHNOLOGY_TD_SCDMA
    | RADIO_TECHNOLOGY_EVDO
    | RADIO_TECHNOLOGY_EHRPD
    | RADIO_TECHNOLOGY_LTE
    | RADIO_TECHNOLOGY_LTE_CA
    | RADIO_TECHNOLOGY_IWLAN
    | RADIO_TECHNOLOGY_NR
    | ...
}
```

**功能：** 无线接入技术。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

### RADIO_TECHNOLOGY_1XRTT

```cangjie
RADIO_TECHNOLOGY_1XRTT
```

**功能：** 无线接入技术1XRTT（Single-Carrier Radio Transmission Technology）。

**起始版本：** 19

### RADIO_TECHNOLOGY_EHRPD

```cangjie
RADIO_TECHNOLOGY_EHRPD
```

**功能：** 无线接入技术EHRPD（Evolved High Rate Package Data）。

**起始版本：** 19

### RADIO_TECHNOLOGY_EVDO

```cangjie
RADIO_TECHNOLOGY_EVDO
```

**功能：** 无线接入技术EVDO（Evolution Data Only）。

**起始版本：** 19

### RADIO_TECHNOLOGY_GSM

```cangjie
RADIO_TECHNOLOGY_GSM
```

**功能：** 无线接入技术GSM（Global System For Mobile Communication）。

**起始版本：** 19

### RADIO_TECHNOLOGY_HSPA

```cangjie
RADIO_TECHNOLOGY_HSPA
```

**功能：** 无线接入技术HSPA（High Speed Packet Access）。

**起始版本：** 19

### RADIO_TECHNOLOGY_HSPAP

```cangjie
RADIO_TECHNOLOGY_HSPAP
```

**功能：** 无线接入技术HSPAP（High Speed packet access (HSPA+) ）。

**起始版本：** 19

### RADIO_TECHNOLOGY_IWLAN

```cangjie
RADIO_TECHNOLOGY_IWLAN
```

**功能：** 无线接入技术IWLAN（Industrial Wireless LAN）。

**起始版本：** 19

### RADIO_TECHNOLOGY_LTE

```cangjie
RADIO_TECHNOLOGY_LTE
```

**功能：** 无线接入技术LTE（Long Term Evolution）。

**起始版本：** 19

### RADIO_TECHNOLOGY_LTE_CA

```cangjie
RADIO_TECHNOLOGY_LTE_CA
```

**功能：** 无线接入技术LTE_CA（Long Term Evolution_Carrier Aggregation）。

**起始版本：** 19

### RADIO_TECHNOLOGY_NR

```cangjie
RADIO_TECHNOLOGY_NR
```

**功能：** 无线接入技术NR（New Radio）。

**起始版本：** 19

### RADIO_TECHNOLOGY_TD_SCDMA

```cangjie
RADIO_TECHNOLOGY_TD_SCDMA
```

**功能：** 无线接入技术TD_SCDMA（TimeDivision-Synchronous Code Division Multiple Access）。

**起始版本：** 19

### RADIO_TECHNOLOGY_UNKNOWN

```cangjie
RADIO_TECHNOLOGY_UNKNOWN
```

**功能：** 未知无线接入技术（RAT）。

**起始版本：** 19

### RADIO_TECHNOLOGY_WCDMA

```cangjie
RADIO_TECHNOLOGY_WCDMA
```

**功能：** 无线接入技术WCDMA（Wideband Code Division Multiple Access）。

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

let i = RadioTechnology.RADIO_TECHNOLOGY_NR.getValue()
```