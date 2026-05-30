## enum WifiSecurityType

```cangjie
public enum WifiSecurityType <: Equatable<WifiSecurityType> & ToString {
    | WIFI_SEC_TYPE_INVALID
    | WIFI_SEC_TYPE_OPEN
    | WIFI_SEC_TYPE_WEP
    | WIFI_SEC_TYPE_PSK
    | WIFI_SEC_TYPE_SAE
    | WIFI_SEC_TYPE_EAP
    | WIFI_SEC_TYPE_EAP_SUITE_B
    | WIFI_SEC_TYPE_OWE
    | WIFI_SEC_TYPE_WAPI_CERT
    | WIFI_SEC_TYPE_WAPI_PSK
    | ...
}
```

**功能：** 表示加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

**父类型：**

- Equatable\<WifiSecurityType>
- ToString

### WIFI_SEC_TYPE_EAP

```cangjie
WIFI_SEC_TYPE_EAP
```

**功能：** EAP加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### WIFI_SEC_TYPE_EAP_SUITE_B

```cangjie
WIFI_SEC_TYPE_EAP_SUITE_B
```

**功能：** Suite-B 192位加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### WIFI_SEC_TYPE_INVALID

```cangjie
WIFI_SEC_TYPE_INVALID
```

**功能：** 无效加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### WIFI_SEC_TYPE_OPEN

```cangjie
WIFI_SEC_TYPE_OPEN
```

**功能：** 开放加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### WIFI_SEC_TYPE_OWE

```cangjie
WIFI_SEC_TYPE_OWE
```

**功能：** 机会性无线加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### WIFI_SEC_TYPE_PSK

```cangjie
WIFI_SEC_TYPE_PSK
```

**功能：** Pre-shared key (PSK)加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### WIFI_SEC_TYPE_SAE

```cangjie
WIFI_SEC_TYPE_SAE
```

**功能：** Simultaneous Authentication of Equals (SAE)加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### WIFI_SEC_TYPE_WAPI_CERT

```cangjie
WIFI_SEC_TYPE_WAPI_CERT
```

**功能：** WAPI-Cert加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### WIFI_SEC_TYPE_WAPI_PSK

```cangjie
WIFI_SEC_TYPE_WAPI_PSK
```

**功能：** WAPI-PSK加密类型。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

### WIFI_SEC_TYPE_WEP

```cangjie
WIFI_SEC_TYPE_WEP
```

**功能：** Wired Equivalent Privacy (WEP)加密类型。候选网络配置不支持该加密类型。

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

### func ==(WifiSecurityType)

```cangjie
public operator func ==(that: WifiSecurityType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|that|[WifiSecurityType](#enum-wifisecuritytype)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|