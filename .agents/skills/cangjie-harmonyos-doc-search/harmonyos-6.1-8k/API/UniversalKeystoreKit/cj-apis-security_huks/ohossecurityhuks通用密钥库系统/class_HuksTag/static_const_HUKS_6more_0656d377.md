### static const HUKS_TAG_RSA_PSS_SALT_LEN_TYPE

```cangjie
public static const HUKS_TAG_RSA_PSS_SALT_LEN_TYPE: UInt32 = HuksTagType.HUKS_TAG_TYPE_UINT | 30
```

**功能：** 表示rsa_pss_salt_length的类型。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_SALT

```cangjie
public static const HUKS_TAG_SALT: UInt32 = HuksTagType.HUKS_TAG_TYPE_BYTES | 12
```

**功能：** 表示密钥派生时的盐值。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_UNWRAP_ALGORITHM_SUITE

```cangjie
public static const HUKS_TAG_UNWRAP_ALGORITHM_SUITE: UInt32 = HuksTagType.HUKS_TAG_TYPE_UINT | 26
```

**功能：** 表示导入加密密钥的套件。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_USER_AUTH_TYPE

```cangjie
public static const HUKS_TAG_USER_AUTH_TYPE: UInt32 = HuksTagType.HUKS_TAG_TYPE_UINT | 304
```

**功能：** 表示用户认证类型。从[HuksUserAuthType](#class-huksuserauthtype)中选择，需要与安全访问控制类型同时设置。支持同时指定两种用户认证类型，如：安全访问控制类型指定为HUKS_SECURE_ACCESS_INVALID_NEW_BIO_ENROLL时，密钥访问认证类型可以指定以下三种： HUKS_USER_AUTH_TYPE_FACE、HUKS_USER_AUTH_TYPE_FINGERPRINT、HUKS_USER_AUTH_TYPE_FACE | HUKS_USER_AUTH_TYPE_FINGERPRINT。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

### static const HUKS_TAG_USER_ID

```cangjie
public static const HUKS_TAG_USER_ID: UInt32 = HuksTagType.HUKS_TAG_TYPE_UINT | 302
```

**功能：** 表示当前密钥属于哪个userID。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_AUTH_STORAGE_LEVEL

```cangjie
public static const HUKS_TAG_AUTH_STORAGE_LEVEL: UInt32 = HuksTagType.HUKS_TAG_TYPE_UINT | 316
```

**功能：** 表示密钥存储安全等级的tag。从[HuksAuthStorageLevel](#class-huksauthstoragelevel)中选择。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22