## class PriKey

```cangjie
public class PriKey <: Key {}
```

**功能：** 私钥，是[Key](#interface-key)的子类，在非对称加解密、签名、密钥协商时需要将其作为输入使用。

私钥可以通过非对称密钥生成器[AsyKeyGenerator](#class-asykeygenerator)、[AsyKeyGeneratorBySpec](#class-asykeygeneratorbyspec)来生成。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

**父类型：**

- [Key](#interface-key)

### func clearMem()

```cangjie
public func clearMem(): Unit
```

**功能：** 将系统底层内存中的的密钥内容清零。调用该方法后，调用其他方法将发生不可预期现象。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let keyGenAlg = "RSA1024"
let generator = createAsyKeyGenerator(keyGenAlg)
let keyPair = generator.generateKeyPair()
let key: PriKey = keyPair.priKey
key.clearMem()
```

### func getAsyKeySpec(AsyKeySpecItem)

```cangjie
public func getAsyKeySpec(itemType: AsyKeySpecItem): ResultSpec
```

**功能：** 获取密钥参数。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|itemType|[AsyKeySpecItem](#enum-asykeyspecitem)|是|-|指定的密钥参数类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[ResultSpec](#enum-resultspec)|用于查看密钥参数的具体内容。|

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

let keyGenAlg = "RSA1024"
let generator = createAsyKeyGenerator(keyGenAlg)
let keyPair = generator.generateKeyPair()
let key: PriKey = keyPair.priKey
let p = key.getAsyKeySpec(ECC_FP_P_BN)
```