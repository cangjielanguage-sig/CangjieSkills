### func doFinal(?DataBlob)

```cangjie
public func doFinal(data: ?DataBlob): DataBlob
```

**功能：** （1）在对称加解密中，doFinal加/解密（分组模式产生的）剩余数据和本次传入的数据，最后结束加密或者解密数据操作，获取加密或者解密数据。

如果数据量较小，可以在doFinal中一次性传入数据，而不使用update；如果在本次加解密流程中，已经使用update传入过数据，可以在doFinal的data参数处传入None。

根据对称加解密的模式不同，doFinal的输出有如下区别：

- 对于GCM和CCM模式的对称加密：一次加密流程中，如果将每次update和doFinal的结果拼接起来，会得到“密文 + authTag”。即末尾的16字节（GCM模式）或12字节（CCM模式）是authTag，其余部分均为密文。也就是说，如果doFinal的data参数传入None，则doFinal的结果就是 authTag。

  authTag需要填入解密时的[GcmParamsSpec](#class-gcmparamsspec)或[CcmParamsSpec](#class-ccmparamsspec)；密文则作为解密时的入参data。
- 对于其他模式的对称加解密、GCM和CCM模式的对称解密：一次加/解密流程中，每一次update和doFinal的结果拼接起来，得到完整的明文/密文。

（2）在RSA和SM2非对称加解密中，doFinal用于加解密本次传入的数据，获取加密或解密后的数据。如果数据量超过单次处理能力，可以多次调用doFinal，并将结果拼接以获得完整的明文或密文。

> **说明：**
>
> 1. 对称加解密中，调用doFinal标志着一次加解密流程已经完成，即[Cipher](#class-cipher)实例的状态被清除，因此当后续开启新一轮加解密流程时，需要重新调用initialize()并传入完整的参数列表进行初始化
> （比如即使是对同一个Cipher实例，采用同样的对称密钥，进行加密然后解密，则解密中调用initialize的时候仍需填写params参数，而不能直接省略为None）。
> 2. 如果遇到解密失败，需检查加解密数据和initialize时的参数是否匹配，包括GCM模式下加密得到的authTag是否填入解密时的GcmParamsSpec等。
>
> 对于加密，CFB、OFB和CTR模式，如果doFinal传None, 则返回结果为空。
>
> 对于解密，GCM、CCM、CFB、OFB和CTR模式，如果doFinal传None，则返回结果为空；对于解密，其他模式，如果明文是加密块大小的整倍数，调用update传入所有密文，调用doFinal传None, 则返回结果为空。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|?[DataBlob](#class-datablob)|是|-|加密或解密的数据。在对称加解密中可为None，但不可传入{data: Array\<UInt8>()}。|

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#class-datablob)|加/解密结果DataBlob。|

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