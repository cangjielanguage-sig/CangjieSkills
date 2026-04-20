## class GattPermissions

```cangjie
public class GattPermissions {
    public var read: Bool
    public var readEncrypted: Bool
    public var readEncryptedMitm: Bool
    public var write: Bool
    public var writeEncrypted: Bool
    public var writeEncryptedMitm: Bool
    public var writeSigned: Bool
    public var writeSignedMitm: Bool
    public init (
        read!: Bool = true,
        readEncrypted!: Bool = false,
        readEncryptedMitm!: Bool = false,
        write!: Bool = true,
        writeEncrypted!: Bool = false,
        writeEncryptedMitm!: Bool = false,
        writeSigned!: Bool = false,
        writeSignedMitm!: Bool = false
    )
}
```

**功能：** 描述读写GATT特征值或描述符需具备的权限。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var read

```cangjie
public var read: Bool
```

**功能：** 是否允许读取该特征值或描述符内容。

true表示允许，false表示不允许。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var readEncrypted

```cangjie
public var readEncrypted: Bool
```

**功能：** 读取该特征值或描述符内容是否需要加密。

true表示需要加密后，方可读取内容，false表示不需要普通方式加密。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var readEncryptedMitm

```cangjie
public var readEncryptedMitm: Bool
```

**功能：** 读取该特征值或描述符内容是否需要防中间人攻击的加密。

防中间人攻击表示操作需要经过认证，防止数据被第三方篡改。true表示需要防中间人攻击的加密后才能读取内容，false表示不需要防中间人攻击的加密。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var write

```cangjie
public var write: Bool
```

**功能：** 是否允许写入该特征值或描述符内容。

true表示允许，false表示不允许。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var writeEncrypted

```cangjie
public var writeEncrypted: Bool
```

**功能：** 写入该特征值或描述符内容是否需要加密。

true表示需要加密后，方可写入内容，false表示不需要普通方式加密。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var writeEncryptedMitm

```cangjie
public var writeEncryptedMitm: Bool
```

**功能：** 写入该特征值或描述符内容是否需要防中间人攻击的加密。

true表示需要防中间人攻击的加密后才能写入内容，false表示不需要防中间人攻击的加密。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var writeSigned

```cangjie
public var writeSigned: Bool
```

**功能：** 写入该特征值或描述符内容是否需要经过签名处理。

true表示内容需要签名处理后方可写入，false表示不需要签名处理。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var writeSignedMitm

```cangjie
public var writeSignedMitm: Bool
```

**功能：** 写入该特征值或描述符内容是否需要经过防中间人攻击方式的签名处理。

true表示需要防中间人攻击方式的签名处理后方可写入，false表示不需要以防中间人攻击方式签名处理。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22