### static func getPreferences(UIAbilityContext, PreferencesOptions)

```cangjie
public static func getPreferences(context: UIAbilityContext, options: PreferencesOptions): Preferences
```

**功能：** 获取Preferences实例。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiabilitycontext)|是|-|应用上下文。|
|options|[PreferencesOptions](#class-preferencesoptions)|是|-|与Preferences实例相关的配置选项。|

**返回值：**

|类型|说明|
|:----|:----|
|[Preferences](#class-preferences)|返回Preferences实例。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[用户首选项错误码](./cj-errorcode-preferences.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 801 | Capability not supported. |
  | 15500000 | Inner error. |
  | 15501001 | The operations is supported in stage mode only. |
  | 15501002 | Invalid dataGroupId. |

**示例：**

<!-- compile only -->
<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let preferences = Preferences.getPreferences(Global.abilityContext, PreferencesOptions("mystore", dataGroupId:"myGroupID")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    // 删除 Preferences 实例的缓存
    Preferences.removePreferencesFromCache(Global.abilityContext, PreferencesOptions("mystore", dataGroupId:"myGroupID"))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func removePreferencesFromCache(UIAbilityContext, String)

```cangjie
public static func removePreferencesFromCache(context: UIAbilityContext, name: String): Unit
```

**功能：** 从缓存中移除指定的Preferences实例。

应用首次调用[getPreferences](#static-func-getpreferencesuiabilitycontext-string)接口获取某个Preferences实例后，该实例会被缓存起来。后续再次调用getPreferences时，不会再从持久化文件中读取，而是直接从缓存中获取Preferences实例。

调用此接口移除缓存中的实例之后，再次调用getPreferences将会重新读取持久化文件，生成新的Preferences实例。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会出现数据一致性问题。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiabilitycontext)|是|-|应用上下文。|
|name|String|是|-|Preferences实例的名称。|

**异常：**

- BusinessException：对应错误码如下表，详见[用户首选项错误码](./cj-errorcode-preferences.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 15500000 | Inner error. |

**示例：**

<!-- compile only -->
<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let preferences = Preferences.getPreferences(Global.abilityContext, PreferencesOptions("mystore", dataGroupId:"myGroupID")) // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    // 删除 Preferences 实例的缓存
    Preferences.removePreferencesFromCache(Global.abilityContext, PreferencesOptions("mystore", dataGroupId:"myGroupID"))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```