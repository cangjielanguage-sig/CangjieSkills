## class HuksTagType

```cangjie
public class HuksTagType {
    public static const HUKS_TAG_TYPE_INVALID: UInt32 = 0 << 28
    public static const HUKS_TAG_TYPE_INT: UInt32 = 1 << 28
    public static const HUKS_TAG_TYPE_UINT: UInt32 = 2 << 28
    public static const HUKS_TAG_TYPE_ULONG: UInt32 = 3 << 28
    public static const HUKS_TAG_TYPE_BOOL: UInt32 = 4 << 28
    public static const HUKS_TAG_TYPE_BYTES: UInt32 = 5 << 28
}
```

**功能：** 表示Tag的数据类型。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

### static const HUKS_TAG_TYPE_BOOL

```cangjie
public static const HUKS_TAG_TYPE_BOOL: UInt32 = 4 << 28
```

**功能：** 表示该Tag的数据类型为boolean。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** UInt32

**起始版本：** 15

### static const HUKS_TAG_TYPE_BYTES

```cangjie
public static const HUKS_TAG_TYPE_BYTES: UInt32 = 5 << 28
```

**功能：** 表示该Tag的数据类型为Uint8Array。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** UInt32

**起始版本：** 15

### static const HUKS_TAG_TYPE_INT

```cangjie
public static const HUKS_TAG_TYPE_INT: UInt32 = 1 << 28
```

**功能：** 表示该Tag的数据类型为UInt32。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** UInt32

**起始版本：** 15

### static const HUKS_TAG_TYPE_INVALID

```cangjie
public static const HUKS_TAG_TYPE_INVALID: UInt32 = 0 << 28
```

**功能：** 表示非法的Tag类型。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** UInt32

**起始版本：** 15

### static const HUKS_TAG_TYPE_UINT

```cangjie
public static const HUKS_TAG_TYPE_UINT: UInt32 = 2 << 28
```

**功能：** 表示该Tag的数据类型为UInt32。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** UInt32

**起始版本：** 15

### static const HUKS_TAG_TYPE_ULONG

```cangjie
public static const HUKS_TAG_TYPE_ULONG: UInt32 = 3 << 28
```

**功能：** 表示该Tag的数据类型为bigint。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** UInt32

**起始版本：** 15