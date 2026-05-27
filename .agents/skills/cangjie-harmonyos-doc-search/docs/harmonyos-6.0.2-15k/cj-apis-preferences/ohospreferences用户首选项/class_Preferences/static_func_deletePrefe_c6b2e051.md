### static func deletePreferences(StageContext, PreferencesOptions)

```cangjie
public static func deletePreferences(context: StageContext, options: PreferencesOptions): Unit
```

**功能：** 从缓存中移出指定的Preferences实例，若Preferences实例有对应的持久化文件，则同时删除其持久化文件。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会出现数据一致性问题。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[StageContext](../../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)|是|-|应用上下文。|
|options|[PreferencesOptions](#struct-preferencesoptions)|是|-|与Preferences实例相关的配置选项。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[用户首选项错误码](../../errorcodes/cj-errorcode-preferences.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息                       |
  | :-------- | :------------------------------|
  | 401 | Parameter error. Possible causes:<br>1. Mandatory parameters are left unspecified;<br>2. Parameter verification failed.   |
  | 15500000 | Inner error.                   |
  | 15500010 | Failed to delete preferences file. |
  | 15501002 | The data group id is not valid.     |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.base.*

// 获取 Preferences 实例
let preferences = Preferences.getPreferences(Global.getStageContext(), "myStore")  // 需获取Context应用上下文，详见本文使用说明
try {
    // 删除 Preferences 实例
    Preferences.deletePreferences(Global.getStageContext(), "myStore")
} catch (e: Exception) {
    AppLog.info("delete Preferences failed")
}
```