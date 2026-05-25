## class LinkAddress

```cangjie
public class LinkAddress {
    public LinkAddress(
        public let address: NetAddress,
        public let prefixLength: Int32
    )
}
```

**功能：** 网络链路信息。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

### let address

```cangjie
public let address: NetAddress
```

**功能：** 链路地址。

**类型：** [NetAddress](#class-netaddress)

**读写能力：** 只读

**起始版本：** 12

### let prefixLength

```cangjie
public let prefixLength: Int32
```

**功能：** 链路地址前缀的长度。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### LinkAddress(NetAddress, Int32)

```cangjie
public LinkAddress(
    public let address: NetAddress,
    public let prefixLength: Int32
)
```

**功能：** 构造LinkAddress实例。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|address|[NetAddress](#class-netaddress)|是|-|链路地址。|
|prefixLength|Int32|是|-|链路地址前缀的长度。|

## class NetAddress

```cangjie
public class NetAddress {
    public NetAddress(
        public let address: String,
        public let family: ?UInt32,
        public let port: ?UInt16
    )
}
```

**功能：** 网络地址。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

### let address

```cangjie
public let address: String
```

**功能：** 地址。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let family

```cangjie
public let family: ?UInt32
```

**功能：** IPv4 = 1，IPv6 = 2，默认IPv4。

**类型：** ?UInt32

**读写能力：** 只读

**起始版本：** 12

### let port

```cangjie
public let port: ?UInt16
```

**功能：** 端口，取值范围[0, 65535]。

**类型：** ?UInt16

**读写能力：** 只读

**起始版本：** 12

### NetAddress(String, ?UInt32, ?UInt16)

```cangjie
public NetAddress(
    public let address: String,
    public let family: ?UInt32,
    public let port: ?UInt16
)
```

**功能：** 构造NetAddress实例。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|address|String|是|-|地址。|
|family|?UInt32|是|-|IPv4 = 1，IPv6 = 2，默认IPv4。|
|port|?UInt16|是|-|端口，取值范围[0, 65535]。|