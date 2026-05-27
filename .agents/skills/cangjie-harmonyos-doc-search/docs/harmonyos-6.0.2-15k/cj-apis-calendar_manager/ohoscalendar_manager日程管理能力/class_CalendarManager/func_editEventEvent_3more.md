### func editEvent(Event)

```cangjie
public func editEvent(event: Event): Int64
```

**功能：** 创建单个日程，入参Event不填日程id，调用该接口会跳转到日程创建页面。使用该接口创建的日程，三方应用无法查询和修改，只能通过系统日历进行查询和修改。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[Event](#class-event)|是|-|Event对象。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|日程的id，日程id是日程的唯一标识符，是数据库的自增主键。创建失败时没有返回值；当返回值小于0时代表用户取消创建；当返回值大于0时代表日程创建成功；没有等于0的情况。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CalendarKit.*
import std.time.DateTime as d

let manager = getCalendarManager(context) // 获取日历管理对象

let startDate1 = d.nowUTC()
let duration1 = startDate1.toUnixTimeStamp()
let satrt_datems1 = duration1.toMilliseconds()
let endTime_datems1 = satrt_datems1 + 60 * 60 * 1000
let eve = Event(EventType.NORMAL, satrt_datems1, endTime_datems1, title: "title", isAllDay: true) // 构建日程对象
let arr = manager.editEvent(eve)
```

### func getAllCalendars()

```cangjie
public func getAllCalendars(): Array<Calendar>
```

**功能：** 获取当前应用所有创建的Calendar对象以及默认Calendar对象。

**需要权限：** ohos.permission.READ_CALENDAR

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[Calendar](#class-calendar)>|查询到的Calendar对象数组。|

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
let arr = manager.getAllCalendars() // 获取所有日历对象
```

### func getCalendar(?CalendarAccount)

```cangjie
public func getCalendar(calendarAccount!: ?CalendarAccount = None): Calendar
```

**功能：** 获取默认Calendar对象或者指定Calendar对象。

**需要权限：** ohos.permission.READ_CALENDAR

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|calendarAccount|?[CalendarAccount](#class-calendaraccount)|否|None|日历账户信息，用来获取指定Calendar对象，不填时，表示获取默认Calendar对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[Calendar](#class-calendar)|查询到的Calendar对象。|

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
let arr = manager.getCalendar(account) // 获取日历对象
```