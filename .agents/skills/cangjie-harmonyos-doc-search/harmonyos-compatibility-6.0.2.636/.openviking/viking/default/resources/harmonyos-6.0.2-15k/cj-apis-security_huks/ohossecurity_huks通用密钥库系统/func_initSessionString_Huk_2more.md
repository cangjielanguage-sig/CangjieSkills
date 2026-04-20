## func initSession(String, HuksOptions)

```cangjie
public func initSession(keyAlias: String, options: HuksOptions): HuksSessionHandle
```

**功能：** initSession操作密钥接口。[security_huks.initSession](#func-initsessionstring-huksoptions)、[security_huks.updateSession](#func-updatesessionhukshandle-huksoptions)、[security_huks.finishSession](#func-finishsessionhukshandle-huksoptions)为三段式接口，需要一起使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|keyAlias|String|是|initSession操作密钥的别名。|
|options|[HuksOptions](#class-huksoptions)|是|initSession操作的参数集合。|

**返回值：**

|类型|说明|
|:----|:----|
|[HuksSessionHandle](#class-hukssessionhandle)|返回密钥huks Handle。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[HUKS错误码](../../errorcodes/cj-errorcode-huks.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |801|Capability not supported.|
  |12000001|algorithm mode is not supported.|
  |12000002|algorithm param is missing.|
  |12000003|algorithm param is invalid.|
  |12000004|operating file failed.|
  |12000005|IPC communication failed.|
  |12000006|error occurred in crypto engine.|
  |12000010|the number of sessions has reached limit.|
  |12000011|queried entity does not exist.|
  |12000012|external error.|
  |12000014|memory is insufficient.|

## func isKeyItemExist(String, HuksOptions)

```cangjie
public func isKeyItemExist(keyAlias: String, options: HuksOptions): Bool
```

**功能：** 判断密钥是否存在。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|keyAlias|String|是|待查找的密钥的别名。|
|options|[HuksOptions](#class-huksoptions)|是|用于查询时指定密钥的属性Tag，比如查询的密钥范围（全量/单个），当查询单个时，Tag字段可传空。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|表示密钥是否存在。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[HUKS错误码](../../errorcodes/cj-errorcode-huks.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |801|Capability not supported.|
  |12000002|algorithm param is missing.|
  |12000003|algorithm param is invalid.|
  |12000004|operating file failed.|
  |12000005|IPC communication failed.|
  |12000006|error occurred in crypto engine.|
  |12000012|external error.|
  |12000014|memory is insufficient.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.UniversalKeystoreKit.*

// 此处代码可添加在依赖项定义中
func generateSimpleKey(keyAlias: String) {
    let options = HuksOptions(
        [
            HuksParam(HuksTag.HUKS_TAG_ALGORITHM, HuksKeyAlg.HUKS_ALG_AES),
            HuksParam(HuksTag.HUKS_TAG_KEY_SIZE, HuksKeySize.HUKS_AES_KEY_SIZE_128),
            HuksParam(
                HuksTag.HUKS_TAG_PURPOSE,
                HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
            )
        ],
        Option.None
    )
    generateKeyItem(keyAlias, options)
}

let keyAlias = "test_is_key_item_exist"
isKeyItemExist(keyAlias, HuksOptions.NONE) // false
generateSimpleKey(keyAlias)
isKeyItemExist(keyAlias, HuksOptions.NONE) // true
```