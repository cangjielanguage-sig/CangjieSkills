# 证书管理开发指导

> **说明:**
>
> 本开发指导需使用API version 12及以上版本SDK。

## 场景说明

1. 典型场景：

   - 安装应用证书和私有凭据。
   - 获取应用证书和私有凭据。
   - 使用应用证书和私有凭据对数据进行签名、验签。
   - 卸载指定的应用证书和私有凭据。

2. 支持安装的私有凭据算法类型&签名验签支持的参数组合。

   证书管理安装凭据及使用凭据中的密钥进行签名、验签，依赖[通用密钥库](../UniversalKeystoreKit/cj-huks-overview.md)（HUKS）能力，证书管理支持的算法为其子集，当前仅支持RSA及ECC算法类型的私有凭据安装及使用。签名、验签支持的参数组合，详情请参见HUKS声明的[签名/验签介绍及算法规格](../UniversalKeystoreKit/cj-huks-signing-signature-verification-overview.md)中RSA及ECC的描述。

## 接口说明

详细接口说明可参见[API参考](../../../API_Reference/source_zh_cn/apis/DeviceCertificateKit/cj-apis-cert_manager.md)。

以上场景涉及的常用接口如下表所示：

|实例名| 接口名|描述|
| --------------- | ------------------------------------------------------------ | -------------------------------------------- |
| certificateManager  | installPrivateCertificate(keystore: Array\<UInt8>, keystorePwd: String, certAlias: String): String | 安装私有凭据。|
| certificateManager | getPrivateCertificate(keyUri: String): Credential| 获取应用私有凭据详情。|
| certificateManager | uninstallPrivateCertificate(keyUri: String): Unit | 卸载指定的私有凭据。|
| certificateManager | \`init\`(authUri: String, spec: CMSignatureSpec): CMHandle| 使用凭据进行签名、验签的初始化操作。|
| certificateManager| update(handle: CMHandle, data: Array\<UInt8>): Unit | 签名、验签的数据更新操作。|
| certificateManager | finish(handle: CMHandle): Array\<UInt8> |完成数据的签名操作。|
| certificateManager |abort(handle: CMHandle): Unit | 中止签名、验证操作。|