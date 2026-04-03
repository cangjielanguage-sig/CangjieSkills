## class NetCapabilityInfo

```cangjie
public class NetCapabilityInfo {
    public var netHandle: NetHandle
    public var netCap: NetCapabilities
}
```

**功能：** 提供承载数据网络能力的实例。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var netCap

```cangjie
public var netCap: NetCapabilities
```

**功能：** 存储数据网络的传输能力和承载类型。

**类型：** [NetCapabilities](#class-netcapabilities)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var netHandle

```cangjie
public var netHandle: NetHandle
```

**功能：** 数据网络句柄。

**类型：** [NetHandle](#class-nethandle)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22