## func createX500DistinguishedName(Array\<UInt8>)

```cangjie
public func createX500DistinguishedName(nameDer: Array<UInt8>): X500DistinguishedName
```

**功能：** 表示使用DER格式的名称创建X500DistinguishedName对象，并返回结果。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|nameDer|Array\<UInt8>|是|X509定义的Array\<UInt8>类型的DER格式数据。|

**返回值：**

|类型|说明|
|:----|:----|
|[X500DistinguishedName](#class-x500distinguishedname)|表示X509的可分辨对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书错误码](../../errorcodes/cj-errorcode-cert-framework.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |19020001|memory error.|
  |19020002|runtime error.|
  |19030001|crypto operation error.|
  |19030002|the certificate signature verification failed.|
  |19030003|the certificate has not taken effect.|
  |19030004|the certificate has expired.|
  |19030005|failed to obtain the certificate issuer.|
  |19030006|the key cannot be used for signing a certificate.|
  |19030007|the key cannot be used for digital signature.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

let nameBlob: Array<UInt8> = [48, 41, 49, 11, 48, 9, 6, 3, 85, 4, 3, 12, 2, 67, 65, 49, 13, 48, 11, 6, 3, 85, 4, 10, 12,
    4, 116, 101, 115, 116, 49, 11, 48, 9, 6, 3, 85, 4, 6, 19, 2, 67, 78]
let dgname = createX500DistinguishedName(nameBlob)
```

## func createX509CRL(EncodingBlob)

```cangjie
public func createX509CRL(inStream: EncodingBlob): X509CRL
```

**功能：** 表示创建X509证书吊销列表的对象。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|inStream|[EncodingBlob](#class-encodingblob)|是|表示证书吊销列表序列化数据。|

**返回值：**

|类型|说明|
|:----|:----|
|[X509CRL](#class-x509crl)| 表示X509证书吊销列表的对象。|

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

let crlData = "example data"
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
```

## func createX509Cert(EncodingBlob)

```cangjie
public func createX509Cert(inStream: EncodingBlob): X509Cert
```

**功能：** 表示创建X509证书对象。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|inStream|[EncodingBlob](#class-encodingblob)|是|X509证书序列化数据。|

**返回值：**

|类型|说明|
|:----|:----|
|[X509Cert](#class-x509cert)|表示X509证书对象。|

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

let crlData = "example data"
let x509Crl = createX509CRL(EncodingBlob(crlData.toArray(), EncodingFormat.FORMAT_PEM))
```