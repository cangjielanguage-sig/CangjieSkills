## enum WifiStandard

```cangjie
public enum WifiStandard <: ToString {
    | WIFI_STANDARD_UNDEFINED
    | WIFI_STANDARD_11A
    | WIFI_STANDARD_11B
    | WIFI_STANDARD_11G
    | WIFI_STANDARD_11N
    | WIFI_STANDARD_11AC
    | WIFI_STANDARD_11AX
    | WIFI_STANDARD_11AD
    | ...
}
```

**功能：** 表示WIFI标准。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**父类型：**

- ToString

### WIFI_STANDARD_11A

```cangjie
WIFI_STANDARD_11A
```

**功能：** 802.11a WiFi标准类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### WIFI_STANDARD_11AC

```cangjie
WIFI_STANDARD_11AC
```

**功能：** 802.11ac WiFi标准类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### WIFI_STANDARD_11AD

```cangjie
WIFI_STANDARD_11AD
```

**功能：** 802.11ad WiFi标准类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### WIFI_STANDARD_11AX

```cangjie
WIFI_STANDARD_11AX
```

**功能：** 802.11ax WiFi标准类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### WIFI_STANDARD_11B

```cangjie
WIFI_STANDARD_11B
```

**功能：** 802.11b WiFi标准类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### WIFI_STANDARD_11G

```cangjie
WIFI_STANDARD_11G
```

**功能：** 802.11g WiFi标准类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### WIFI_STANDARD_11N

```cangjie
WIFI_STANDARD_11N
```

**功能：** 802.11n WiFi标准类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### WIFI_STANDARD_UNDEFINED

```cangjie
WIFI_STANDARD_UNDEFINED
```

**功能：** 无效WIFI标准类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

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