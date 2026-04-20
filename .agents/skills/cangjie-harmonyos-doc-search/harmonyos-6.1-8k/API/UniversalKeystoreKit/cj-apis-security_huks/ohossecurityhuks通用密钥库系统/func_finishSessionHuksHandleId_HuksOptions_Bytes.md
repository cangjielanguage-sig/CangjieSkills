## func finishSession(HuksHandleId, HuksOptions, Bytes)

```cangjie
public func finishSession(handle: HuksHandleId, options: HuksOptions, token!: Bytes = Bytes<UInt8>()): Option<Bytes>
```

**功能：** finishSession操作密钥接口。[security_huks.initSession](#func-initsessionstring-huksoptions)、[security_huks.updateSession](#func-updatesessionhukshandleid-huksoptions-bytes)、[security_huks.finishSession](#func-finishsessionhukshandleid-huksoptions-bytes)为三段式接口，需要一起使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|handle|[HuksHandleId](#class-hukshandleid)|是|-|finishSession操作的handle。|
|options|[HuksOptions](#class-huksoptions)|是|-|finishSession操作的参数集合。|
|token|Bytes|否|Bytes()|**命名参数。** 密钥二次认证密钥访问控制的用户鉴权证明(AuthToken)，不填表示不进行二次认证密钥访问控制。|

**返回值：**

|类型|说明|
|:----|:----|
|Option\<Bytes>|表示USER IAM服务的AuthToken的值。|

**异常：**

- BusinessException：对应错误码如下表，详见[HUKS错误码](./cj-errorcode-huks.md)和[通用错误码](../cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 801 | api is not supported. |
  | 12000001 | algorithm mode is not supported. |
  | 12000002 | algorithm param is missing. |
  | 12000003 | algorithm param is invalid. |
  | 12000004 | operating file failed. |
  | 12000005 | IPC communication failed. |
  | 12000006 | error occurred in crypto engine. |
  | 12000007 | this credential is already invalidated permanently .|
  | 12000008 | verify auth token failed. |
  | 12000009 | auth token is already timeout. |
  | 12000011 | queried entity does not exist. |
  | 12000012 | Device environment or input parameter abnormal. |
  | 12000014 | memory is insufficient. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.UniversalKeystoreKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let keyAlias = "KEY_ALIAS" // 密钥别名，在生成密钥时指定，在加密、解密和删除密钥时使用
    let options = HuksOptions(properties:
        [
            HuksParam(HuksTag.HUKS_TAG_ALGORITHM, Uint32Value(HuksKeyAlg.HUKS_ALG_AES)),
            HuksParam(HuksTag.HUKS_TAG_KEY_SIZE, Uint32Value(HuksKeySize.HUKS_AES_KEY_SIZE_128)),
            HuksParam(
                HuksTag.HUKS_TAG_PURPOSE,
                Uint32Value(HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT)
            ),
            HuksParam(HuksTag.HUKS_TAG_PADDING, Uint32Value(HuksKeyPadding.HUKS_PADDING_PKCS7)),
            HuksParam(HuksTag.HUKS_TAG_BLOCK_MODE, Uint32Value(HuksCipherMode.HUKS_MODE_CBC))
        ]
    )
    generateKeyItem(keyAlias, options)
    // encrypt
    let handle = initSession(keyAlias, options).handle
    let cipherData = finishSession(handle, options)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```