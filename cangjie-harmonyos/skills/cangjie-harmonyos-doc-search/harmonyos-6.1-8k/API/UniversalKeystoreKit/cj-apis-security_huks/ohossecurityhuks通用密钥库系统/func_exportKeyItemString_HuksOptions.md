## func exportKeyItem(String, HuksOptions)

```cangjie
public func exportKeyItem(keyAlias: String, _: HuksOptions): Bytes
```

**功能：** 导出密钥。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keyAlias|String|是|-|密钥别名，应与所用密钥生成时使用的别名相同。|
|_|[HuksOptions](#class-huksoptions)|是|-|空对象（此处传空即可）。|

**返回值：**

|类型|说明|
|:----|:----|
|Bytes|<返回从密钥中导出的公钥。|

**异常：**

- BusinessException：对应错误码如下表，详见[HUKS错误码](./cj-errorcode-huks.md)和[通用错误码](../cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 801 | api is not supported. |
  | 12000001 | algorithm mode is not supported. |
  | 12000004 | operating file failed. |
  | 12000005 | IPC communication failed. |
  | 12000006 | error occurred in crypto engine. |
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
    /* 1. Generate Key */
    generateKeyItem(
        keyAlias,
        HuksOptions(properties:
            [
                HuksParam(HuksTag.HUKS_TAG_ALGORITHM, Uint32Value(HuksKeyAlg.HUKS_ALG_ECC)),
                HuksParam(HuksTag.HUKS_TAG_KEY_SIZE, Uint32Value(HuksKeySize.HUKS_ECC_KEY_SIZE_256)),
                HuksParam(
                    HuksTag.HUKS_TAG_PURPOSE,
                    Uint32Value(HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY | HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
                )),
                HuksParam(HuksTag.HUKS_TAG_DIGEST, Uint32Value(HuksKeyDigest.HUKS_DIGEST_SHA256))
            ]
        )
    )
    /* 2. Export Key */
    let data = exportKeyItem(keyAlias, HuksOptions())
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```