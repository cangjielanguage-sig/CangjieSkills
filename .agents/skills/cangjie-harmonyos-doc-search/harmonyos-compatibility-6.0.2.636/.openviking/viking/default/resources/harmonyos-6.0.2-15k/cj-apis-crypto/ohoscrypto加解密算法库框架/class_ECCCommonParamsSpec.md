## class ECCCommonParamsSpec

```cangjie
public class ECCCommonParamsSpec <: AsyKeySpec {
    public init(algName!: String, specType!: AsyKeySpecType, field!: ECField, a!: BigInt,
                b!: BigInt, g!: Point, n!: BigInt, h!: Int32)
}
```

**功能：** 密钥参数[AsyKeySpec](#interface-asykeyspec)的子类，用于指定ECC算法中公私钥包含的公共参数，随机生成公/私钥。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#func-createasykeygeneratorbyspecasykeyspec)方法创建密钥生成器。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

**父类型：**

- [AsyKeySpec](#interface-asykeyspec)

### prop a

```cangjie
public mut prop a: BigInt
```

**功能：** 指定椭圆曲线的第一个系数a。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** BigInt

**读写能力：** 可读写

**起始版本：** 19

### prop algName

```cangjie
public mut prop algName: String
```

**功能：** 指定非对称密钥的算法名称。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### prop b

```cangjie
public mut prop b: BigInt
```

**功能：** 指定椭圆曲线的第二个系数b。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** BigInt

**读写能力：** 可读写

**起始版本：** 19

### prop field

```cangjie
public mut prop field: ECField
```

**功能：** 指定椭圆曲线的域（当前只支持Fp域）。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** [ECField](#interface-ecfield)

**读写能力：** 可读写

**起始版本：** 19

### prop g

```cangjie
public mut prop g: Point
```

**功能：** 指定基点g。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** [Point](#class-point)

**读写能力：** 可读写

**起始版本：** 19

### prop h

```cangjie
public mut prop h: Int32
```

**功能：** 指定余因子h。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### prop n

```cangjie
public mut prop n: BigInt
```

**功能：** 指定基点g的阶数n。

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

### init(String, AsyKeySpecType, ECField, BigInt, BigInt, Point, BigInt, Int32)

```cangjie
public init(algName!: String, specType!: AsyKeySpecType, field!: ECField, a!: BigInt,
            b!: BigInt, g!: Point, n!: BigInt, h!: Int32)
```

**功能：** 创建ECCCommonParamsSpec实例。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-| **命名参数。** 指定非对称密钥的算法名称。|
|specType|[AsyKeySpecType](#enum-asykeyspectype)|是|-| **命名参数。** 指定密钥参数类型，用于区分公/私钥参数。|
|field|[ECField](#interface-ecfield)|是|-| **命名参数。** 指定椭圆曲线的域（当前只支持Fp域）。|
|a|BigInt|是|-| **命名参数。** 指定椭圆曲线的第一个系数a。|
|b|BigInt|是|-| **命名参数。** 指定椭圆曲线的第二个系数b。|
|g|[Point](#class-point)|是|-| **命名参数。** 指定基点g。|
|n|BigInt|是|-| **命名参数。** 指定基点g的阶数n。|
|h|Int32|是|-| **命名参数。** 指定余因子h。|