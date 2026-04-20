## class HuksHandle

```cangjie
public class HuksHandle {}
```

**功能：** 表示handle值。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

## class HuksImportKeyType

```cangjie
public class HuksImportKeyType {
    public static const HUKS_KEY_TYPE_PUBLIC_KEY: HuksParamValue = HuksParamValue.uint32(0)
    public static const HUKS_KEY_TYPE_PRIVATE_KEY: HuksParamValue = HuksParamValue.uint32(1)
    public static const HUKS_KEY_TYPE_KEY_PAIR: HuksParamValue = HuksParamValue.uint32(2)
}
```

**功能：** 表示导入密钥的密钥类型，默认为导入公钥，导入对称密钥时不需要该字段。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

### static const HUKS_KEY_TYPE_KEY_PAIR

```cangjie
public static const HUKS_KEY_TYPE_KEY_PAIR: HuksParamValue = HuksParamValue.uint32(2)
```

**功能：** 表示导入的密钥类型为公私钥对。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_KEY_TYPE_PRIVATE_KEY

```cangjie
public static const HUKS_KEY_TYPE_PRIVATE_KEY: HuksParamValue = HuksParamValue.uint32(1)
```

**功能：** 表示导入的密钥类型为私钥。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_KEY_TYPE_PUBLIC_KEY

```cangjie
public static const HUKS_KEY_TYPE_PUBLIC_KEY: HuksParamValue = HuksParamValue.uint32(0)
```

**功能：** 表示导入的密钥类型为公钥。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15