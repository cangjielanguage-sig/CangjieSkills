## enum TextSelectableMode

```cangjie
public enum TextSelectableMode {
    | SELECTABLE_UNFOCUSABLE
    | SELECTABLE_FOCUSABLE
    | UNSELECTABLE
}
```

**功能：** 文本是否支持可选择、可获焦。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SELECTABLE_FOCUSABLE

```cangjie
SELECTABLE_FOCUSABLE
```

**功能：** 文本可选择，可获焦并Touch后获得焦点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SELECTABLE_UNFOCUSABLE

```cangjie
SELECTABLE_UNFOCUSABLE
```

**功能：** 文本可选择，但不可获焦，设置属性selection、bindSelectionMenu、copyOption不影响当前行为。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### UNSELECTABLE

```cangjie
UNSELECTABLE
```

**功能：** 文本不可选择，不可获焦，设置属性selection、bindSelectionMenu、copyOption都不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum ThemeColorMode

```cangjie
public enum ThemeColorMode {
    | SYSTEM
    | LIGHT
    | DARK
}
```

**功能：** 主题颜色模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### DARK

```cangjie
DARK
```

**功能：** 固定使用深色模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### LIGHT

```cangjie
LIGHT
```

**功能：** 固定使用浅色模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### SYSTEM

```cangjie
COMPONENT_ULTRA_THICK
```

**功能：** 跟随系统深浅色模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum TitleHeight

```cangjie
public enum TitleHeight {
    | MainOnly
    | MainWithSub
}
```

**功能：** 设置标题栏高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### MainOnly

```cangjie
MainOnly
```

**功能：** 只有主标题时标题栏的推荐高度（56vp）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### MainWithSub

```cangjie
MainWithSub
```

**功能：** 同时有主标题和副标题时标题栏的推荐高度（82vp）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum TouchType

```cangjie
public enum TouchType {
    | Down
    | Up
    | Move
    | Cancel
    | Unknown
}
```

**功能：** 触摸触发方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Cancel

```cangjie
Cancel
```

**功能：** 触摸事件取消时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Down

```cangjie
Down
```

**功能：** 手指按下时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Move

```cangjie
Move
```

**功能：** 手指按压态在屏幕上移动时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Up

```cangjie
Up
```

**功能：** 手指抬起时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum TransitionType

```cangjie
public enum TransitionType {
    | All
    | Insert
    | Delete
}
```

**功能：** 指定该转场样式生效的场景。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### All

```cangjie
All
```

**功能：** 指定当前的Transition动效生效在组件的所有变化场景。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Delete

```cangjie
Delete
```

**功能：** 指定当前的Transition动效生效在组件的删除隐藏场景。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Insert

```cangjie
Insert
```

**功能：** 指定当前的Transition动效生效在组件的插入显示场景。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19