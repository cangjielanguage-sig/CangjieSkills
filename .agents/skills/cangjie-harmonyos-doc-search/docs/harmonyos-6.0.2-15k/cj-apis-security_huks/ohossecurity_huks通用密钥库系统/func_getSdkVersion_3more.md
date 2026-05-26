## func getSdkVersion()

```cangjie
public func getSdkVersion(): String
```

**功能：** 获取当前系统sdk版本。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|String|返回sdk版本。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.UniversalKeystoreKit.*

// 此处代码可添加在依赖项定义中
func test_get_sdk_version() {
    let res = getSdkVersion()
    return res
}

test_get_sdk_version()
```

## func importKeyItem(String, HuksOptions)

```cangjie
public func importKeyItem(keyAlias: String, options: HuksOptions): Unit
```

**功能：** 导入明文密钥。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|keyAlias|String|是|密钥别名。|
|options|[HuksOptions](#class-huksoptions)|是|用于导入时所需Tag和需要导入的密钥。其中密钥使用的算法、密钥用途、密钥长度为必选参数。|

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
  |12000011|queried entity does not exist.|
  |12000012|external error.|
  |12000013|queried credential does not exist.|
  |12000014|memory is insufficient.|
  |12000015|call service failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.UniversalKeystoreKit.*

let keyAlias = "test_import_aes"
let key = Array<UInt8>(Int64(HuksKeySize.HUKS_AES_KEY_SIZE_256.toUInt32().getOrThrow() / 8),
    {i => UInt8(i & 0xFF)})
importKeyItem(
    keyAlias,
    HuksOptions(
        [
            HuksParam(HuksTag.HUKS_TAG_ALGORITHM, HuksKeyAlg.HUKS_ALG_AES),
            HuksParam(HuksTag.HUKS_TAG_KEY_SIZE, HuksKeySize.HUKS_AES_KEY_SIZE_256),
            HuksParam(
                HuksTag.HUKS_TAG_PURPOSE,
                HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
            )
        ],
        key
    )
)
```

## func importWrappedKeyItem(String, String, HuksOptions)

```cangjie
public func importWrappedKeyItem(keyAlias: String, wrappingKeyAlias: String, options: HuksOptions): Unit
```

**功能：** 导入加密密钥。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|keyAlias|String|是|密钥别名，存放待导入密钥的别名。|
|wrappingKeyAlias|String|是|密钥别名，对应密钥用于解密加密的密钥数据。|
|options|[HuksOptions](#class-huksoptions)|是|用于导入时所需Tag和需要导入的加密的密钥数据。其中密钥使用的算法、密钥用途、密钥长度为必选参数。|

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
  |12000011|queried entity does not exist.|
  |12000012|external error.|
  |12000013|queried credential does not exist.|
  |12000014|memory is insufficient.|
  |12000015|call service failed.|