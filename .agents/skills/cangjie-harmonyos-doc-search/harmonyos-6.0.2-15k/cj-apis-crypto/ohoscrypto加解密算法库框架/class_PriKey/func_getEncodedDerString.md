### func getEncodedDer(String)

```cangjie
public func getEncodedDer(format: String): DataBlob
```

**功能：** 支持根据指定的密钥格式（如采用哪个规范），获取满足ASN.1语法、DER编码的私钥数据。当前仅支持获取PKCS8格式的ECC私钥数据。

> **说明：**
>
> 本接口和[Key.getEncoded()](#func-getencoded)的区别是：
>
> - 本接口可根据入参决定数据的输出格式，当前支持获取PKCS8格式的ecc私钥数据。
> - [Key.getEncoded()](#func-getencoded)接口，不支持指定密钥格式。

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|format|String|是|-|用于指定当前密钥格式，取值当前仅支持"PKCS8"。|

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#struct-datablob)|返回指定密钥格式的，满足ASN.1语法、DER编码的ecc私钥数据。|

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
let p = key.getEncodedDer('PKCS8')
```