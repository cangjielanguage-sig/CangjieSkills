### static const HUKS_TAG_CHALLENGE_TYPE

```cangjie
public static const HUKS_TAG_CHALLENGE_TYPE: UInt32 = HuksTagType.HUKS_TAG_TYPE_UINT | 309
```

**功能：** 表示密钥使用时生成的challenge类型。从[HuksChallengeType](#class-hukschallengetype)中选择。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

### static const HUKS_TAG_DERIVE_KEY_SIZE

```cangjie
public static const HUKS_TAG_DERIVE_KEY_SIZE: UInt32 = HuksTagType.HUKS_TAG_TYPE_UINT | 24
```

**功能：** 表示派生密钥的大小。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG

```cangjie
public static const HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG: UInt32 = HuksTagType.HUKS_TAG_TYPE_UINT | 29
```

**功能：** 表示派生密钥/协商密钥的存储类型。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_DIGEST

```cangjie
public static const HUKS_TAG_DIGEST: UInt32 = HuksTagType.HUKS_TAG_TYPE_UINT | 4
```

**功能：** 表示摘要算法的Tag。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_IMPORT_KEY_TYPE

```cangjie
public static const HUKS_TAG_IMPORT_KEY_TYPE: UInt32 =  HuksTagType.HUKS_TAG_TYPE_UINT | 25
```

**功能：** 表示导入的密钥类型。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_INFO

```cangjie
public static const HUKS_TAG_INFO: UInt32 = HuksTagType.HUKS_TAG_TYPE_BYTES | 11
```

**功能：** 表示密钥派生时的info。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_IS_ALLOWED_WRAP

```cangjie
public static const HUKS_TAG_IS_ALLOWED_WRAP: UInt32 = HuksTagType.HUKS_TAG_TYPE_BOOL | 1003
```

**功能：** 预留。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_IS_KEY_ALIAS

```cangjie
public static const HUKS_TAG_IS_KEY_ALIAS: UInt32 = HuksTagType.HUKS_TAG_TYPE_BOOL | 1001
```

**功能：** 表示是否使用生成key时传入的别名的Tag。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_ITERATION

```cangjie
public static const HUKS_TAG_ITERATION: UInt32 = HuksTagType.HUKS_TAG_TYPE_UINT | 14
```

**功能：** 表示密钥派生时的迭代次数。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_IV

```cangjie
public static const HUKS_TAG_IV: UInt32 = HuksTagType.HUKS_TAG_TYPE_BYTES | 10
```

**功能：** 表示密钥初始化的向量。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_KEY

```cangjie
public static const HUKS_TAG_KEY: UInt32 = HuksTagType.HUKS_TAG_TYPE_BYTES | 10006
```

**功能：** 预留。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_KEY_ALIAS

```cangjie
public static const HUKS_TAG_KEY_ALIAS: UInt32 = HuksTagType.HUKS_TAG_TYPE_BYTES | 23
```

**功能：** 表示密钥别名。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_KEY_AUTH_ACCESS_TYPE

```cangjie
public static const HUKS_TAG_KEY_AUTH_ACCESS_TYPE: UInt32 = HuksTagType.HUKS_TAG_TYPE_UINT | 307
```

**功能：** 表示安全访问控制类型。从[HuksAuthAccessType](#class-huksauthaccesstype)中选择，需要和用户认证类型同时设置。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22