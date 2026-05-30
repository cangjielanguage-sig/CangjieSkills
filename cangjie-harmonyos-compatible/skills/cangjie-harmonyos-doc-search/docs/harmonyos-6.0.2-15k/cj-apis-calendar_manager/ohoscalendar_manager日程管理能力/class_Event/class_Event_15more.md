## class Event

```cangjie
public class Event {
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
}
```

**功能：** 日程对象，包含日程标题、开始时间、结束时间等信息。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

### var \`type\`

```cangjie
public var `type`: EventType
```

**功能：** 日程类型。

**类型：** [EventType](#enum-eventtype)

**读写能力：** 可读写

**起始版本：** 20

### var attendee

```cangjie
public var attendee: ?Array<Attendee> = None
```

**功能：** 会议日程参与者。不填时，默认为None。

**类型：** ?Array\<[Attendee](#class-attendee)>

**读写能力：** 可读写

**起始版本：** 20

### var description

```cangjie
public var description: String = ""
```

**功能：** 日程描述。不填时，默认为空字符串。

**类型：** String

**读写能力：** 可读写

**起始版本：** 20

### var endTime

```cangjie
public var endTime: Int64
```

**功能：** 日程结束时间，需要13位时间戳。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 20

### var id

```cangjie
public var id: ?Int64 = 0
```

**功能：** 日程id。当调用addEvent()、addEvents()创建日程时，不填写此参数。

**类型：** ?Int64

**读写能力：** 可读写

**起始版本：** 20

### var identifier

```cangjie
public var identifier: ?String = ""
```

**功能：** 写入方可指定日程唯一标识。不填时，默认为""。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 20

### var isAllDay

```cangjie
public var isAllDay: Bool = false
```

**功能：** 是否为全天日程。当取值为true时，说明为全天日程；当取值为false时，说明不是全天日程，默认为非全天日程。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 20

### var isLunar

```cangjie
public var isLunar: Bool = false
```

**功能：** 是否为全天日程。当取值为true时，说明为全天日程；当取值为false时，说明不是全天日程，默认为非全天日程。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 20

### var location

```cangjie
public var location: ?Location = None
```

**功能：** 日程地点。

**类型：** ?[Location](#class-location)

**读写能力：** 可读写

**起始版本：** 20

### var recurrenceRule

```cangjie
public var recurrenceRule: ?RecurrenceRule = None
```

**功能：** 日程重复规则。不填时，默认为不重复。

**类型：** ?[RecurrenceRule](#class-recurrencerule)

**读写能力：** 可读写

**起始版本：** 20

### var reminderTime

```cangjie
public var reminderTime: Array<Int64> = []
```

**功能：** 日程提醒时间，单位为分钟。填写x分钟，即距开始时间提前x分钟提醒，不填时，默认为不提醒。为负值时表示延期多长时间提醒。

**类型：** Array\<Int64>

**读写能力：** 可读写

**起始版本：** 20

### var service

```cangjie
public var service: ?EventService = None
```

**功能：** 日程服务。不填时，默认没有一键服务。

**类型：** ?[EventService](#class-eventservice)

**读写能力：** 可读写

**起始版本：** 20

### var startTime

```cangjie
public var startTime: Int64
```

**功能：** 日程开始时间，需要13位时间戳。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 20

### var timeZone

```cangjie
public var timeZone: String = ""
```

**功能：** 日程时区。不填时，默认为当前所在时区，当需要创建与当前不一样的时区时，可填入对应的时区。

**类型：** String

**读写能力：** 可读写

**起始版本：** 20