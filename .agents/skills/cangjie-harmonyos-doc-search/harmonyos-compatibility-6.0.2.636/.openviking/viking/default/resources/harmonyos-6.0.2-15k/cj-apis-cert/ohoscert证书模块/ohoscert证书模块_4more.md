# ohos.cert（证书模块）

证书算法库提供证书相关API。其中，依赖加解密算法库框架基础算法能力的部分，详见[cryptoFramework](../CryptoArchitectureKit/cj-apis-crypto.md)。

## 导入模块

```cangjie
import kit.DeviceCertificateKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func buildX509CertChain(CertChainBuildParameters)

```cangjie
public func buildX509CertChain(buildParams: CertChainBuildParameters): CertChainBuildResult
```

**功能：** 表示使用CertChainBuildParameters创建X509证书链对象，并返回结果。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|buildParams|[CertChainBuildParameters](#class-certchainbuildparameters)|是|构建证书链的参数对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[CertChainBuildResult](#class-certchainbuildresult)|表示X509证书链对象。|

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

let certPem = "test certPem data"
let caPem = "test caPem data"
let caCert = createX509Cert(EncodingBlob(caPem.toArray(), EncodingFormat.FORMAT_PEM))
let x509Cert = createX509Cert(EncodingBlob(certPem.toArray(), EncodingFormat.FORMAT_PEM))
let certCrlCollection = createCertCRLCollection([x509Cert], Option.None)

var anchor = X509TrustAnchor()
anchor.CACert = caCert
var certMatchParameters = X509CertMatchParameters()
certMatchParameters.validDate = "20240812080000Z"
var validationParameters = CertChainValidationParameters(trustAnchors: [anchor, anchor])
validationParameters.certCRLs = [certCrlCollection]
validationParameters.date = "20240812080000Z"
var param = CertChainBuildParameters(certMatchParameters, validationParameters)

let certChainBuildResult = buildX509CertChain(param)
```