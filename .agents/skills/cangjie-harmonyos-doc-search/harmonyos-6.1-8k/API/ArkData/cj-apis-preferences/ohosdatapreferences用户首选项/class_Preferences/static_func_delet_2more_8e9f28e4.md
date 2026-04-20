### static func deletePreferences(UIAbilityContext, PreferencesOptions)

```cangjie
public static func deletePreferences(context: UIAbilityContext, options: PreferencesOptions): Unit
```

**功能：** 从缓存中删除指定的Preferences实例，若Preferences实例有对应的持久化文件，则同时删除其持久化文件。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题。

不支持该接口与其他preference接口并发调用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiabilitycontext)|是|-|应用上下文。|
|options|[PreferencesOptions](#class-preferencesoptions)|是|-|与Preferences实例相关的配置选项。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[用户首选项错误码](./cj-errorcode-preferences.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 801 | Capability not supported. |
  | 15500000 | Inner error. |
  | 15500010 | Failed to delete the user preferences persistence file. |
  | 15501001 | The operations is supported in stage mode only. |
  | 15501002 | Invalid dataGroupId. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    // 获取 Preferences 实例
    let preferences = Preferences.getPreferences(Global.abilityContext, "myStore")  // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    // 删除 Preferences 实例
    Preferences.deletePreferences(Global.abilityContext, "myStore")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func getPreferences(UIAbilityContext, String)

```cangjie
public static func getPreferences(context: UIAbilityContext, name: String): Preferences
```

**功能：** 获取Preferences实例。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiabilitycontext)|是|-|应用上下文。|
|name|String|是|-|Preferences实例的名称。|

**返回值：**

|类型|说明|
|:----|:----|
|[Preferences](#class-preferences)|返回Preferences实例。|

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
    let preferences = Preferences.getPreferences(Global.abilityContext, "mystore") // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    // 删除 Preferences 实例的缓存
    Preferences.removePreferencesFromCache(Global.abilityContext, PreferencesOptions("mystore", dataGroupId:"myGroupID"))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```