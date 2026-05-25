## class NetSpecifier

```cangjie
public class NetSpecifier {
    public var netCapabilities: NetCapabilities
    public var bearerPrivateIdentifier: String
    public init(netCapabilities: NetCapabilities, bearerPrivateIdentifier!: String = "")
}
```

**功能：** 提供承载数据网络能力的实例。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var bearerPrivateIdentifier

```cangjie
public var bearerPrivateIdentifier: String
```

**功能：** 网络标识符，蜂窝网络的标识符是"slot0"（对应SIM卡1）、"slot1"（对应SIM卡2）。可以通过传递注册的WLAN热点信息表示应用希望激活的指定的WLAN网络。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var netCapabilities

```cangjie
public var netCapabilities: NetCapabilities
```

**功能：** 存储数据网络的传输能力和承载类型。

**类型：** [NetCapabilities](#class-netcapabilities)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### init(NetCapabilities, String)

```cangjie
public init(netCapabilities: NetCapabilities, bearerPrivateIdentifier!: String = "")
```

**功能：** 提供承载数据网络能力的实例。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|netCapabilities|[NetCapabilities](#class-netcapabilities)|是|-|存储数据网络的传输能力和承载类型。|
|bearerPrivateIdentifier|String|否|""|**命名参数。** 网络标识符，蜂窝网络的标识符是"slot0"（对应SIM卡1）、"slot1"（对应SIM卡2）。可以通过传递注册的WLAN热点信息表示应用希望激活的指定的WLAN网络。|

## class RouteInfo

```cangjie
public class RouteInfo {
    public var interfaceName: String
    public var destination: LinkAddress
    public var gateway: NetAddress
    public var hasGateway: Bool
    public var isDefaultRoute: Bool
}
```

**功能：** 网络路由信息。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var destination

```cangjie
public var destination: LinkAddress
```

**功能：** 目的地址。

**类型：** [LinkAddress](#class-linkaddress)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var gateway

```cangjie
public var gateway: NetAddress
```

**功能：** 网关地址。

**类型：** [NetAddress](#class-netaddress)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var hasGateway

```cangjie
public var hasGateway: Bool
```

**功能：** 是否有网关。true：有网关；false：无网关。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var interfaceName

```cangjie
public var interfaceName: String
```

**功能：** 网卡名称。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var isDefaultRoute

```cangjie
public var isDefaultRoute: Bool
```

**功能：** 是否为默认路由。true：默认路由；false：非默认路由。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22