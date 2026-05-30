## enum Action

```cangjie
public enum Action <: Equatable<Action> & ToString {
    | ACTION_ACCESSIBILITYFOCUS
    | ACTION_CLEARACCESSIBILITYFOCUS
    | ACTION_FOCUS
    | ACTION_CLEARFOCUS
    | ACTION_CLEARSELECTION
    | ACTION_CLICK
    | ACTION_LONGCLICK
    | ACTION_CUT
    | ACTION_COPY
    | ACTION_PASTE
    | ACTION_SELECT
    | ACTION_SETTEXT
    | ACTION_DELETE
    | ACTION_SCROLLFORWARD
    | ACTION_SCROLLBACKWARD
    | ACTION_SETSELECTION
    | ACTION_SETCURSORPOSITION
    | ACTION_HOME
    | ACTION_BACK
    | ACTION_RECENTTASK
    | ACTION_NOTIFICATIONCENTER
    | ACTION_CONTROLCENTER
    | ACTION_COMMON
    | ...
}
```

**功能：** 应用所支持的目标动作，需要配置参数的目标动作已在描述中标明。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**父类型：**

- Equatable\<[Action](#enum-action)>
- ToString

### ACTION_ACCESSIBILITYFOCUS

```cangjie
ACTION_ACCESSIBILITYFOCUS
```

**功能：** 表示获得无障碍焦点操作。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_BACK

```cangjie
ACTION_BACK
```

**功能：** 表示返回上一级操作。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_CLEARACCESSIBILITYFOCUS

```cangjie
ACTION_CLEARACCESSIBILITYFOCUS
```

**功能：** 表示清除无障碍焦点操作。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_CLEARFOCUS

```cangjie
ACTION_CLEARFOCUS
```

**功能：** 表示清除焦点操作。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_CLEARSELECTION

```cangjie
ACTION_CLEARSELECTION
```

**功能：** 表示清除选择操作。当前版本暂不支持。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_CLICK

```cangjie
ACTION_CLICK
```

**功能：** 表示点击操作。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_COMMON

```cangjie
ACTION_COMMON
```

**功能：** 表示没有特定操作，用于主动聚焦、主动播报等场景。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_CONTROLCENTER

```cangjie
ACTION_CONTROLCENTER
```

**功能：** 表示打开控制中心操作。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_COPY

```cangjie
ACTION_COPY
```

**功能：** 表示复制操作。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_CUT

```cangjie
ACTION_CUT
```

**功能：** 表示剪切操作。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_DELETE

```cangjie
ACTION_DELETE
```

**功能：** 表示删除操作。当前版本暂不支持。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_FOCUS

```cangjie
ACTION_FOCUS
```

**功能：** 表示获得焦点操作。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_HOME

```cangjie
ACTION_HOME
```

**功能：** 表示返回桌面操作。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_LONGCLICK

```cangjie
ACTION_LONGCLICK
```

**功能：** 表示长按操作。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_NOTIFICATIONCENTER

```cangjie
ACTION_NOTIFICATIONCENTER
```

**功能：** 表示打开通知栏操作。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_PASTE

```cangjie
ACTION_PASTE
```

**功能：** 表示粘贴操作。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19