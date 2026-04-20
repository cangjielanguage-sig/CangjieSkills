### func getSignatureAlgOid()

```cangjie
public func getSignatureAlgOid(): String
```

**功能：** 表示获取X509证书吊销列表签名算法的对象标识符OID(Object Identifier)。OID是由国际标准组织(ISO)的名称注册机构分配。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|表示X509证书吊销列表签名算法的对象标识符OID。|

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
let sigAlgOid = x509Crl.getSignatureAlgOid()
```

### func getSignatureAlgParams()

```cangjie
public func getSignatureAlgParams(): DataBlob
```

**功能：** 表示获取X509证书吊销列表签名的算法参数。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#class-datablob)|表示X509证书吊销列表签名的算法参数。|

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

let crlData = "test crl"
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
let sigAlgParam = x509Crl.getSignatureAlgParams().data
```

### func getTBSInfo()

```cangjie
public func getTBSInfo(): DataBlob
```

**功能：** 表示获取证书吊销列表的tbsCertList信息。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#class-datablob)|表示证书吊销列表的tbsCertList信息。|

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
let tbsData = x509Crl.getTBSInfo().data
```

### func getType()

```cangjie
public func getType(): String
```

**功能：** 表示获取证书吊销列表类型。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|表示证书吊销列表类型。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

let crlData = "test crl"
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
let revokedType = x509Crl.getType()
```

### func getVersion()

```cangjie
public func getVersion(): Int32
```

**功能：** 表示获取X509证书吊销列表的版本号。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|表示获取X509证书吊销列表的版本号。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

let crlData = "test crl"
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
let version = x509Crl.getVersion()
```