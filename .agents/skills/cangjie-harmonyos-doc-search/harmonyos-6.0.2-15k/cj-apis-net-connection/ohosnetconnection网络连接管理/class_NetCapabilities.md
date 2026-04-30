## class NetCapabilities

```cangjie
public class NetCapabilities {
    public NetCapabilities(
        public let bearerTypes: Array<NetBearType>,
        public let linkUpBandwidthKbps!: ?UInt32 = None,
        public let linkDownBandwidthKbps!: ?UInt32 = None,
        public let networkCap!: ?Array<NetCap> = None
    )
}
```

**功能：** 网络的能力集。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

### let bearerTypes

```cangjie
public let bearerTypes: Array<NetBearType>
```

**功能：** 网络类型。

**类型：** Array\<[NetBearType](#enum-netbeartype)>

**读写能力：** 只读

**起始版本：** 12

### let linkDownBandwidthKbps

```cangjie
public let linkDownBandwidthKbps: ?UInt32 = None
```

**功能：** 下行（网络到设备）带宽，0表示无法评估当前网络带宽。

**类型：** ?UInt32

**读写能力：** 只读

**起始版本：** 12

### let linkUpBandwidthKbps

```cangjie
public let linkUpBandwidthKbps: ?UInt32 = None
```

**功能：** 上行（设备到网络）带宽，0表示无法评估当前网络带宽。

**类型：** ?UInt32

**读写能力：** 只读

**起始版本：** 12

### let networkCap

```cangjie
public let networkCap: ?Array<NetCap> = None
```

**功能：** 网络具体能力。

**类型：** ?Array\<[NetCap](#enum-netcap)>

**读写能力：** 只读

**起始版本：** 12

### NetCapabilities(Array\<NetBearType>, ?UInt32, ?UInt32, ?Array\<NetCap>)

```cangjie
public NetCapabilities(
    public let bearerTypes: Array<NetBearType>,
    public let linkUpBandwidthKbps!: ?UInt32 = None,
    public let linkDownBandwidthKbps!: ?UInt32 = None,
    public let networkCap!: ?Array<NetCap> = None
)
```

**功能：** 构造NetCapabilities实例。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bearerTypes|Array\<[NetBearType](#enum-netbeartype)>|是|-|网络类型。|
|linkUpBandwidthKbps|?UInt32|否|None| **命名参数。** 上行（设备到网络）带宽，0表示无法评估当前网络带宽。|
|linkDownBandwidthKbps|?UInt32|否|None| **命名参数。** 下行（网络到设备）带宽，0表示无法评估当前网络带宽。|
|networkCap|?Array\<[NetCap](#enum-netcap)>|否|None| **命名参数。** 网络具体能力。|