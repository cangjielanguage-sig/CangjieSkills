## class ScanFilter

```cangjie
public class ScanFilter {
    public var deviceId: String
    public var name: String
    public var serviceUUID: String
    public var serviceUUIDMask: String
    public var serviceSolicitationUUID: String
    public var serviceSolicitationUUIDMask: String
    public var serviceData: Array<Byte>
    public var serviceDataMask: Array<Byte>
    public var manufactureId: UInt16
    public var manufactureData: Array<Byte>
    public var manufactureDataMask: Array<Byte>
    public init(
        deviceId!: String = "",
        name!: String = "",
        serviceUUID!: String = "",
        serviceUUIDMask!: String = "",
        serviceSolicitationUUID!: String = "",
        serviceSolicitationUUIDMask!: String = "",
        serviceData!: Array<Byte> = [],
        serviceDataMask!: Array<Byte> = [],
        manufactureId!: UInt16 = 0,
        manufactureData!: Array<Byte> = [],
        manufactureDataMask!: Array<Byte> = []
    )
}
```

**功能：** 扫描BLE广播的过滤条件，只有符合该条件的广播报文才会上报。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var deviceId

```cangjie
public var deviceId: String
```

**功能：** 过滤该BLE设备地址的广播报文。例如："XX:XX:XX:XX:XX:XX"。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var manufactureData

```cangjie
public var manufactureData: Array<Byte>
```

**功能：** 过滤包含该制造商标识符的广播报文。例如：0x0006。

**类型：** Array\<Byte>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var manufactureDataMask

```cangjie
public var manufactureDataMask: Array<Byte>
```

**功能：** 搭配manufactureId过滤器使用，过滤包含该制造商数据的广播报文。例如：[0x1F,0x2F,0x3F]。

**类型：** Array\<Byte>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var manufactureId

```cangjie
public var manufactureId: UInt16
```

**功能：** 表示过滤包含该制造商ID的设备，例如：0x0006。

**类型：** UInt16

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var name

```cangjie
public var name: String
```

**功能：** 过滤该BLE设备名称的广播报文。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var serviceData

```cangjie
public var serviceData: Array<Byte>
```

**功能：** 过滤包含该服务数据的广播报文。例如：[0x90,0x00,0xF1,0xF2]。

**类型：** Array\<Byte>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var serviceDataMask

```cangjie
public var serviceDataMask: Array<Byte>
```

**功能：** 搭配serviceData过滤器使用，可设置过滤部分服务数据。例如：[0xFF,0xFF,0xFF,0xFF]。

**类型：** Array\<Byte>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var serviceSolicitationUUID

```cangjie
public var serviceSolicitationUUID: String
```

**功能：** 过滤包含该服务请求UUID的广播报文。例如：00001888-0000-1000-8000-00805F9B34FB。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var serviceSolicitationUUIDMask

```cangjie
public var serviceSolicitationUUIDMask: String
```

**功能：** 搭配serviceSolicitationUUID过滤器使用，可设置过滤部分服务请求UUID。例如：FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22