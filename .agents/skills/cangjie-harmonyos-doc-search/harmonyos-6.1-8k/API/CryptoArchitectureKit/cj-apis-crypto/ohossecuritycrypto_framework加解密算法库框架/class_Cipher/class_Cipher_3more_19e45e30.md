## class Cipher

```cangjie
public class Cipher {}
```

**功能：** 提供加解密的算法操作功能，按序调用本类中的[initialize()](#func-initializecryptomode-key-paramsspec)、[update()](#func-updatedatablob)、[doFinal()](#func-dofinaldatablob)方法，可以实现对称加密/对称解密/非对称加密/非对称解密。

一次完整的加/解密流程在对称加密和非对称加密中略有不同：

- 对称加解密：initialize为必选，update为可选（且允许多次update加/解密大数据），doFinal为必选；doFinal结束后可以重新initialize开始新一轮加/解密流程。
- RSA、SM2非对称加解密：initialize为必选，不支持update操作，doFinal为必选（允许连续多次doFinal加/解密大数据）；RSA不支持重复initialize，切换加解密模式或填充方式时，需要重新创建Cipher对象。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

### prop algName

```cangjie
public prop algName: String
```

**功能：** 加解密生成器指定的算法名称。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

### func initialize(CryptoMode, Key, ?ParamsSpec)

```cangjie
public func initialize(opMode: CryptoMode, key: Key, params: ?ParamsSpec): Unit
```

**功能：** 初始化加解密的[Cipher](#class-cipher)对象。initialize、update、doFinal为三段式接口，需要成组使用。其中initialize和doFinal必选，update可选。

必须在使用[createCipher](#func-createcipherstring)创建[Cipher](#class-cipher)实例后，才能使用本函数。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|opMode|[CryptoMode](#enum-cryptomode)|是|-|加密或者解密模式。|
|key|[Key](#interface-key)|是|-|指定加密或解密的密钥。|
|params|?[ParamsSpec](#class-paramsspec)|是|-|指定加密或解密的参数，对于ECB等没有参数的算法模式，可以传入None。|

**异常：**

- BusinessException：对应错误码如下表，详见[crypto framework错误码](./cj-errorcode-crypto.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17620001 | memory operation failed. |
  | 17620002 | failed to convert parameters between cj and c. |
  | 17630001 | crypto operation error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let skg = createSymKeyGenerator("AES128")
    let sk = skg.convertKey(DataBlob([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]))
    let encoder = createCipher("AES128|CBC|PKCS7")
    let ivBlob = DataBlob([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    var ivParamsSpec = IvParamsSpec("IvParamsSpec", ivBlob)
    ivParamsSpec.algName = "IvParamsSpec"
    ivParamsSpec.iv = ivBlob
    encoder.initialize(CryptoMode.EncryptMode, sk, ivParamsSpec)
    let message = "This is a test"
    let blob = DataBlob(message.toArray())
    let encryptText = encoder.doFinal(blob)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```