### var title

```cangjie
public var title: String = ""
```

**功能：** 日程标题。不填时，默认为空字符串。

**类型：** String

**读写能力：** 可读写

**起始版本：** 20

### Event(EventType, Int64, Int64, ?Int64, String, ?Location, Bool, ?Array\<Attendee>, String, Array\<Int64>, ?RecurrenceRule, String, ?EventService, ?String, Bool)

```cangjie
public Event(
    public var `type`: EventType,
    public var startTime: Int64,
    public var endTime: Int64,
    public var id!: ?Int64 = 0,
    public var title!: String = "",
    public var location!: ?Location = None,
    public var isAllDay!: Bool = false,
    public var attendee!: ?Array<Attendee> = None,
    public var timeZone!: String = "",
    public var reminderTime!: Array<Int64> = [],
    public var recurrenceRule!: ?RecurrenceRule = None,
    public var description!: String = "",
    public var service!: ?EventService = None,
    public var identifier!: ?String = "",
    public var isLunar!: Bool = false
)
```

**功能：** 构造Event对象。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[EventType](#enum-eventtype)|是|-|日程类型。|
|startTime|Int64|是|-|日程开始时间，需要13位时间戳。|
|endTime|Int64|是|-|日程结束时间，需要13位时间戳。|
|id|?Int64|否|0|日程id。当调用addEvent()、addEvents()创建日程时，不填写此参数。|
|title|String|否|""|日程标题。不填时，默认为空字符串。|
|location|?[Location](#class-location)|否|None|日程地点。|
|isAllDay|Bool|否|false|是否为全天日程。当取值为true时，说明为全天日程；当取值为false时，说明不是全天日程，默认为非全天日程。|
|attendee|?Array\<[Attendee](#class-attendee)>|否|None|会议日程参与者。|
|timeZone|String|否|""|日程时区。不填时，默认为当前所在时区，当需要创建与当前不一样的时区时，可填入对应的时区。|
|reminderTime|Array\<Int64>|否|[]|日程提醒时间，单位为分钟。填写x分钟，即距开始时间提前x分钟提醒，不填时，默认为不提醒。为负值时表示延期多长时间提醒。|
|recurrenceRule|?[RecurrenceRule](#class-recurrencerule)|否|None|日程重复规则。不填时，默认为不重复。|
|description|String|否|""|日程描述。不填时，默认为空字符串。|
|service|?[EventService](#class-eventservice)|否|None|日程服务。不填时，默认没有一键服务。|
|identifier|?String|否|""|写入方可指定日程唯一标识。|
|isLunar|Bool|否|false|是否为农历日程。当取值为true时，说明为农历日程；当取值为false时，说明不是农历日程，默认为非农历日程。|