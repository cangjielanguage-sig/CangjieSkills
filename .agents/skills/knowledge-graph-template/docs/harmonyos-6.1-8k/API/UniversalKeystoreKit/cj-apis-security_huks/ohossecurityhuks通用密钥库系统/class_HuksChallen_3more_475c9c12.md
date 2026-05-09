## class HuksChallengeType

```cangjie
public class HuksChallengeType {
    public static const HUKS_CHALLENGE_TYPE_NORMAL: UInt32 = 0
    public static const HUKS_CHALLENGE_TYPE_CUSTOM: UInt32 = 1
    public static const HUKS_CHALLENGE_TYPE_NONE: UInt32 = 2
}
```

**功能：** 表示密钥使用时生成challenge的类型。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

### static const HUKS_CHALLENGE_TYPE_CUSTOM

```cangjie
public static const HUKS_CHALLENGE_TYPE_CUSTOM: UInt32 = 1
```

**功能：** 表示challenge为用户自定义类型。支持使用多个密钥仅一次认证。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

### static const HUKS_CHALLENGE_TYPE_NONE

```cangjie
public static const HUKS_CHALLENGE_TYPE_NONE: UInt32 = 2
```

**功能：** 表示免challenge类型。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

### static const HUKS_CHALLENGE_TYPE_NORMAL

```cangjie
public static const HUKS_CHALLENGE_TYPE_NORMAL: UInt32 = 0
```

**功能：** 表示challenge为普通类型，默认32字节。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

## class HuksCipherMode

```cangjie
public class HuksCipherMode {
    public static const HUKS_MODE_ECB: UInt32 = 1
    public static const HUKS_MODE_CBC: UInt32 = 2
    public static const HUKS_MODE_CTR: UInt32 = 3
    public static const HUKS_MODE_OFB: UInt32 = 4
    public static const HUKS_MODE_CCM: UInt32 = 31
    public static const HUKS_MODE_GCM: UInt32 = 32
}
```

**功能：** 表示加密模式。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_MODE_CBC

```cangjie
public static const HUKS_MODE_CBC: UInt32 = 2
```

**功能：** 表示使用CBC加密模式。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_MODE_CCM

```cangjie
public static const HUKS_MODE_CCM: UInt32 = 31
```

**功能：** 表示使用CCM加密模式。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_MODE_CTR

```cangjie
public static const HUKS_MODE_CTR: UInt32 = 3
```

**功能：** 表示使用CTR加密模式。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_MODE_ECB

```cangjie
public static const HUKS_MODE_ECB: UInt32 = 1
```

**功能：** 表示使用ECB加密模式。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_MODE_GCM

```cangjie
public static const HUKS_MODE_GCM: UInt32 = 32
```

**功能：** 表示使用GCM加密模式。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_MODE_OFB

```cangjie
public static const HUKS_MODE_OFB: UInt32 = 4
```

**功能：** 表示使用OFB加密模式。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

## class HuksHandleId

```cangjie
public class HuksHandleId {}
```

**功能：** 加密handle的id。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22