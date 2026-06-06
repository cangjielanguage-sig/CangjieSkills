## func isAuthorizedApp(String)

```cangjie
public func isAuthorizedApp(keyUri: String): Bool
```

**功能：** 表示当前应用是否由指定的用户凭据授权。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|keyUri|String|是|表示用户授权给应用使用的凭据的唯一标识符。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回查询应用是否被授权的结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书管理错误码](../../errorcodes/cj-errorcode-cert-manager.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission verification failed.|
  |401|Parameter error.|
  |17500001|Internal error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

// 此处代码可添加在依赖项定义中
func asset_query(): Bool {
    let keyUri = "test_isAuthorizedApp"
    let retVal = isAuthorizedApp(keyUri)
    return retVal
}

asset_query()
```

## func uninstallPrivateCertificate(String)

```cangjie
public func uninstallPrivateCertificate(keyUri: String): Unit
```

**功能：** 表示卸载指定的私有凭据。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|keyUri|String|是|表示待卸载凭据的唯一标识符。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书管理错误码](../../errorcodes/cj-errorcode-cert-manager.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission verification failed.|
  |401|Parameter error.|
  |17500001|Internal error.|
  |17500002|The certificate does not exist.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

// 此处代码可添加在依赖项定义中
func cm_uninstallPrivateCertificate(): Unit {
    //以下只是一个示例，需要根据具体业务来赋值
    let g_rsa2048P12CertInfo: Array<UInt8> = [0x30, 0x82, 0x01, 0x22, 0x30, 0x0d]
    let test_certInfo = g_rsa2048P12CertInfo
    let test_passwd = "xxxxxx" // 用户自定义密码
    let test_alias = "test_uninstall"
    let keyUri = installPrivateCertificate(g_rsa2048P12CertInfo, test_passwd, test_alias)
    uninstallPrivateCertificate(keyUri)
}

cm_uninstallPrivateCertificate()
```