## class HuksKeyPurpose

```cangjie
public class HuksKeyPurpose {
    public static const HUKS_KEY_PURPOSE_ENCRYPT: HuksParamValue = HuksParamValue.uint32(1)
    public static const HUKS_KEY_PURPOSE_DECRYPT: HuksParamValue = HuksParamValue.uint32(2)
    public static const HUKS_KEY_PURPOSE_SIGN: HuksParamValue = HuksParamValue.uint32(4)
    public static const HUKS_KEY_PURPOSE_VERIFY: HuksParamValue = HuksParamValue.uint32(8)
    public static const HUKS_KEY_PURPOSE_DERIVE: HuksParamValue = HuksParamValue.uint32(16)
    public static const HUKS_KEY_PURPOSE_WRAP: HuksParamValue = HuksParamValue.uint32(32)
    public static const HUKS_KEY_PURPOSE_UNWRAP: HuksParamValue = HuksParamValue.uint32(64)
    public static const HUKS_KEY_PURPOSE_MAC: HuksParamValue = HuksParamValue.uint32(128)
    public static const HUKS_KEY_PURPOSE_AGREE: HuksParamValue = HuksParamValue.uint32(256)
}
```

**功能：** 表示密钥用途。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

### static const HUKS_KEY_PURPOSE_AGREE

```cangjie
public static const HUKS_KEY_PURPOSE_AGREE: HuksParamValue = HuksParamValue.uint32(256)
```

**功能：** 表示密钥用于进行密钥协商。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_KEY_PURPOSE_DECRYPT

```cangjie
public static const HUKS_KEY_PURPOSE_DECRYPT: HuksParamValue = HuksParamValue.uint32(2)
```

**功能：** 表示密钥用于对密文进行解密操作。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_KEY_PURPOSE_DERIVE

```cangjie
public static const HUKS_KEY_PURPOSE_DERIVE: HuksParamValue = HuksParamValue.uint32(16)
```

**功能：** 表示密钥用于派生密钥。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_KEY_PURPOSE_ENCRYPT

```cangjie
public static const HUKS_KEY_PURPOSE_ENCRYPT: HuksParamValue = HuksParamValue.uint32(1)
```

**功能：** 表示密钥用于对明文进行加密操作。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_KEY_PURPOSE_MAC

```cangjie
public static const HUKS_KEY_PURPOSE_MAC: HuksParamValue = HuksParamValue.uint32(128)
```

**功能：** 表示密钥用于生成mac消息验证码。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_KEY_PURPOSE_SIGN

```cangjie
public static const HUKS_KEY_PURPOSE_SIGN: HuksParamValue = HuksParamValue.uint32(4)
```

**功能：** 表示密钥用于对数据进行签名。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_KEY_PURPOSE_UNWRAP

```cangjie
public static const HUKS_KEY_PURPOSE_UNWRAP: HuksParamValue = HuksParamValue.uint32(64)
```

**功能：** 表示密钥加密导入。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_KEY_PURPOSE_VERIFY

```cangjie
public static const HUKS_KEY_PURPOSE_VERIFY: HuksParamValue = HuksParamValue.uint32(8)
```

**功能：** 表示密钥用于验证签名后的数据。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15