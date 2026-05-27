## struct AssetAccessibility

```cangjie
public struct AssetAccessibility {
    public static const DEVICE_POWERED_ON: UInt32 = 0
    public static const DEVICE_FIRST_UNLOCKED: UInt32 = 1
    public static const DEVICE_UNLOCKED: UInt32 = 2
}
```

**功能：** 关键资产基于锁屏状态的访问控制类型。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### static const DEVICE_FIRST_UNLOCKED

```cangjie
public static const DEVICE_FIRST_UNLOCKED: UInt32 = 1
```

**功能：** 首次解锁后可访问。未设置锁屏密码时，等同于开机后可访问。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const DEVICE_POWERED_ON

```cangjie
public static const DEVICE_POWERED_ON: UInt32 = 0
```

**功能：** 开机后可访问。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const DEVICE_UNLOCKED

```cangjie
public static const DEVICE_UNLOCKED: UInt32 = 2
```

**功能：** 解锁状态时可访问。未设置锁屏密码时，等同于开机后可访问。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

## struct AssetAuthType

```cangjie
public struct AssetAuthType {
    public static const NONE: UInt32 = 0x00
    public static const ANY: UInt32 = 0xFF
}
```

**功能：** 关键资产支持的用户认证类型。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### static const ANY

```cangjie
public static const ANY: UInt32 = 0xFF
```

**功能：** 任意一种用户认证方式（PIN码、人脸、指纹等）通过后，均可访问关键资产。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const NONE

```cangjie
public static const NONE: UInt32 = 0x00
```

**功能：** 访问关键资产前无需用户认证。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

## struct AssetConflictResolution

```cangjie
public struct AssetConflictResolution {
    public static const OVERWRITE: UInt32 = 0
    public static const THROW_ERROR: UInt32 = 1
}
```

**功能：** 新增关键资产时的冲突（如：别名相同）处理策略。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### static const OVERWRITE

```cangjie
public static const OVERWRITE: UInt32 = 0
```

**功能：** 覆盖原有的关键资产。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const THROW_ERROR

```cangjie
public static const THROW_ERROR: UInt32 = 1
```

**功能：** 抛出异常，由业务进行后续处理。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

## struct AssetOperationType

```cangjie
public struct AssetOperationType {
    public static const NEED_SYNC: UInt32 = 0
    public static const NEED_LOGOUT: UInt32 = 1
}
```

**功能：** 附属的操作类型。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### static const NEED_LOGOUT

```cangjie
public static const NEED_LOGOUT: UInt32 = 1
```

**功能：** 需要进行登出操作。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const NEED_SYNC

```cangjie
public static const NEED_SYNC: UInt32 = 0
```

**功能：** 需要进行同步操作。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19