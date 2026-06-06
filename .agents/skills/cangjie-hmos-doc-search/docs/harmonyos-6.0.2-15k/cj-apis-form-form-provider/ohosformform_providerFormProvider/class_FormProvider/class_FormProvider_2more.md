## class FormProvider

```cangjie
public class FormProvider {}
```

**功能：** FormProvider模块提供了卡片提供方相关接口的能力，开发者在开发卡片时，可通过该模块提供接口实现更新卡片、设置卡片更新时间、获取卡片信息、请求发布卡片等。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

### static func getFormsInfo(FormInfoFilter)

```cangjie
public static func getFormsInfo(filter!: FormInfoFilter = FormInfoFilter("")): Array<FormInfo>
```

**功能：** 获取设备上当前应用程序的卡片信息。

**系统能力：**  SystemCapability.Ability.Form

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|filter|[FormInfoFilter](cj-apis-form-form-info.md#class-forminfofilter)|否|FormInfoFilter("")|卡片信息过滤器。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[FormInfo](cj-apis-form-form-info.md#class-forminfo)>|返回查询到符合条件的卡片信息。|

**异常：**

- IllegalArgumentException:

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |Parameter is error, please check|传入错误的参数。|检查传入的参数是否满足要求。|

- BusinessException：对应错误码的详细介绍请参见[卡片错误码](../../errorcodes/cj-errorcode-form.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |16500050|IPC connection error.|
  |16500100|Failed to obtain configuration information.|
  |16501000|An internal functional error occurred.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.FormKit.*
import kit.UIKit.{AppLog, BusinessException}

try {
    let arrayInfo = FormProvider.getFormsInfo()
    for (info in arrayInfo) {
        AppLog.info("info.bundleName  ${info.bundleName}")
        AppLog.info("info.abilityName  ${info.abilityName}")
        AppLog.info("info.moduleName  ${info.moduleName}")
        AppLog.info("info.customizeData  ${info.customizeData}")
        AppLog.info("info.defaultDimension  ${info.defaultDimension}")
        AppLog.info("info.supportDimensions  ${info.supportDimensions}")
        AppLog.info("info.supportedShapes  ${info.supportedShapes}")
        AppLog.info("info.colorMode  ${info.colorMode}")
        AppLog.info("info.formType  ${info.formType}")
        AppLog.info("info.name  ${info.name}")
        AppLog.info("info.updateDuration  ${info.updateDuration}")
        // ...
    }
} catch (e: BusinessException) {
    AppLog.error("getFormsInfo error:${e.code}, ${e.message}")
}
```