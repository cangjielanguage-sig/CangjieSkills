## class PubKey

```cangjie
public class PubKey <: Key {}
```

**功能：** 公钥，是[Key](#interface-key)的子类，在非对称加解密、验签、密钥协商时需要将其对象作为输入使用。

公钥可以通过非对称密钥生成器[AsyKeyGenerator](#class-asykeygenerator)、[AsyKeyGeneratorBySpec](#class-asykeygeneratorbyspec)生成。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

**父类型：**

- [Key](#interface-key)

### func getAsyKeySpec(AsyKeySpecItem)

```cangjie
public func getAsyKeySpec(itemType: AsyKeySpecItem): ResultSpec
```

**功能：** 获取秘钥参数。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|itemType|[AsyKeySpecItem](#enum-asykeyspecitem)|是|-|指定的密钥参数。|

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
let key: PubKey = keyPair.pubKey
key.getAsyKeySpec(ECC_FP_P_BN)
```

### func getEncodedDer(String)

```cangjie
public func getEncodedDer(format: String): DataBlob
```

**功能：** 支持根据指定的密钥格式（如采用哪个规范、是否压缩等），获取满足ASN.1语法、DER编码的公钥数据。当前仅支持获取ECC压缩/非压缩格式的公钥数据。

> **说明：**
>
> 本接口和[Key.getEncoded()](#func-getencoded)的区别是：
>
> - 本接口可根据入参决定数据的输出格式。
> - [Key.getEncoded()](#func-getencoded)接口不支持指定密钥格式，生成的数据格式与原始数据格式(通过[convertKey](#func-convertkeydatablob-datablob)接口生成密钥对象时的数据格式)保持一致。

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|format|String|是|-|用于指定当前密钥格式，取值仅支持"X509MagIc_StrINgCOMPRESSED"和"X509MagIc_StrINgUNCOMPRESSED"。|

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#struct-datablob)|返回指定密钥格式的，满足ASN.1语法、DER编码的公钥数据。|

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
let key: PubKey = keyPair.pubKey
key.getEncodedDer("X509|UNCOMPRESSED")
```