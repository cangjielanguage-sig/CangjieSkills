## class X509Cert

```cangjie
public class X509Cert <: ToString {}
```

**功能：** 表示X509证书类。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**父类型：**

- ToString

### func checkValidityWithDate(String)

```cangjie
public func checkValidityWithDate(date: String): Unit
```

**功能：** 表示检查X509证书有效期。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|date|String|是|日期，为ASN.1时间格式。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书错误码](../../errorcodes/cj-errorcode-cert-framework.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |19020001|memory error.|
  |19030001|crypto operation error.|
  |19030003|the certificate has not taken effect.|
  |19030004|the certificate has expired.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

let certData = "example certdata"
let x509Cert = createX509Cert(EncodingBlob(certData.toArray(), EncodingFormat.FORMAT_PEM))
let date = '20230930000001Z'
x509Cert.checkValidityWithDate(date)
```

### func getBasicConstraints()

```cangjie
public func getBasicConstraints(): Int32
```

**功能：** 表示获取X509证书基本约束。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|表示X509证书基本约束。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

let certData = "example certdata"
let x509Cert = createX509Cert(EncodingBlob(certData.toArray(), EncodingFormat.FORMAT_PEM))
let cons = x509Cert.getBasicConstraints()
```

### func getCRLDistributionPoint()

```cangjie
public func getCRLDistributionPoint(): Array<DataBlob>
```

**功能：** 获取X509证书CRL的分发点统一资源标识符。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[DataBlob](#class-datablob)>|表示X509证书CRL的分发点统一资源标识符。|

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
let dp = x509Cert.getCRLDistributionPoint()
```

### func getCertSerialNumber()

```cangjie
public func getCertSerialNumber(): BigInt
```

**功能：** 表示获取X509证书序列号。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|BigInt|表示X509证书序列号。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书错误码](../../errorcodes/cj-errorcode-cert-framework.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |19020002|runtime error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

let certData = "example certdata"
let x509Cert = createX509Cert(EncodingBlob(certData.toArray(), EncodingFormat.FORMAT_PEM))
let serial = x509Cert.getCertSerialNumber()
```