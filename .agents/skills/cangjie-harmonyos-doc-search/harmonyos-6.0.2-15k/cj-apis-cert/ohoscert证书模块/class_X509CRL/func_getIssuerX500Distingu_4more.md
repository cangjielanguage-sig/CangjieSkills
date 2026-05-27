### func getIssuerX500DistinguishedName()

```cangjie
public func getIssuerX500DistinguishedName(): X500DistinguishedName
```

**功能：** 获取颁发者的X509可分辨名称。

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

let crlData = "test crl"
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
let x500DgName = x509Crl.getIssuerX500DistinguishedName().getName()
```

### func getLastUpdate()

```cangjie
public func getLastUpdate(): String
```

**功能：** 表示获取X509证书吊销列表最后一次更新日期，日期为ASN.1时间格式。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|表示X509证书吊销列表最后一次更新日期，日期为ASN.1时间格式。|

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
let lu = x509Crl.getLastUpdate()
```

### func getNextUpdate()

```cangjie
public func getNextUpdate(): String
```

**功能：** 表示获取证书吊销列表下一次更新的日期，日期为ASN.1时间格式。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|表示X509证书吊销列表下一次更新的日期，日期为ASN.1时间格式。|

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
let lu = x509Crl.getNextUpdate()
```

### func getRevokedCert(BigInt)

```cangjie
public func getRevokedCert(serialNumber: BigInt): X509CRLEntry
```

**功能：** 表示通过指定证书序列号获取被吊销X509证书对象。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|serialNumber|BigInt|是|表示证书序列号。|

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
import std.math.numeric.BigInt

let crlData = "test crl"
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
let rc = x509Crl.getRevokedCert(BigInt(1000))
```