## func initSession(String, HuksOptions)

```cangjie
public func initSession(keyAlias: String, options: HuksOptions): HuksSessionHandle
```

**功能：** initSession操作密钥接口。[security_huks.initSession](#func-initsessionstring-huksoptions)、[security_huks.updateSession](#func-updatesessionhukshandleid-huksoptions-bytes)、[security_huks.finishSession](#func-finishsessionhukshandleid-huksoptions-bytes)为三段式接口，需要一起使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keyAlias|String|是|-|initSession操作密钥的别名。|
|options|[HuksOptions](#class-huksoptions)|是|-|initSession操作的参数集合。|

**返回值：**

|类型|说明|
|:----|:----|
|[HuksSessionHandle](#class-hukssessionhandle)|返回密钥huks Handle。|

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
  | 12000010 | the number of sessions has reached limit. |
  | 12000011 | queried entity does not exist. |
  | 12000012 | Device environment or input parameter abnormal. |
  | 12000014 | memory is insufficient. |
  | 12000018 | the input parameter is invalid. |

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
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```