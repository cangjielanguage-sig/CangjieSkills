## class HuksUnwrapSuite

```cangjie
public class HuksUnwrapSuite {
    public static const HUKS_UNWRAP_SUITE_X25519_AES_256_GCM_NO_PADDING: UInt32 = 1
    public static const HUKS_UNWRAP_SUITE_ECDH_AES_256_GCM_NO_PADDING: UInt32 = 2
}
```

**功能：** 表示导入加密密钥的算法套件。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_UNWRAP_SUITE_ECDH_AES_256_GCM_NO_PADDING

```cangjie
public static const HUKS_UNWRAP_SUITE_ECDH_AES_256_GCM_NO_PADDING: UInt32 = 2
```

**功能：** 导入加密密钥时，ECDH密钥协商后使用AES-256 GCM加密。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_UNWRAP_SUITE_X25519_AES_256_GCM_NO_PADDING

```cangjie
public static const HUKS_UNWRAP_SUITE_X25519_AES_256_GCM_NO_PADDING: UInt32 = 1
```

**功能：** 导入加密密钥时，X25519密钥协商后使用AES-256 GCM加密。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

## class HuksUserAuthType

```cangjie
public class HuksUserAuthType {
    public static const HUKS_USER_AUTH_TYPE_FINGERPRINT: UInt32 = 1 << 0
    public static const HUKS_USER_AUTH_TYPE_FACE: UInt32 = 1 << 1
    public static const HUKS_USER_AUTH_TYPE_PIN: UInt32 = 1 << 2
}
```

**功能：** 表示用户认证类型。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

### static const HUKS_USER_AUTH_TYPE_FACE

```cangjie
public static const HUKS_USER_AUTH_TYPE_FACE: UInt32 = 1 << 1
```

**功能：** 表示用户认证类型为人脸。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

### static const HUKS_USER_AUTH_TYPE_FINGERPRINT

```cangjie
public static const HUKS_USER_AUTH_TYPE_FINGERPRINT: UInt32 = 1 << 0
```

**功能：** 表示用户认证类型为指纹。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

### static const HUKS_USER_AUTH_TYPE_PIN

```cangjie
public static const HUKS_USER_AUTH_TYPE_PIN: UInt32 = 1 << 2
```

**功能：** 表示用户认证类型为PIN码。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

## enum HuksParamValue

```cangjie
public enum HuksParamValue {
    | BooleanValue(Bool)
    | Int32Value(Int32)
    | Uint32Value(UInt32)
    | Uint64Value(UInt64)
    | BytesValue(Bytes)
    | ...
}
```

**功能：** 用于表示HuksParam中value的值，支持Bool、Int32、UInt32、UInt64、Bytes格式。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### BooleanValue(Bool)

```cangjie
BooleanValue(Bool)
```

**功能：** 该字段用于传入Bool类型的value值。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### BytesValue(Bytes)

```cangjie
BytesValue(Bytes)
```

**功能：** 该字段用于传入Bytes类型的value值。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### Int32Value(Int32)

```cangjie
Int32Value(Int32)
```

**功能：** 该字段用于传入Int32类型的value值。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### Uint32Value(UInt32)

```cangjie
Uint32Value(UInt32)
```

**功能：** 该字段用于传入UInt32类型的value值。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### Uint64Value(UInt64)

```cangjie
Uint64Value(UInt64)
```

**功能：** 该字段用于传入UInt64类型的value值。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

## type Bytes

```cangjie
public type Bytes = Array<UInt8>
```

**功能：** [Bytes](#type-bytes)用于表示密钥输入输出值，支持Array\<UInt8>格式。