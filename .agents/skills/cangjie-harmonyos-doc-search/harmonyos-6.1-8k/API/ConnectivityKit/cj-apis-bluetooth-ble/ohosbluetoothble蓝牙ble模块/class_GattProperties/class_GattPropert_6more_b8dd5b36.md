## class GattProperties

```cangjie
public class GattProperties {
    public var write: Bool
    public var writeNoResponse: Bool
    public var read: Bool
    public var notify: Bool
    public var indicate: Bool
    public init(
        write!: Bool = true,
        writeNoResponse!: Bool = true,
        read!: Bool = true,
        notify!: Bool = false,
        indicate!: Bool = false,
        broadcast!: Bool = false,
        authenticatedSignedWrite!: Bool = false,
        extendedProperties!: Bool = false
    )
}
```

**功能：** 描述GATT特征值支持的属性。决定了特征值内容和描述符如何被使用和访问。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var indicate

```cangjie
public var indicate: Bool
```

**功能：** 该特征值是否支持向对端设备指示特征值内容。

true表示支持，对端设备需要回复确认，false表示不支持。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var notify

```cangjie
public var notify: Bool
```

**功能：** 该特征值是否支持主动向对端设备通知特征值内容。

true表示支持，且对端设备不需要回复确认，false表示不支持。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var read

```cangjie
public var read: Bool
```

**功能：** 该特征值是否支持读取操作。

true表示支持，false表示不支持。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var write

```cangjie
public var write: Bool
```

**功能：** 该特征值是否支持写入操作。

true表示支持，且被写入时需要回复对端设备，false表示不支持。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var writeNoResponse

```cangjie
public var writeNoResponse: Bool
```

**功能：** 该特征值是否支持写入操作。

true表示支持，且被写入时无需回复对端设备，false表示不支持。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22