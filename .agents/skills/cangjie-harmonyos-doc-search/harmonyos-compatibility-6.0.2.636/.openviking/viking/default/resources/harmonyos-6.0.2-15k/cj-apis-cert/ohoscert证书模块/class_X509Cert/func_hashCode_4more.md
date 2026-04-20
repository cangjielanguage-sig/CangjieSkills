### func hashCode()

```cangjie
public func hashCode(): Array<UInt8>
```

**功能：** 获取输入数据的哈希值。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt8>|数据的哈希值。|

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

let certData = "example certdata"
let x509Cert = createX509Cert(EncodingBlob(certData.toArray(), EncodingFormat.FORMAT_PEM))
let certStr = x509Cert.hashCode()
```

### func isMatch(X509CertMatchParameters)

```cangjie
public func isMatch(param: X509CertMatchParameters): Bool
```

**功能：** 判断证书是否与输入参数匹配。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|param|[X509CertMatchParameters](#class-x509certmatchparameters)|是|表示需要匹配的参数。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|当参数匹配时，该方法返回true，否则返回false。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书错误码](../../errorcodes/cj-errorcode-cert-framework.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |19020001|memory error.|
  |19030001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

let certData = "example certdata"
let x509Cert = createX509Cert(EncodingBlob(certData.toArray(), EncodingFormat.FORMAT_PEM))
var matchParam = X509CertMatchParameters()
matchParam.validDate = "20230930000001Z"
matchParam.serialNumber = x509Cert.getCertSerialNumber()
let matchResult = x509Cert.isMatch(matchParam)
```

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

let certData = "example certdata"
let x509Cert = createX509Cert(EncodingBlob(certData.toArray(), EncodingFormat.FORMAT_PEM))
let certStr = x509Cert.toString()
```

### func verify(PubKey)

```cangjie
public func verify(key: PubKey)
```

**功能：** 表示对证书验签。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|key|[PubKey](../CryptoArchitectureKit/cj-apis-crypto.md#class-pubkey)|是|用于验签的公钥对象。|

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

let certData = "example certdata"
let x509Cert = createX509Cert(EncodingBlob(certData.toArray(), EncodingFormat.FORMAT_PEM))
let pubKey = x509Cert.getPublicKey()
x509Cert.verify(pubKey)
```