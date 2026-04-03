## class TimeZone

```cangjie
public class TimeZone {}
```

**功能：** 时区对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### static func getAvailableIDs()

```cangjie
public static func getAvailableIDs(): Array<String>
```

**功能：** 获取系统支持的时区ID。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|系统支持的时区ID列表。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// ids = ["America/Adak", "America/Anchorage", "America/Bogota", "America/Denver", "America/Los_Angeles", "America/Montevideo", "America/Santiago", "America/Sao_Paulo", "Asia/Ashgabat", "Asia/Hovd", "Asia/Jerusalem", "Asia/Magadan", "Asia/Omsk", "Asia/Shanghai", "Asia/Tokyo", "Asia/Yerevan", "Atlantic/Cape_Verde", "Australia/Lord_Howe", "Europe/Dublin", "Europe/London", "Europe/Moscow", "Pacific/Auckland", "Pacific/Easter", "Pacific/Pago-Pago"]
let ids = TimeZone.getAvailableIDs()
```

### static func getAvailableZoneCityIDs()

```cangjie
public static func getAvailableZoneCityIDs(): Array<String>
```

**功能：** 获取系统支持的时区城市ID。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|系统支持的时区城市ID列表。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// cityIDs = ["Auckland", "Magadan", "Lord Howe Island", "Tokyo", "Shanghai", "Hovd", "Omsk", "Ashgabat", "Yerevan", "Moscow", "Tel Aviv", "Dublin", "London", "Praia", "Montevideo", "Brasília", "Santiago", "Bogotá", "Easter Island", "Salt Lake City", "Los Angeles", "Anchorage", "Adak", "Pago Pago"]
let cityIDs = TimeZone.getAvailableZoneCityIDs()
```

### static func getCityDisplayName(String, String)

```cangjie
public static func getCityDisplayName(cityID: String, locale: String): String
```

**功能：** 获取某时区城市在该区域的本地化显示。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cityID|String|是|-|时区城市ID。|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。|

**返回值：**

|类型|说明|
|:----|:----|
|String|时区城市在某区域的本地化显示。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let displayName = TimeZone.getCityDisplayName("Shanghai", "zh-CN") // displayName = "上海（中国）"
```

### static func getTimezoneFromCity(String)

```cangjie
public static func getTimezoneFromCity(cityID: String): TimeZone
```

**功能：** 创建某时区城市对应的时区对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cityID|String|是|-|时区城市ID。|

**返回值：**

|类型|说明|
|:----|:----|
|[TimeZone](#class-timezone)|时区城市对应的时区对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let timezone = TimeZone.getTimezoneFromCity("Shanghai")
```