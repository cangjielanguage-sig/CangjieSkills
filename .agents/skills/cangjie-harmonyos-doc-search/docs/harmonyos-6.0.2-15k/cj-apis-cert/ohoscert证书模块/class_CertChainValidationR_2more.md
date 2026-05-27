## class CertChainValidationResult

```cangjie
public class CertChainValidationResult {}
```

**功能：** 表示证书链校验的返回值。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

### let entityCert

```cangjie
public let entityCert: X509Cert
```

**功能：** 表示实体证书。

**类型：** [X509Cert](#class-x509cert)

**读写能力：** 只读

**起始版本：** 19

### let trustAnchor

```cangjie
public let trustAnchor: X509TrustAnchor
```

**功能：** 表示信任锚。

**类型：** [X509TrustAnchor](#class-x509trustanchor)

**读写能力：** 只读

**起始版本：** 19

## class CertChainValidator

```cangjie
public class CertChainValidator {}
```

**功能：** 表示证书链校验器对象。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

### let algorithm

```cangjie
public let algorithm: String
```

**功能：** 表示X509证书链校验器算法名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### func validate(CertChainData)

```cangjie
public func validate(certChain: CertChainData): Unit
```

**功能：** 表示校验X509证书链。由于端侧系统时间不可信，证书链校验不包含对证书有效时间的校验。如果需要检查证书的时间有效性，可使用X509证书的[checkValidityWithDate](#func-checkvaliditywithdatestring)方法进行检查。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|certChain|[CertChainData](#class-certchaindata)|是|表示X509证书链序列化数据。|

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

let validator = createCertChainValidator("PKIX")
let bs: Array<UInt8> = [183, 4, 45, 45, 45, 45]   //example data
let certChainData = CertChainData(bs, 2, EncodingFormat.FORMAT_PEM)
validator.validate(certChainData)
```