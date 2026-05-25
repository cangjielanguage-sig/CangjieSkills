## class RSAKeyPairSpec

```cangjie
public class RSAKeyPairSpec <: AsyKeySpec {
    public init(params!: RSACommonParamsSpec, sk!: BigInt, pk!: BigInt)
}
```

**功能：** 密钥参数[AsyKeySpec](#interface-asykeyspec)的子类，用于指定RSA算法中公私钥包含的全量参数。

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

### prop params

```cangjie
public mut prop params: RSACommonParamsSpec
```

**功能：** 指定RSA算法中公私钥都包含的公共参数。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** [RSACommonParamsSpec](#class-rsacommonparamsspec)

**读写能力：** 可读写

**起始版本：** 19

### prop pk

```cangjie
public mut prop pk: BigInt
```

**功能：** 指定RSA算法的公钥pk。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** BigInt

**读写能力：** 可读写

**起始版本：** 19

### prop sk

```cangjie
public mut prop sk: BigInt
```

**功能：** 指定RSA算法的公钥sk。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** BigInt

**读写能力：** 可读写

**起始版本：** 19

### prop specType

```cangjie
public mut prop specType: AsyKeySpecType
```

**功能：** 指定密钥参数类型。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** [AsyKeySpecType](#enum-asykeyspectype)

**读写能力：** 可读写

**起始版本：** 19

### init(RSACommonParamsSpec, BigInt, BigInt)

```cangjie
public init(params!: RSACommonParamsSpec, sk!: BigInt, pk!: BigInt)
```

**功能：** 创建RSAKeyPairSpec实例。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|params|[RSACommonParamsSpec](#class-rsacommonparamsspec)|是|-| **命名参数。** 指定RSA算法中公私钥都包含的公共参数。|
|sk|BigInt|是|-| **命名参数。** 指定RSA算法的私钥sk。|
|pk|BigInt|是|-| **命名参数。** 指定RSA算法的公钥pk。|