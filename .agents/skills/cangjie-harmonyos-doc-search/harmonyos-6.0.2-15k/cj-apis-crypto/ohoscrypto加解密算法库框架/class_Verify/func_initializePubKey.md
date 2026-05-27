### func initialize(PubKey)

```cangjie
public func initialize(pubKey: PubKey): Unit
```

**功能：** 传入公钥初始化Verify对象，通过注册回调函数获取结果。init、update、verify为三段式接口，需要成组使用。其中init和verify必选，update可选。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pubKey|[PubKey](#class-pubkey)|是|-|公钥对象，用于Verify的初始化。|

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
```