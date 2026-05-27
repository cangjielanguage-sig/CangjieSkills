## 导入模块

```cangjie
import kit.CalendarKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func getCalendarManager(UIAbilityContext)

```cangjie
public func getCalendarManager(context: UIAbilityContext): CalendarManager
```

**功能：** 根据上下文获取CalendarManager对象，用于管理日历。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|UIAbilityContext|是|-|应用上下文Context.|

**返回值：**

|类型|说明|
|:----|:----|
|[CalendarManager](#class-calendarmanager)|CalendarManager对象|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CalendarKit.*

let calendarMnager = getCalendarManager(uIAbilityContext) // 获取日历管理对象
```

## class Attendee

```cangjie
public class Attendee {
    public Attendee(
        public var name: String,
        public var email: String,
        public var role!: ?AttendeeRole = None
    )
}
```

**功能：** 会议日程参与者。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

### var email

```cangjie
public var email: String
```

**功能：** 会议日程参与者的邮箱。

**类型：** String

**读写能力：** 可读写

**起始版本：** 20

### var name

```cangjie
public var name: String
```

**功能：** 会议日程参与者的姓名。

**类型：** String

**读写能力：** 可读写

**起始版本：** 20

### var role

```cangjie
public var role: ?AttendeeRole = None
```

**功能：** 会议日程参与者的角色，不填时默认为空。

**类型：** ?[AttendeeRole](#enum-attendeerole)

**读写能力：** 可读写

**起始版本：** 20

### Attendee(String, String, ?AttendeeRole)

```cangjie
public Attendee(
    public var name: String,
    public var email: String,
    public var role!: ?AttendeeRole = None
)
```

**功能：** 构造Attendee对象

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|会议日程参与者的姓名。|
|email|String|是|-|会议日程参与者的邮箱。|
|role|?[AttendeeRole](#enum-attendeerole)|否|None|会议日程参与者的角色，不填时默认为空。|