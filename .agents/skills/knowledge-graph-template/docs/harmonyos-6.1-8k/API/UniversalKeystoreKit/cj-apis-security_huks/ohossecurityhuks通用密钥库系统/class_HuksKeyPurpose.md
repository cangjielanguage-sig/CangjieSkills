## class HuksKeyPurpose

```cangjie
public class HuksKeyPurpose {
    public static const HUKS_KEY_PURPOSE_ENCRYPT: UInt32 = 1
    public static const HUKS_KEY_PURPOSE_DECRYPT: UInt32 = 2
    public static const HUKS_KEY_PURPOSE_SIGN: UInt32 = 4
    public static const HUKS_KEY_PURPOSE_VERIFY: UInt32 = 8
    public static const HUKS_KEY_PURPOSE_DERIVE: UInt32 = 16
    public static const HUKS_KEY_PURPOSE_WRAP: UInt32 = 32
    public static const HUKS_KEY_PURPOSE_UNWRAP: UInt32 = 64
    public static const HUKS_KEY_PURPOSE_MAC: UInt32 = 128
    public static const HUKS_KEY_PURPOSE_AGREE: UInt32 = 256
}
```

**功能：** 表示密钥用途。

一个密钥仅能用于单类用途，不能既用于加解密又用于签名验签。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_KEY_PURPOSE_AGREE

```cangjie
public static const HUKS_KEY_PURPOSE_AGREE: UInt32 = 256
```

**功能：** 表示密钥用于进行密钥协商。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_KEY_PURPOSE_DECRYPT

```cangjie
public static const HUKS_KEY_PURPOSE_DECRYPT: UInt32 = 2
```

**功能：** 表示密钥用于对密文进行解密操作。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_KEY_PURPOSE_DERIVE

```cangjie
public static const HUKS_KEY_PURPOSE_DERIVE: UInt32 = 16
```

**功能：** 表示密钥用于派生密钥。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_KEY_PURPOSE_ENCRYPT

```cangjie
public static const HUKS_KEY_PURPOSE_ENCRYPT: UInt32 = 1
```

**功能：** 表示密钥用于对明文进行加密操作。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_KEY_PURPOSE_MAC

```cangjie
public static const HUKS_KEY_PURPOSE_MAC: UInt32 = 128
```

**功能：** 表示密钥用于生成mac消息验证码。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_KEY_PURPOSE_SIGN

```cangjie
public static const HUKS_KEY_PURPOSE_SIGN: UInt32 = 4
```

**功能：** 表示密钥用于对数据进行签名。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_KEY_PURPOSE_UNWRAP

```cangjie
public static const HUKS_KEY_PURPOSE_UNWRAP: UInt32 = 64
```

**功能：** 表示密钥加密导入。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_KEY_PURPOSE_VERIFY

```cangjie
public static const HUKS_KEY_PURPOSE_VERIFY: UInt32 = 8
```

**功能：** 表示密钥用于验证签名后的数据。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_KEY_PURPOSE_WRAP

```cangjie
public static const HUKS_KEY_PURPOSE_WRAP: UInt32 = 32
```

**功能：** 表示密钥用于加密导出。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22