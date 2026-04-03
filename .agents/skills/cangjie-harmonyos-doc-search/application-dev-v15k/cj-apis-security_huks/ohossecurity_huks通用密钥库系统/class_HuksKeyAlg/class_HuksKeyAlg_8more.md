## class HuksKeyAlg

```cangjie
public class HuksKeyAlg {
    public static const HUKS_ALG_RSA: HuksParamValue = HuksParamValue.uint32(1)
    public static const HUKS_ALG_ECC: HuksParamValue = HuksParamValue.uint32(2)
    public static const HUKS_ALG_DSA: HuksParamValue = HuksParamValue.uint32(3)
    public static const HUKS_ALG_AES: HuksParamValue = HuksParamValue.uint32(20)
    public static const HUKS_ALG_HMAC: HuksParamValue = HuksParamValue.uint32(50)
    public static const HUKS_ALG_HKDF: HuksParamValue = HuksParamValue.uint32(51)
    public static const HUKS_ALG_PBKDF2: HuksParamValue = HuksParamValue.uint32(52)
    public static const HUKS_ALG_ECDH: HuksParamValue = HuksParamValue.uint32(100)
    public static const HUKS_ALG_X25519: HuksParamValue = HuksParamValue.uint32(101)
    public static const HUKS_ALG_ED25519: HuksParamValue = HuksParamValue.uint32(102)
    public static const HUKS_ALG_DH: HuksParamValue = HuksParamValue.uint32(103)
    public static const HUKS_ALG_SM2: HuksParamValue = HuksParamValue.uint32(150)
    public static const HUKS_ALG_SM3: HuksParamValue = HuksParamValue.uint32(151)
    public static const HUKS_ALG_SM4: HuksParamValue = HuksParamValue.uint32(152)
    public static const HUKS_ALG_DES: HuksParamValue = HuksParamValue.uint32(160)
    public static const HUKS_ALG_3DES: HuksParamValue = HuksParamValue.uint32(161)
    public static const HUKS_ALG_CMAC: HuksParamValue = HuksParamValue.uint32(162)
}
```

**功能：** 表示密钥使用的算法。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

### static const HUKS_ALG_3DES

```cangjie
public static const HUKS_ALG_3DES: HuksParamValue = HuksParamValue.uint32(161)
```

**功能：** 表示使用3DES算法。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 19

### static const HUKS_ALG_AES

```cangjie
public static const HUKS_ALG_AES: HuksParamValue = HuksParamValue.uint32(20)
```

**功能：** 表示使用AES算法。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_ALG_CMAC

```cangjie
public static const HUKS_ALG_CMAC: HuksParamValue = HuksParamValue.uint32(162)
```

**功能：** 表示使用CMAC算法。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 19

### static const HUKS_ALG_DES

```cangjie
public static const HUKS_ALG_DES: HuksParamValue = HuksParamValue.uint32(160)
```

**功能：** 表示使用DES算法。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 19

### static const HUKS_ALG_DH

```cangjie
public static const HUKS_ALG_DH: HuksParamValue = HuksParamValue.uint32(103)
```

**功能：** 表示使用DH算法。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_ALG_DSA

```cangjie
public static const HUKS_ALG_DSA: HuksParamValue = HuksParamValue.uint32(3)
```

**功能：** 表示使用DSA算法。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_ALG_ECC

```cangjie
public static const HUKS_ALG_ECC: HuksParamValue = HuksParamValue.uint32(2)
```

**功能：** 表示使用ECC算法。

**系统能力：** SystemCapability.Security.Huks.Extension

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15