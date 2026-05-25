## enum AttendeeRole

```cangjie
public enum AttendeeRole {
    | ORGANIZER
    | PARTICIPANT
    | ...
}
```

**功能：** 会议日程参与者角色类型枚举。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

### Organizer

```cangjie
Organizer
```

**功能：** 会议组织者。

**起始版本：** 20

### Participant

```cangjie
Participant
```

**功能：** 会议参与者。

**起始版本：** 20

## enum CalendarType

```cangjie
public enum CalendarType {
    | Local
    | Email
    | Birthday
    | CalDAV
    | Subscribed
    | ...
}
```

**功能：** 账户类型枚举。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

### Birthday

```cangjie
Birthday
```

**功能：** 生日账户。

**起始版本：** 20

### CalDAV

```cangjie
CalDAV
```

**功能：** 支持CalDAV协议账户。

**起始版本：** 20

### Email

```cangjie
Email
```

**功能：** 邮箱账户。

**起始版本：** 20

### Local

```cangjie
Local
```

**功能：** 本地账户。

**起始版本：** 20

### Subscribed

```cangjie
Subscribed
```

**功能：** 订阅账户。

**起始版本：** 20

## enum EventType

```cangjie
public enum EventType {
    | Normal
    | Important
    | ...
}
```

**功能：** 日程类型枚举。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

### Important

```cangjie
Important
```

**功能：** 重要日程，例如结婚纪念日等具有重要意义的日期，不推荐三方开发者使用，重要日程类型不支持一键服务跳转功能及无法自定义提醒时间。

**起始版本：** 20

### Normal

```cangjie
Normal
```

**功能：** 普通日程，例如会议，闹钟等日常提醒的日程。

**起始版本：** 20

## enum RecurrenceFrequency

```cangjie
public enum RecurrenceFrequency {
    | Yearly
    | Monthly
    | Weekly
    | Daily
    | ...
}
```

**功能：** 日程重复规则类型枚举。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

### Daily

```cangjie
Daily
```

**功能：** 每天重复。

**起始版本：** 20

### Monthly

```cangjie
Monthly
```

**功能：** 每月重复。

**起始版本：** 20

### Weekly

```cangjie
Weekly
```

**功能：** 每周重复。

**起始版本：** 20

### Yearly

```cangjie
Yearly
```

**功能：** 每年重复。

**起始版本：** 20

## enum ServiceType

```cangjie
public enum ServiceType <: ToString {
    | Meeting
    | Watching
    | Repayment
    | Live
    | Shopping
    | Trip
    | Class
    | SportsEvents
    | SportsExercise
    | ...
}
```

**功能：** 日程服务类型枚举。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**父类型：**

- ToString

### Class

```cangjie
Class
```

**功能：** 一键上课。

**起始版本：** 20

### Live

```cangjie
Live
```

**功能：** 一键直播。

**起始版本：** 20

### Meeting

```cangjie
Meeting
```

**功能：** 一键入会。

**起始版本：** 20

### Repayment

```cangjie
Repayment
```

**功能：** 一键还款。

**起始版本：** 20

### Shopping

```cangjie
Shopping
```

**功能：** 一键购物。

**起始版本：** 20

### SportsEvents

```cangjie
SportsEvents
```

**功能：** 一键看赛事。

**起始版本：** 20

### SportsExercise

```cangjie
SportsExercise
```

**功能：** 一键运动。

**起始版本：** 20

### Trip

```cangjie
Trip
```

**功能：** 一键查看。

**起始版本：** 20

### Watching

```cangjie
Watching
```

**功能：** 一键追剧。

**起始版本：** 20

### func toString()

```cangjie
public func toString(): String
```

**功能：** 日程服务类型枚举转换为String类型。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|日程服务类型枚举值|