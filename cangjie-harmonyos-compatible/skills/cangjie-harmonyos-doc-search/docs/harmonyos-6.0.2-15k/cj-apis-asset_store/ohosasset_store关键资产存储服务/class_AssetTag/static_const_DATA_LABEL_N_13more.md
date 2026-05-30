### static const DATA_LABEL_NORMAL_4

```cangjie
public static const DATA_LABEL_NORMAL_4: UInt32 = AssetTagType.BYTES | 0x33
```

**功能：** 关键资产附属信息，内容由业务自定义且无完整性保护。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const DATA_LABEL_NORMAL_LOCAL_1

```cangjie
public static const DATA_LABEL_NORMAL_LOCAL_1: UInt32 = AssetTagType.BYTES | 0x34
```

**功能：** 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const DATA_LABEL_NORMAL_LOCAL_2

```cangjie
public static const DATA_LABEL_NORMAL_LOCAL_2: UInt32 = AssetTagType.BYTES | 0x35
```

**功能：** 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const DATA_LABEL_NORMAL_LOCAL_3

```cangjie
public static const DATA_LABEL_NORMAL_LOCAL_3: UInt32 = AssetTagType.BYTES | 0x36
```

**功能：** 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const DATA_LABEL_NORMAL_LOCAL_4

```cangjie
public static const DATA_LABEL_NORMAL_LOCAL_4: UInt32 = AssetTagType.BYTES | 0x37
```

**功能：** 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const IS_PERSISTENT

```cangjie
public static const IS_PERSISTENT: UInt32 = AssetTagType.BOOL | 0x11
```

**功能：** 在应用卸载时是否需要保留关键资产。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const OPERATION_TYPE

```cangjie
public static const OPERATION_TYPE: UInt32 = AssetTagType.NUMBER | 0x46
```

**功能：** 附加的操作类型。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const REQUIRE_PASSWORD_SET

```cangjie
public static const REQUIRE_PASSWORD_SET: UInt32 = AssetTagType.BOOL | 0x04
```

**功能：** 是否仅在设置了锁屏密码的情况下，可访问关键资产。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const RETURN_LIMIT

```cangjie
public static const RETURN_LIMIT: UInt32 = AssetTagType.NUMBER | 0x41
```

**功能：** 关键资产查询返回的结果数量。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const RETURN_OFFSET

```cangjie
public static const RETURN_OFFSET: UInt32 = AssetTagType.NUMBER | 0x42
```

**功能：** 关键资产查询返回的结果偏移量。用于分批查询场景，指定从第几个开始返回。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const RETURN_ORDERED_BY

```cangjie
public static const RETURN_ORDERED_BY: UInt32 = AssetTagType.NUMBER | 0x43
```

**功能：** 关键资产查询返回的结果排序依据，仅支持按照附属信息排序。默认按照关键资产新增的顺序返回。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const RETURN_TYPE

```cangjie
public static const RETURN_TYPE: UInt32 = AssetTagType.NUMBER | 0x40
```

**功能：** 关键资产查询返回的结果类型。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19

### static const SECRET

```cangjie
public static const SECRET: UInt32 = AssetTagType.BYTES | 0x01
```

**功能：** 关键资产明文。

**系统能力：** SystemCapability.Security.Asset

**类型：** UInt32

**起始版本：** 19