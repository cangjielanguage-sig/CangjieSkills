# ohos.i18n（国际化-I18n）

本模块提供系统相关的或者增强的国际化能力，包括区域管理、电话号码处理、日历等，相关接口为ECMA 402标准中未定义的补充接口。Intl模块提供了ECMA 402标准定义的基础国际化接口，与本模块共同使用可提供完整地国际化支持能力。

## 导入模块

```cangjie
import kit.LocalizationKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func getCalendar(String, ?String)

```cangjie
public func getCalendar(locale: String, calendarType!: ?String = None): Calendar
```

**功能：** 获取日历对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成，例如zh-Hans-CN。|
|calendarType|?String|否|None| **命名参数。** 合法的日历类型，目前合法的类型有buddhist, chinese, coptic, ethiopic, hebrew, gregory, indian, islamic_civil, islamic_tbla, islamic_umalqura, japanese, persian。取默认值None时是区域默认的日历类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[Calendar](#class-calendar)|日历对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let calendar = getCalendar("zh-Hans", calendarType: "chinese") // 获取中国农历日历对象
```

## func getInstance(String)

```cangjie
public func getInstance(locale!: String = ""): IndexUtil
```

**功能：** 创建并返回IndexUtil对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|否|""| **命名参数。** 表示区域信息的字符串，由语言、脚本、国家或地区组成。默认值""时取系统Locale。|

**返回值：**

|类型|说明|
|:----|:----|
|[IndexUtil](#class-indexutil)|locale对应的IndexUtil对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let indexUtil = getInstance(locale: "zh-CN")
```

## func getLineInstance(String)

```cangjie
public func getLineInstance(locale: String): BreakIterator
```

**功能：** 获取一个用于断句的[BreakIterator](#class-breakiterator)对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。生成的BreakIterator将按照locale所指定的区域规则进行断句。|

**返回值：**

|类型|说明|
|:----|:----|
|[BreakIterator](#class-breakiterator)|用于进行断句的处理器。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let iterator = getLineInstance("en")
```

## func getTimeZone(String)

```cangjie
public func getTimeZone(zoneID!: String = ""): TimeZone
```

**功能：** 获取时区ID对应的时区对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|zoneID|String|否|""| **命名参数。** 时区ID。默认值为""时是系统Locale。|

**返回值：**

|类型|说明|
|:----|:----|
|[TimeZone](#class-timezone)|时区ID对应的时区对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let timezone = getTimeZone()
```