## class HuksChallengePosition

```cangjie
public class HuksChallengePosition {
    public static const HUKS_CHALLENGE_POS_0: HuksParamValue = HuksParamValue.uint32(0)
    public static const HUKS_CHALLENGE_POS_1: HuksParamValue = HuksParamValue.uint32(1)
    public static const HUKS_CHALLENGE_POS_2: HuksParamValue = HuksParamValue.uint32(2)
    public static const HUKS_CHALLENGE_POS_3: HuksParamValue = HuksParamValue.uint32(3)
}
```

**功能：** 表示challenge类型为用户自定义类型时，生成的challenge有效长度仅为8字节连续的数据，且仅支持4种位置 。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

### static const HUKS_CHALLENGE_POS_0

```cangjie
public static const HUKS_CHALLENGE_POS_0: HuksParamValue = HuksParamValue.uint32(0)
```

**功能：** 表示0~7字节为当前密钥的有效challenge。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_CHALLENGE_POS_1

```cangjie
public static const HUKS_CHALLENGE_POS_1: HuksParamValue = HuksParamValue.uint32(1)
```

**功能：** 表示8~15字节为当前密钥的有效challenge。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_CHALLENGE_POS_2

```cangjie
public static const HUKS_CHALLENGE_POS_2: HuksParamValue = HuksParamValue.uint32(2)
```

**功能：** 表示16~23字节为当前密钥的有效challenge。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_CHALLENGE_POS_3

```cangjie
public static const HUKS_CHALLENGE_POS_3: HuksParamValue = HuksParamValue.uint32(3)
```

**功能：** 表示24~31字节为当前密钥的有效challenge。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15