### static const HUKS_TAG_AE_TAG

```cangjie
public static const HUKS_TAG_AE_TAG: UInt32 = HuksTagType.HUKS_TAG_TYPE_BYTES | 10009
```

**功能：** 用于传入GCM模式中的AEAD数据的字段。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_ALG_FOR_AGREEMENT

```cangjie
public static const HUKS_TAG_ALG_FOR_AGREEMENT: UInt32 = HuksTagType.HUKS_TAG_TYPE_UINT | 19
```

**功能：** 表示密钥协商时的算法类型。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_PRIVATE_KEY_ALIAS_FOR_AGREEMENT

```cangjie
public static const HUKS_TAG_PRIVATE_KEY_ALIAS_FOR_AGREEMENT: UInt32 = HuksTagType.HUKS_TAG_TYPE_BYTES | 21
```

**功能：** 表示密钥协商时的私钥别名。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_PUBLIC_KEY_FOR_AGREEMENT

```cangjie
public static const HUKS_TAG_PUBLIC_KEY_FOR_AGREEMENT: UInt32 = HuksTagType.HUKS_TAG_TYPE_BYTES | 22
```

**功能：** 表示密钥协商时的公钥。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_AGREE_PUBLIC_KEY_IS_KEY_ALIAS

```cangjie
public static const HUKS_TAG_AGREE_PUBLIC_KEY_IS_KEY_ALIAS: UInt32 = HuksTagType.HUKS_TAG_TYPE_BOOL | 20
```

**功能：** 表示密钥协商时的公钥别名。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_ALGORITHM

```cangjie
public static const HUKS_TAG_ALGORITHM: UInt32 =  HuksTagType.HUKS_TAG_TYPE_UINT | 1
```

**功能：** 表示算法的Tag。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_ASSOCIATED_DATA

```cangjie
public static const HUKS_TAG_ASSOCIATED_DATA: UInt32 = HuksTagType.HUKS_TAG_TYPE_BYTES | 8
```

**功能：** 表示附加身份验证数据的Tag。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_ATTESTATION_CHALLENGE

```cangjie
public static const HUKS_TAG_ATTESTATION_CHALLENGE: UInt32 = HuksTagType.HUKS_TAG_TYPE_BYTES | 501
```

**功能：** 表示attestation时的挑战值。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

### static const HUKS_TAG_AUTH_TIMEOUT

```cangjie
public static const HUKS_TAG_AUTH_TIMEOUT: UInt32 = HuksTagType.HUKS_TAG_TYPE_UINT | 305
```

**功能：** 表示auth token单次有效期。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

### static const HUKS_TAG_AUTH_TOKEN

```cangjie
public static const HUKS_TAG_AUTH_TOKEN: UInt32 = HuksTagType.HUKS_TAG_TYPE_BYTES | 306
```

**功能：** 用于传入authToken的字段。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

### static const HUKS_TAG_BLOCK_MODE

```cangjie
public static const HUKS_TAG_BLOCK_MODE: UInt32 = HuksTagType.HUKS_TAG_TYPE_UINT | 6
```

**功能：** 表示加密模式的Tag。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_TAG_CHALLENGE_POS

```cangjie
public static const HUKS_TAG_CHALLENGE_POS: UInt32 = HuksTagType.HUKS_TAG_TYPE_UINT | 310
```

**功能：** 表示challenge类型为用户自定义类型时，huks产生的challenge有效长度仅为8字节连续的数据。从[HuksChallengePosition](#class-hukschallengeposition)中选择。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22