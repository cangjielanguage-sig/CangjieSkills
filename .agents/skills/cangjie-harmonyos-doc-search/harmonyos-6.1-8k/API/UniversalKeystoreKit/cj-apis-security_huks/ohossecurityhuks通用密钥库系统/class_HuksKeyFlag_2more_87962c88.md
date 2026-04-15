## class HuksKeyFlag

```cangjie
public class HuksKeyFlag {
    public static const HUKS_KEY_FLAG_IMPORT_KEY: UInt32 = 1
    public static const HUKS_KEY_FLAG_GENERATE_KEY: UInt32 = 2
    public static const HUKS_KEY_FLAG_AGREE_KEY: UInt32 = 3
    public static const HUKS_KEY_FLAG_DERIVE_KEY: UInt32 = 4
}
```

**功能：** 表示密钥的产生方式。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_KEY_FLAG_AGREE_KEY

```cangjie
public static const HUKS_KEY_FLAG_AGREE_KEY: UInt32 = 3
```

**功能：** 表示通过生成密钥协商接口生成的密钥。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_KEY_FLAG_DERIVE_KEY

```cangjie
public static const HUKS_KEY_FLAG_DERIVE_KEY: UInt32 = 4
```

**功能：** 表示通过生成密钥派生接口生成的密钥。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_KEY_FLAG_GENERATE_KEY

```cangjie
public static const HUKS_KEY_FLAG_GENERATE_KEY: UInt32 = 2
```

**功能：** 表示通过生成密钥接口生成的密钥。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_KEY_FLAG_IMPORT_KEY

```cangjie
public static const HUKS_KEY_FLAG_IMPORT_KEY: UInt32 = 1
```

**功能：** 表示通过导入公钥接口导入的密钥。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

## class HuksKeyGenerationType

```cangjie
public class HuksKeyGenerationType {
    public static const HUKS_KEY_GENERATE_TYPE_DEFAULT: UInt32 = 0
    public static const HUKS_KEY_GENERATE_TYPE_DERIVE: UInt32 = 1
    public static const HUKS_KEY_GENERATE_TYPE_AGREE: UInt32 = 2
}
```

**功能：** 表示生成密钥的类型。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_KEY_GENERATE_TYPE_AGREE

```cangjie
public static const HUKS_KEY_GENERATE_TYPE_AGREE: UInt32 = 2
```

**功能：** 协商生成的密钥。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_KEY_GENERATE_TYPE_DEFAULT

```cangjie
public static const HUKS_KEY_GENERATE_TYPE_DEFAULT: UInt32 = 0
```

**功能：** 默认生成的密钥。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_KEY_GENERATE_TYPE_DERIVE

```cangjie
public static const HUKS_KEY_GENERATE_TYPE_DERIVE: UInt32 = 1
```

**功能：** 派生生成的密钥。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22