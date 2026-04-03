## enum WifiSecurityType

```cangjie
public enum WifiSecurityType <: Equatable<WifiSecurityType> & ToString {
    | WifiSecTypeInvalid
    | WifiSecTypeOpen
    | WifiSecTypeWep
    | WifiSecTypePsk
    | WifiSecTypeSae
    | WifiSecTypeEap
    | WifiSecTypeEapSuiteB
    | WifiSecTypeOwe
    | WifiSecTypeWapiCert
    | WifiSecTypeWapiPsk
    | ...
}
```

**功能：** 表示加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

**父类型：**

- Equatable\<WifiSecurityType>
- ToString

### WifiSecTypeEap

```cangjie
WifiSecTypeEap
```

**功能：** EAP加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

### WifiSecTypeEapSuiteB

```cangjie
WifiSecTypeEapSuiteB
```

**功能：** Suite-B 192位加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

### WifiSecTypeInvalid

```cangjie
WifiSecTypeInvalid
```

**功能：** 无效加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

### WifiSecTypeOpen

```cangjie
WifiSecTypeOpen
```

**功能：** 开放加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

### WifiSecTypeOwe

```cangjie
WifiSecTypeOwe
```

**功能：** 机会性无线加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

### WifiSecTypePsk

```cangjie
WifiSecTypePsk
```

**功能：** Pre-shared key (PSK)加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

### WifiSecTypeSae

```cangjie
WifiSecTypeSae
```

**功能：** Simultaneous Authentication of Equals (SAE)加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

### WifiSecTypeWapiCert

```cangjie
WifiSecTypeWapiCert
```

**功能：** WAPI-Cert加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

### WifiSecTypeWapiPsk

```cangjie
WifiSecTypeWapiPsk
```

**功能：** WAPI-PSK加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

### WifiSecTypeWep

```cangjie
WifiSecTypeWep
```

**功能：** Wired Equivalent Privacy (WEP)加密类型。候选网络配置不支持该加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

### func !=(WifiSecurityType)

```cangjie
public operator func !=(other: WifiSecurityType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WifiSecurityType](#enum-wifisecuritytype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(WifiSecurityType)

```cangjie
public operator func ==(other: WifiSecurityType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WifiSecurityType](#enum-wifisecuritytype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|