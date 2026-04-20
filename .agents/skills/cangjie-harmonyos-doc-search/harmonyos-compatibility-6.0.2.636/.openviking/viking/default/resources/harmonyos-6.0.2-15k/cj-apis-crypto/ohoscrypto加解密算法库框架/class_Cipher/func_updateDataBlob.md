### func update(DataBlob)

```cangjie
public func update(data: DataBlob): DataBlob
```

**功能：** 分段更新加密或者解密数据操作，获取加/解密数据。

必须在对[Cipher](#class-cipher)实例使用[init()](#func-initcryptomode-key-paramsspec)初始化后，才能使用本函数。

> **说明：**
>
> - 在进行对称加解密操作的时候，如果开发者对各个分组模式不够熟悉，建议对每次update和doFinal的结果都判断是否为空数组，并在结果不为空数组时取出其中的数据进行拼接，形成完整的密文/明文。这是因为选择的分组模式等各项规格都可能对update和doFinal结果产生影响。
>（例如对于ECB和CBC模式，不论update传入的数据是否为分组长度的整数倍，都会以分组作为基本单位进行加/解密，并输出本次update新产生的加/解密分组结果。
> 可以理解为，update只要凑满一个新的分组就会有输出，如果没有凑满则此次update输出为None，把当前还没被加/解密的数据留着，等下一次update/doFinal传入数据的时候，拼接起来继续凑分组。
> 最后doFinal的时候，会把剩下的还没加/解密的数据，根据[createCipher](#func-createcipherstring)时设置的padding模式进行填充，补齐到分组的整数倍长度，再输出剩余加解密结果。
> 而对于可以将分组密码转化为流模式实现的模式，还可能出现密文长度和明文长度相同的情况等。）
> - 根据数据量，可以不调用update（即init完成后直接调用doFinal）或多次调用update。
> 算法库目前没有对update（单次或累计）的数据量设置大小限制，建议对于大数据量的对称加解密，可以采用多次update的方式传入数据。
> - RSA、SM2非对称加解密不支持update操作。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|[DataBlob](#struct-datablob)|是|-|加密或者解密的数据。data不允许传入{data: Array\<UInt8>() }。|

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#struct-datablob)|返回此次更新的加/解密结果DataBlob。|

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
let plainText: DataBlob = DataBlob("this is test".toArray())
cipher.update(plainText)
```