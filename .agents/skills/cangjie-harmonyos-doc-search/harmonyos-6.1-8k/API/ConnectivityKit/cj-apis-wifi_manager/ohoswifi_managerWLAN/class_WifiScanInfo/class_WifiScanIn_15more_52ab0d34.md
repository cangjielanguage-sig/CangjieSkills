## class WifiScanInfo

```cangjie
public class WifiScanInfo {
    public var ssid: String
    public var bssid: String
    public var bssidType: DeviceAddressType
    public var capabilities: String
    public var securityType: WifiSecurityType
    public var rssi: Int32
    public var band: Int32
    public var frequency: Int32
    public var channelWidth: Int32
    public var centerFrequency0: Int32
    public var centerFrequency1: Int32
    public var infoElems: Array<WifiInfoElement>
    public var timestamp: Int64
    public var supportedWifiCategory: WifiCategory
    public var isHiLinkNetwork: Bool
}
```

**功能：** WLAN热点信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

### var band

```cangjie
public var band: Int32
```

**功能：**  WLAN接入点的频段，1:2.4GHZ；2:5GHZ。

**类型：** Int32

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

### var bssid

```cangjie
public var bssid: String
```

**功能：** 热点的BSSID，例如：00:11:22:33:44:55。

**类型：** String

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

### var bssidType

```cangjie
public var bssidType: DeviceAddressType
```

**功能：** 热点的BSSID类型。

**类型：** [DeviceAddressType](#enum-deviceaddresstype)

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

### var capabilities

```cangjie
public var capabilities: String
```

**功能：** 热点能力。

**类型：** String

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

### var centerFrequency0

```cangjie
public var centerFrequency0: Int32
```

**功能：** 热点的中心频率。

**类型：** Int32

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

### var centerFrequency1

```cangjie
public var centerFrequency1: Int32
```

**功能：** 热点的中心频率。如果热点使用两个不重叠的WLAN信道，则返回两个中心频率，分别用centerFrequency0和centerFrequency1表示。

**类型：** Int32

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

### var channelWidth

```cangjie
public var channelWidth: Int32
```

**功能：** WLAN接入点的带宽。

**类型：** Int32

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

### var frequency

```cangjie
public var frequency: Int32
```

**功能：** WLAN接入点的频率。

**类型：** Int32

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

### var infoElems

```cangjie
public var infoElems: Array<WifiInfoElement>
```

**功能：** 信息元素。

**类型：** Array\<[WifiInfoElement](#class-wifiinfoelement)>

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

### var isHiLinkNetwork

```cangjie
public var isHiLinkNetwork: Bool
```

**功能：** 热点是否支持hiLink，true:支持，&nbsp;false:不支持。

**类型：** Bool

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

### var rssi

```cangjie
public var rssi: Int32
```

**功能：** 热点的信号强度(dBm)。

**类型：** Int32

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

### var securityType

```cangjie
public var securityType: WifiSecurityType
```

**功能：** WLAN加密类型。

**类型：** [WifiSecurityType](#enum-wifisecuritytype)

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

### var ssid

```cangjie
public var ssid: String
```

**功能：** 热点的SSID，最大长度为32字节，编码格式为UTF-8。

**类型：** String

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

### var supportedWifiCategory

```cangjie
public var supportedWifiCategory: WifiCategory
```

**功能：** 热点支持的最高wifi级别。

**类型：** [WifiCategory](#enum-wificategory)

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22