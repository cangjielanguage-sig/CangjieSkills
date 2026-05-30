## class AsyKeyGeneratorBySpec

```cangjie
public class AsyKeyGeneratorBySpec {}
```

**功能：** 非对称密钥生成器。在使用该类的方法前，需要先使用[createAsyKeyGeneratorBySpec()](#func-createasykeygeneratorbyspecasykeyspec)方法构建一个AsyKeyGeneratorBySpec实例。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### prop algName

```cangjie
public prop algName: String
```

**功能：** 非对称密钥生成器的算法名。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### func generateKeyPair()

```cangjie
public func generateKeyPair(): KeyPair
```

**功能：** 获取该非对称密钥生成器生成的密钥。

当使用[COMMON_PARAMS_SPEC](#enum-asykeyspectype)类型的密钥参数来创建密钥生成器时，可以得到随机生成的密钥对；当使用[KEY_PAIR_SPEC](#enum-asykeyspectype)类型的密钥参数来创建密钥生成器时，可以得到各项数据与密钥参数一致的密钥对。

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
import std.math.numeric.BigInt

let dsaCommonSpec = DSACommonParamsSpec(
    algName: "DSA",
    specType: KEY_PAIR_SPEC,
    p: BigInt(
        "ed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729",
        base: 16
    ),
    q: BigInt("d23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b", base: 16),
    g: BigInt(
        "2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd",
        base: 16
    )
)
let generator = createAsyKeyGenerator("DSA1024")
let keyPair = generator.generateKeyPair()
let dsaKeyPairSpec = DSAKeyPairSpec(
    params: dsaCommonSpec,
    sk: BigInt(keyPair.priKey.getEncoded().data),
    pk: BigInt(keyPair.pubKey.getEncoded().data),
)
let asyKeyGeneratorBySpec = createAsyKeyGeneratorBySpec(dsaKeyPairSpec)
let keyPairData = asyKeyGeneratorBySpec.generateKeyPair()
```