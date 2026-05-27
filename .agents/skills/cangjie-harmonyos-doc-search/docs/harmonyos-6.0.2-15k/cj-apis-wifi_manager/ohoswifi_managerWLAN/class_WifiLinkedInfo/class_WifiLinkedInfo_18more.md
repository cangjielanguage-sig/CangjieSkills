## class WifiLinkedInfo

```cangjie
public class WifiLinkedInfo <: ToString {
    public let ssid: String
    public let bssid: String
    public let rssi: Int32
    public let band: Int32
    public let linkSpeed: Int32
    public let rxLinkSpeed: Int32
    public let maxSupportedTxLinkSpeed: Int32
    public let maxSupportedRxLinkSpeed: Int32
    public let frequency: Int32
    public let isHidden: Bool
    public let isRestricted: Bool
    public let macType: Int32
    public let macAddress: String
    public let ipAddress: UInt32
    public let connState: ConnState
    public let channelWidth: WifiChannelWidth
    public let wifiStandard: WifiStandard
    public let supportedWifiCategory: WifiCategory
    public let isHiLinkNetwork: Bool
}
```

**功能：** 提供WLAN连接的相关信息。

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

**功能：** 热点的BSSID。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let channelWidth

```cangjie
public let channelWidth: WifiChannelWidth
```

**功能：** 当前连接热点的信道带宽。

**类型：** [WifiChannelWidth](#enum-wifichannelwidth)

**读写能力：** 只读

**起始版本：** 19

### let connState

```cangjie
public let connState: ConnState
```

**功能：** WLAN连接状态。

**类型：** [ConnState](#enum-connstate)

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

### let ipAddress

```cangjie
public let ipAddress: UInt32
```

**功能：** WLAN连接的IP地址。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let isHiLinkNetwork

```cangjie
public let isHiLinkNetwork: Bool
```

**功能：** 热点是否支持hilink，true:支持，&nbsp;false:不支持。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let isHidden

```cangjie
public let isHidden: Bool
```

**功能：** WLAN接入点是否是隐藏网络。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let isRestricted

```cangjie
public let isRestricted: Bool
```

**功能：** WLAN接入点是否限制数据量。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let linkSpeed

```cangjie
public let linkSpeed: Int32
```

**功能：** WLAN接入点的上行速度。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let macAddress

```cangjie
public let macAddress: String
```

**功能：** 设备的MAC地址。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let macType

```cangjie
public let macType: Int32
```

**功能：** MAC地址类型。0 表示随机MAC地址，1 表示设备MAC地址。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let maxSupportedRxLinkSpeed

```cangjie
public let maxSupportedRxLinkSpeed: Int32
```

**功能：** 当前支持的最大下行速率。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let maxSupportedTxLinkSpeed

```cangjie
public let maxSupportedTxLinkSpeed: Int32
```

**功能：** 当前支持的最大上行速率。

**类型：** Int32

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

### let rxLinkSpeed

```cangjie
public let rxLinkSpeed: Int32
```

**功能：** WLAN接入点的下行速度。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let ssid

```cangjie
public let ssid: String
```

**功能：** 热点的SSID，编码格式为UTF-8。

**类型：** String

**读写能力：** 只读

**起始版本：** 19