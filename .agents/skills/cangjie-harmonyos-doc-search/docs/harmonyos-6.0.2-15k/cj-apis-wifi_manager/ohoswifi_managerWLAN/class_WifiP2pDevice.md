## class WifiP2pDevice

```cangjie
public class WifiP2pDevice <: ToString {
    public let deviceName: String
    public let deviceAddress: String
    public let primaryDeviceType: String
    public let deviceStatus: P2pDeviceStatus
    public let groupCapabilities: Int32
    public let deviceAddressType: ?DeviceAddressType = None
}
```

**功能：** 表示P2P设备信息。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**父类型：**

- ToString

### let deviceAddress

```cangjie
public let deviceAddress: String
```

**功能：** 设备MAC地址。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let deviceAddressType

```cangjie
public let deviceAddressType: ?DeviceAddressType = None
```

**功能：** 设备MAC地址类型。

**类型：** ?[DeviceAddressType](#enum-deviceaddresstype)

**读写能力：** 只读

**起始版本：** 19

### let deviceName

```cangjie
public let deviceName: String
```

**功能：** 设备名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let deviceStatus

```cangjie
public let deviceStatus: P2pDeviceStatus
```

**功能：** 设备状态。

**类型：** [P2pDeviceStatus](#enum-p2pdevicestatus)

**读写能力：** 只读

**起始版本：** 19

### let groupCapabilities

```cangjie
public let groupCapabilities: Int32
```

**功能：** 群组能力。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let primaryDeviceType

```cangjie
public let primaryDeviceType: String
```

**功能：** 主设备类型。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前类的字符串表示。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前类的字符串表示。|