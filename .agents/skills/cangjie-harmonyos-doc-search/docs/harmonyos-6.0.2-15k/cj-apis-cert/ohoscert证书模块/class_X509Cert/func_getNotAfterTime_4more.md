### func getNotAfterTime()

```cangjie
public func getNotAfterTime(): String
```

**功能：** 表示获取X509证书有效期截止时间。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|表示X509证书有效期截止时间，日期为ASN.1时间格式。|

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
let beforeTime = x509Cert.getNotAfterTime()
```

### func getNotBeforeTime()

```cangjie
public func getNotBeforeTime(): String
```

**功能：** 表示获取X509证书有效期起始时间。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|表示X509证书有效期起始时间，日期为ASN.1时间格式。|

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
let beforeTime = x509Cert.getNotBeforeTime()
```

### func getPublicKey()

```cangjie
public func getPublicKey(): PubKey
```

**功能：** 表示获取X509证书公钥。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[PubKey](../CryptoArchitectureKit/cj-apis-crypto.md#class-pubkey)|X509证书公钥对象：仅用于X509Cert的verify接口。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书错误码](../../errorcodes/cj-errorcode-cert-framework.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |19020001|memory error.|
  |19030001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

let certData = "example certdata"
let x509Cert = createX509Cert(EncodingBlob(certData.toArray(), EncodingFormat.FORMAT_PEM))
let pubKey = x509Cert.getPublicKey()
```

### func getSignature()

```cangjie
public func getSignature(): DataBlob
```

**功能：** 表示获取X509证书签名数据。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#class-datablob)|表示X509证书签名数据。|

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
let signData = x509Cert.getSignature().data
```