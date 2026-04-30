## func createCertCRLCollection(Array\<X509Cert>, ?Array\<X509CRL>)

```cangjie
public func createCertCRLCollection(certs: Array<X509Cert>, crls: ?Array<X509CRL>): CertCRLCollection
```

**功能：** 表示创建证书和证书吊销列表集合对象，并返回相应的结果。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|certs|Array\<[X509Cert](#class-x509cert)>|是|X509Cert数组。|
|crls|?Array\<[X509CRL](#class-x509crl)>|是|X509CRL数组。|

**返回值：**

|类型|说明|
|:----|:----|
|[CertCRLCollection](#class-certcrlcollection)|表示证书和证书吊销列表集合对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书错误码](../../errorcodes/cj-errorcode-cert-framework.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |19020001|memory error.|

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
```

## func createCertChainValidator(String)

```cangjie
public func createCertChainValidator(algorithm: String): CertChainValidator
```

**功能：** 表示创建证书链校验器对象。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|algorithm|String|是|表示证书链校验器算法。当前仅支持输入“PKIX”。|

**返回值：**

|类型|说明|
|:----|:----|
|[CertChainValidator](#class-certchainvalidator)|表示证书链校验器对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书错误码](../../errorcodes/cj-errorcode-cert-framework.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |801|Capability not supported.|
  |19020001|memory error.|
  |19020002|runtime error.|
  |19030001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

let validator = createCertChainValidator("PKIX")
let bs: Array<UInt8> = [183, 4, 45, 45, 45, 45] //example data
let certChainData = CertChainData(bs, 2, EncodingFormat.FORMAT_PEM)
```

## func createCertExtension(EncodingBlob)

```cangjie
public func createCertExtension(inStream: EncodingBlob): CertExtension
```

**功能：** 表示创建证书扩展域段的对象。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|inStream|[EncodingBlob](#class-encodingblob)|是|表示证书扩展域段序列化数据。|

**返回值：**

|类型|说明|
|:----|:----|
|[CertExtension](#class-certextension)|表示证书扩展域段对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书错误码](../../errorcodes/cj-errorcode-cert-framework.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |801|Capability not supported.|
  |19020001|memory error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

let extensionData: Array<UInt8> = [0x30, 0x40, 0x30, 0x0F, 0x06] //example data
let ext = createCertExtension(EncodingBlob(extensionData, EncodingFormat.FORMAT_DER))
```