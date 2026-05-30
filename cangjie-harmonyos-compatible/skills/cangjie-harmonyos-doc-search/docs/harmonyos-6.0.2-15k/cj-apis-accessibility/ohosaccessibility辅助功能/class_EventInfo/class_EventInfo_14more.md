## class EventInfo

```cangjie
public class EventInfo {
    public var `type`: EventType
    public var windowUpdateType: ?WindowUpdateType
    public var bundleName: String
    public var componentType: ?String
    public var pageId: ?Int32
    public var description: ?String
    public var triggerAction: Action
    public var textMoveUnit: ?TextMoveUnit
    public var contents: ?Array<String>
    public var lastContent: ?String
    public var beginIndex: ?Int32
    public var currentIndex: ?Int32
    public var endIndex: ?Int32
    public var itemCount: ?Int32
    public var elementId: ?Int64
    public var textAnnouncedForAccessibility: ?String
    public var customId: ?String
    public init(`type`!: EventType, bundleName!: String, triggerAction!: Action)
}
```

**功能：** 界面变更事件。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### var \`type\`

```cangjie
public var `type`: EventType
```

**功能：** 无障碍事件类型。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**类型：** [EventType](#enum-eventtype)

**读写能力：** 可读写

**起始版本：** 19

### var beginIndex

```cangjie
public var beginIndex: ?Int32
```

**功能：** 画面显示条目的开始序号。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 19

### var bundleName

```cangjie
public var bundleName: String
```

**功能：** 目标应用名。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var componentType

```cangjie
public var componentType: ?String
```

**功能：** 事件源组件类型，如按钮、图表。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var contents

```cangjie
public var contents: ?Array<String>
```

**功能：** 内容列表。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**类型：** ?Array\<String>

**读写能力：** 可读写

**起始版本：** 19

### var currentIndex

```cangjie
public var currentIndex: ?Int32
```

**功能：** 当前条目序号。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 19

### var customId

```cangjie
public var customId: ?String
```

**功能：** 主动聚焦的组件ID。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var description

```cangjie
public var description: ?String
```

**功能：** 事件描述。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var elementId

```cangjie
public var elementId: ?Int64
```

**功能：** 组件elementId。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**类型：** ?Int64

**读写能力：** 可读写

**起始版本：** 19

### var endIndex

```cangjie
public var endIndex: ?Int32
```

**功能：** 画面显示条目的结束序号。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 19

### var itemCount

```cangjie
public var itemCount: ?Int32
```

**功能：** 条目总数。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 19

### var lastContent

```cangjie
public var lastContent: ?String
```

**功能：** 最新内容。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var pageId

```cangjie
public var pageId: ?Int32
```

**功能：** 事件源的页面ID。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 19