## class HuksReturnResult

```cangjie
public class HuksReturnResult {
    public HuksReturnResult(
        public let outData: Option<Array<UInt8>>,
        public let properties: Option<Array<HuksParam>>,
        public let certChains: Option<Array<String>>
    )
}
```

**功能：** 表示接口返回的结果，存放返回数据。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

### let certChains

```cangjie
public let certChains: Option<Array<String>>
```

**功能：** 表示证书链数据。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** Option\<Array\<String>>

**读写能力：** 只读

**起始版本：** 15

### let outData

```cangjie
public let outData: Option<Array<UInt8>>
```

**功能：** 表示输出数据。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** Option\<Array\<UInt8>>

**读写能力：** 只读

**起始版本：** 15

### let properties

```cangjie
public let properties: Option<Array<HuksParam>>
```

**功能：** 表示属性信息。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** Option\<Array\<[HuksParam](#class-huksparam)>>

**读写能力：** 只读

**起始版本：** 15

### HuksReturnResult(Option\<Array\<UInt8>>, Option\<Array\<HuksParam>>, Option\<Array\<String>>)

```cangjie
public HuksReturnResult(
    public let outData: Option<Array<UInt8>>,
    public let properties: Option<Array<HuksParam>>,
    public let certChains: Option<Array<String>>
)
```

**功能：** 构建HuksReturnResult实例。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|outData|Option\<Array\<UInt8>>|是|表示输出数据。|
|properties|Option\<Array\<[HuksParam](#class-huksparam)>>|是|表示属性信息。|
|certChains|Option\<Array\<String>>|是|表示证书链数据。|

## class HuksRsaPssSaltLenType

```cangjie
public class HuksRsaPssSaltLenType {
    public static const HUKS_RSA_PSS_SALT_LEN_DIGEST: HuksParamValue = HuksParamValue.uint32(0)
    public static const HUKS_RSA_PSS_SALT_LEN_MAX: HuksParamValue = HuksParamValue.uint32(1)
}
```

**功能：** 表示Rsa在签名或者验签且padding为pss时，需指定的salt_len类型。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

### static const HUKS_RSA_PSS_SALT_LEN_DIGEST

```cangjie
public static const HUKS_RSA_PSS_SALT_LEN_DIGEST: HuksParamValue = HuksParamValue.uint32(0)
```

**功能：** 表示以摘要长度设置salt_len。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

### static const HUKS_RSA_PSS_SALT_LEN_MAX

```cangjie
public static const HUKS_RSA_PSS_SALT_LEN_MAX: HuksParamValue = HuksParamValue.uint32(1)
```

**功能：** 表示以最大长度设置salt_len。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15

## class HuksSecureSignType

```cangjie
public class HuksSecureSignType {
    public static const HUKS_SECURE_SIGN_WITH_AUTHINFO: HuksParamValue = HuksParamValue.uint32(1)
}
```

**功能：** 表示生成或导入密钥时，指定该密钥的签名类型。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

### static const HUKS_SECURE_SIGN_WITH_AUTHINFO

```cangjie
public static const HUKS_SECURE_SIGN_WITH_AUTHINFO: HuksParamValue = HuksParamValue.uint32(1)
```

**功能：** 表示签名类型为携带认证信息。生成或导入密钥时指定该字段，则在使用密钥进行签名时，对待签名的数据添加认证信息后进行签名。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**起始版本：** 15