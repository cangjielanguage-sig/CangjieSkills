### func getIssuerName()

```cangjie
public func getIssuerName(): DataBlob
```

**功能：** 表示获取X509证书颁发者名称。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#class-datablob)|表示X509证书颁发者名称。|

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
let issuerData = x509Cert.getIssuerName().data
```

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

let certData = "example certdata"
let x509Cert = createX509Cert(EncodingBlob(certData.toArray(), EncodingFormat.FORMAT_PEM))
let dgName = x509Cert.getIssuerX500DistinguishedName().getName()
let dgData = x509Cert.getIssuerX500DistinguishedName().getEncoded().data
```

### func getItem(CertItemType)

```cangjie
public func getItem(itemType: CertItemType): DataBlob
```

**功能：** 表示获取X509证书对应的字段。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|itemType|[CertItemType](#enum-certitemtype)|是|表示获取证书字段。|

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#class-datablob)|表示X509证书对应的字段，返回值为DER格式。|

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

let certData = "example certdata"
let x509Cert = createX509Cert(EncodingBlob(certData.toArray(), EncodingFormat.FORMAT_PEM))
let item = x509Cert.getItem(CERT_ITEM_TYPE_TBS).data
```

### func getKeyUsage()

```cangjie
public func getKeyUsage(): DataBlob
```

**功能：** 表示获取X509证书密钥用途。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#class-datablob)|表示X509证书密钥用途。|

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
let keyUsage = x509Cert.getKeyUsage().data
```