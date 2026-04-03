# ohos.i18n（国际化-I18n）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

i18n模块提供系统相关的或者增强的[国际化](../../internationalization/cj-i18n-l10n.md)能力，包括区域管理、电话号码处理、日历等，相关接口为ECMA 402标准中未定义的补充接口。

## 导入模块

```cangjie
import kit.LocalizationKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。

## func getCalendar(String, ?CalendarType)

```cangjie
public func getCalendar(locale: String, calendarType!: ?CalendarType = None): Calendar
```

**功能：** 获取指定区域和历法的日历对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家地区组成，例如zh-Hans-CN。|
|calendarType|?CalendarType|否|None|**命名参数。** 表示历法，取值包括：buddhist,&nbsp;chinese,&nbsp;coptic,&nbsp;ethiopic,&nbsp;hebrew,&nbsp;gregory,&nbsp;indian,&nbsp;islamic_civil,&nbsp;islamic_tbla,&nbsp;islamic_umalqura,&nbsp;japanese,&nbsp;persian。<br>默认值：区域默认的历法。|

**返回值：**

|类型|说明|
|:----|:----|
|Calendar|日历对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.i18n.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let calendar = getCalendar("en-US", calendarType: CalendarType.Buddhist)// 获得一个基于 en-US 区域设置的佛教日历对象
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```