## class HuksKeyFlag

```cangjie
public class HuksKeyFlag {
    public static const HUKS_KEY_FLAG_IMPORT_KEY: HuksParamValue = HuksParamValue.uint32(1)
    public static const HUKS_KEY_FLAG_GENERATE_KEY: HuksParamValue = HuksParamValue.uint32(2)
    public static const HUKS_KEY_FLAG_AGREE_KEY: HuksParamValue = HuksParamValue.uint32(3)
    public static const HUKS_KEY_FLAG_DERIVE_KEY: HuksParamValue = HuksParamValue.uint32(4)
}
```

**功能：** 表示密钥的产生方式。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

### static const HUKS_KEY_FLAG_AGREE_KEY

```cangjie
public static const HUKS_KEY_FLAG_AGREE_KEY: HuksParamValue = HuksParamValue.uint32(3)
```

**功能：** 表示通过生成密钥协商接口生成的密钥。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_KEY_FLAG_DERIVE_KEY

```cangjie
public static const HUKS_KEY_FLAG_DERIVE_KEY: HuksParamValue = HuksParamValue.uint32(4)
```

**功能：** 表示通过生成密钥派生接口生成的密钥。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_KEY_FLAG_GENERATE_KEY

```cangjie
public static const HUKS_KEY_FLAG_GENERATE_KEY: HuksParamValue = HuksParamValue.uint32(2)
```

**功能：** 表示通过生成密钥接口生成的密钥。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_KEY_FLAG_IMPORT_KEY

```cangjie
public static const HUKS_KEY_FLAG_IMPORT_KEY: HuksParamValue = HuksParamValue.uint32(1)
```

**功能：** 表示通过导入公钥接口导入的密钥。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

## class HuksKeyGenerateType

```cangjie
public class HuksKeyGenerateType {
    public static const HUKS_KEY_GENERATE_TYPE_DEFAULT: HuksParamValue = HuksParamValue.uint32(0)
    public static const HUKS_KEY_GENERATE_TYPE_DERIVE: HuksParamValue = HuksParamValue.uint32(1)
    public static const HUKS_KEY_GENERATE_TYPE_AGREE: HuksParamValue = HuksParamValue.uint32(2)
}
```

**功能：** 表示生成密钥的类型。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

### static const HUKS_KEY_GENERATE_TYPE_AGREE

```cangjie
public static const HUKS_KEY_GENERATE_TYPE_AGREE: HuksParamValue = HuksParamValue.uint32(2)
```

**功能：** 协商生成的密钥。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_KEY_GENERATE_TYPE_DEFAULT

```cangjie
public static const HUKS_KEY_GENERATE_TYPE_DEFAULT: HuksParamValue = HuksParamValue.uint32(0)
```

**功能：** 默认生成的密钥。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_KEY_GENERATE_TYPE_DERIVE

```cangjie
public static const HUKS_KEY_GENERATE_TYPE_DERIVE: HuksParamValue = HuksParamValue.uint32(1)
```

**功能：** 派生生成的密钥。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15