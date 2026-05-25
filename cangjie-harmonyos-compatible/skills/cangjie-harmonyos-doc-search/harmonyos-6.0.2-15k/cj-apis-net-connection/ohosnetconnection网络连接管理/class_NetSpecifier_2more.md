## class NetSpecifier

```cangjie
public class NetSpecifier {
    public NetSpecifier(
        public let netCapabilities: NetCapabilities,
        public let bearerPrivateIdentifier!: ?String = None
    )
}
```

**功能：** 提供承载数据网络能力的实例。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

### let bearerPrivateIdentifier

```cangjie
public let bearerPrivateIdentifier: ?String = None
```

**功能：** 网络标识符，Wi-Fi网络的标识符是"wifi"，蜂窝网络的标识符是"slot0"（对应SIM卡1）。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 12

### let netCapabilities

```cangjie
public let netCapabilities: NetCapabilities
```

**功能：** 存储数据网络的传输能力和承载类型。

**类型：** [NetCapabilities](#class-netcapabilities)

**读写能力：** 只读

**起始版本：** 12

### NetSpecifier(NetCapabilities, ?String)

```cangjie
public NetSpecifier(
    public let netCapabilities: NetCapabilities,
    public let bearerPrivateIdentifier!: ?String = None
)
```

**功能：** 构造NetSpecifier实例。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|netCapabilities|[NetCapabilities](#class-netcapabilities)|是|-|存储数据网络的传输能力和承载类型。|
|bearerPrivateIdentifier|?String|否|None| **命名参数。** 网络标识符，Wi-Fi网络的标识符是"wifi"，蜂窝网络的标识符是"slot0"（对应SIM卡1）。|

## class RouteInfo

```cangjie
public class RouteInfo {
    public RouteInfo(
        public let interfaceName: String,
        public let destination: LinkAddress,
        public let gateway: NetAddress,
        public let hasGateway: Bool,
        public let isDefaultRoute: Bool
    )
}
```

**功能：** 网络路由信息。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

### let destination

```cangjie
public let destination: LinkAddress
```

**功能：** 目的地址。

**类型：** [LinkAddress](#class-linkaddress)

**读写能力：** 只读

**起始版本：** 12

### let gateway

```cangjie
public let gateway: NetAddress
```

**功能：** 网关地址。

**类型：** [NetAddress](#class-netaddress)

**读写能力：** 只读

**起始版本：** 12

### let hasGateway

```cangjie
public let hasGateway: Bool
```

**功能：** 是否有网关。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let interfaceName

```cangjie
public let interfaceName: String
```

**功能：** 网卡名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let isDefaultRoute

```cangjie
public let isDefaultRoute: Bool
```

**功能：** 是否为默认路由。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### RouteInfo(String, LinkAddress, NetAddress, Bool, Bool)

```cangjie
public RouteInfo(
    public let interfaceName: String,
    public let destination: LinkAddress,
    public let gateway: NetAddress,
    public let hasGateway: Bool,
    public let isDefaultRoute: Bool
)
```

**功能：** 构造RouteInfo实例。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|interfaceName|String|是|-|网卡名称。|
|destination|[LinkAddress](#class-linkaddress)|是|-|目的地址。|
|gateway|[NetAddress](#class-netaddress)|是|-|网关地址。|
|hasGateway|Bool|是|-|是否有网关。|
|isDefaultRoute|Bool|是|-|是否为默认路由。|