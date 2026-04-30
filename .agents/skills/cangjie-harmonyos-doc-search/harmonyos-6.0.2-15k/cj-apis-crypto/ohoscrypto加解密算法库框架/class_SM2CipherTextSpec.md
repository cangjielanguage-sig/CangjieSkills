## class SM2CipherTextSpec

```cangjie
public class SM2CipherTextSpec {
    public init(xCoordinate!: BigInt, yCoordinate!: BigInt, cipherTextData!: Array<UInt8>, hashData!: Array<UInt8>)
}
```

**功能：** SM2密文参数，使用SM2密文格式转换函数进行格式转换时，需要用到此对象。可以通过指定此参数，生成符合国密标准的ASN.1格式的SM2密文，反之，也可以从ASN.1格式的SM2密文中获取具体参数。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### prop cipherTextData

```cangjie
public mut prop cipherTextData: Array<UInt8>
```

**功能：** 密文。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** Array\<UInt8>

**读写能力：** 可读写

**起始版本：** 19

### prop hashData

```cangjie
public mut prop hashData: Array<UInt8>
```

**功能：** 杂凑值。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** Array\<UInt8>

**读写能力：** 可读写

**起始版本：** 19

### prop xCoordinate

```cangjie
public mut prop xCoordinate: BigInt
```

**功能：** x分量。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** BigInt

**读写能力：** 可读写

**起始版本：** 19

### prop yCoordinate

```cangjie
public mut prop yCoordinate: BigInt
```

**功能：** y分量。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** BigInt

**读写能力：** 可读写

**起始版本：** 19

### init(BigInt, BigInt, Array\<UInt8>, Array\<UInt8>)

```cangjie
public init(xCoordinate!: BigInt, yCoordinate!: BigInt, cipherTextData!: Array<UInt8>, hashData!: Array<UInt8>)
```

**功能：** 创建SM2CipherTextSpec实例。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|xCoordinate|BigInt|是|-| **命名参数。** x分量。|
|yCoordinate|BigInt|是|-| **命名参数。** y分量。|
|cipherTextData|Array\<UInt8>|是|-| **命名参数。** 密文。|
|hashData|Array\<UInt8>|是|-| **命名参数。** 杂凑值。|