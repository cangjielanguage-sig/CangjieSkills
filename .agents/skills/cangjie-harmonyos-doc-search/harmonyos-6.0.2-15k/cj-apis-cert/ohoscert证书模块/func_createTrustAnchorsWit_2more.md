## func createTrustAnchorsWithKeyStore(Array\<UInt8>, String)

```cangjie
public func createTrustAnchorsWithKeyStore(keystore: Array<UInt8>, pwd: String): Array<X509TrustAnchor>
```

**功能：** 表示从P12文件中读取ca证书来构造[TrustAnchor](#class-x509trustanchor)对象数组，并返回结果。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|keystore|Array\<UInt8>|是|p12文件，DER格式。|
|pwd|String|是|p12文件的密码。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[X509TrustAnchor](#class-x509trustanchor)>|表示X509TrustAnchor对象数组。|

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

let p12Data: Array<UInt8> = [0x30, 0x82, 0x07, 0x5C, 0x02] //example data
let data: Array<X509TrustAnchor> = createTrustAnchorsWithKeyStore(p12Data, "123456")
```

## func createX500DistinguishedName(String)

```cangjie
public func createX500DistinguishedName(nameStr: String): X500DistinguishedName
```

**功能：** 表示使用字符串格式的名称创建X500DistinguishedName对象，并返回结果。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|nameStr|String|是|X509定义的String类型的Name字符串格式数据。|

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

let nameStr = '/CN=John Doe/OU=IT Department/O=ACME Inc./L=San Francisco/ST=California/C=US/CN=ALN C/CN=XTS'
let dgName = createX500DistinguishedName(nameStr)
```