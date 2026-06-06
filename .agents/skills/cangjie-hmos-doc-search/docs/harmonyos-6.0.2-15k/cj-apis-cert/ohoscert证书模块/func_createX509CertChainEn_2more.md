## func createX509CertChain(EncodingBlob)

```cangjie
public func createX509CertChain(inStream: EncodingBlob): X509CertChain
```

**功能：** 表示创建X509证书链对象，并返回结果。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|inStream|[EncodingBlob](#class-encodingblob)|是|X509证书序列化数据。|

**返回值：**

|类型|说明|
|:----|:----|
|[X509CertChain](#class-x509certchain)|表示X509证书链对象。|

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

let certChainData = "test certChain data"
let x509CertChain = createX509CertChain(EncodingBlob(certChainData.toArray(), EncodingFormat.FORMAT_PEM))
```

## func createX509CertChain(Array\<X509Cert>)

```cangjie
public func createX509CertChain(certs: Array<X509Cert>): X509CertChain
```

**功能：** 表示使用X509Cert数组方式创建X509证书链对象，并同步返回结果。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|certs|Array\<[X509Cert](#class-x509cert)>|是|X509证书对象数组。|

**返回值：**

|类型|说明|
|:----|:----|
|[X509CertChain](#class-x509certchain)|表示X509证书链对象。|

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

let certChainData1 = "test certChain data1"
let certChainData2 = "test certChain data2"
let certChainData3 = "test certChain data3"
let cert1 = createX509Cert(EncodingBlob(certChainData1.toArray(), EncodingFormat.FORMAT_PEM))
let cert2 = createX509Cert(EncodingBlob(certChainData2.toArray(), EncodingFormat.FORMAT_PEM))
let cert3 = createX509Cert(EncodingBlob(certChainData3.toArray(), EncodingFormat.FORMAT_PEM))
let x509CertChain = createX509CertChain([cert1, cert2, cert3])
```