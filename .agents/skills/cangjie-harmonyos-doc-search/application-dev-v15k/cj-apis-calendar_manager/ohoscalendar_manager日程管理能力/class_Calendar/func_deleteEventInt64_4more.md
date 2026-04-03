### func deleteEvent(Int64)

```cangjie
public func deleteEvent(id: Int64): Unit
```

**功能：** 删除指定id的日程。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int64|是|-|日程id，传入的日程id为正整数，表示已创建日程的id，是日程的唯一标识符。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CalendarKit.*
import std.time.DateTime as d

let manager = getCalendarManager(context) // 获取日历管理对象

let account = CalendarAccount("122", CalendarType.LOCAL)
let c = manager.createCalendar(account)// 创建日历对象

let startDate1 = d.nowUTC()
let duration1 = startDate1.toUnixTimeStamp()
let satrt_datems1 = duration1.toMilliseconds()
let endTime_datems1 = satrt_datems1 + 60*60*1000
let eve = Event(EventType.NORMAL, satrt_datems1, endTime_datems1, title: "title", isAllDay: true)// 构建日程对象
let eveid = c.addEvent(eve)

c.deleteEvent(eveid)
```

### func deleteEvents(Array\<Int64>)

```cangjie
public func deleteEvents(ids: Array<Int64>): Unit
```

**功能：** 根据日程id，批量删除日程。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|ids|Array\<Int64>|是|-|日程id数组。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CalendarKit.*
import std.time.DateTime as d

let manager = getCalendarManager(context) // 获取日历管理对象

let account = CalendarAccount("122", CalendarType.LOCAL)
let c = manager.createCalendar(account)// 创建日历对象

let startDate1 = d.nowUTC()
let duration1 = startDate1.toUnixTimeStamp()
let satrt_datems1 = duration1.toMilliseconds()
let endTime_datems1 = satrt_datems1 + 60*60*1000
let eve = Event(EventType.NORMAL, satrt_datems1, endTime_datems1, title: "title", isAllDay: true)// 构建日程对象
let eveid = c.addEvent(eve)
let eveid1 = c.addEvent(eve)

c.deleteEvents([eveid, eveid1])
```

### func getAccount()

```cangjie
public func getAccount(): CalendarAccount
```

**功能：** 获取日历账户信息。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[CalendarAccount](#class-calendaraccount)|日历账户信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CalendarKit.*

let manager = getCalendarManager(context) // 获取日历管理对象

let account = CalendarAccount("122", CalendarType.LOCAL)
let c = manager.createCalendar(account) // 创建日历对象

let account = c.getAccount()
```

### func getConfig()

```cangjie
public func getConfig(): CalendarConfig
```

**功能：** 获取日历配置信息。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[CalendarConfig](#class-calendarconfig)|日历配置信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CalendarKit.*

let manager = getCalendarManager(context) // 获取日历管理对象

let account = CalendarAccount("122", CalendarType.LOCAL)
let c = manager.createCalendar(account) // 创建日历对象

let config = c.getConfig()
```