## class WifiWapiConfig

```cangjie
public class WifiWapiConfig <: ToString {
    public WifiWapiConfig(
        public let wapiPskType: WapiPskType,
        public let wapiAsCert: String,
        public let wapiUserCert: String
    )
}
```

**功能：** WAPI身份验证协议配置。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**父类型：**

- ToString

### let wapiAsCert

```cangjie
public let wapiAsCert: String
```

**功能：** As证书。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let wapiPskType

```cangjie
public let wapiPskType: WapiPskType
```

**功能：** 加密类型。

**类型：** [WapiPskType](#enum-wapipsktype)

**读写能力：** 只读

**起始版本：** 19

### let wapiUserCert

```cangjie
public let wapiUserCert: String
```

**功能：** 用户证书。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### WifiWapiConfig(WapiPskType, String, String)

```cangjie
public WifiWapiConfig(
    public let wapiPskType: WapiPskType,
    public let wapiAsCert: String,
    public let wapiUserCert: String
)
```

**功能：** 构造WifiWapiConfig实例。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|wapiPskType|[WapiPskType](#enum-wapipsktype)|是|加密类型。|
|wapiAsCert|String|是|As证书。|
|wapiUserCert|String|是|用户证书。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前类的字符串表示。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前类的字符串表示。|

## enum ConnState

```cangjie
public enum ConnState <: ToString {
    | SCANNING
    | CONNECTING
    | AUTHENTICATING
    | OBTAINING_IPADDR
    | CONNECTED
    | DISCONNECTING
    | DISCONNECTED
    | UNKNOWN
    | ...
}
```

**功能：** 表示WLAN连接状态。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**父类型：**

- ToString

### AUTHENTICATING

```cangjie
AUTHENTICATING
```

**功能：** WLAN连接正在认证中。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### CONNECTED

```cangjie
CONNECTED
```

**功能：** WLAN连接已建立。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### CONNECTING

```cangjie
CONNECTING
```

**功能：** 正在建立WLAN连接。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### DISCONNECTED

```cangjie
DISCONNECTED
```

**功能：** WLAN连接已断开。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### DISCONNECTING

```cangjie
DISCONNECTING
```

**功能：** WLAN连接正在断开。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### OBTAINING_IPADDR

```cangjie
OBTAINING_IPADDR
```

**功能：** 正在获取WLAN连接的IP地址。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### SCANNING

```cangjie
SCANNING
```

**功能：** 设备正在搜索可用的AP。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** WLAN连接建立失败。

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