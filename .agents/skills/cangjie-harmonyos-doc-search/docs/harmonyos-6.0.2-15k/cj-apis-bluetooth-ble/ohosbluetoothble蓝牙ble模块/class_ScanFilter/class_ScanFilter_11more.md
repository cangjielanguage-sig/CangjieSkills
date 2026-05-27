## class ScanFilter

```cangjie
public class ScanFilter {
    public var deviceId: ?String = None
    public var name: ?String = None
    public var serviceUuid: ?String = None
    public var serviceUuidMask: ?String = None
    public var serviceSolicitationUuid: ?String = None
    public var serviceSolicitationUuidMask: ?String = None
    public var serviceData: ?Array<Byte>= None
    public var serviceDataMask: ?Array<Byte>= None
    public var manufactureId: UInt16 = 0
    public var manufactureData: ?Array<Byte>= None
    public var manufactureDataMask: ?Array<Byte>= None
    public init()
}
```

**功能：** 扫描过滤参数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### var deviceId

```cangjie
public var deviceId: ?String = None
```

**功能：** 表示过滤的BLE设备地址，例如："XX:XX:XX:XX:XX:XX"。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var manufactureData

```cangjie
public var manufactureData: ?Array<Byte> = None
```

**功能：** 表示过滤包含该制造商相关数据的设备，例如：[0x1F,0x2F,0x3F]。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** ?Array\<Byte>

**读写能力：** 可读写

**起始版本：** 19

### var manufactureDataMask

```cangjie
public var manufactureDataMask: ?Array<Byte> = None
```

**功能：** 表示过滤包含该制造商相关数据掩码的设备，例如：[0xFF,0xFF,0xFF]。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** ?Array\<Byte>

**读写能力：** 可读写

**起始版本：** 19

### var manufactureId

```cangjie
public var manufactureId: UInt16 = 0
```

**功能：** 表示过滤包含该制造商ID的设备，例如：0x0006。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** UInt16

**读写能力：** 可读写

**起始版本：** 19

### var name

```cangjie
public var name: ?String = None
```

**功能：** 表示过滤的BLE设备名。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var serviceData

```cangjie
public var serviceData: ?Array<Byte> = None
```

**功能：** 表示过滤包含该服务相关数据的设备，例如：[0x90,0x00,0xF1,0xF2]。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** ?Array\<Byte>

**读写能力：** 可读写

**起始版本：** 19

### var serviceDataMask

```cangjie
public var serviceDataMask: ?Array<Byte> = None
```

**功能：** 表示过滤包含该服务相关数据掩码的设备，例如：[0xFF,0xFF,0xFF,0xFF]。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** ?Array\<Byte>

**读写能力：** 可读写

**起始版本：** 19

### var serviceSolicitationUuid

```cangjie
public var serviceSolicitationUuid: ?String = None
```

**功能：** 表示过滤包含该UUID服务请求的设备，例如：00001888-0000-1000-8000-00805F9B34FB。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var serviceSolicitationUuidMask

```cangjie
public var serviceSolicitationUuidMask: ?String = None
```

**功能：** 表示过滤包含该UUID服务请求掩码的设备，例如：FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var serviceUuid

```cangjie
public var serviceUuid: ?String = None
```

**功能：** 表示过滤包含该UUID服务的设备，例如：00001888-0000-1000-8000-00805f9b34fb。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19