## enum BlurStyleActivePolicy

```cangjie
public enum BlurStyleActivePolicy {
    | FOLLOWS_WINDOW_ACTIVE_STATE
    | ALWAYS_ACTIVE
    | ALWAYS_INACTIVE
}
```

**功能：** 模糊效果激活策略。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### ALWAYS_ACTIVE

```cangjie
ALWAYS_ACTIVE
```

**功能：** 一直有模糊效果。

**起始版本：** 12

### ALWAYS_INACTIVE

```cangjie
ALWAYS_INACTIVE
```

**功能：** 一直无模糊效果。

**起始版本：** 12

### FOLLOWS_WINDOW_ACTIVE_STATE

```cangjie
FOLLOWS_WINDOW_ACTIVE_STATE
```

**功能：** 模糊效果跟随窗口焦点状态变化，非焦点不模糊，焦点模糊。

**起始版本：** 12

## enum BorderStyle

```cangjie
public enum BorderStyle {
    | Solid
    | Dashed
    | Dotted
}
```

**功能：** 边框样式，用于描述组件边框四条边的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Dashed

```cangjie
Dashed
```

**功能：** 显示为一系列短的方形虚线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Dotted

```cangjie
Dotted
```

**功能：** 显示为一系列圆点，圆点半径为borderWidth的一半。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Solid

```cangjie
Solid
```

**功能：** 显示为一条实线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum ButtonRole

```cangjie
public enum ButtonRole {
    | NORMAL
    | ERROR
}
```

**功能：** 按键类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### ERROR

```cangjie
ERROR
```

**功能：** 警示按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### NORMAL

```cangjie
NORMAL
```

**功能：** 正常按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum ButtonStyleMode

```cangjie
public enum ButtonStyleMode {
    | NORMAL
    | EMPHASIZED
    | TEXTUAL
}
```

**功能：** 按钮的样式和重要程度类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### EMPHASIZED

```cangjie
EMPHASIZED
```

**功能：** 强调按钮（用于强调当前操作）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### NORMAL

```cangjie
NORMAL
```

**功能：** 普通按钮（一般界面操作）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### TEXTUAL

```cangjie
TEXTUAL
```

**功能：** 文本按钮（纯文本，无背景颜色）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum ButtonType

```cangjie
public enum ButtonType {
    | Normal
    | Capsule
    | Circle
    | ROUNDED_RECTANGLE
}
```

**功能：** 按键形状类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Capsule

```cangjie
Capsule
```

**功能：** 胶囊型按钮（圆角默认为高度的一半）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Circle

```cangjie
Circle
```

**功能：** 圆形按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Normal

```cangjie
Normal
```

**功能：** 普通按钮（默认不带圆角）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### ROUNDED_RECTANGLE

```cangjie
ROUNDED_RECTANGLE
```

**功能：** 圆角矩形按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum CanvasDirection

```cangjie
public enum CanvasDirection {
    | inherit
    | ltr
    | rtl
}
```

**功能：** 设置绘制文字时使用的文字方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### inherit

```cangjie
inherit
```

**功能：** 继承canvas组件通用属性已设定的文本方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### ltr

```cangjie
ltr
```

**功能：** 从左往右。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### rtl

```cangjie
rtl
```

**功能：** 从右往左。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19