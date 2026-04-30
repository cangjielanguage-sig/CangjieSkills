## class NetCapabilityInfo

```cangjie
public class NetCapabilityInfo {
    public NetCapabilityInfo(
        public let netHandle: NetHandle,
        public let netCap!: ?NetCapabilities = None
    )
}
```

**功能：** 提供承载数据网络能力的实例。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

### let netCap

```cangjie
public let netCap: ?NetCapabilities = None
```

**功能：** 存储数据网络的传输能力和承载类型。

**类型：** ?[NetCapabilities](#class-netcapabilities)

**读写能力：** 只读

**起始版本：** 12

### let netHandle

```cangjie
public let netHandle: NetHandle
```

**功能：** 数据网络句柄。

**类型：** [NetHandle](#class-nethandle)

**读写能力：** 只读

**起始版本：** 12

### NetCapabilityInfo(NetHandle, ?NetCapabilities)

```cangjie
public NetCapabilityInfo(
    public let netHandle: NetHandle,
    public let netCap!: ?NetCapabilities = None
)
```

**功能：** 构造NetCapabilityInfo实例。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|netHandle|[NetHandle](#class-nethandle)|是|-|数据网络句柄。|
|netCap|?[NetCapabilities](#class-netcapabilities)|否|None| **命名参数。** 存储数据网络的传输能力和承载类型。|