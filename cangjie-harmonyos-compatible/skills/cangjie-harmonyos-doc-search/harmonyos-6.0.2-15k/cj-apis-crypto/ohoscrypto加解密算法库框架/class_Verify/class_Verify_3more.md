## class Verify

```cangjie
public class Verify {}
```

**功能：** Verify类，使用Verify方法之前需要创建该类的实例进行操作，通过[createVerify(algName: String): Verify](#func-createverifystring)方法构造此实例。按序调用本类中的init、update、verify方法完成签名操作。

Verify类不支持重复初始化，当业务方需要使用新密钥验签时，需要重新创建新Verify对象并调用init初始化。

业务方使用时，在createVerify时确定验签的模式，调用init接口设置密钥。

当被签名的消息较短时，可在init初始化后，（无需update）直接调用verify接口传入被签名的消息和签名(signatureData)进行验签。

当被签名的消息较长时，可通过update接口分段传入被签名的消息，最后调用verify接口对消息全文进行验签。业务方可在循环中调用update接口，循环结束后调用verify传入签名(signatureData)进行验签。

当使用DSA算法进行验签，并设置了摘要算法为NoHash时，则不支持update操作，update接口会返回错误码ERR_CRYPTO_OPERATION。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### prop algName

```cangjie
public prop algName: String
```

**功能：** 验签指定的算法名称。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### func getVerifySpec(SignSpecItem)

```cangjie
public func getVerifySpec(itemType: SignSpecItem): ResultSpec
```

**功能：** 获取验签参数。当前只支持RSA算法。

验签的参数应当与签名的参数保持一致。

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|itemType|[SignSpecItem](#enum-signspecitem)|是|-|用于指定需要获取的验签参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[ResultSpec](#enum-resultspec)|获取的验签参数的具体值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  |801|this operation is not supported.|
  |17620001|memory error.|
  |17630001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let keyGenAlg = "RSA1024"
let generator = createAsyKeyGenerator(keyGenAlg)
let keyPair = generator.generateKeyPair()
let verifyAlg = "RSA1024|PKCS1|SHA256"
let verifier = createVerify(verifyAlg)
verifier.initialize(keyPair.pubKey)
let saltLen = verifier.getVerifySpec(PSS_SALT_LEN_NUM)
```