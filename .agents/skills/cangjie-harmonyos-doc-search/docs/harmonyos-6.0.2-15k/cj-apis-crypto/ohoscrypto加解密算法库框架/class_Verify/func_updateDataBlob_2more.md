### func update(DataBlob)

```cangjie
public func update(data: DataBlob): Unit
```

**功能：** 追加待验签数据。

> **说明：**
>
> 根据数据量，可以不调用update（即[initialize](#func-initializeprikey)完成后直接调用[verify](#func-verifydatablob-datablob)）或多次调用update。
> 算法库目前没有对update（单次或累计）的数据量设置大小限制，建议对于大数据量的验签操作，采用多次update的方式传入数据，避免一次性申请过大内存。
> 当使用DSA算法进行验签，并设置了摘要算法为NoHash时，则不支持update操作，update接口会返回错误码ERR_CRYPTO_OPERATION。

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|[DataBlob](#struct-datablob)|是|-|传入的消息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  |17620001|memory error.|
  |17620002|runtime error.|
  |17630001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let keyGenAlg = "RSA1024"
let generator = createAsyKeyGenerator(keyGenAlg)
let keyPair = generator.generateKeyPair()
let signAlg = "RSA1024|PKCS1|SHA256"
let signer = createSign(signAlg)
signer.initialize(keyPair.priKey)
let input1 = DataBlob("This is Sign test plan1".toArray())
signer.update(input1)
let signData = signer.sign(Option<DataBlob>.None)
let verifyAlg = "RSA1024|PKCS1|SHA256"
let verifier = createVerify(verifyAlg)
verifier.initialize(keyPair.pubKey)
verifier.update(input1)
```

### func verify(?DataBlob, DataBlob)

```cangjie
public func verify(data: ?DataBlob, signatureData: DataBlob): Bool
```

**功能：** 对数据进行验签。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|?[DataBlob](#struct-datablob)|是|-|传入的消息。|
|signatureData|[DataBlob](#struct-datablob)|是|-|签名数据。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|同步返回值，代表验签是否通过。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  |17620001|memory error.|
  |17620002|runtime error.|
  |17630001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let keyGenAlg = "RSA1024"
let generator = createAsyKeyGenerator(keyGenAlg)
let keyPair = generator.generateKeyPair()
let signAlg = "RSA1024|PKCS1|SHA256"
let signer = createSign(signAlg)
signer.initialize(keyPair.priKey)
let input1 = DataBlob("This is Sign test plan1".toArray())
let input2 = DataBlob("This is Sign test plan2".toArray())
signer.update(input1)
let signData = signer.sign(input2)
let verifyAlg = "RSA1024|PKCS1|SHA256"
let verifier = createVerify(verifyAlg)
verifier.initialize(keyPair.pubKey)
verifier.update(input1)
let res = verifier.verify(input2, signData)
```