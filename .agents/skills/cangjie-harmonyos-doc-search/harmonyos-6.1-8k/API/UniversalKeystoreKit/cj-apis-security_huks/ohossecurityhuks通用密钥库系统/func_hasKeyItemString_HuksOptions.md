## func hasKeyItem(String, HuksOptions)

```cangjie
public func hasKeyItem(keyAlias: String, options: HuksOptions): Bool
```

**功能：** 判断密钥是否存在。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keyAlias|String|是|-|待查找的密钥的别名。|
|options|[HuksOptions](#class-huksoptions)|是|-|用于查询时指定密钥的属性Tag，比如查询的密钥范围（全量/单个），当查询单个时，Tag字段可传空。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|表示密钥是否存在。|

**异常：**

- BusinessException：对应错误码如下表，详见[HUKS错误码](./cj-errorcode-huks.md)和[通用错误码](../cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 801 | api is not supported. |
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
    // 此处代码可添加在依赖项定义中
    func generateSimpleKey(keyAlias: String) {
        let options = HuksOptions(properties:
            [
                HuksParam(HuksTag.HUKS_TAG_ALGORITHM, Uint32Value(HuksKeyAlg.HUKS_ALG_AES)),
                HuksParam(HuksTag.HUKS_TAG_KEY_SIZE, Uint32Value(HuksKeySize.HUKS_AES_KEY_SIZE_128)),
                HuksParam(
                    HuksTag.HUKS_TAG_PURPOSE,
                    Uint32Value(HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT)
                )
            ]
        )
        generateKeyItem(keyAlias, options)
    }

    let keyAlias = "KEY_ALIAS" // 密钥别名，在生成密钥时指定，在加密、解密和删除密钥时使用
    var result = hasKeyItem(keyAlias, HuksOptions()) // false
    generateSimpleKey(keyAlias)
    result = hasKeyItem(keyAlias, HuksOptions()) // true
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```