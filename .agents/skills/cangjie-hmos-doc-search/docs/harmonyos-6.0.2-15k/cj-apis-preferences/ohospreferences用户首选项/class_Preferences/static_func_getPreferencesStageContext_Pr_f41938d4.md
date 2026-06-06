### static func getPreferences(StageContext, PreferencesOptions)

```cangjie
public static func getPreferences(context: StageContext, options: PreferencesOptions): Preferences
```

**功能：** 从缓存中移出指定的Preferences实例。

应用首次调用[getPreferences](#static-func-getpreferencesstagecontext-string)接口获取某个Preferences实例后，该实例会被会被缓存起来，后续再次[getPreferences](#static-func-getpreferencesstagecontext-string)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移出缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会出现数据一致性问题。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[StageContext](../../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)|是|-|应用上下文。|
|options|[PreferencesOptions](#struct-preferencesoptions)|是|-|Preferences实例的名称。|

**返回值：**

|类型|说明|
|:----|:----|
|[Preferences](#class-preferences)|Preferences实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[用户首选项错误码](../../errorcodes/cj-errorcode-preferences.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息                       |
  | :-------- | :------------------------------|
  | 401 | Parameter error. Possible causes:<br>1. Mandatory parameters are left unspecified;<br>2. Parameter verification failed.   |
  | 15500000 | Inner error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.base.*

let preferences = Preferences.getPreferences(Global.getStageContext(), PreferencesOptions("mystore", "myGroupID")) // 需获取Context应用上下文，详见本文使用说明
try {
    // 删除 Preferences 实例的缓存
    Preferences.removePreferencesFromCache(Global.getStageContext(), PreferencesOptions("mystore", "myGroupID"))
} catch (e: Exception) {
    AppLog.info("Failed to remove cache for preferences")
}
```