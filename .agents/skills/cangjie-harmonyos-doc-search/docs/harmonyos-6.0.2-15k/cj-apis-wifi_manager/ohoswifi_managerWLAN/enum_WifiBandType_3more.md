## enum WifiBandType

```cangjie
public enum WifiBandType <: ToString {
    | WIFI_BAND_NONE
    | WIFI_BAND_2G
    | WIFI_BAND_5G
    | WIFI_BAND_6G
    | WIFI_BAND_60G
    | ...
}
```

**功能：** 表示WIFI频段类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**父类型：**

- ToString

### WIFI_BAND_2G

```cangjie
WIFI_BAND_2G
```

**功能：** 2.4G频段类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### WIFI_BAND_5G

```cangjie
WIFI_BAND_5G
```

**功能：** 5G频段类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### WIFI_BAND_60G

```cangjie
WIFI_BAND_60G
```

**功能：** 60G频段类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### WIFI_BAND_6G

```cangjie
WIFI_BAND_6G
```

**功能：** 6G频段类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### WIFI_BAND_NONE

```cangjie
WIFI_BAND_NONE
```

**功能：** 无效频段类型。

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

## enum WifiCategory

```cangjie
public enum WifiCategory <: ToString {
    | DEFAULT
    | WIFI6
    | WIFI6_PLUS
    | ...
}
```

**功能：** 表示热点支持的最高wifi类别。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**父类型：**

- ToString

### DEFAULT

```cangjie
DEFAULT
```

**功能：** Default。Wifi6以下的wifi类别。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### WIFI6

```cangjie
WIFI6
```

**功能：** Wifi6。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### WIFI6_PLUS

```cangjie
WIFI6_PLUS
```

**功能：** Wifi6+。

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

## enum WifiChannelWidth

```cangjie
public enum WifiChannelWidth <: ToString {
    | WIDTH_20MHZ
    | WIDTH_40MHZ
    | WIDTH_80MHZ
    | WIDTH_160MHZ
    | WIDTH_80MHZ_PLUS
    | WIDTH_INVALID
    | ...
}
```

**功能：** 表示带宽类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**父类型：**

- ToString

### WIDTH_160MHZ

```cangjie
WIDTH_160MHZ
```

**功能：** 160MHZ。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### WIDTH_20MHZ

```cangjie
WIDTH_20MHZ
```

**功能：** 20MHZ。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### WIDTH_40MHZ

```cangjie
WIDTH_40MHZ
```

**功能：** 40MHZ。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### WIDTH_80MHZ

```cangjie
WIDTH_80MHZ
```

**功能：** 80MHZ。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### WIDTH_80MHZ_PLUS

```cangjie
WIDTH_80MHZ_PLUS
```

**功能：** 80MHZ。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### WIDTH_INVALID

```cangjie
WIDTH_INVALID
```

**功能：** 无效值

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