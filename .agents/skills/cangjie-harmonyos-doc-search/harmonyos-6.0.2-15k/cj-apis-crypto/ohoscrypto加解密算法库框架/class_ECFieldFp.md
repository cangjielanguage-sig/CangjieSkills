## class ECFieldFp

```cangjie
public class ECFieldFp <: ECField {
    public init(fieldType!: String, p!: BigInt)
}
```

**功能：** 指定椭圆曲线素数域。该结构体是[ECField](#interface-ecfield)的子类。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

**父类型：**

- [ECField](#interface-ecfield)

### prop fieldType

```cangjie
public mut prop fieldType: String
```

**功能：** 指定椭圆曲线域的类型，当前只支持"Fp"。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### prop p

```cangjie
public mut prop p: BigInt

```

**功能：** 指定素数p。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** BigInt

**读写能力：** 可读写

**起始版本：** 19

### init(String, BigInt)

```cangjie
public init(fieldType!: String, p!: BigInt)
```

**功能：** 创建ECFieldFp实例。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fieldType|String|是|-| **命名参数。** 指定椭圆曲线域的类型，当前只支持"Fp"。|
|p|BigInt|是|-| **命名参数。** 指定素数p。|