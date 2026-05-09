## class IvParamsSpec

```cangjie
public class IvParamsSpec <: ParamsSpec {
    public var iv: DataBlob
    public init(algName: String, iv: DataBlob)
}
```

**功能：** 加解密参数[ParamsSpec](#class-paramsspec)的子类，用于在对称加解密时作为[initialize()](#func-initializecryptomode-key-paramsspec)方法的参数。

适用于CBC、CTR、OFB、CFB、Poly1305这些需要iv作为参数的加解密模式。

> **说明：**
> 
> 传入[initialize()](#func-initializecryptomode-key-paramsspec)方法前需要指定其algName属性（来源于父类[ParamsSpec](#class-paramsspec)）。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

**父类型：**

- [ParamsSpec](#class-paramsspec)

### var iv

```cangjie
public var iv: DataBlob
```

**功能：** 指明加解密参数iv。常见取值如下：

AES的CBC\|CTR\|OFB\|CFB模式：iv长度为16字节。

3DES的CBC\|OFB\|CFB模式：iv长度为8字节。

SM4的CBC\|CTR\|OFB\|CFB模式：iv长度为16字节。

**类型：** [DataBlob](#class-datablob)

**读写能力：** 可读写

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

### init(String, DataBlob)

```cangjie
public init(algName: String, iv: DataBlob)
```

**功能：** 创建IvParamsSpec实例。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-|指明对称加解密参数的算法模式。|
|iv|[DataBlob](#class-datablob)|是|-|指明加解密参数iv。常见取值如下：<br/>- AES的CBC\|CTR\|OFB\|CFB模式：iv长度为16字节。<br/>- 3DES的CBC\|OFB\|CFB模式：iv长度为8字节。<br/>- SM4的CBC\|CTR\|OFB\|CFB模式：iv长度为16字节。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let iv = IvParamsSpec("IvParamsSpec", DataBlob(Array<UInt8>(8, repeat: 1)))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```