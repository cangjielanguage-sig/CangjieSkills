## class RSACommonParamsSpec

```cangjie
public class RSACommonParamsSpec <: AsyKeySpec {
    public init(algName!: String, specType!: AsyKeySpecType, n!: BigInt)
}
```

**功能：** 密钥参数[AsyKeySpec](#interface-asykeyspec)的子类，用于指定RSA算法中公私钥包含的公共参数，随机生成公/私钥。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#func-createasykeygeneratorbyspecasykeyspec)方法创建密钥生成器。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

**父类型：**

- [AsyKeySpec](#interface-asykeyspec)

### prop algName

```cangjie
public mut prop algName: String
```

**功能：** 指定非对称密钥的算法名称。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### prop n

```cangjie
public mut prop n: BigInt
```

**功能：** 指定模数n。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** BigInt

**读写能力：** 可读写

**起始版本：** 19

### prop specType

```cangjie
public mut prop specType: AsyKeySpecType
```

**功能：** 指定密钥参数类型，用于区分公/私钥参数。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** [AsyKeySpecType](#enum-asykeyspectype)

**读写能力：** 可读写

**起始版本：** 19

### init(String, AsyKeySpecType, BigInt)

```cangjie
public init(algName!: String, specType!: AsyKeySpecType, n!: BigInt)
```

**功能：** 创建RSACommonParamsSpec实例。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-| **命名参数。** 指定非对称密钥的算法名称。|
|specType|[AsyKeySpecType](#enum-asykeyspectype)|是|-| **命名参数。** 指定密钥参数类型，用于区分公/私钥参数。|
|n|BigInt|是|-| **命名参数。** 指定模数n。|