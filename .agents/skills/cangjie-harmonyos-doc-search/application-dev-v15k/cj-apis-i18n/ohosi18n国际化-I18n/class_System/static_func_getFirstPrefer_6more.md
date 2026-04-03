### static func getFirstPreferredLanguage()

```cangjie
public static func getFirstPreferredLanguage(): String
```

**功能：** 获取系统偏好语言列表中的第一个偏好语言。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|获取系统偏好语言列表中的第一个偏好语言。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let firstPreferredLanguage = System.getFirstPreferredLanguage() // 获取系统当前偏好语言列表中的第一个偏好语言
```

### static func getPreferredLanguageList()

```cangjie
public static func getPreferredLanguageList(): Array<String>
```

**功能：** 获取系统偏好语言列表。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|系统偏好语言列表。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let preferredLanguageList = System.getPreferredLanguageList() // 获取系统当前偏好语言列表
```

### static func getSystemCountries(String)

```cangjie
public static func getSystemCountries(language: String): Array<String>
```

**功能：** 针对输入语言，系统支持的国家或地区列表。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|language|String|是|-|合法的语言ID。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|系统支持某种特定语言的国家或地区列表。|

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

let systemCountries = System.getSystemCountries('zh') // systemCountries = [ "ZW", "YT", "YE", ..., "ER", "CN", "DE" ]
```

### static func getSystemLanguage()

```cangjie
public static func getSystemLanguage(): String
```

**功能：** 获取系统语言。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|系统语言ID。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let systemLanguage = System.getSystemLanguage() // systemLanguage为当前系统语言
```

### static func getSystemLanguages()

```cangjie
public static func getSystemLanguages(): Array<String>
```

**功能：** 获取系统支持的语言列表。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|系统支持的语言ID列表。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let systemLanguages = System.getSystemLanguages() // [ "ug", "bo", "zh-Hant", "en-Latn-US", "zh-Hans" ]
```

### static func getSystemLocale()

```cangjie
public static func getSystemLocale(): String
```

**功能：** 获取系统区域。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|区域信息的字符串。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let systemLocale = System.getSystemLocale() // 获取系统当前Locale
```