### var textAnnouncedForAccessibility

```cangjie
public var textAnnouncedForAccessibility: ?String
```

**功能：** 主动播报的内容。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var textMoveUnit

```cangjie
public var textMoveUnit: ?TextMoveUnit
```

**功能：** 文本移动粒度。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**类型：** ?[TextMoveUnit](#enum-textmoveunit)

**读写能力：** 可读写

**起始版本：** 19

### var triggerAction

```cangjie
public var triggerAction: Action
```

**功能：** 触发事件的Action。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**类型：** [Action](#enum-action)

**读写能力：** 可读写

**起始版本：** 19

### var windowUpdateType

```cangjie
public var windowUpdateType: ?WindowUpdateType
```

**功能：** 窗口变化类型。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**类型：** ?[WindowUpdateType](#enum-windowupdatetype)

**读写能力：** 可读写

**起始版本：** 19

### init(EventType, String, Action)

```cangjie
public init(`type`!: EventType, bundleName!: String, triggerAction!: Action)
```

**功能：** EventInfo的构造函数。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[EventType](#enum-eventtype)|是|-| **命名参数。** 无障碍事件类型。|
|bundleName|String|是|-| **命名参数。** 目标应用名。|
|triggerAction|[Action](#enum-action)|是|-| **命名参数。** 触发事件的Action。|