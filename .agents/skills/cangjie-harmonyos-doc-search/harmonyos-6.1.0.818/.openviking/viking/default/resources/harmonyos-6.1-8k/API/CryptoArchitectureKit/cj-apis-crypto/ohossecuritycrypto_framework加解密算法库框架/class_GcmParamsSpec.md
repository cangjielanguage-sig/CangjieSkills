## class GcmParamsSpec

```cangjie
public class GcmParamsSpec <: ParamsSpec {
    public var aad: DataBlob
    public var iv: DataBlob
    public var authTag: DataBlob
    public init(algName: String, iv: DataBlob, aad: DataBlob, authTag: DataBlob)
}
```

**功能：** 加解密参数[ParamsSpec](#class-paramsspec)的子类，用于在对称加解密时作为[initialize()](#func-initializecryptomode-key-paramsspec)方法的参数。

适用于GCM模式。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

**父类型：**

- [ParamsSpec](#class-paramsspec)

> **说明：**
> 
> 1. 传入[initialize()](#func-initializecryptomode-key-paramsspec)方法前需要指定其algName属性（来源于父类[ParamsSpec](#class-paramsspec)）。
> 2. 对于1~16字节长度的iv，加解密算法库无额外限制，但结果取决于底层openssl的支持情况。
> 3. 当aad参数不需要使用或aad长度为0时，可以将aad的data属性设置为一个空的Array\<UInt8>，来构造GcmParamsSpec，写法为aad: { data: Array\<UInt8>() }。

### var aad

```cangjie
public var aad: DataBlob
```

**功能：** 指明加解密参数aad，长度为0~INT32_MAX字节，常用为16字节。

**类型：** [DataBlob](#class-datablob)

**读写能力：** 可读写

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

### var authTag

```cangjie
public var authTag: DataBlob
```

**功能：** 指明加解密参数authTag，长度为16字节。

采用GCM模式加密时，需从[doFinal()](#func-dofinaldatablob)输出的[DataBlob](#class-datablob)中提取末尾16字节，作为[initialize()](#func-initializecryptomode-key-paramsspec)方法中GcmParamsSpec的authTag。

**类型：** [DataBlob](#class-datablob)

**读写能力：** 可读写

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

### var iv

```cangjie
public var iv: DataBlob
```

**功能：** 指明加解密参数iv，长度为1~16字节，常用为12字节。

**类型：** [DataBlob](#class-datablob)

**读写能力：** 可读写

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

### init(String, DataBlob, DataBlob, DataBlob)

```cangjie
public init(algName: String, iv: DataBlob, aad: DataBlob, authTag: DataBlob)
```

**功能：** 创建GcmParamsSpec实例。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-|指明对称加解密参数的算法模式。|
|iv|[DataBlob](#class-datablob)|是|-|指明加解密参数iv，长度为1~16字节，常用为12字节。|
|aad|[DataBlob](#class-datablob)|是|-|指明加解密参数aad，长度为0~INT32_MAX字节，常用为16字节。|
|authTag|[DataBlob](#class-datablob)|是|-|指明加解密参数authTag，长度为16字节。<br/>采用GCM模式加密时，需从[doFinal()](#func-dofinaldatablob)输出的[DataBlob](#class-datablob)中提取末尾16字节，作为[initialize()](#func-initializecryptomode-key-paramsspec)方法中GcmParamsSpec的authTag。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let gcm = GcmParamsSpec("GcmParamsSpec", DataBlob(Array<UInt8>(12, repeat: 1)), DataBlob(Array<UInt8>(8, repeat: 1)), DataBlob(Array<UInt8>(16, repeat: 1)))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```