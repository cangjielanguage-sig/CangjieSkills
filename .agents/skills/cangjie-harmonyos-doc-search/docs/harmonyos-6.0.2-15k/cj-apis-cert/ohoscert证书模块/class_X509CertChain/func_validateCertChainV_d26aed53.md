### func validate(CertChainValidationParameters)

```cangjie
public func validate(param: CertChainValidationParameters): CertChainValidationResult
```

**功能：** 校验证书链，并返回结果。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|param|[CertChainValidationParameters](#class-certchainvalidationparameters)|是|表示校验X509证书链的参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[CertChainValidationResult](#class-certchainvalidationresult)|返回证书链校验结果。|

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

var anchor = X509TrustAnchor()
let param = CertChainValidationParameters(trustAnchors: [anchor])
let certChainData = "test certChain data"
let x509CertChain = createX509CertChain(EncodingBlob(certChainData.toArray(), EncodingFormat.FORMAT_PEM))
let validationRes = x509CertChain.validate(param)
```