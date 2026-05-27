## enum ScrollState

```cangjie
public enum ScrollState {
    | Idle
    | Scrolling
    | Fling
}
```

**功能：** 设置当前滑动状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Fling

```cangjie
Fling
```

**功能：** 惯性滑动状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Idle

```cangjie
Idle
```

**功能：** 未滑动状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Scrolling

```cangjie
Scrolling
```

**功能：** 手指拖动状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum StickyStyle

```cangjie
public enum StickyStyle {
    | None
    | Header
    | Footer
    | Both
}
```

**功能：** 设置ListItemGroup中header和footer是否要吸顶或吸底。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### None

```cangjie
None
```

**功能：** 设置ListItemGroup的headerh不吸顶，footer不吸底。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Header

```cangjie
Header
```

**功能：** 设置ListItemGroup的headerh吸顶。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Footer

```cangjie
Footer
```

**功能：** 设置ListItemGroup的footer吸底。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Both

```cangjie
Both
```

**功能：** 设置ListItemGroup的headerh吸顶，footer吸底。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum SwipeEdgeEffect

```cangjie
public enum SwipeEdgeEffect {
    | Spring
    | None
}
```

**功能：** ListItem的滑动效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Spring

```cangjie
Spring
```

**功能：** ListItem划动距离超过划出组件大小后可以继续划动，松手后按照弹簧阻尼曲线回弹。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### CARD

```cangjie
CARD
```

**功能：** ListItem划动距离不能超过划出组件大小。

**起始版本：** 12

## enum ShadowStyle

```cangjie
public enum ShadowStyle {
    | OUTER_DEFAULT_XS
    | OUTER_DEFAULT_SM
    | OUTER_DEFAULT_MD
    | OUTER_DEFAULT_LG
    | OUTER_FLOATING_SM
    | OUTER_FLOATING_MD
}
```

**功能：** 阴影样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OUTER_DEFAULT_LG

```cangjie
OUTER_DEFAULT_LG
```

**功能：** 大阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OUTER_DEFAULT_MD

```cangjie
OUTER_DEFAULT_MD
```

**功能：** 中阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OUTER_DEFAULT_SM

```cangjie
OUTER_DEFAULT_SM
```

**功能：** 小阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OUTER_DEFAULT_XS

```cangjie
OUTER_DEFAULT_XS
```

**功能：** 超小阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OUTER_FLOATING_MD

```cangjie
OUTER_FLOATING_MD
```

**功能：** 浮动中阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OUTER_FLOATING_SM

```cangjie
OUTER_FLOATING_SM
```

**功能：** 浮动小阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum ShadowType

```cangjie
public enum ShadowType {
    | COLOR
    | BLUR
}
```

**功能：** 阴影类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### BLUR

```cangjie
BLUR
```

**功能：** 模糊。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### COLOR

```cangjie
COLOR
```

**功能：** 颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19