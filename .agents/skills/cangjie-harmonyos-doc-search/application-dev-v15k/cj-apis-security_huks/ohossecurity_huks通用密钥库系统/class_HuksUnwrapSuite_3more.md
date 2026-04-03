## class HuksUnwrapSuite

```cangjie
public class HuksUnwrapSuite {
    public static const HUKS_UNWRAP_SUITE_X25519_AES_256_GCM_NOPADDING: HuksParamValue = HuksParamValue.uint32(1)
    public static const HUKS_UNWRAP_SUITE_ECDH_AES_256_GCM_NOPADDING: HuksParamValue = HuksParamValue.uint32(2)
}
```

**功能：** 表示导入加密密钥的算法套件。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

### static const HUKS_UNWRAP_SUITE_ECDH_AES_256_GCM_NOPADDING

```cangjie
public static const HUKS_UNWRAP_SUITE_ECDH_AES_256_GCM_NOPADDING: HuksParamValue = HuksParamValue.uint32(2)
```

**功能：** 导入加密密钥时，ECDH密钥协商后使用AES-256 GCM加密。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_UNWRAP_SUITE_X25519_AES_256_GCM_NOPADDING

```cangjie
public static const HUKS_UNWRAP_SUITE_X25519_AES_256_GCM_NOPADDING: HuksParamValue = HuksParamValue.uint32(1)
```

**功能：** 导入加密密钥时，X25519密钥协商后使用AES-256 GCM加密。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

## class HuksUserAuthMode

```cangjie
public class HuksUserAuthMode {
    public static const HUKS_USER_AUTH_MODE_LOCAL: HuksParamValue = HuksParamValue.uint32(0)
    public static const HUKS_USER_AUTH_MODE_COAUTH: HuksParamValue = HuksParamValue.uint32(1)
}
```

**功能：** 表示用户认证模式。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 19

### static const HUKS_USER_AUTH_MODE_COAUTH

```cangjie
public static const HUKS_USER_AUTH_MODE_COAUTH: HuksParamValue = HuksParamValue.uint32(1)
```

**功能：** 跨端协同认证模式。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 19

### static const HUKS_USER_AUTH_MODE_LOCAL

```cangjie
public static const HUKS_USER_AUTH_MODE_LOCAL: HuksParamValue = HuksParamValue.uint32(0)
```

**功能：** 本地认证模式。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 19

## class HuksUserAuthType

```cangjie
public class HuksUserAuthType {
    public static const HUKS_USER_AUTH_TYPE_FINGERPRINT: HuksParamValue = HuksParamValue.uint32(1 << 0)
    public static const HUKS_USER_AUTH_TYPE_FACE: HuksParamValue = HuksParamValue.uint32(1 << 1)
    public static const HUKS_USER_AUTH_TYPE_PIN: HuksParamValue = HuksParamValue.uint32(1 << 2)
}
```

**功能：** 表示用户认证类型。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

### static const HUKS_USER_AUTH_TYPE_FACE

```cangjie
public static const HUKS_USER_AUTH_TYPE_FACE: HuksParamValue = HuksParamValue.uint32(1 << 1)
```

**功能：** 表示用户认证类型为人脸。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_USER_AUTH_TYPE_FINGERPRINT

```cangjie
public static const HUKS_USER_AUTH_TYPE_FINGERPRINT: HuksParamValue = HuksParamValue.uint32(1 << 0)
```

**功能：** 表示用户认证类型为指纹。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_USER_AUTH_TYPE_PIN

```cangjie
public static const HUKS_USER_AUTH_TYPE_PIN: HuksParamValue = HuksParamValue.uint32(1 << 2)
```

**功能：** 表示用户认证类型为PIN码。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15