### WifiDeviceConfig(String, String, WifiSecurityType, ?String, ?DeviceAddressType, ?Bool, ?WifiEapConfig, ?WifiWapiConfig)

```cangjie
public WifiDeviceConfig(
    public let ssid: String,
    public let preSharedKey: String,
    public let securityType: WifiSecurityType,
    public let bssid!: ?String = None,
    public let bssidType!: ?DeviceAddressType = RANDOM_DEVICE_ADDRESS,
    public let isHiddenSsid!: ?Bool = false,
    public var eapConfig!: ?WifiEapConfig = None,
    public var wapiConfig!: ?WifiWapiConfig = None
)
```

**功能：** 构造WifiDeviceConfig实例。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|ssid|String|是|-|热点的SSID，最大长度为32字节，编码格式为UTF-8。|
|preSharedKey|String|是|-|热点的密钥，最大长度为64字节。与securityType的取值相关，详见[let preSharedKey](#let-presharedkey)。|
|securityType|[WifiSecurityType](#enum-wifisecuritytype)|是|-|加密类型。|
|bssid|?String|否|None| **命名参数。** 热点的BSSID，例如：00:11:22:33:44:55。|
|bssidType|?[DeviceAddressType](#enum-deviceaddresstype) |否|RANDOM_DEVICE_ADDRESS| **命名参数。** 热点的BSSID类型。|
|isHiddenSsid|?Bool|否|false| **命名参数。** 是否是隐藏网络。|
|eapConfig|?[WifiEapConfig](#class-wifieapconfig)|否|None| **命名参数。** 可扩展身份验证协议配置。只有securityType为WIFI_SEC_TYPE_EAP时需要填写。|
|wapiConfig|?[WifiWapiConfig](#class-wifiwapiconfig)|否|None| **命名参数。** WAPI身份验证协议配置。只有securityType为WIFI_SEC_TYPE_WAPI_CERT或WIFI_SEC_TYPE_WAPI_PSK时需要填写。|

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