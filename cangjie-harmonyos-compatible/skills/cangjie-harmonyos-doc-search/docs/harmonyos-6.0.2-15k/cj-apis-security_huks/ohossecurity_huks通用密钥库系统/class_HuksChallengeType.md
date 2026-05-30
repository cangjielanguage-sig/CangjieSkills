## class HuksChallengeType

```cangjie
public class HuksChallengeType {
    public static const HUKS_CHALLENGE_TYPE_NORMAL: HuksParamValue = HuksParamValue.uint32(0)
    public static const HUKS_CHALLENGE_TYPE_CUSTOM: HuksParamValue = HuksParamValue.uint32(1)
    public static const HUKS_CHALLENGE_TYPE_NONE: HuksParamValue = HuksParamValue.uint32(2)
}
```

**功能：** 表示密钥使用时生成challenge的类型。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

### static const HUKS_CHALLENGE_TYPE_CUSTOM

```cangjie
public static const HUKS_CHALLENGE_TYPE_CUSTOM: HuksParamValue = HuksParamValue.uint32(1)
```

**功能：** 表示challenge为用户自定义类型。支持使用多个密钥仅一次认证。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_CHALLENGE_TYPE_NONE

```cangjie
public static const HUKS_CHALLENGE_TYPE_NONE: HuksParamValue = HuksParamValue.uint32(2)
```

**功能：** 表示免challenge类型。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_CHALLENGE_TYPE_NORMAL

```cangjie
public static const HUKS_CHALLENGE_TYPE_NORMAL: HuksParamValue = HuksParamValue.uint32(0)
```

**功能：** 表示challenge为普通类型，默认32字节。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15