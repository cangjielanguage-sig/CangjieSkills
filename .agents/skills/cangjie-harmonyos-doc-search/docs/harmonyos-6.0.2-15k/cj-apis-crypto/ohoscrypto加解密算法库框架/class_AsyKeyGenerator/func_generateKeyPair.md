### func generateKeyPair()

```cangjie
public func generateKeyPair(): KeyPair
```

**功能：** 获取非对称密钥生成器随机生成的密钥。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[KeyPair](#class-keypair)|非对称密钥。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  |17620001|memory error.|
  |17630001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let asyKeyGenerator = createAsyKeyGenerator('RSA1024')
let keyPairData = asyKeyGenerator.generateKeyPair()
```