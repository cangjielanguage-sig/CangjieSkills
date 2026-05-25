## enum TextDecorationStyle

```cangjie
public enum TextDecorationStyle {
    | SOLID
    | DOUBLE
    | DOTTED
    | DASHED
    | WAVY
}
```

**功能：** 设置文本装饰线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### DASHED

```cangjie
DASHED
```

**功能：** 虚线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### DOTTED

```cangjie
DOTTED
```

**功能：** 点线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### DOUBLE

```cangjie
DOUBLE
```

**功能：** 双实线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SOLID

```cangjie
SOLID
```

**功能：** 单实线（默认值）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### WAVY

```cangjie
WAVY
```

**功能：** 波浪线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum TextDecorationType

```cangjie
public enum TextDecorationType {
    | None
    | Underline
    | Overline
    | LineThrough
}
```

**功能：** 装饰线类型枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### LineThrough

```cangjie
LineThrough
```

**功能：** 穿过文本的修饰线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### None

```cangjie
None
```

**功能：** 不使用文本装饰线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Overline

```cangjie
Overline
```

**功能：** 文字上划线修饰。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Underline

```cangjie
Underline
```

**功能：** 文字下划线修饰。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum TextHeightAdaptivePolicy

```cangjie
public enum TextHeightAdaptivePolicy {
    | MAX_LINES_FIRST
    | MIN_FONT_SIZE_FIRST
    | LAYOUT_CONSTRAINT_FIRST
}
```

**功能：** 设置文本高度自适应方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### LAYOUT_CONSTRAINT_FIRST

```cangjie
LAYOUT_CONSTRAINT_FIRST
```

**功能：** 设置文本高度自适应方式为以布局约束（高度）优先。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### MAX_LINES_FIRST

```cangjie
MAX_LINES_FIRST
```

**功能：** 设置文本高度自适应方式为以MaxLines优先。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### MIN_FONT_SIZE_FIRST

```cangjie
MIN_FONT_SIZE_FIRST
```

**功能：** 设置文本高度自适应方式为以缩小字体优先。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum TextOverflow

```cangjie
public enum TextOverflow {
    | Clip
    | Ellipsis
    | None
    | MARQUEE
}
```

**功能：** 文本超长时的显示方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Clip

```cangjie
Clip
```

**功能：** 文本超长时按最大行截断显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Ellipsis

```cangjie
Ellipsis
```

**功能：** 文本超长时显示不下的文本用省略号代替。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### MARQUEE

```cangjie
MARQUEE
```

**功能：** 文本超长时以跑马灯的方式展示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### None

```cangjie
None
```

**功能：** 文本超长时按最大行截断显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12