## class X509CRLEntry

```cangjie
public class X509CRLEntry <: ToString {}
```

**功能：** 表示被吊销证书对象。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**父类型：**

- ToString

### func getCertIssuer()

```cangjie
public func getCertIssuer(): DataBlob
```

**功能：** 表示获取被吊销证书的颁发者信息。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#class-datablob)|表示被吊销证书的颁发者信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书错误码](../../errorcodes/cj-errorcode-cert-framework.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|
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
let rc = x509Crl.getRevokedCert(BigInt(1000)).getCertIssuer().data
```

### func getCertIssuerX500DistinguishedName()

```cangjie
public func getCertIssuerX500DistinguishedName(): X500DistinguishedName
```

**功能：** 获取证书颁发者的X509可分辨名称。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[X500DistinguishedName](#class-x500distinguishedname)|X509的可分辨对象。|

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
let rc = x509Crl.getRevokedCert(BigInt(1000)).getCertIssuerX500DistinguishedName().getName()
```

### func getEncoded()

```cangjie
public func getEncoded(): EncodingBlob
```

**功能：** 表示获取被吊销证书的序列化数据。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[EncodingBlob](#class-encodingblob)|表示被吊销证书的序列化数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书错误码](../../errorcodes/cj-errorcode-cert-framework.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
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
let rc = x509Crl.getRevokedCert(BigInt(1000)).getEncoded().data
```