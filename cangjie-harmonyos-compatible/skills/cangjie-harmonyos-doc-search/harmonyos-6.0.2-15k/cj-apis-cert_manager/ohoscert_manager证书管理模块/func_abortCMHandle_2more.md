## func abort(CMHandle)

```cangjie
public func abort(handle: CMHandle): Unit
```

**功能：** 表示中止签名、验签的操作。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|handle|[CMHandle](#class-cmhandle)|是|表示初始化操作返回的句柄。|

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

//以下只是一个示例，需要根据具体业务来赋值
let g_rsa2048P12CertInfo: Array<UInt8> = [0x30, 0x82, 0x01, 0x22, 0x30, 0x0d]
let test_certInfo = g_rsa2048P12CertInfo
let test_passwd = "xxxxxx" // 用户自定义密码
let test_alias = "test_install"
var keyUri = installPrivateCertificate(g_rsa2048P12CertInfo, test_passwd, test_alias)

let spec: CMSignatureSpec = CMSignatureSpec(CmKeyPurpose.CM_KEY_PURPOSE_SIGN, CmKeyPadding.CM_PADDING_PSS, CmKeyDigest.CM_DIGEST_SHA256)
let handle1: CMHandle = `init`(keyUri, spec)
let data: Array<UInt8> = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08]
update(handle1, data)
abort(handle1)
uninstallPrivateCertificate(keyUri)
```

## func finish(CMHandle, Array\<UInt8>)

```cangjie
public func finish(handle: CMHandle, signature: Array<UInt8>): Unit
```

**功能：** 表示完成验签的操作。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|handle|[CMHandle](#class-cmhandle)|是|表示初始化操作返回的句柄。|
|signature|Array\<UInt8>|是|表示签名数据。|

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

//以下只是一个示例，需要根据具体业务来赋值
let g_rsa2048P12CertInfo: Array<UInt8> = [0x30, 0x82, 0x01, 0x22, 0x30, 0x0d]
let signRes: Array<UInt8> = [0]
let test_certInfo = g_rsa2048P12CertInfo
let test_passwd = "xxxxxx" // 用户自定义密码
let test_alias = "test_install"
var keyUri = installPrivateCertificate(g_rsa2048P12CertInfo, test_passwd, test_alias)

let spec: CMSignatureSpec = CMSignatureSpec(CmKeyPurpose.CM_KEY_PURPOSE_SIGN, CmKeyPadding.CM_PADDING_PSS, CmKeyDigest.CM_DIGEST_SHA256)
let handle1: CMHandle = `init`(keyUri, spec)
let data: Array<UInt8> = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08]
update(handle1, data)
finish(handle1, signRes)
uninstallPrivateCertificate(keyUri)
```