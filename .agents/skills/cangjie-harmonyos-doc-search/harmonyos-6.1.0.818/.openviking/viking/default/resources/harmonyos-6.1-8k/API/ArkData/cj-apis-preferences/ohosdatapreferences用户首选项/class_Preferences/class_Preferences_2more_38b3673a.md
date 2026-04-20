## class Preferences

```cangjie
public class Preferences {}
```

**功能：** 首选项实例，提供获取和修改存储数据的接口。

下列接口都需先使用[getPreferences](#static-func-getpreferencesuiabilitycontext-preferencesoptions)获取到Preferences实例，再通过此实例调用对应接口。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

### static func deletePreferences(UIAbilityContext, String)

```cangjie
public static func deletePreferences(context: UIAbilityContext, name: String): Unit
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
|name|String|是|-|Preferences实例的名称。|

**异常：**

- BusinessException：对应错误码如下表，详见[用户首选项错误码](./cj-errorcode-preferences.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 15500000 | Inner error. |
  | 15500010 | Failed to delete the user preferences persistence file. |

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