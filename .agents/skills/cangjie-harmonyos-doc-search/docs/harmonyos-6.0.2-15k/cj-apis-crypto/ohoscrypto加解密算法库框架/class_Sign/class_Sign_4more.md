## class Sign

```cangjie
public class Sign {}
```

**功能：** Sign类，使用Sign方法之前需要创建该类的实例进行操作，通过[createSign](#func-createsignstring)方法构造此实例。按序调用本类中的init、update、sign方法完成签名操作。

Sign类不支持重复初始化，当业务方需要使用新密钥签名时，需要重新创建新Sign对象并调用init初始化。

业务方使用时，在createSign时确定签名的模式，调用init接口设置密钥。

当待签名数据较短时，可在init初始化后，（无需update）直接调用sign接口传入原文数据进行签名。

当待签名数据较长时，可通过update接口分段传入切分后的原文数据，最后调用sign接口对整体原文数据进行签名。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

### prop algName

```cangjie
public prop algName: String
```

**功能：** 签名指定的算法名称。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### func getSignSpec(SignSpecItem)

```cangjie
public func getSignSpec(itemType: SignSpecItem): ResultSpec
```

**功能：** 获取签名参数。当前只支持RSA算法。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|itemType|[SignSpecItem](#enum-signspecitem)|是|-|用于指定需要获取的签名参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[ResultSpec](#enum-resultspec)|获取的签名参数的具体值。|

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
let signAlg = "RSA1024|PKCS1|SHA256"
let signer = createSign(signAlg)
signer.initialize(keyPair.priKey)
let saltLen = signer.getSignSpec(PSS_SALT_LEN_NUM)
```

### func initialize(PriKey)

```cangjie
public func initialize(priKey: PriKey): Unit
```

**功能：** 使用私钥初始化Sign对象。initialize、update、sign为三段式接口，需要成组使用。其中initialize和sign必选，update可选。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|priKey|[PriKey](#class-prikey)|是|-|用于Sign的初始化。|