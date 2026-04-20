# ohos.settings（设置数据项名称）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

settings模块提供访问设置数据项的能力。

> **说明：**
>
> 如果访问的数据项没有获取到值，表示当前系统应用没有将该数据项的值添加到数据库。

## 导入模块

```cangjie
import kit.BasicServicesKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

## func getValue\<T>(UIAbilityContext, T, String) where T \<: ToString

```cangjie
public func getValue<T>(context: UIAbilityContext, name: T, defValue: String): String where T <: ToString
```

**功能：** 获取数据库中DEVICE_SHARED域指定数据项的值。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiabilitycontext)|是|-|应用上下文。|
|name|T|是|-|类型T需实现ToString接口。数据项的名称。数据项名称分为以下两种：<br>- 上述任意一个数据库中已存在的数据项。<br>- 开发者自行添加的数据项。|
|defValue|String|是|-|默认值。由开发者设置，在数据库中查询不到该数据时，返回默认值。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回数据项的值。|

**异常：**

- BusinessException：对应错误码如下表，详见[设置数据项错误码](./cj-errorcode-settings.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 14800000 | Parameter error. |

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    let context = Global.abilityContext
    let value = getValue(context, Date.DateFormat, "MM/dd/yyyy")
    Hilog.info(0, "cangjie_ohos_test", "Succeeded in getting date format: ${value}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```