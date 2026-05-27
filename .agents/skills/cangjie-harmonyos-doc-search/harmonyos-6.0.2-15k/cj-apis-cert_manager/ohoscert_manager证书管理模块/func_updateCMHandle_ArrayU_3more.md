## func update(CMHandle, Array\<UInt8>)

```cangjie
public func update(handle: CMHandle, data: Array<UInt8>): Unit
```

**功能：** 表示签名、验签的数据更新操作。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|handle|[CMHandle](#class-cmhandle)|是|表示初始化操作返回的句柄。|
|data|Array\<UInt8>|是|表示待签名、验签的数据。|

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
func cm_update(): Unit {
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
    uninstallPrivateCertificate(keyUri)
}

cm_update()
```

## class CMHandle

```cangjie
public class CMHandle {}
```

**功能：** 表示签名、验签的初始化操作句柄。

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

## class CMSignatureSpec

```cangjie
public class CMSignatureSpec {
    public CMSignatureSpec(
        public var purpose: CmKeyPurpose,
        public var padding: ?CmKeyPadding,
        public var digest: ?CmKeyDigest
    )
}
```

**功能：** 表示签名、验签操作使用的参数集合，包括密钥使用目的、填充方式和摘要算法。

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

### var digest

```cangjie
public var digest: ?CmKeyDigest
```

**功能：** 表示摘要算法。

**类型：** ?[CmKeyDigest](#enum-cmkeydigest)

**读写能力：** 可读写

**起始版本：** 19

### var padding

```cangjie
public var padding: ?CmKeyPadding
```

**功能：** 表示填充方式。

**类型：** ?[CmKeyPadding](#enum-cmkeypadding)

**读写能力：** 可读写

**起始版本：** 19

### var purpose

```cangjie
public var purpose: CmKeyPurpose
```

**功能：** 表示密钥使用目的。

**类型：** [CmKeyPurpose](#enum-cmkeypurpose)

**读写能力：** 可读写

**起始版本：** 19

### CMSignatureSpec(CmKeyPurpose, ?CmKeyPadding, ?CmKeyDigest)

```cangjie
public CMSignatureSpec(
    public var purpose: CmKeyPurpose,
    public var padding: ?CmKeyPadding,
    public var digest: ?CmKeyDigest
)
```

**功能：** 构建CMSignatureSpec实例。

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|purpose|[CmKeyPurpose](#enum-cmkeypurpose)|是|表示密钥使用目的。|
|padding|?[CmKeyPadding](#enum-cmkeypadding)|是|表示填充方式。|
|digest|?[CmKeyDigest](#enum-cmkeydigest)|是|表示摘要算法。|