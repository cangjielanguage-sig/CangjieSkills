## enum RichEditorResponseType

```cangjie
public enum RichEditorResponseType {
    | LONG_PRESS
    | RIGHT_CLICK
    | SELECT
}
```

**功能：** 菜单的响应类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### LONG_PRESS

```cangjie
LONG_PRESS
```

**功能：** 通过长按触发菜单弹出。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### RIGHT_CLICK

```cangjie
RIGHT_CLICK
```

**功能：** 通过鼠标右键触发菜单弹出。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SELECT

```cangjie
SELECT
```

**功能：** 通过鼠标选中触发菜单弹出。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum ScrollBarDirection

```cangjie
public enum ScrollBarDirection {
    | Vertical
    | Horizontal
}
```

**功能：** 设置滚动条的方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Vertical

```cangjie
Vertical
```

**功能：** 设置滚动条方向为纵向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Horizontal

```cangjie
Horizontal
```

**功能：** 设置滚动条方向为横向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum ScrollDirection

```cangjie
public enum ScrollDirection {
    | Vertical
    | Horizontal
    | None
}
```

**功能：** 滚动方向枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Horizontal

```cangjie
Horizontal
```

**功能：** 仅支持水平方向滚动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### None

```cangjie
None
```

**功能：** 不可滚动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Vertical

```cangjie
Vertical
```

**功能：** 仅支持竖直方向滚动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum ScrollSource

```cangjie
public enum ScrollSource {
    | DRAG
    | FLING
    | EDGE_EFFECT
    | OTHER_USER_INPUT
    | SCROLL_BAR
    | SCROLL_BAR_FLING
    | SCROLLER
    | SCROLLER_ANIMATION
}
```

**功能：** 滑动操作的来源。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### DRAG

```cangjie
DRAG
```

**功能：** 拖拽事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### EDGE_EFFECT

```cangjie
EDGE_EFFECT
```

**功能：** EdgeEffect.Spring的边缘滚动效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### FLING

```cangjie
FLING
```

**功能：** 拖拽结束之后的惯性滑动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OTHER_USER_INPUT

```cangjie
OTHER_USER_INPUT
```

**功能：** 除拖拽外的其他用户输入，如鼠标滚轮、键盘事件等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SCROLL_BAR

```cangjie
SCROLL_BAR
```

**功能：** 滚动条的拖拽事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SCROLL_BAR_FLING

```cangjie
SCROLL_BAR_FLING
```

**功能：** 滚动条拖拽结束后的带速度的惯性滑动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SCROLLER

```cangjie
SCROLLER
```

**功能：** Scroller的不带动效方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SCROLLER_ANIMATION

```cangjie
SCROLLER_ANIMATION
```

**功能：** Scroller的带动效方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19