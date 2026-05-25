## class NetCapabilities

```cangjie
public class NetCapabilities {
    public var bearerTypes: Array<NetBearType>
    public var linkUpBandwidthKbps: UInt32
    public var linkDownBandwidthKbps: UInt32
    public var networkCap: Array<NetCap>
    public init(bearerTypes: Array<NetBearType>, linkUpBandwidthKbps!: UInt32 = 0, linkDownBandwidthKbps!: UInt32 = 0,
        networkCap!: Array<NetCap> = Array<NetCap>())
}
```

**功能：** 网络的能力集。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var bearerTypes

```cangjie
public var bearerTypes: Array<NetBearType>
```

**功能：** 网络类型。数组里面只包含了一种网络类型。

**类型：** Array\<[NetBearType](#enum-netbeartype)>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var linkDownBandwidthKbps

```cangjie
public var linkDownBandwidthKbps: UInt32
```

**功能：** 下行（网络到设备）带宽，单位(kb/s)。0表示无法评估当前网络带宽。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var linkUpBandwidthKbps

```cangjie
public var linkUpBandwidthKbps: UInt32
```

**功能：** 上行（设备到网络）带宽，单位(kb/s)。0表示无法评估当前网络带宽。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var networkCap

```cangjie
public var networkCap: Array<NetCap>
```

**功能：** 网络具体能力。

**类型：** Array\<[NetCap](#enum-netcap)>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### init(Array\<NetBearType>, UInt32, UInt32, Array\<NetCap>)

```cangjie
public init(bearerTypes: Array<NetBearType>, linkUpBandwidthKbps!: UInt32 = 0, linkDownBandwidthKbps!: UInt32 = 0,
    networkCap!: Array<NetCap> = Array<NetCap>())
```

**功能：** 网络的能力集。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bearerTypes|Array\<[NetBearType](#enum-netbeartype)>|是|-|网络类型。数组里面只包含了一种网络类型。|
|linkUpBandwidthKbps|UInt32|否|0|**命名参数。** 上行（设备到网络）带宽，单位(kb/s)。0表示无法评估当前网络带宽。|
|linkDownBandwidthKbps|UInt32|否|0|**命名参数。** 下行（网络到设备）带宽，单位(kb/s)。0表示无法评估当前网络带宽。|
|networkCap|Array\<[NetCap](#enum-netcap)>|否|Array\<NetCap>()|**命名参数。** 网络具体能力。|