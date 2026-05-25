### func getSubjectName()

```cangjie
public func getSubjectName(): DataBlob
```

**功能：** 表示获取X509证书主体名称。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#class-datablob)|表示X509证书主体名称。|

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
let subData = x509Cert.getSubjectName(EncodingType.ENCODING_UTF8).data
```

### func getSubjectName(EncodingType)

```cangjie
public func getSubjectName(encodingType: EncodingType): DataBlob
```

**功能：** 表示获取X509证书主体名称。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|encodingType|[EncodingType](#enum-encodingtype)|是|编码类型。设置参数表示获取UTF8格式编码；不设置默认获取ASCII格式编码。|

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#class-datablob)|表示X509证书主体名称。|

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
let subData = x509Cert.getSubjectName(EncodingType.ENCODING_UTF8).data
```

### func getSubjectX500DistinguishedName()

```cangjie
public func getSubjectX500DistinguishedName(): X500DistinguishedName
```

**功能：** 获取证书主题的X509可分辨名称。

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
let subDgName = x509Cert.getSubjectX500DistinguishedName().getName()
let subDgData = x509Cert.getSubjectX500DistinguishedName().getEncoded().data
```

### func getVersion()

```cangjie
public func getVersion(): Int32
```

**功能：** 表示获取X509证书版本。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|表示X509证书版本。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

let certData = "example certdata"
let x509Cert = createX509Cert(EncodingBlob(certData.toArray(), EncodingFormat.FORMAT_PEM))
let version = x509Cert.getVersion()
```