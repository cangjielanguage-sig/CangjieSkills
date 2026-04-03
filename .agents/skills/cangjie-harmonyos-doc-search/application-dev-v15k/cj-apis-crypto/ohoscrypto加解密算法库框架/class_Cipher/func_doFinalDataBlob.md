### func doFinal(?DataBlob)

```cangjie
public func doFinal(data: ?DataBlob): DataBlob
```

**功能：** （1）在对称加解密中，doFinal加/解密（分组模式产生的）剩余数据和本次传入的数据，最后结束加密或者解密数据操作，获取加密或者解密数据。

如果数据量较小，可以在doFinal中一次性传入数据，而不使用update；如果在本次加解密流程中，已经使用update传入过数据，可以在doFinal的data参数处传入None。

根据对称加解密的模式不同，doFinal的输出有如下区别：

- 对于GCM和CCM模式的对称加密：一次加密流程中，如果将每一次update和doFinal的结果拼接起来，会得到“密文+authTag”，即末尾的16字节（GCM模式）或12字节（CCM模式）是authTag，而其余部分均为密文。（也就是说，如果doFinal的data参数传入None，则doFinal的结果就是authTag）authTag需要填入解密时的[GcmParamsSpec](#struct-gcmparamsspec)或[CcmParamsSpec](#struct-ccmparamsspec)；密文则作为解密时的入参data。
- 对于其他模式的对称加解密、GCM和CCM模式的对称解密：一次加/解密流程中，每一次update和doFinal的结果拼接起来，得到完整的明文/密文。

（2）在RSA、SM2非对称加解密中，doFinal加/解密本次传入的数据，获取加密或者解密数据。如果数据量较大，可以多次调用doFinal，拼接结果得到完整的明文/密文。

> **说明：**
>
> - 对称加解密中，调用doFinal标志着一次加解密流程已经完成，即[Cipher](#class-cipher)实例的状态被清除，因此当后续开启新一轮加解密流程时，需要重新调用init()并传入完整的参数列表进行初始化
>（比如即使是对同一个Cipher实例，采用同样的对称密钥，进行加密然后解密，则解密中调用init的时候仍需填写params参数，而不能直接省略为None）。
> - 如果遇到解密失败，需检查加解密数据和init时的参数是否匹配，包括GCM模式下加密得到的authTag是否填入解密时的GcmParamsSpec等。
> - doFinal的结果可能为空，因此使用.data字段访问doFinal结果的具体数据前，请记得先判断结果是否为空，避免产生异常。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|?[DataBlob](#struct-datablob)|是|-|加密或者解密的数据。data参数允许为None，但不允许传入{data: Array\<UInt8>() }。|

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#struct-datablob)|返回剩余数据的加/解密结果DataBlob。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters.|
  |17620001|memory error.|
  |17620002|runtime error.|
  |17630001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let cipherAlgName = "RSA|PKCS1_OAEP|SHA256|MGF1_SHA1"
let cipher = createCipher(cipherAlgName)
let syg = createSymKeyGenerator("AES128")
let sk = syg.generateSymKey()
cipher.`init`(CryptoMode.ENCRYPT_MODE, sk, None)
cipher.doFinal(None)
```