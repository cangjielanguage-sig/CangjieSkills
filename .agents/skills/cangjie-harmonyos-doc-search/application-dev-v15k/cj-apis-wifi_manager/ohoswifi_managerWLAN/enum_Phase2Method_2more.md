## enum Phase2Method

```cangjie
public enum Phase2Method <: ToString {
    | PHASE2_NONE
    | PHASE2_PAP
    | PHASE2_MSCHAP
    | PHASE2_MSCHAPV2
    | PHASE2_GTC
    | PHASE2_SIM
    | PHASE2_AKA
    | PHASE2_AKA_PRIME
    | ...
}
```

**功能：** 表示第二阶段认证方式。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**父类型：**

- ToString

### PHASE2_AKA

```cangjie
PHASE2_AKA
```

**功能：** AKA类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### PHASE2_AKA_PRIME

```cangjie
PHASE2_AKA_PRIME
```

**功能：** AKA Prime类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### PHASE2_GTC

```cangjie
PHASE2_GTC
```

**功能：** GTC类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### PHASE2_MSCHAP

```cangjie
PHASE2_MSCHAP
```

**功能：** MSCHAP类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### PHASE2_MSCHAPV2

```cangjie
PHASE2_MSCHAPV2
```

**功能：** MSCHAPV2类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### PHASE2_NONE

```cangjie
PHASE2_NONE
```

**功能：** 不指定。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### PHASE2_PAP

```cangjie
PHASE2_PAP
```

**功能：** PAP类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### PHASE2_SIM

```cangjie
PHASE2_SIM
```

**功能：** SIM类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|

## enum WapiPskType

```cangjie
public enum WapiPskType <: ToString {
    | WAPI_PSK_ASCII
    | WAPI_PSK_HEX
    | ...
}
```

**功能：** WAPI认证方式。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

**父类型：**

- ToString

### WAPI_PSK_ASCII

```cangjie
WAPI_PSK_ASCII
```

**功能：** ASCII类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### WAPI_PSK_HEX

```cangjie
WAPI_PSK_HEX
```

**功能：** HEX类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|