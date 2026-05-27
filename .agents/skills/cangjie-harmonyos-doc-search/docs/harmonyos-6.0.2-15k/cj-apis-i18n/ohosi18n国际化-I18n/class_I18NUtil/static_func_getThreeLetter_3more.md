### static func getThreeLetterRegion(String)

```cangjie
public static func getThreeLetterRegion(locale: String): String
```

**功能：** 将地区的二字母代码转换为三字母。
例如，中国的二字母地区代码是CN，三字母是CHN，更多详细信息可参考[ISO 3166](https://www.iso.org/iso-3166-country-codes.html)。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|是|-|待转换的地区二字母代码，如：CN。|

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后的地区三字母代码，如：CHN。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[I18n错误码](../../errorcodes/cj-errorcode-i18n.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.|
  |890001|Invalid parameter. Possible causes: Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let region = I18NUtil.getThreeLetterRegion('CN') // CHN
```

### static func getTimePeriodName(Int32, ?String)

```cangjie
public static func getTimePeriodName(hour: Int32, locale!: ?String = None): String
```

**功能：** 取某区域指定时间的本地化表达。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|hour|Int32|是|-|指定的时间，如：16。|
|locale|?String|否|None| **命名参数。** 表示区域信息的字符串，由语言、脚本、国家或地区组成。如：zh-Hans-CN。None代表当前区域。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回某区域指定时间的本地化表达。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[I18n错误码](../../errorcodes/cj-errorcode-i18n.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.|
  |890001|Invalid parameter. Possible causes: Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let name = I18NUtil.getTimePeriodName(2, locale: "zh-CN") // name = "凌晨"
```

### static func unitConvert(UnitInfo, UnitInfo, Float64, String, ?String)

```cangjie
public static func unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: Float64, locale: String, style!: ?String = None): String
```

**功能：** 将fromUnit的单位转换为toUnit的单位，并根据区域与风格进行格式化。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fromUnit|[UnitInfo](#class-unitinfo)|是|-|需要转换的单位。|
|toUnit|[UnitInfo](#class-unitinfo)|是|-|转换成的目标单位。|
|value|Float64|是|-|需要转换的单位的数量值。|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成，如：zh-Hans-CN。|
|style|?String|否|None| **命名参数。** 格式化使用的风格，取值包括："long", "short", "narrow"。None代表short。|

**返回值：**

|类型|说明|
|:----|:----|
|String|按照toUnit的单位格式化后，得到的字符串。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let fromUnit = UnitInfo("cup", "US")
let toUnit = UnitInfo("liter", "SI")
let res = I18NUtil.unitConvert(fromUnit, toUnit, 1000.0, "en-US", style: "long") // res = "236.588 liters"
```