## func getValue\<T, P>(UIAbilityContext, T, String, P) where T \<: ToString

```cangjie
public func getValue<T, P>(context: UIAbilityContext, name: T, defValue: String, domainName: P): String where T <: ToString
```

**功能：** 获取数据项的值。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiabilitycontext)|是|-|应用上下文。|
|name|T|是|-|类型T需实现ToString 接口。数据项的名称。数据项名称分为以下两种：<br>- 上述任意一个数据库中已存在的数据项。<br>- 开发者自行添加的数据项。|
|defValue|String|是|-|默认值。由开发者设置，当未从数据库中查询到该数据时，表示返回该默认值。|
|domainName|P|是|-|类型P需实现ToString 接口。指定要设置的域名。 <br>- domainName为domainName.DEVICE_SHARED,<br>&nbsp;&nbsp;&nbsp;设备属性共享域。<br>- domainName为domainName.USER_PROPERTY,<br>&nbsp;&nbsp;&nbsp;表示为用户属性域。 <br>- domainName为domainName.USER_SECURITY,<br>&nbsp;&nbsp;&nbsp;表示为用户安全属性域(仅对系统应用开放)。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回获得的数据项的值。|

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
    let value = getValue(context, Display.ScreenBrightnessStatus, "100", DomainName.DeviceShared)
    Hilog.info(0, "cangjie_ohos_test", "Succeeded in getting screen brightness: ${value}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```