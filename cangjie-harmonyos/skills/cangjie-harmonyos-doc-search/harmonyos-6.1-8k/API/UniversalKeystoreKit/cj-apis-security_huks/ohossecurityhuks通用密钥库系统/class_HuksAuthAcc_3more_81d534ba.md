## class HuksAuthAccessType

```cangjie
public class HuksAuthAccessType {
    public static const HUKS_AUTH_ACCESS_INVALID_CLEAR_PASSWORD: UInt32 = 1 << 0
    public static const HUKS_AUTH_ACCESS_INVALID_NEW_BIO_ENROLL: UInt32 = 1 << 1
}
```

**功能：** 表示安全访问控制类型。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

### static const HUKS_AUTH_ACCESS_INVALID_CLEAR_PASSWORD

```cangjie
public static const HUKS_AUTH_ACCESS_INVALID_CLEAR_PASSWORD: UInt32 = 1 << 0
```

**功能：** 表示安全访问控制类型为清除密码后密钥无效。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

### static const HUKS_AUTH_ACCESS_INVALID_NEW_BIO_ENROLL

```cangjie
public static const HUKS_AUTH_ACCESS_INVALID_NEW_BIO_ENROLL: UInt32 = 1 << 1
```

**功能：** 表示安全访问控制类型为新录入生物特征后密钥无效。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

## class HuksAuthStorageLevel

```cangjie
public class HuksAuthStorageLevel {
    public static const HUKS_AUTH_STORAGE_LEVEL_DE: UInt32 = 0
    public static const HUKS_AUTH_STORAGE_LEVEL_CE: UInt32 = 1
    public static const HUKS_AUTH_STORAGE_LEVEL_ECE: UInt32 = 2
}
```

**功能：** 表示生成或导入密钥时，指定该密钥的存储安全等级。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_AUTH_STORAGE_LEVEL_CE

```cangjie
public static const HUKS_AUTH_STORAGE_LEVEL_CE: UInt32 = 1
```

**功能：** 表示密钥仅在首次解锁后可访问。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_AUTH_STORAGE_LEVEL_DE

```cangjie
public static const HUKS_AUTH_STORAGE_LEVEL_DE: UInt32 = 0
```

**功能：** 表示密钥仅在开机后可访问。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_AUTH_STORAGE_LEVEL_ECE

```cangjie
public static const HUKS_AUTH_STORAGE_LEVEL_ECE: UInt32 = 2
```

**功能：** 表示密钥仅在解锁状态时可访问。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

## class HuksChallengePosition

```cangjie
public class HuksChallengePosition {
    public static const HUKS_CHALLENGE_POS_0: UInt32 = 0
    public static const HUKS_CHALLENGE_POS_1: UInt32 = 1
    public static const HUKS_CHALLENGE_POS_2: UInt32 = 2
    public static const HUKS_CHALLENGE_POS_3: UInt32 = 3
}
```

**功能：** 表示challenge类型为用户自定义类型时，生成的challenge有效长度仅为8字节连续的数据，且仅支持4种位置。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

### static const HUKS_CHALLENGE_POS_0

```cangjie
public static const HUKS_CHALLENGE_POS_0: UInt32 = 0
```

**功能：** 表示0~7字节为当前密钥的有效challenge。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

### static const HUKS_CHALLENGE_POS_1

```cangjie
public static const HUKS_CHALLENGE_POS_1: UInt32 = 1
```

**功能：** 表示8~15字节为当前密钥的有效challenge。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

### static const HUKS_CHALLENGE_POS_2

```cangjie
public static const HUKS_CHALLENGE_POS_2: UInt32 = 2
```

**功能：** 表示16~23字节为当前密钥的有效challenge。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

### static const HUKS_CHALLENGE_POS_3

```cangjie
public static const HUKS_CHALLENGE_POS_3: UInt32 = 3
```

**功能：** 表示24~31字节为当前密钥的有效challenge。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22