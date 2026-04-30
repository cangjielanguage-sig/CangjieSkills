## func attestKeyItem(String, HuksOptions)

```cangjie
public func attestKeyItem(keyAlias: String, options: HuksOptions): Array<String>
```

**功能：** 获取密钥证书。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|keyAlias|String|是|密钥别名，存放待获取证书的密钥别名。|
|options|[HuksOptions](#class-huksoptions)|是|用于获取证书时指定所需参数与数据。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|返回密钥证书链。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[HUKS错误码](../../errorcodes/cj-errorcode-huks.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission verification failed.|
  |401|Parameter error.|
  |801|Capability not supported.|
  |12000001|algorithm mode is not supported.|
  |12000002|algorithm param is missing.|
  |12000003|algorithm param is invalid.|
  |12000004|operating file failed.|
  |12000005|IPC communication failed.|
  |12000006|error occurred in crypto engine.|
  |12000011|queried entity does not exist.|
  |12000012|external error.|
  |12000014|memory is insufficient.|

## func deleteKeyItem(String, HuksOptions)

```cangjie
public func deleteKeyItem(keyAlias: String, _: HuksOptions): Unit
```

**功能：** 删除密钥。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|keyAlias|String|是|密钥别名，应为生成key时传入的别名。|
|\_|[HuksOptions](#class-huksoptions)|是|用于删除时指定密钥的属性Tag，比如删除的密钥范围（全量/单个），当删除单个时，Tag字段可传空。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[HUKS错误码](../../errorcodes/cj-errorcode-huks.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |801|Capability not supported.|
  |12000004|operating file failed.|
  |12000005|IPC communication failed.|
  |12000011|queried entity does not exist.|
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
        None
    )
    generateKeyItem(keyAlias, options)
}

func test_delete_key() {
    let keyAlias = "test_delete_key"
    generateSimpleKey(keyAlias)
    // delete
    deleteKeyItem(keyAlias, HuksOptions.NONE)
}

test_delete_key()
```