## class Calendar

```cangjie
public class Calendar {
    public let calendarId: Int64
}
```

**功能：** 需先通过createCalendar()、getCalendar()中任一方法获取Calendar对象，再通过此对象调用对应方法，对该Calendar下的日程进行创建、删除、修改、查询等操作。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

### let calendarId

```cangjie
public let calendarId: Int64
```

**功能：** 日历账户id，日历账户id是日历账户的唯一标识符，是数据库的自增主键，小于0代表日历账户创建失败，大于0代表日历账户创建成功，没有等于0的情况。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**类型：** Int64

**读写能力：** 只读

### func addEvent(Event)

```cangjie
public func addEvent(event: Event): Int64
```

**功能：** 创建日程，入参Event不填日程id。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[Event](#class-event)|是|-|Event对象。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回日程的id。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CalendarKit.*
import std.time.DateTime as d

let manager = getCalendarManager(context) // 获取日历管理对象

let account = CalendarAccount("122", CalendarType.LOCAL)
let arr = manager.createCalendar(account)// 创建日历对象

let startDate1 = d.nowUTC()
let duration1 = startDate1.toUnixTimeStamp()
let satrt_datems1 = duration1.toMilliseconds()
let endTime_datems1 = satrt_datems1 + 60*60*1000
let eve = Event(EventType.NORMAL, satrt_datems1, endTime_datems1, title: "title", isAllDay: true)
arr.addEvent(eve)// 添加日程
```

### func addEvents(Array\<Event>)

```cangjie
public func addEvents(events: Array<Event>): Unit
```

**功能：** 批量创建日程，入参Event不填日程id。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|events|Array\<[Event](#class-event)>|是|-|Event对象数组。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CalendarKit.*
import std.time.DateTime as d

let manager = getCalendarManager(context) // 获取日历管理对象

let account = CalendarAccount("122", CalendarType.LOCAL)
let c = manager.createCalendar(account) // 创建日历对象

let startDate1 = d.nowUTC()
let duration1 = startDate1.toUnixTimeStamp()
let satrt_datems1 = duration1.toMilliseconds()
let endTime_datems1 = satrt_datems1 + 60 * 60 * 1000
let eve = Event(EventType.NORMAL, satrt_datems1, endTime_datems1, title: "title", isAllDay: true) // 构建日程对象
let eve1 = Event(EventType.NORMAL, satrt_datems1, endTime_datems1, title: "title") // 构建日程对象
let eveid = c.addEvents([eve, eve1])
```