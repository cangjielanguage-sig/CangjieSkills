## class DHPubKeySpec

```cangjie
public class DHPubKeySpec <: AsyKeySpec {
    public init(params!: DHCommonParamsSpec, pk!: BigInt)
}
```

**功能：** 密钥参数[AsyKeySpec](#interface-asykeyspec)的子类，用于指定DH算法中公钥包含的参数。

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
public mut prop params: DHCommonParamsSpec
```

**功能：** 指定DH算法中公私钥都包含的公共参数。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** [DHCommonParamsSpec](#class-dhcommonparamsspec)

**读写能力：** 可读写

**起始版本：** 19

### prop pk

```cangjie
public mut prop pk: BigInt
```

**功能：** 指定DH算法的公钥pk。

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

### init(DHCommonParamsSpec, BigInt)

```cangjie
public init(params!: DHCommonParamsSpec, pk!: BigInt)
```

**功能：** 创建DHPubKeySpec实例。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|params|[DHCommonParamsSpec](#class-dhcommonparamsspec)|是|-| **命名参数。** 指定DH算法中公私钥都包含的公共参数。|
|pk|BigInt|是|-| **命名参数。** 指定DH算法的公钥pk。|