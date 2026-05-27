## class X509CertChain

```cangjie
public class X509CertChain <: ToString {}
```

**功能：** 表示X509证书链对象。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**父类型：**

- ToString

### func getCertList()

```cangjie
public func getCertList(): Array<X509Cert>
```

**功能：** 获取X509证书列表。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[X509Cert](#class-x509cert)>|X509证书数组。|

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
let certList = x509CertChain.getCertList()
```

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

let certChainData = "test certChain data"
let x509CertChain = createX509CertChain(EncodingBlob(certChainData.toArray(), EncodingFormat.FORMAT_PEM))
let str = x509CertChain.hashCode()
```

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取对象的字符串类型数据。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|对象的字符串类型数据。|

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

let certChainData = "test certChain data"
let x509CertChain = createX509CertChain(EncodingBlob(certChainData.toArray(), EncodingFormat.FORMAT_PEM))
let str = x509CertChain.toString()
```