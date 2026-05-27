# ohos.cert_manager（证书管理模块）

证书管理主要提供系统级的证书管理能力，实现证书全生命周期（安装，存储，使用，销毁）的管理和安全使用。

## 导入模块

```cangjie
import kit.DeviceCertificateKit.*
```

## 权限列表

ohos.permission.ACCESS_CERT_MANAGER

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func \`init\`(String, CMSignatureSpec)

```cangjie
public func `init`(authUri: String, spec: CMSignatureSpec): CMHandle
```

**功能：** 表示使用凭据进行签名、验签的初始化操作。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|authUri|String|是|表示使用凭据的唯一标识符。|
|spec|[CMSignatureSpec](#class-cmsignaturespec)|是|表示签名、验签的属性。|

**返回值：**

|类型|说明|
|:----|:----|
|[CMHandle](#class-cmhandle)|返回签名、验签的初始化操作结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书管理错误码](../../errorcodes/cj-errorcode-cert-manager.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission verification failed.|
  |401|Parameter error.|
  |17500001|Internal error.|
  |17500002|The certificate does not exist.|
  |17500005|Permission verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

// 此处代码可添加在依赖项定义中
func cm_init(): CMHandle {
    //以下只是一个示例，需要根据具体业务来赋值
    let g_rsa2048P12CertInfo: Array<UInt8> = [0x30, 0x82, 0x01, 0x22, 0x30, 0x0d]
    let test_certInfo = g_rsa2048P12CertInfo
    let test_passwd = "xxxxxx" // 用户自定义密码
    let test_alias = "test_install"
    var keyUri = installPrivateCertificate(g_rsa2048P12CertInfo, test_passwd, test_alias)

    let spec: CMSignatureSpec = CMSignatureSpec(CmKeyPurpose.CM_KEY_PURPOSE_SIGN, CmKeyPadding.CM_PADDING_PSS, CmKeyDigest.CM_DIGEST_SHA256)
    let handle1: CMHandle = `init`(keyUri, spec)
    uninstallPrivateCertificate(keyUri)
    return handle1
    }

cm_init()
```