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

let crlData = "test crl"
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
let crlHash = x509Crl.hashCode()
```

### func isMatch(X509CRLMatchParameters)

```cangjie
public func isMatch(param: X509CRLMatchParameters): Bool
```

**功能：** 判断证书吊销列表是否与输入参数匹配。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|param|[X509CRLMatchParameters](#class-x509crlmatchparameters)|是|表示需要匹配的参数。|

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

let crlData = "test crl"
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
let certData = "test cert"
let x509Cert = createX509Cert(EncodingBlob(certData.toArray(), EncodingFormat.FORMAT_PEM))
var matchParam = X509CRLMatchParameters()
matchParam.x509Cert = x509Cert
let ismatch = x509Crl.isMatch(matchParam)
```

### func isRevoked(X509Cert)

```cangjie
public func isRevoked(cert: X509Cert): Bool
```

**功能：** 表示检查证书是否吊销。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|cert|[X509Cert](#class-x509cert)|是|表示被检查的证书对象。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|表示证书吊销状态，true表示已吊销，false表示未吊销。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

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