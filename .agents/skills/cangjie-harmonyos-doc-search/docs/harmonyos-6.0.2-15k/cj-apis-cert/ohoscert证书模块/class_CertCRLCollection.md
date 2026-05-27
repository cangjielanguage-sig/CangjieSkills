## class CertCRLCollection

```cangjie
public class CertCRLCollection {}
```

**功能：** 表示证书和证书吊销列表集合。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

### func selectCRLs(X509CRLMatchParameters)

```cangjie
public func selectCRLs(param: X509CRLMatchParameters): Array<X509CRL>
```

**功能：** 在证书和证书吊销列表集合中，查找所有与参数匹配的证书吊销列表对象，并返回结果。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|param|[X509CRLMatchParameters](#class-x509crlmatchparameters)|是|表示证书吊销列表需匹配的参数。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[X509CRL](#class-x509crl)>|表示匹配到的证书对象数组。|

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
let crlData = "test crl"
let x509Cert = createX509Cert(EncodingBlob(certData.toArray(), EncodingFormat.FORMAT_PEM))
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
let collection = createCertCRLCollection([x509Cert], [x509Crl])
var crlParam = X509CRLMatchParameters()
crlParam.x509Cert = x509Cert
let crls = collection.selectCRLs(crlParam)
```

### func selectCerts(X509CertMatchParameters)

```cangjie
public func selectCerts(param: X509CertMatchParameters): Array<X509Cert>
```

**功能：** 在证书和证书吊销列表集合中，查找所有与参数匹配的证书对象。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|param|[X509CertMatchParameters](#class-x509certmatchparameters)|是|表示证书需匹配的参数。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[X509Cert](#class-x509cert)>|表示匹配到的证书对象数组。|

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
let crlData = "test crl"
let x509Cert = createX509Cert(EncodingBlob(certData.toArray(), EncodingFormat.FORMAT_PEM))
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
let collection = createCertCRLCollection([x509Cert], [x509Crl])
var certParam = X509CertMatchParameters()
certParam.validDate = "231128000000Z"
let certs = collection.selectCerts(certParam)
```