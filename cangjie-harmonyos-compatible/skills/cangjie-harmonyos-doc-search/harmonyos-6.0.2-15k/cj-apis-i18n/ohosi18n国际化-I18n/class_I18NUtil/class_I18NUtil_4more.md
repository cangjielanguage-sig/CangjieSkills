## class I18NUtil

```cangjie
public class I18NUtil {}
```

**功能：** 综合处理对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### static func getBestMatchLocale(String, Array\<String>)

```cangjie
public static func getBestMatchLocale(locale: String, localeList: Array<String>): String
```

**功能：** 在指定区域列表中获取与某个区域最佳匹配的区域。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|是|-|待匹配的区域信息字符串，如：zh-Hans-CN。|
|localeList|Array\<String>|是|-|被指定的区域字符串列表。|

**返回值：**

|类型|说明|
|:----|:----|
|String|与某个区域最佳匹配的区域ID。当指定区域列表中没有匹配的区域时，返回空字串。|

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

let res = I18NUtil.getBestMatchLocale("zh-Hans-CN", ["en-Latn-US", "en-GB", "zh-Hant-CN", "zh-Hans-MO"]) // res = "zh-Hans-MO"
```

### static func getDateOrder(String)

```cangjie
public static func getDateOrder(locale: String): String
```

**功能：** 获取某区域日期中年、月、日的排列顺序。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成，如：zh-Hans-CN。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回该区域年、月、日的排列顺序。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let order = I18NUtil.getDateOrder("zh-CN") // order = "y-L-d"
```

### static func getThreeLetterLanguage(String)

```cangjie
public static func getThreeLetterLanguage(locale: String): String
```

**功能：** 将语言代码由二字母转换为三字母。
例如，中文的二字母语言代码是zh，对应的三字母语言代码是zho，更多详细信息可参考[ISO 639](https://www.iso.org/iso-639-language-code)。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|是|-|待转换的语言二字母代码，如：zh。|

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后的语言三字母代码，如：zho。|

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

let language = I18NUtil.getThreeLetterLanguage('zh') // zho
```