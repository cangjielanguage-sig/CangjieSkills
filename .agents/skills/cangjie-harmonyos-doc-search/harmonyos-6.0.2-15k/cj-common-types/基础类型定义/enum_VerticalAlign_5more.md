## enum VerticalAlign

```cangjie
public enum VerticalAlign {
    | Top
    | Center
    | Bottom
}
```

**功能：** 垂直方向上对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Bottom

```cangjie
Bottom
```

**功能：** 底部对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Center

```cangjie
Center
```

**功能：** 居中对齐，默认对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Top

```cangjie
Top
```

**功能：** 顶部对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum Visibility

```cangjie
public enum Visibility {
    | Visible
    | Hidden
    | None
}
```

**功能：** 当前组件显示或隐藏。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Hidden

```cangjie
Hidden
```

**功能：** 隐藏，但参与布局进行占位。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### None

```cangjie
None
```

**功能：** 隐藏，但不参与布局，不进行占位。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Visible

```cangjie
Visible
```

**功能：** 显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum WebDarkMode

public enum WebDarkMode {
    | Off
    | On
    | Auto
}

**功能：** Web的深色模式，默认关闭。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Off

```cangjie
Off
```

**功能：** Web的深色模式为关闭。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### On

```cangjie
On
```

**功能：** Web的深色模式为开启。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Auto

```cangjie
Auto
```

**功能：** Web的深色模式为跟随系统。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum Week

```cangjie
public enum Week {
    | Mon
    | Tue
    | Wed
    | Thur
    | Fri
    | Sat
    | Sun
}
```

**功能：** 星期日期信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Fri

```cangjie
Fri
```

**功能：** 星期五。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Mon

```cangjie
Mon
```

**功能：** 星期一。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Sat

```cangjie
Sat
```

**功能：** 星期六。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Sun

```cangjie
Sun
```

**功能：** 星期日。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Thur

```cangjie
Thur
```

**功能：** 星期四。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Tue

```cangjie
Tue
```

**功能：** 星期二。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Wed

```cangjie
Wed
```

**功能：** 星期三。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum WordBreak

```cangjie
public enum WordBreak {
    | Normal
    | BreakAll
    | BreakWord
}
```

**功能：** 设置文本断行规则。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### BreakAll

```cangjie
Normal
```

**功能：** 对于Non-CJK的文本，可在任意2个字符间断行。对于CJK与NORMAL效果一致。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### BreakWord

```cangjie
BreakWord
```

**功能：** 与BREAKALL相同，对于Non-CJK的文本可在任意2个字符间断行，一行文本中有断行破发点（如空白符）时，优先按破发点换行，保障单词优先完整显示。若整一行文本均无断行破发点时，则在任意2个字符间断行。对于CJK与NORMAL效果一致。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Normal

```cangjie
Normal
```

**功能：** CJK(中文、日文、韩文)文本可以在任意2个字符间断行，而Non-CJK文本（如英文等）只能在空白符处断行。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12