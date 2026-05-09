## class LinkAddress

```cangjie
public class LinkAddress {
    public var address: NetAddress
    public var prefixLength: Int32
}
```

**功能：** 网络链路信息。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var address

```cangjie
public var address: NetAddress
```

**功能：** 链路地址。

**类型：** [NetAddress](#class-netaddress)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var prefixLength

```cangjie
public var prefixLength: Int32
```

**功能：** 链路地址前缀的长度。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

## class NetAddress

```cangjie
public class NetAddress {
    public var address: String
    public var family: UInt32
    public var port: UInt32
    public init(address: String, family!: UInt32 = 1, port!: UInt32 = 0)
}
```

**功能：** 网络地址。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var address

```cangjie
public var address: String
```

**功能：** 地址。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var family

```cangjie
public var family: UInt32
```

**功能：** IPv4 = 1，IPv6 = 2。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var port

```cangjie
public var port: UInt32
```

**功能：** 端口，取值范围\[0, 65535]。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### init(String, UInt32, UInt32)

```cangjie
public init(address: String, family!: UInt32 = 1, port!: UInt32 = 0)
```

**功能：** 构造NetAddress实例。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|address|String|是|-|地址。|
|family|UInt32|否|1|**命名参数。** IPv4 = 1，IPv6 = 2，默认IPv4。|
|port|UInt32|否|0|**命名参数。** 端口，取值范围\[0, 65535]，默认值为0。|

## class NetBlockStatusInfo

```cangjie
public class NetBlockStatusInfo {
    public var netHandle: NetHandle
    public var blocked: Bool
}
```

**功能：** 获取网络状态信息。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var blocked

```cangjie
public var blocked: Bool
```

**功能：** 标识当前网络是否是堵塞状态。true：标识当前网络是堵塞状态；false：标识当前网络不是堵塞状态。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var netHandle

```cangjie
public var netHandle: NetHandle
```

**功能：** 数据网络句柄(netHandle)。

**类型：** [NetHandle](#class-nethandle)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22