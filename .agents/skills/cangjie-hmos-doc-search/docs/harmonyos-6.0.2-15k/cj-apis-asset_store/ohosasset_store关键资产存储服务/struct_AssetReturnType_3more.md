## struct AssetReturnType

```cangjie
public struct AssetReturnType {
    public static const ALL: UInt32 = 0
    public static const ATTRIBUTES: UInt32 = 1
}
```

**功能：** 关键资产查询返回的结果类型。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### static const ALL

```cangjie
public static const ALL: UInt32 = 0
```

**功能：** 返回关键资产明文及属性。查询单条关键资产明文时，需设置此类型。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const ATTRIBUTES

```cangjie
public static const ATTRIBUTES: UInt32 = 1
```

**功能：** 返回关键资产属性，不含关键资产明文。批量查询关键资产属性时，需设置此类型。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

## struct AssetSyncType

```cangjie
public struct AssetSyncType {
    public static const NEVER: UInt32 = 0
    public static const THIS_DEVICE: UInt32 = 1 << 0
    public static const TRUSTED_DEVICE: UInt32 = 1 << 1
    public static const TRUSTED_ACCOUNT: UInt32 = 1 << 2
}
```

**功能：** 关键资产支持的同步类型。

> **说明：**
>
> 本字段属于能力预埋，当前不支持同步。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### static const NEVER

```cangjie
public static const NEVER: UInt32 = 0
```

**功能：** 不允许同步关键资产。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const THIS_DEVICE

```cangjie
public static const THIS_DEVICE: UInt32 = 1 << 0
```

**功能：** 只在本设备进行同步，如仅在本设备还原的备份场景。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const TRUSTED_ACCOUNT

```cangjie
public static const TRUSTED_ACCOUNT: UInt32 = 1 << 2
```

**功能：** 只在登录可信账号的设备间进行同步，如云同步场景。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const TRUSTED_DEVICE

```cangjie
public static const TRUSTED_DEVICE: UInt32 = 1 << 1
```

**功能：** 只在可信设备间进行同步，如克隆场景。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

## struct AssetTagType

```cangjie
public struct AssetTagType {
    public static const BOOL: UInt32 = 0x01 << 28
    public static const NUMBER: UInt32 = 0x02 << 28
    public static const BYTES: UInt32 = 0x03 << 28
}
```

**功能：** 关键资产属性支持的数据类型。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### static const BOOL

```cangjie
public static const BOOL: UInt32 = 0x01 << 28
```

**功能：** 标识关键资产属性对应的数据类型是布尔类型。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const BYTES

```cangjie
public static const BYTES: UInt32 = 0x03 << 28
```

**功能：** 标识关键资产属性对应的数据类型是字节数组。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const NUMBER

```cangjie
public static const NUMBER: UInt32 = 0x02 << 28
```

**功能：** 标识关键资产属性对应的数据类型是整型。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19