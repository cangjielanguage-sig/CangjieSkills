## enum RectChangeReason

```cangjie
public enum RectChangeReason {
    | UNDEFINED
    | MAXIMIZE
    | RECOVER
    | MOVE
    | DRAG
    | DRAG_START
    | DRAG_END
}
```

**功能：** 窗口矩形（窗口位置及窗口大小）变化的原因。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### UNDEFINED

```cangjie
UNDEFINED
```

**功能：** 默认值。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### MAXIMIZE

```cangjie
MAXIMIZE
```

**功能：** 窗口最大化。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### RECOVER

```cangjie
RECOVER
```

**功能：** 窗口恢复到上一次的状态。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### MOVE

```cangjie
MOVE
```

**功能：** 窗口拖拽移动。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### DRAG

```cangjie
DRAG
```

**功能：** 窗口拖拽缩放。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### DRAG_START

```cangjie
DRAG_START
```

**功能：** 窗口开始拖拽缩放。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### DRAG_END

```cangjie
DRAG_END
```

**功能：** 窗口结束拖拽缩放。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

## enum SpecificSystemBar

```cangjie
public enum SpecificSystemBar {
    | status
    | navigation
    | navigationIndicator
}
```

**功能：** 当前支持显示或隐藏的系统栏类型。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### status

```cangjie
status
```

**功能：** 状态栏。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### navigation

```cangjie
navigation
```

**功能：** 三键导航栏。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### navigationIndicator

```cangjie
navigationIndicator
```

**功能：** 底部导航条。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19