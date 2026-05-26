## class HolidayManager

```cangjie
public class HolidayManager {
    public init(icsPath: String)
}
```

**功能：** 用于节假日管理的对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### init(String)

```cangjie
public init(icsPath: String)
```

**功能：** 创建HolidayManager对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icsPath|String|是|-|在设备上有应用读取权限的iCalendar格式的ics文件路径。|

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

let holidayManager = HolidayManager("/system/lib/US.ics")
```

### func getHolidayInfoItemArray(?Int32)

```cangjie
public func getHolidayInfoItemArray(year!: ?Int32 = None): Array<HolidayInfoItem>
```

**功能：** 获取指定某年的节假日信息列表。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|year|?Int32|否|None| **命名参数。** 年，例如2023。None代表当年。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[HolidayInfoItem](#class-holidayinfoitem)>|返回节假日信息列表。|

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

let holidayManager = HolidayManager("/system/lib/US.ics")
let holidayInfoItemArray = holidayManager.getHolidayInfoItemArray(year: 2024)
```

### func isHoliday(?DateTime)

```cangjie
public func isHoliday(date!: ?DateTime = None): Bool
```

**功能：** 判断指定的日期是否是节假日。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|date|?DateTime|否|None| **命名参数。** JavaScript的Date对象。None代表当天。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true表示指定的日期是节假日，false表示指定的日期不是节假日。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let holidayManager = HolidayManager("/system/lib/US.ics")
let isHoliday = holidayManager.isHoliday()
```