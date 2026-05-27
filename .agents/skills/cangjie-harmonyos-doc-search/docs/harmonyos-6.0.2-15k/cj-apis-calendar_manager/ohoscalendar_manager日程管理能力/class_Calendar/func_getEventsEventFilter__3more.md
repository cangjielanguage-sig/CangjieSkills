### func getEvents(?EventFilter, ?Array\<String>)

```cangjie
public func getEvents(eventFilter!: ?EventFilter = None, eventKey!: ?Array<String> = None): Array<Event>
```

**功能：** 获取Calendar下符合查询条件的Event，只有一个入参时，参数必须为查询条件，对应参数类型为EventFilter。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventFilter|?[EventFilter](#class-eventfilter)|否|None|查询条件。|
|eventKey|?Array\<String>|否|None|查询字段。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[Event](#class-event)>|Event对象数组。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CalendarKit.*

let manager = getCalendarManager(context) // 获取日历管理对象

let account = CalendarAccount("122", CalendarType.LOCAL)
let c = manager.createCalendar(account) // 创建日历对象

let events = c.getEvents()
```

### func setConfig(CalendarConfig)

```cangjie
public func setConfig(config: CalendarConfig): Unit
```

**功能：** 设置日历配置信息。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|config|[CalendarConfig](#class-calendarconfig)|是|-|日历配置信息。|

### func updateEvent(Event)

```cangjie
public func updateEvent(event: Event): Unit
```

**功能：** 更新日程。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[Event](#class-event)|是|-|Event对象。|

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
c.updateEvent(eve)
```