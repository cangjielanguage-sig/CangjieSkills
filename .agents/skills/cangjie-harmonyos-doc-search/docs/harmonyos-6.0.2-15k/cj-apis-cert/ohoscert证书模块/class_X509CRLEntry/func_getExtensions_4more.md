### func getExtensions()

```cangjie
public func getExtensions(): DataBlob
```

**功能：** 表示获取CRL的扩展。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#class-datablob)|表示X509CRLEntry扩展用途。|

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
import std.math.numeric.BigInt

let crlData = "test crl"
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
let rc = x509Crl.getRevokedCert(BigInt(1000)).getExtensions().data
```

### func getExtensionsObject()

```cangjie
public func getExtensionsObject(): CertExtension
```

**功能：** 获取对应实体的扩展域DER格式数据。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[CertExtension](#class-certextension)|证书扩展域段类对象。|

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
import std.math.numeric.BigInt

let crlData = "test crl"
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
let rc = x509Crl.getRevokedCert(BigInt(1000)).getExtensionsObject().getEncoded().data
```

### func getRevocationDate()

```cangjie
public func getRevocationDate(): String
```

**功能：** 表示获取证书被吊销的日期，日期为ASN.1时间格式。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|表示证书被吊销的日期，日期为ASN.1时间格式。|

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
import std.math.numeric.BigInt

let crlData = "test crl"
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
let rc = x509Crl.getRevokedCert(BigInt(1000)).getRevocationDate()
```

### func getSerialNumber()

```cangjie
public func getSerialNumber(): BigInt
```

**功能：** 表示获取被吊销证书的序列号。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|BigInt|表示被吊销证书的序列号。|

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
import std.math.numeric.BigInt

let crlData = "test crl"
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
let rc = x509Crl.getRevokedCert(BigInt(1000)).getSerialNumber()
```