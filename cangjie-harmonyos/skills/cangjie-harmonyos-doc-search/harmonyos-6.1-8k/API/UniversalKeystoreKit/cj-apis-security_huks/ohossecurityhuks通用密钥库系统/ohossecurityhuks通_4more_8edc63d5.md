# ohos.security.huks（通用密钥库系统）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

huks模块向应用提供密钥库能力，包括密钥管理及密钥的密码学操作等功能。

HUKS所管理的密钥可以由应用导入或者由应用调用HUKS接口生成。

## 导入模块

```cangjie
import kit.UniversalKeystoreKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。

## func abortSession(HuksHandleId, HuksOptions)

```cangjie
public func abortSession(handle: HuksHandleId, options: HuksOptions): Unit
```

**功能：** abortSession操作密钥接口。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|handle|[HuksHandleId](#class-hukshandleid)|是|-|abortSession操作的handle。|
|options|[HuksOptions](#class-huksoptions)|是|-|abortSession操作的参数集合。|

**异常：**

- BusinessException：对应错误码如下表，详见[HUKS错误码](./cj-errorcode-huks.md)和[通用错误码](../cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 801 | api is not supported. |
  | 12000004 | operating file failed. |
  | 12000005 | IPC communication failed. |
  | 12000006 | error occurred in crypto engine. |
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
            )
        ]
    )

    generateKeyItem(keyAlias, options)

    // encrypt and abort
    let handle = initSession(keyAlias, options).handle

    abortSession(handle, options)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```