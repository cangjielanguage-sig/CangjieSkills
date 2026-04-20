## class CcmParamsSpec

```cangjie
public class CcmParamsSpec <: ParamsSpec {
    public var authTag: DataBlob
    public var aad: DataBlob
    public var iv: DataBlob
    public init(algName: String, iv: DataBlob, aad: DataBlob, authTag: DataBlob)
}
```

**功能：** 加解密参数[ParamsSpec](#class-paramsspec)的子类，用于在对称加解密时作为[initialize()](#func-initializecryptomode-key-paramsspec)方法的参数。

适用于CCM模式。

> **说明：**
>
> 传入[initialize()](#func-initializecryptomode-key-paramsspec)方法前需要指定其algName属性（来源于父类[ParamsSpec](#class-paramsspec)）。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

**父类型：**

- [ParamsSpec](#class-paramsspec)

### var aad

```cangjie
public var aad: DataBlob
```

**功能：** 指明加解密参数aad，长度为8字节。

**类型：** [DataBlob](#class-datablob)

**读写能力：** 可读写

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

### var authTag

```cangjie
public var authTag: DataBlob
```

**功能：** 指定加解密参数authTag，长度为12字节。

在CCM模式加密时，需从[doFinal()](#func-dofinaldatablob)输出的[DataBlob](#class-datablob)末尾提取12字节，作为[initialize()](#func-initializecryptomode-key-paramsspec)方法的参数[CcmParamsSpec](#class-ccmparamsspec)中的authTag。

**类型：** [DataBlob](#class-datablob)

**读写能力：** 可读写

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

### var iv

```cangjie
public var iv: DataBlob
```

**功能：** 指明加解密参数iv，长度为7字节。

**类型：** [DataBlob](#class-datablob)

**读写能力：** 可读写

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

### init(String, DataBlob, DataBlob, DataBlob)

```cangjie
public init(algName: String, iv: DataBlob, aad: DataBlob, authTag: DataBlob)
```

**功能：** 创建CcmParamsSpec实例。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-|指明对称加解密参数的算法模式。|
|iv|[DataBlob](#class-datablob)|是|-|指明加解密参数iv，长度为7字节。|
|aad|[DataBlob](#class-datablob)|是|-|指明加解密参数aad，长度为8字节。|
|authTag|[DataBlob](#class-datablob)|是|-|指定加解密参数authTag，长度为12字节。<br/>在CCM模式加密时，需从[doFinal()](#func-dofinaldatablob)输出的[DataBlob](#class-datablob)末尾提取12字节，作为[initialize()](#func-initializecryptomode-key-paramsspec)方法的参数[CcmParamsSpec](#class-ccmparamsspec)中的authTag。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ccm = CcmParamsSpec("CcmParamsSpec", DataBlob(Array<UInt8>(7, repeat: 1)), DataBlob(Array<UInt8>(8, repeat: 1)), DataBlob(Array<UInt8>(12, repeat: 1)))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```