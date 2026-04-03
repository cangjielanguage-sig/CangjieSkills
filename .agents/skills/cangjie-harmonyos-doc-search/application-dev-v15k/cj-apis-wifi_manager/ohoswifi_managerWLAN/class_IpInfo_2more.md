## class IpInfo

```cangjie
public class IpInfo {
    public let ipAddress: UInt32
    public let gateway: UInt32
    public let netmask: UInt32
    public let primaryDns: UInt32
    public let secondDns: UInt32
    public let serverIp: UInt32
    public let leaseDuration: UInt32
}
```

**功能：** IP信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

### let gateway

```cangjie
public let gateway: UInt32
```

**功能：** 网关。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let ipAddress

```cangjie
public let ipAddress: UInt32
```

**功能：** IP地址。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let leaseDuration

```cangjie
public let leaseDuration: UInt32
```

**功能：** IP地址租用时长，单位：秒。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let netmask

```cangjie
public let netmask: UInt32
```

**功能：** 掩码。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let primaryDns

```cangjie
public let primaryDns: UInt32
```

**功能：** 主DNS服务器IP地址。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let secondDns

```cangjie
public let secondDns: UInt32
```

**功能：** 备DNS服务器IP地址。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let serverIp

```cangjie
public let serverIp: UInt32
```

**功能：** DHCP服务端IP地址。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

## class Ipv6Info

```cangjie
public class Ipv6Info <: ToString {}
```

**功能：** Ipv6信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**父类型：**

- ToString

### let gateway

```cangjie
public let gateway: String
```

**功能：** 网关。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let globalIpv6Address

```cangjie
public let globalIpv6Address: String
```

**功能：** 全局Ipv6地址。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let linkIpv6Address

```cangjie
public let linkIpv6Address: String
```

**功能：** 链路Ipv6地址。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let netmask

```cangjie
public let netmask: String
```

**功能：** 网络掩码。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let primaryDNS

```cangjie
public let primaryDNS: String
```

**功能：** 主DNS服务器Ipv6地址。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let randomGlobalIpv6Address

```cangjie
public let randomGlobalIpv6Address: String
```

**功能：** 随机全局Ipv6地址。 预留字段，暂不支持。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let randomUniqueIpv6Address

```cangjie
public let randomUniqueIpv6Address: ?String = None
```

**功能：** 随机唯一本地Ipv6地址。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 19

### let secondDNS

```cangjie
public let secondDNS: String
```

**功能：** 备DNS服务器Ipv6地址。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let uniqueIpv6Address

```cangjie
public let uniqueIpv6Address: ?String = None
```

**功能：** 唯一本地Ipv6地址。

**类型：** ?String

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