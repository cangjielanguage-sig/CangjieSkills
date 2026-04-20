# ohos.net.networkSecurity（网络安全）

本模块提供网络安全校验能力。应用可以通过证书校验API完成证书校验功能。

## 导入模块

```cangjie
import kit.NetworkKit.*
```

## 权限列表

ohos.permission.INTERNET

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func certVerification(CertBlob, ?CertBlob)

```cangjie
public func certVerification(cert: CertBlob, caCert!: ?CertBlob = None): Int64
```

**功能：** 从证书管理获取系统预置的CA证书和用户安装的CA证书，对应用传入的证书进行校验。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cert|[CertBlob](#class-certblob)|是|-| 被校验的证书。|
|caCert|?[CertBlob](#class-certblob)|否|None| **命名参数。** 传入自定义的CA证书。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|表示证书验证的结果。如果证书验证成功，则返回0；否则验证失败。|

**异常：**

- BusinessException：对应错误码和错误信息如下所示。

  |错误码ID|错误信息|
  |:---|:---|
  |2305001|Unspecified error.|
  |2305002|Unable to get issuer certificate.|
  |2305003|Unable to get certificate revocation list (CRL).|
  |2305004|Unable to decrypt certificate signature.|
  |2305005|Unable to decrypt CRL signature.|
  |2305006|Unable to decode issuer public key.|
  |2305007|Certificate signature failure.|
  |2305008|CRL signature failure.|
  |2305009|Certificate is not yet valid.|
  |2305010|Certificate has expired.|
  |2305011|Upload failed.|
  |2305012|Failed to open/read local data from file/application.|
  |2305018|Self-signed certificate.|
  |2305023|Certificate has been revoked.|
  |2305024|Invalid certificate authority (CA).|
  |2305027|Certificate is untrusted.|
  |2305069|Invalid certificate verification context.|

- IllegalArgumentException: 传入证书编码格式和传入的对应编码格式的枚举值不一致，抛出此异常。

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |The cert type and content mismatch.|传入证书编码格式和传入的对应编码格式的枚举值不一致。|检查证书编码格式和编码格式枚举值是否匹配。|

## class CertBlob

```cangjie
public class CertBlob {
    public var data: CertData
    public var `type`: SecurityCertType
    public init(certType: SecurityCertType, certData: CertData)
}
```

**功能：** 表示证书数据。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

### var data

```cangjie
public var data: CertData
```

**功能：** 证书内容。

**类型：** [CertData](#enum-certdata)

**起始版本：** 20

### var \`type`

**功能：** 证书编码类型。

**类型：** [SecurityCertType](#enum-securitycerttype)

**起始版本：** 20

### init(SecurityCertType, CertData)

```cangjie
public init(certType: SecurityCertType, certData: CertData)
```

**功能：** 构造证书数据实例。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|certType|[SecurityCertType](#enum-securitycerttype)|是|-|证书编码类型。|
|certData|[CertData](#enum-certdata)|是|-|证书内容。|