## func createAsyKeyGeneratorBySpec(AsyKeySpec)

```cangjie
public func createAsyKeyGeneratorBySpec(asyKeySpec: AsyKeySpec): AsyKeyGeneratorBySpec
```

**功能：** 通过指定密钥参数，获取相应的非对称密钥生成器实例。

支持的规格详见[非对称密钥生成和转换规格](../../../../Dev_Guide/security/CryptoArchitectureKit/cj-crypto-asym-key-generation-conversion-spec.md)。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|asyKeySpec|[AsyKeySpec](#interface-asykeyspec)|是|-|密钥参数。非对称密钥生成器根据指定的这些参数生成公/私钥。|

**返回值：**

|类型|说明|
|:----|:----|
|[AsyKeyGeneratorBySpec](#class-asykeygeneratorbyspec)|返回非对称密钥生成器实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  |801|this operation is not supported.|
  |17620001|memory error.|

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
```