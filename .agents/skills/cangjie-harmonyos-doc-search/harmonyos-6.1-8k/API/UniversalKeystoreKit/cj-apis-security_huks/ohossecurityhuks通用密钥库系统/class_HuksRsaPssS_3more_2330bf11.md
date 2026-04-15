## class HuksRsaPssSaltLenType

```cangjie
public class HuksRsaPssSaltLenType {
    public static const HUKS_RSA_PSS_SALT_LEN_DIGEST: UInt32 = 0
    public static const HUKS_RSA_PSS_SALT_LEN_MAX: UInt32 = 1
}
```

**功能：** 表示Rsa在签名验签、padding为pss时需指定的salt_len类型。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_RSA_PSS_SALT_LEN_DIGEST

```cangjie
public static const HUKS_RSA_PSS_SALT_LEN_DIGEST: UInt32 = 0
```

**功能：** 表示以摘要长度设置salt_len。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_RSA_PSS_SALT_LEN_MAX

```cangjie
public static const HUKS_RSA_PSS_SALT_LEN_MAX: UInt32 = 1
```

**功能：** 表示以最大长度设置salt_len。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

## class HuksSecureSignType

```cangjie
public class HuksSecureSignType {
    public static const HUKS_SECURE_SIGN_WITH_AUTH_INFO: UInt32 = 1
}
```

**功能：** 表示生成或导入密钥时，指定该密钥的签名类型。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

### static const HUKS_SECURE_SIGN_WITH_AUTH_INFO

```cangjie
public static const HUKS_SECURE_SIGN_WITH_AUTH_INFO: UInt32 = 1
```

**功能：** 表示签名类型为携带认证信息。生成或导入密钥时指定该字段，则在使用密钥进行签名时，对待签名的数据添加认证信息后进行签名。

> **注意：**
>
> 携带的认证信息包含身份信息，开发者需在其隐私声明中对此身份信息的使用目的、存留策略和销毁方式进行说明。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

## class HuksSessionHandle

```cangjie
public class HuksSessionHandle {
    public var handle: HuksHandleId
    public var challenge: Bytes
}
```

**功能：** huks Handle结构体。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### var challenge

```cangjie
public var challenge: Bytes
```

**功能：** 表示[initSession](#func-initsessionstring-huksoptions)操作之后获取到的challenge信息。

**类型：** Bytes

**读写能力：** 可读写

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### var handle

```cangjie
public var handle: HuksHandleId
```

**功能：** 表示handle值。

**类型：** [HuksHandleId](#class-hukshandleid)

**读写能力：** 可读写

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22