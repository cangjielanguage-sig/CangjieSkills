# ohos.security_huks（通用密钥库系统）

向应用提供密钥库能力，包括密钥管理及密钥的密码学操作等功能。

HUKS所管理的密钥可以由应用导入或者由应用调用HUKS接口生成。

## 导入模块

```cangjie
import kit.UniversalKeystoreKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func abortSession(HuksHandle, HuksOptions)

```cangjie
public func abortSession(handle: HuksHandle, options: HuksOptions): Unit
```

**功能：** abortSession操作密钥接口。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|handle|[HuksHandle](#class-hukshandle)|是|abortSession操作的handle。|
|options|[HuksOptions](#class-huksoptions)|是|abortSession操作的参数集合。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[HUKS错误码](../../errorcodes/cj-errorcode-huks.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |801|Capability not supported.|
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

let keyAlias = "test_abort"
let plainText = "123456"
let iv = "xxxxxxxxxxxxxxxx" // 用户自定义密钥初始化的向量
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
let encOptions = HuksOptions(
    [
        HuksParam(HuksTag.HUKS_TAG_ALGORITHM, HuksKeyAlg.HUKS_ALG_AES),
        HuksParam(HuksTag.HUKS_TAG_KEY_SIZE, HuksKeySize.HUKS_AES_KEY_SIZE_128),
        HuksParam(HuksTag.HUKS_TAG_PURPOSE, HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT),
        HuksParam(HuksTag.HUKS_TAG_PADDING, HuksKeyPadding.HUKS_PADDING_PKCS7),
        HuksParam(HuksTag.HUKS_TAG_BLOCK_MODE, HuksCipherMode.HUKS_MODE_CBC),
        HuksParam(HuksTag.HUKS_TAG_IV, HuksParamValue.bytes(iv.toArray()))
    ],
    plainText.toArray()
)

generateKeyItem(keyAlias, options)

// encrypt and abort
let handle = initSession(keyAlias, encOptions).handle

abortSession(handle, encOptions)
```