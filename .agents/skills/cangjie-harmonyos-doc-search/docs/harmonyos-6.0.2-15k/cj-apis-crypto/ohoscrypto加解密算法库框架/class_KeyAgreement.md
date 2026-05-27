## class KeyAgreement

```cangjie
public class KeyAgreement {}
```

**功能：** KeyAgreement类，使用密钥协商方法之前需要创建该类的实例进行操作，通过[createKeyAgreement(algName: String): KeyAgreement](#func-createkeyagreementstring)方法构造此实例。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### prop algName

```cangjie
public prop algName: String
```

**功能：** 指定密钥协商算法：目前仅支持ECC，X25519和DH。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### func generateSecret(PriKey, PubKey)

```cangjie
public func generateSecret(priKey: PriKey, pubKey: PubKey): DataBlob
```

**功能：** 基于传入的私钥与公钥进行密钥协商。

**系统能力：** SystemCapability.Security.CryptoFramework.KeyAgreement

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|priKey|[PriKey](#class-prikey)|是|-|设置密钥协商的私钥输入。|
|pubKey|[PubKey](#class-pubkey)|是|-|设置密钥协商的公钥输入。|

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#struct-datablob)|共享秘密。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  | 错误码ID | 错误信息               |
  | :-------- | :---------------------- |
  | 401 | invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  | 801 | this operation is not supported.          |
  | 17620001 | memory error.          |
  | 17630001 | crypto operation error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let asyGenerator = createAsyKeyGenerator("ECC256")
let globalKeyPair = asyGenerator.generateKeyPair()
let keyAgreement = createKeyAgreement('ECC256')
let secret = keyAgreement.generateSecret(globalKeyPair.priKey, globalKeyPair.pubKey)
```