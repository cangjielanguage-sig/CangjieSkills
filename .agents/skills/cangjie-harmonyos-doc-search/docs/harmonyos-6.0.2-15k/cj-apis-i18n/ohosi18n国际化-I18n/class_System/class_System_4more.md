## class System

```cangjie
public class System {}
```

**功能：** I18n系统对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### static func getAppPreferredLanguage()

```cangjie
public static func getAppPreferredLanguage(): String
```

**功能：** 获取应用的偏好语言。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|应用的偏好语言。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let appPreferredLanguage = System.getAppPreferredLanguage() // 获取应用偏好语言
```

### static func getDisplayCountry(String, String, Bool)

```cangjie
public static func getDisplayCountry(country: String, locale: String, sentenceCase!: Bool = true): String
```

**功能：** 文本按指定国家进行本地化显示。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|country|String|是|-|用于指定国家，要求是合法的国家码。|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。|
|sentenceCase|Bool|否|true| **命名参数。** true表示按照首字母大写的格式显示文本，false表示按照区域默认的大小写格式显示文本。|

**返回值：**

|类型|说明|
|:----|:----|
|String|按指定国家，本地化显示的文本。|

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

let displayCountry = System.getDisplayCountry("zh-CN", "en-GB") // displayCountry = "China"
```

### static func getDisplayLanguage(String, String, Bool)

```cangjie
public static func getDisplayLanguage(language: String, locale: String, sentenceCase!: Bool = true): String
```

**功能：** 文本按指定语言进行本地化显示。例如，getDisplayLanguage("de", "zh-Hans-CN")用中文显示德文，接口输出结果为：德文。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|language|String|是|-|指定语言，要求是合法的语言ID。|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。|
|sentenceCase|Bool|否|true| **命名参数。** true表示按照首字母大写的格式显示文本，false表示按照区域默认的大小写格式显示文本。|

**返回值：**

|类型|说明|
|:----|:----|
|String|按指定语言，本地化显示的语言。|

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

let displayLanguage = System.getDisplayLanguage("zh", "en-GB") // 用英文形式显示中文，displayLanguage = Chinese
```