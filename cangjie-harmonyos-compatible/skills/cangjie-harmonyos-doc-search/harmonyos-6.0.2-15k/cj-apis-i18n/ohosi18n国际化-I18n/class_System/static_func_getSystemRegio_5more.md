### static func getSystemRegion()

```cangjie
public static func getSystemRegion(): String
```

**功能：** 获取系统地区。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|系统地区ID。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let systemRegion = System.getSystemRegion() // 获取系统当前地区设置
```

### static func getUsingLocalDigit()

```cangjie
public static func getUsingLocalDigit(): Bool
```

**功能：** 判断系统是否使用本地数字。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true表示本地数字开关已打开，false表示本地数字开关未打开。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let status = System.getUsingLocalDigit() // 判断本地化数字开关是否打开
```

### static func is24HourClock()

```cangjie
public static func is24HourClock(): Bool
```

**功能：** 判断系统时间是否为24小时制。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true，表示系统24小时开关开启；返回false，表示系统24小时开关关闭。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let is24HourClock = System.is24HourClock() // 系统24小时开关是否开启
```

### static func isSuggested(String, ?String)

```cangjie
public static func isSuggested(language: String, region!: ?String = None): Bool
```

**功能：** 判断当前语言和地区是否匹配。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|language|String|是|-|合法的语言ID，例如zh。|
|region|?String|否|None| **命名参数。** 合法的地区ID，例如CN。None代表使用SIM卡国家或地区。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true，表示当前语言和地区匹配；返回false，表示当前语言和地区不匹配。|

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

let res = System.isSuggested('zh', region: 'CN') // res = true
```

### static func setAppPreferredLanguage(String)

```cangjie
public static func setAppPreferredLanguage(language: String): Unit
```

**功能：** 设置应用的偏好语言。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|language|String|是|-|合法的语言ID。|

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

System.setAppPreferredLanguage('zh') // 设置应用当前的偏好语言为"zh"
```