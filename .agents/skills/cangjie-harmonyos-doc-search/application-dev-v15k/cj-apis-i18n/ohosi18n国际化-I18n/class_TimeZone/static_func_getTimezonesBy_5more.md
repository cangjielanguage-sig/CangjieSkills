### static func getTimezonesByLocation(Float64, Float64)

```cangjie
public static func getTimezonesByLocation(longitude: Float64, latitude: Float64): Array<TimeZone>
```

**功能：** 创建某经纬度对应的时区对象数组。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|longitude|Float64|是|-|经度，范围[-180, 179.9)，东经取正值，西经取负值。|
|latitude|Float64|是|-|纬度，范围[-90, 89.9)，北纬取正值，南纬取负值。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[TimeZone](#class-timezone)>|时区对象数组。|

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

let timezoneArray = TimeZone.getTimezonesByLocation(-118.1, 34.0)
```

### func getDisplayName(?String, ?Bool)

```cangjie
public func getDisplayName(locale!: ?String = None, isDST!: ?Bool = None): String
```

**功能：** 获取时区对象的本地化表示。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|?String|否|None| **命名参数。** 表示区域信息的字符串，由语言、脚本、国家或地区组成。None代表系统Locale。|
|isDST|?Bool|否|None| **命名参数。** true表示时区对象本地化时考虑夏令时，false表示时区对象本地化时不考虑夏令时。None代表false。|

**返回值：**

|类型|说明|
|:----|:----|
|String|时区对象在指定区域的本地化表示。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let timezone = getTimeZone()
let timezoneName = timezone.getDisplayName(locale: "zh-CN", isDST: false) // timezoneName = "中国标准时间"
```

### func getID()

```cangjie
public func getID(): String
```

**功能：** 获取时区对象的ID。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|时区对象对应的时区ID。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let timezone = getTimeZone()
let timezoneID = timezone.getID() // timezoneID = "Asia/Shanghai"
```

### func getOffset(?Float64)

```cangjie
public func getOffset(date!: ?Float64 = None): Int32
```

**功能：** 获取某一时刻时区对象表示的时区与UTC时区的偏差。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|date|?Float64|否|None| **命名参数。** 待计算偏差的时刻，单位是毫秒。None代表系统时间。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|某一时刻时区对象表示的时区与UTC时区的偏差，单位是毫秒。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let timezone = getTimeZone()
let offset = timezone.getOffset(date: 123456789e1) // offset = 28800000
```

### func getRawOffset()

```cangjie
public func getRawOffset(): Int32
```

**功能：** 获取时区对象表示的时区与UTC时区的偏差。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|时区对象表示的时区与UTC时区的偏差，单位是毫秒。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let timezone = getTimeZone()
let offset = timezone.getRawOffset() // offset = 28800000
```