## class CalendarManager

```cangjie
public class CalendarManager {}
```

**功能：** 需先通过getCalendarManager()方法获取CalendarManager对象，再通过此对象调用对应方法，进行Calendar的创建、删除、修改、查询等操作。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

### func createCalendar(CalendarAccount)

```cangjie
public func createCalendar(calendarAccount: CalendarAccount): Calendar
```

**功能：** 根据日历账户信息，创建一个Calendar对象。

**需要权限：** ohos.permission.WRITE_CALENDAR

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|calendarAccount|[CalendarAccount](#class-calendaraccount)|是|-|日历账户信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[Calendar](#class-calendar)|返回创建的Calendar对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

|错误码ID|错误信息|
|:---|:---|
|201|Permission denied.|
|401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.|
|801|Capability not supported.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CalendarKit.*

let manager = getCalendarManager(context) // 获取日历管理对象

let account = CalendarAccount("122", CalendarType.LOCAL)
let arr = manager.createCalendar(account) // 创建日历对象
```

### func deleteCalendar(Calendar)

```cangjie
public func deleteCalendar(calendar: Calendar): Unit
```

**功能：** 删除指定Calendar对象

**需要权限：** ohos.permission.WRITE_CALENDAR

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|calendar|[Calendar](#class-calendar)|是|-|即将删除的Calendar对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

|错误码ID|错误信息|
|:---|:---|
|201|Permission denied.|
|401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.|
|801|Capability not supported.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CalendarKit.*

let manager = getCalendarManager(context) // 获取日历管理对象

let account = CalendarAccount("122", CalendarType.LOCAL)
let arr = manager.getCalendar(account)// 获取日历对象
manager.deleteCalendar(arr)// 删除日历对象
```