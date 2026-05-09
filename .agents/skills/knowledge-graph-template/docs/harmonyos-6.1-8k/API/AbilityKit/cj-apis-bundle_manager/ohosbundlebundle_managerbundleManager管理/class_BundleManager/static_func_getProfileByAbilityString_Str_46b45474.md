### static func getProfileByAbility(String, String, String)

```cangjie
public static func getProfileByAbility(moduleName: String, abilityName: String, metadataName!: String = ""): Array<String>
```

**功能：** 根据给定的moduleName、abilityName和metadataName（module.json5中metadata标签下的name）获取自身相应配置文件的json格式字符串，返回对象为string数组。

>如果配置文件信息采用了资源引用格式，则返回值将保持资源引用格式（例如 $string:res_id），开发者可以通过[资源管理模块](../LocalizationKit/cj-apis-resource_manager.md)的相关接口，来获取引用的资源。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|moduleName|String|是|-|表示Module名称。|
|abilityName|String|是|-|表示UIAbility组件的名称。|
|metadataName|String|否|""|**命名参数。** 表示UIAbility组件的元信息名称，即module.json5配置文件中abilities标签下的metadata标签的name，默认值为空。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|数组对象，返回Array\<String>。|

**异常：**

- BusinessException：对应错误码如下表，详见[包管理子系统通用错误码](./cj-errorcode-bundle.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17700002 | The specified moduleName is not existed. |
  | 17700003 | The specified abilityName is not existed. |
  | 17700024 | Failed to get the profile because there is no profile in the HAP. |
  | 17700029 | The specified ability is disabled. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let moduleName = "entry"
    let abilityName = "EntryAbility"
    let infoList = BundleManager.getProfileByAbility(moduleName, abilityName)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```