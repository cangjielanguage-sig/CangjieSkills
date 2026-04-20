## class ConnectionProperties

```cangjie
public class ConnectionProperties {
    public var interfaceName: String
    public var domains: String
    public var linkAddresses: Array<LinkAddress>
    public var dnses: Array<NetAddress>
    public var routes: Array<RouteInfo>
    public var mtu: UInt32
}
```

**功能：** 网络连接信息类。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var dnses

```cangjie
public var dnses: Array<NetAddress>
```

**功能：** 网络地址，参考[NetAddress](#class-netaddress)。

**类型：** Array\<[NetAddress](#class-netaddress)>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var domains

```cangjie
public var domains: String
```

**功能：** 域名。

**类型：** String

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

### var linkAddresses

```cangjie
public var linkAddresses: Array<LinkAddress>
```

**功能：** 链路信息。

**类型：** Array\<[LinkAddress](#class-linkaddress)>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var mtu

```cangjie
public var mtu: UInt32
```

**功能：** 最大传输单元。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var routes

```cangjie
public var routes: Array<RouteInfo>
```

**功能：** 路由信息。

**类型：** Array\<[RouteInfo](#class-routeinfo)>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22