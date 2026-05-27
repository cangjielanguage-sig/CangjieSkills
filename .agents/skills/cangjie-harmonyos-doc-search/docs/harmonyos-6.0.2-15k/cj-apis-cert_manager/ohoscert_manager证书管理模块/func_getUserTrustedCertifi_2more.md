## func getUserTrustedCertificate(String)

```cangjie
public func getUserTrustedCertificate(certUri: String): CertInfo
```

**功能：** 表示获取用户根CA证书的详细信息。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|certUri|String|是|表示用户用户根CA证书的唯一标识符。|

**返回值：**

|类型|说明|
|:----|:----|
|[CertInfo](#class-certinfo)|返回获取用户根CA证书详细信息的结果。|

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
func cm_getUserTrustedCertificate(): CertInfo {
    let certList = getAllUserTrustedCertificates()
    let info = getUserTrustedCertificate(certList[0].uri)
    return info
}

cm_getUserTrustedCertificate()
```

## func installPrivateCertificate(Array\<UInt8>, String, String)

```cangjie
public func installPrivateCertificate(keystore: Array<UInt8>, keystorePwd: String, certAlias: String): String
```

**功能：** 表示安装私有凭据。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|keystore|Array\<UInt8>|是|表示带有密钥对和证书的密钥库文件。|
|keystorePwd|String|是|表示密钥库文件的密码，长度限制32字节以内。|
|certAlias|String|是|表示用户输入的凭据别名，当前仅支持传入数字、字母或下划线，长度建议32字节以内。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回安装私有凭据的结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[证书管理错误码](../../errorcodes/cj-errorcode-cert-manager.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission verification failed.|
  |401|Parameter error.|
  |17500001|Internal error.|
  |17500003|The keystore is in an invalid format or the keystore password is incorrect.|
  |17500004|The number of certificates or credentials reaches the maximum allowed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.DeviceCertificateKit.*

// 此处代码可添加在依赖项定义中
func cm_installPrivateCertificate(): String {
    //以下只是一个示例，需要根据具体业务来赋值
    let g_rsa2048P12CertInfo: Array<UInt8> = [0x30, 0x82, 0x01, 0x22, 0x30, 0x0d]
    let test_certInfo = g_rsa2048P12CertInfo
    let test_passwd = "xxxxxx" // 用户自定义密码
    let test_alias = "test_install"
    let keyUri = installPrivateCertificate(g_rsa2048P12CertInfo, test_passwd, test_alias)
    return keyUri
}

cm_installPrivateCertificate()
```