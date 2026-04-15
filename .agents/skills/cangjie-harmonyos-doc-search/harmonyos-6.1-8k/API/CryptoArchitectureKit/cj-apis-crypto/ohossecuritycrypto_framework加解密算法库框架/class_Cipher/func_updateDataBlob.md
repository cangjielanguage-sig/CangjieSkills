### func update(DataBlob)

```cangjie
public func update(data: DataBlob): DataBlob
```

**功能：** 分段更新加密或者解密数据操作，获取加/解密数据。

> **说明：**
>
> 必须在对[Cipher](#class-cipher)实例使用[initialize()](#func-initializecryptomode-key-paramsspec)初始化后，才能使用本函数。

- 在进行对称加解密操作时，如果开发者对各分组模式不够熟悉，建议每次调用update和doFinal后，都判断结果是否为空。如果结果不为空，则取出其中的数据进行拼接，以形成完整的密文或明文。这是因为选择的分组模式等各项规格可能会影响update和doFinal的结果。

    例如，对于ECB和CBC模式，不论update传入的数据是否为分组长度的整数倍，都会以分组作为基本单位进行加/解密，并输出本次update新产生的加/解密分组结果。

    可以理解为，update只要凑满一个新的分组就会有输出，如果没有凑满则此次update输出为空数组，把当前还没被加/解密的数据留着，等下一次update/doFinal传入数据的时候，拼接起来继续凑分组。

    最后doFinal的时候，会把剩下的还没加/解密的数据，根据[createCipher](#func-createcipherstring)时设置的padding模式进行填充，补齐到分组的整数倍长度，再输出剩余加解密结果。

    而对于可以将分组密码转化为流模式实现的模式，还可能出现密文长度和明文长度相同的情况等。

- 根据数据量，可以不调用update（即initialize完成后直接调用doFinal）或多次调用update。

    算法库目前没有对update（单次或累计）的数据量设置大小限制，建议对于大数据量的对称加解密，可以采用多次update的方式传入数据。

    AES使用多次update操作的示例代码详见[使用AES对称密钥分段加解密](../../security/CryptoArchitectureKit/cj-crypto-aes-sym-encrypt-decrypt-gcm-by-segment.md)。

- RSA、SM2非对称加解密不支持update操作。
- 对于CCM模式的对称加解密算法，加密时只能调用1次update接口加密数据并调用doFinal接口获取tag，或直接调用doFinal接口加密数据并获取tag，解密时只能调用1次update接口或调用1次doFinal接口解密数据并验证tag。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|[DataBlob](#class-datablob)|是|-|加密或者解密的数据。data不允许传入{data: Array\<UInt8>()}。|

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#class-datablob)|返回此次更新的加/解密结果DataBlob。|

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
    let cipher = createCipher("AES128|CBC|PKCS7")
    let ivBlob = DataBlob([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    var ivParamsSpec = IvParamsSpec("IvParamsSpec", ivBlob)
    ivParamsSpec.algName = "IvParamsSpec"
    ivParamsSpec.iv = ivBlob
    cipher.initialize(CryptoMode.EncryptMode, sk, ivParamsSpec)
    let plainText: DataBlob = DataBlob("this is test".toArray())
    cipher.update(plainText)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```