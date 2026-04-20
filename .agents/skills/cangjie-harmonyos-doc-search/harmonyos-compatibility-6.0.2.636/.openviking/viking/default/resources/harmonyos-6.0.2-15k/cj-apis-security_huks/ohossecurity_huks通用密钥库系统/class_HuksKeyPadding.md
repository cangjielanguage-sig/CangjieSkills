## class HuksKeyPadding

```cangjie
public class HuksKeyPadding {
    public static const HUKS_PADDING_NONE: HuksParamValue = HuksParamValue.uint32(0)
    public static const HUKS_PADDING_OAEP: HuksParamValue = HuksParamValue.uint32(1)
    public static const HUKS_PADDING_PSS: HuksParamValue = HuksParamValue.uint32(2)
    public static const HUKS_PADDING_PKCS1_V1_5: HuksParamValue = HuksParamValue.uint32(3)
    public static const HUKS_PADDING_PKCS5: HuksParamValue = HuksParamValue.uint32(4)
    public static const HUKS_PADDING_PKCS7: HuksParamValue = HuksParamValue.uint32(5)
    public static const HUKS_PADDING_ISO_IEC_9796_2: HuksParamValue = HuksParamValue.uint32(6)
    public static const HUKS_PADDING_ISO_IEC_9797_1: HuksParamValue = HuksParamValue.uint32(7)
}
```

**功能：** 表示补齐算法。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

### static const HUKS_PADDING_ISO_IEC_9796_2

```cangjie
public static const HUKS_PADDING_ISO_IEC_9796_2: HuksParamValue = HuksParamValue.uint32(6)
```

**功能：** 表示使用ISO_IEC_9796_2补齐算法。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 19

### static const HUKS_PADDING_ISO_IEC_9797_1

```cangjie
public static const HUKS_PADDING_ISO_IEC_9797_1: HuksParamValue = HuksParamValue.uint32(7)
```

**功能：** 表示使用ISO_IEC_9797_1补齐算法。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 19

### static const HUKS_PADDING_NONE

```cangjie
public static const HUKS_PADDING_NONE: HuksParamValue = HuksParamValue.uint32(0)
```

**功能：** 表示不使用补齐算法。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_PADDING_OAEP

```cangjie
public static const HUKS_PADDING_OAEP: HuksParamValue = HuksParamValue.uint32(1)
```

**功能：** 表示使用OAEP补齐算法。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_PADDING_PKCS1_V1_5

```cangjie
public static const HUKS_PADDING_PKCS1_V1_5: HuksParamValue = HuksParamValue.uint32(3)
```

**功能：** 表示使用PKCS1_V1_5补齐算法。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_PADDING_PKCS5

```cangjie
public static const HUKS_PADDING_PKCS5: HuksParamValue = HuksParamValue.uint32(4)
```

**功能：** 表示使用PKCS5补齐算法。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_PADDING_PKCS7

```cangjie
public static const HUKS_PADDING_PKCS7: HuksParamValue = HuksParamValue.uint32(5)
```

**功能：** 表示使用PKCS7补齐算法。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_PADDING_PSS

```cangjie
public static const HUKS_PADDING_PSS: HuksParamValue = HuksParamValue.uint32(2)
```

**功能：** 表示使用PSS补齐算法。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15