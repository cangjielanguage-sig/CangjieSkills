## class ConnectionProperties

```cangjie
public class ConnectionProperties {
    public ConnectionProperties(
        public let interfaceName: String,
        public let domains: String,
        public let linkAddresses: Array<LinkAddress>,
        public let dnses: Array<NetAddress>,
        public let routes: Array<RouteInfo>,
        public let mtu: UInt16
    )
}
```

**功能：** 网络连接信息类。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

### let dnses

```cangjie
public let dnses: Array<NetAddress>
```

**功能：** 网络地址，参考[NetAddress](#class-netaddress)。

**类型：** Array\<[NetAddress](#class-netaddress)>

**读写能力：** 只读

**起始版本：** 12

### let domains

```cangjie
public let domains: String
```

**功能：** 所属域，默认""。

**类型：** String

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

### let linkAddresses

```cangjie
public let linkAddresses: Array<LinkAddress>
```

**功能：** 链路信息。

**类型：** Array\<[LinkAddress](#class-linkaddress)>

**读写能力：** 只读

**起始版本：** 12

### let mtu

```cangjie
public let mtu: UInt16
```

**功能：** 最大传输单元。

**类型：** UInt16

**读写能力：** 只读

**起始版本：** 12

### let routes

```cangjie
public let routes: Array<RouteInfo>
```

**功能：** 路由信息。

**类型：** Array\<[RouteInfo](#class-routeinfo)>

**读写能力：** 只读

**起始版本：** 12

### ConnectionProperties(String, String, Array\<LinkAddress>, Array\<NetAddress>, Array\<RouteInfo>, UInt16)

```cangjie
public ConnectionProperties(
    public let interfaceName: String,
    public let domains: String,
    public let linkAddresses: Array<LinkAddress>,
    public let dnses: Array<NetAddress>,
    public let routes: Array<RouteInfo>,
    public let mtu: UInt16
)
```

**功能：** 构造ConnectionProperties实例。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|interfaceName|String|是|-|网卡名称。|
|domains|String|是|-|所属域，默认""。|
|linkAddresses|Array\<[LinkAddress](#class-linkaddress)>|是|-|链路信息。|
|dnses|Array\<[NetAddress](#class-netaddress)>|是|-|网络地址，参考NetAddress。|
|routes|Array\<[RouteInfo](#class-routeinfo)>|是|-|路由信息。|
|mtu|UInt16|是|-|最大传输单元。|