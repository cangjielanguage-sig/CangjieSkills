## class PhoneNumberFormat

```cangjie
public class PhoneNumberFormat {
    public init(country: String, options!: ?PhoneNumberFormatOptions = None)
}
```

**功能：** 电话号码格式化对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### init(String, ?PhoneNumberFormatOptions)

```cangjie
public init(country: String, options!: ?PhoneNumberFormatOptions = None)
```

**功能：** 创建电话号码格式化对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|country|String|是|-|表示电话号码所属国家或地区代码。|
|options|?[PhoneNumberFormatOptions](#class-phonenumberformatoptions)|否|None| **命名参数。** 电话号码格式化时设置的配置项。None代表NATIONAL。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let phoneNumberFormat = PhoneNumberFormat("CN", options: PhoneNumberFormatOptions(formatType: "E164"))
```

### func format(String)

```cangjie
public func format(number: String): String
```

**功能：** 对电话号码进行格式化。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|number|String|是|-|待格式化的电话号码。|

**返回值：**

|类型|说明|
|:----|:----|
|String|格式化后的电话号码。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let phonenumberfmt = PhoneNumberFormat("CN")
let formattedPhoneNumber = phonenumberfmt.format("158 **** 2312") // *号替换为具体数字formattedPhoneNumber = "158 **** 2312"
```

### func getLocationName(String, String)

```cangjie
public func getLocationName(number: String, locale: String): String
```

**功能：** 判断电话号码归属地。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|number|String|是|-|电话号码。获取其他地区号码的归属地时，需要在号码前加00+国际区号。|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。|

**返回值：**

|类型|说明|
|:----|:----|
|String|电话号码归属地。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let phonenumberfmt = PhoneNumberFormat("CN")
let locationName = phonenumberfmt.getLocationName("158****2345", "zh-CN") //*号替换为具体数字locationName = "广东省湛江市"
```

### func isValidNumber(String)

```cangjie
public func isValidNumber(number: String): Bool
```

**功能：** 判断传入的电话号码格式是否正确。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|number|String|是|-|待判断的电话号码。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示电话号码的格式正确，返回false表示电话号码的格式错误。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let phoneNumberFormat = PhoneNumberFormat("CN")
let isValidNumber = phoneNumberFormat.isValidNumber("158****2312") // *号替换为具体数字isValidNumber = true
```