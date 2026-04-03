## class HuksCipherMode

```cangjie
public class HuksCipherMode {
    public static const HUKS_MODE_ECB: HuksParamValue = HuksParamValue.uint32(1)
    public static const HUKS_MODE_CBC: HuksParamValue = HuksParamValue.uint32(2)
    public static const HUKS_MODE_CTR: HuksParamValue = HuksParamValue.uint32(3)
    public static const HUKS_MODE_OFB: HuksParamValue = HuksParamValue.uint32(4)
    public static const HUKS_MODE_CFB: HuksParamValue = HuksParamValue.uint32(5)
    public static const HUKS_MODE_CCM: HuksParamValue = HuksParamValue.uint32(31)
    public static const HUKS_MODE_GCM: HuksParamValue = HuksParamValue.uint32(32)
}
```

**功能：** 表示加密模式。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

### static const HUKS_MODE_CBC

```cangjie
public static const HUKS_MODE_CBC: HuksParamValue = HuksParamValue.uint32(2)
```

**功能：** 表示使用CBC加密模式。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_MODE_CCM

```cangjie
public static const HUKS_MODE_CCM: HuksParamValue = HuksParamValue.uint32(31)
```

**功能：** 表示使用CCM加密模式。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_MODE_CFB

```cangjie
public static const HUKS_MODE_CFB: HuksParamValue = HuksParamValue.uint32(5)
```

**功能：** 表示使用CFB加密模式。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 19

### static const HUKS_MODE_CTR

```cangjie
public static const HUKS_MODE_CTR: HuksParamValue = HuksParamValue.uint32(3)
```

**功能：** 表示使用CTR加密模式。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_MODE_ECB

```cangjie
public static const HUKS_MODE_ECB: HuksParamValue = HuksParamValue.uint32(1)
```

**功能：** 表示使用ECB加密模式。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_MODE_GCM

```cangjie
public static const HUKS_MODE_GCM: HuksParamValue = HuksParamValue.uint32(32)
```

**功能：** 表示使用GCM加密模式。

 **系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_MODE_OFB

```cangjie
public static const HUKS_MODE_OFB: HuksParamValue = HuksParamValue.uint32(4)
```

**功能：** 表示使用OFB加密模式。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15