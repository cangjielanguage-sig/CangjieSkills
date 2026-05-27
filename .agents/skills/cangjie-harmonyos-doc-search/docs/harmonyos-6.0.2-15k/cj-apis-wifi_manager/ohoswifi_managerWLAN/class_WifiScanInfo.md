## class WifiScanInfo

```cangjie
public class WifiScanInfo <: ToString {
    public let ssid: String
    public let bssid: String
    public let bssidType: DeviceAddressType
    public let capabilities: String
    public let securityType: WifiSecurityType
    public let rssi: Int32
    public let band: Int32
    public let frequency: Int32
    public let channelWidth: Int32
    public let centerFrequency0: Int32
    public let centerFrequency1: Int32
    public let infoElems: Array<WifiInfoElem>
    public let timestamp: Int64
    public let supportedWifiCategory: WifiCategory
    public let isHiLinkNetwork: Bool
}
```

**功能：** WLAN热点信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**父类型：**

- ToString

### let band

```cangjie
public let band: Int32
```

**功能：** WLAN接入点的频段，1:2.4GHZ；2:5GHZ。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let bssid

```cangjie
public let bssid: String
```

**功能：** 热点的BSSID，例如：00:11:22:33:44:55。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let bssidType

```cangjie
public let bssidType: DeviceAddressType
```

**功能：** 热点的BSSID类型。

**类型：** [DeviceAddressType](#enum-deviceaddresstype)

**读写能力：** 只读

**起始版本：** 19

### let capabilities

```cangjie
public let capabilities: String
```

**功能：** 热点能力。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let centerFrequency0

```cangjie
public let centerFrequency0: Int32
```

**功能：** 热点的中心频率。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let centerFrequency1

```cangjie
public let centerFrequency1: Int32
```

**功能：** 热点的中心频率。如果热点使用两个不重叠的WLAN信道，则返回两个中心频率，分别用centerFrequency0和centerFrequency1表示。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let channelWidth

```cangjie
public let channelWidth: Int32
```

**功能：** WLAN接入点的带宽，具体定义参见[WifiChannelWidth](#enum-wifichannelwidth)。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let frequency

```cangjie
public let frequency: Int32
```

**功能：** WLAN接入点的频率。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let infoElems

```cangjie
public let infoElems: Array<WifiInfoElem>
```

**功能：** 信息元素。

**类型：** Array\<[WifiInfoElem](#class-wifiinfoelem)>

**读写能力：** 只读

**起始版本：** 19

### let isHiLinkNetwork

```cangjie
public let isHiLinkNetwork: Bool
```

**功能：** 热点是否支持hiLink，true:支持，&nbsp;false:不支持。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let rssi

```cangjie
public let rssi: Int32
```

**功能：** 热点的信号强度(dBm)。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let securityType

```cangjie
public let securityType: WifiSecurityType
```

**功能：** WLAN加密类型。

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

### let supportedWifiCategory

```cangjie
public let supportedWifiCategory: WifiCategory
```

**功能：** 热点支持的最高wifi级别。

**类型：** [WifiCategory](#enum-wificategory)

**读写能力：** 只读

**起始版本：** 19

### let timestamp

```cangjie
public let timestamp: Int64
```

**功能：** 时间戳。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 19

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