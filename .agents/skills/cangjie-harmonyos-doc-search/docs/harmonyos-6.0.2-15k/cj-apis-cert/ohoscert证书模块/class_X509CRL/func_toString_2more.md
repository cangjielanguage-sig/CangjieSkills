### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取对象的字符串类型数据。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|对象的字符串类型数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书错误码](../../errorcodes/cj-errorcode-cert-framework.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |19020001|memory error.|
  |19020002|runtime error.|
  |19030001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

let crlData = "test crl"
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
let crlStr = x509Crl.toString()
```

### func verify(PubKey)

```cangjie
public func verify(key: PubKey): Unit
```

**功能：** 表示对X509证书吊销列表进行验签。验签支持RSA算法。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|key|[PubKey](../CryptoArchitectureKit/cj-apis-crypto.md#class-pubkey)|是|表示用于验签的公钥对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书错误码](../../errorcodes/cj-errorcode-cert-framework.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |19030001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*
internal import ohos.crypto.createAsyKeyGenerator
internal import ohos.crypto.DataBlob as CryptoDataBlob

let crlData = "test crl"
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
let pubKeyData: Array<UInt8> = [0x30, 0x81, 0x9F, 0x30, 0x0D]  //example pubkey
let keyGenerator = createAsyKeyGenerator("RSA1024|PRIMES_3")
let pubEncodingBlob = CryptoDataBlob(pubKeyData)
let keyPair = keyGenerator.convertKey(pubEncodingBlob, Option.None)
x509Crl.verify
```