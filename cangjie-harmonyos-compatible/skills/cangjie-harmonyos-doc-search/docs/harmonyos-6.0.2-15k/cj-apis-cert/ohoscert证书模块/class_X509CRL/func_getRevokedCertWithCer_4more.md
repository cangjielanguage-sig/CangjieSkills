### func getRevokedCertWithCert(X509Cert)

```cangjie
public func getRevokedCertWithCert(cert: X509Cert): X509CRLEntry
```

**功能：** 表示通过指定证书对象获取被吊销X509证书对象。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|cert|[X509Cert](#class-x509cert)|是|表示证书对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[X509CRLEntry](#class-x509crlentry)|表示被吊销X509证书对象。|

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

let certData = "test cert"
let x509Cert = createX509Cert(EncodingBlob(certData.toArray(), EncodingFormat.FORMAT_PEM))
let crlData = "test crl"
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
let isRevoked = x509Crl.isRevoked(x509Cert)
```

### func getRevokedCerts()

```cangjie
public func getRevokedCerts(): Array<X509CRLEntry>
```

**功能：** 表示获取被吊销X509证书列表。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[X509CRLEntry](#class-x509crlentry)>|表示被吊销X509证书列表。|

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

let crlData = "test crl"
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
let rc = x509Crl.getRevokedCerts()
```

### func getSignature()

```cangjie
public func getSignature(): DataBlob
```

**功能：** 表示获取X509证书吊销列表的签名数据。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#class-datablob)|表示X509证书吊销列表的签名数据。|

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
let sigData = x509Crl.getSignature().data
```

### func getSignatureAlgName()

```cangjie
public func getSignatureAlgName(): String
```

**功能：** 表示获取X509证书吊销列表签名的算法名称。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|表示X509证书吊销列表签名的算法名。|

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
let sigAlgName = x509Crl.getSignatureAlgName()
```