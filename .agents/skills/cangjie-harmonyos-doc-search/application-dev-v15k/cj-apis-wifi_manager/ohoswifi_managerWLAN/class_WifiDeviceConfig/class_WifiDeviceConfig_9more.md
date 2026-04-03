## class WifiDeviceConfig

```cangjie
public class WifiDeviceConfig <: ToString {
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
}
```

**功能：** WLAN配置信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**父类型：**

- ToString

### var eapConfig

```cangjie
public var eapConfig: ?WifiEapConfig = None
```

**功能：** 可扩展身份验证协议配置。

**类型：** ?[WifiEapConfig](#class-wifieapconfig)

**读写能力：** 可读写

**起始版本：** 19

### var wapiConfig

```cangjie
public var wapiConfig: ?WifiWapiConfig = None
```

**功能：** WAPI身份验证协议配置。

**类型：** ?[WifiWapiConfig](#class-wifiwapiconfig)

**读写能力：** 可读写

**起始版本：** 19

### let bssid

```cangjie
public let bssid: ?String = None
```

**功能：** 热点的BSSID，例如：00:11:22:33:44:55。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 19

### let bssidType

```cangjie
public let bssidType: ?DeviceAddressType = RANDOM_DEVICE_ADDRESS
```

**功能：** 热点的BSSID类型。

**类型：** ?[DeviceAddressType](#enum-deviceaddresstype)

**读写能力：** 只读

**起始版本：** 19

### let isHiddenSsid

```cangjie
public let isHiddenSsid: ?Bool = false
```

**功能：** 是否是隐藏网络。

**类型：** ?Bool

**读写能力：** 只读

**起始版本：** 19

### let preSharedKey

```cangjie
public let preSharedKey: String
```

**功能：** 热点的密钥，最大长度为64字节。

- 当securityType为WIFI_SEC_TYPE_OPEN时该字段需为空串，其他加密类型不能为空串。
- 当securityType为WIFI_SEC_TYPE_WEP时，该字段长度只允许为5、10、13、26、16和32字节其中之一，并- 且当字段长度为偶数时，该字段必须为纯十六进制数字构成。
- 当securityType为WIFI_SEC_TYPE_SAE时，该字段最小长度为1字节。
- 当securityType为WIFI_SEC_TYPE_PSK时，该字段最小长度为8字节。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let securityType

```cangjie
public let securityType: WifiSecurityType
```

**功能：** 加密类型。

**类型：** [WifiSecurityType](#enum-wifisecuritytype)

**读写能力：** 只读

**起始版本：** 19

### let ssid

```cangjie
public let ssid: String
```

**功能：** 热点的SSID，最大长度为32字节，编码格式为UTF-8。

**类型：** String

**读写能力：** 只读

**起始版本：** 19