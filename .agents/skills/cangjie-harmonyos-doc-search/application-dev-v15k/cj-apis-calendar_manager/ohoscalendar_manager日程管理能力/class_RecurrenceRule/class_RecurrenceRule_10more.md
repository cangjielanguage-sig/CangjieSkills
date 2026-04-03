## class RecurrenceRule

```cangjie
public class RecurrenceRule {
    public RecurrenceRule(
        public var recurrenceFrequency: RecurrenceFrequency,
        public var expire!: ?Int64 = 0,
        public var count!: ?Int64 = 0,
        public var interval!: ?Int64 = 0,
        public var excludedDates!: ?Array<Int64> = [],
        public var daysOfWeek!: ?Array<Int64> = [],
        public var daysOfMonth!: ?Array<Int64> = [],
        public var daysOfYear!: ?Array<Int64> = [],
        public var weeksOfMonth!: ?Array<Int64> = [],
        public var weeksOfYear!: ?Array<Int64> = [],
        public var monthsOfYear!: ?Array<Int64> = []
    )
}
```

**功能：** 日程重复规则。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

### var count

```cangjie
public var count: ?Int64 = 0
```

**功能：** 重复日程的重复次数，取值为非负整数，不填时默认为0，表示不会限定重复次数，会一直重复，取值为负时，效果等同于取值为0。当count与expire同时存在时以count为准。

**类型：** ?Int64

**读写能力：** 可读写

**起始版本：** 20

### var daysOfMonth

```cangjie
public var daysOfMonth: ?Array<Int64> = []
```

**功能：** 按照一个月第几天重复。不填时，默认为空，表示没有一个月第几天重复的规则。范围为1到31，1到31对应1到31号，其他值为无效值，与空值效果相同。若当月没有31号，31也为无效值。

**类型：** ?Array\<Int64>

**读写能力：** 可读写

**起始版本：** 20

### var daysOfWeek

```cangjie
public var daysOfWeek: ?Array<Int64> = []
```

**功能：** 按照一周第几天重复。不填时，默认为空，表示没有一周第几天重复的规则。范围为1到7，对应周一到周日，其他值为无效值，与空值效果相同。

**类型：** ?Array\<Int64>

**读写能力：** 可读写

**起始版本：** 20

### var daysOfYear

```cangjie
public var daysOfYear: ?Array<Int64> = []
```

**功能：** 按照一年第几天重复。不填时，默认为空，表示没有一年第几天重复的规则。范围为1到366，1到366表示一年的1到366天，其他值为无效值，与空值效果相同。若当年没有366天，366也为无效值。

**类型：** ?Array\<Int64>

**读写能力：** 可读写

**起始版本：** 20

### var excludedDates

```cangjie
public var excludedDates: ?Array<Int64> = []
```

**功能：** 重复日程的排除日期，参数取值为时间戳格式，不填时，默认为空，表示没有排除的日期，0或负数为无效值，与空值效果相同。

**类型：** ?Array\<Int64>

**读写能力：** 可读写

**起始版本：** 20

### var expire

```cangjie
public var expire: ?Int64 = 0
```

**功能：** 重复周期截止日。不填时，默认为0。

**类型：** ?Int64

**读写能力：** 可读写

**起始版本：** 20

### var interval

```cangjie
public var interval: ?Int64 = 0
```

**功能：** 重复日程的重复间隔，取值为非负整数，不填时默认为0，表示日程按照重复规则一直重复，没有间隔。取值为负时，效果等同于取值为0。当interval与expire同时存在时以expire为准。此属性与recurrenceFrequency重复规则相关，不同的重复规则下，表示的重复间隔不同，以interval取2为例，分为以下几种情况：每天重复时：表示日程每隔两天重复一次。每周重复时：表示日程每隔两周重复一次。每月重复时：表示日程每隔两月重复一次。每年重复时：表示日程每隔两年重复一次。

**类型：** ?Int64

**读写能力：** 可读写

**起始版本：** 20

### var monthsOfYear

```cangjie
public var monthsOfYear: ?Array<Int64> = []
```

**功能：** 按照一年中第几个月重复。不填时，默认为空，表示没有一年第几个月重复的规则。范围为1到12，1到12为每年的1到12月，其他值为无效值，与空值效果相同。

**类型：** ?Array\<Int64>

**读写能力：** 可读写

**起始版本：** 20

### var recurrenceFrequency

```cangjie
public var recurrenceFrequency: RecurrenceFrequency
```

**功能：** 日程重复规则类型。

**类型：** [RecurrenceFrequency](#enum-recurrencefrequency)

**读写能力：** 可读写

**起始版本：** 20