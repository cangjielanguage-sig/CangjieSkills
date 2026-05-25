## enum TextAlignStyle

```cangjie
public enum TextAlignStyle {
    | Left
    | Right
    | Center
    | Justify
    | Start
    | End
}
```

**功能：** 文本对齐方式类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Center

```cangjie
Center
```

**功能：** 文本居中对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### End

```cangjie
End
```

**功能：** 文本对齐界线结束的地方。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Justify

```cangjie
Justify
```

**功能：** 文本两端对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Left

```cangjie
Left
```

**功能：** 文本左对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Right

```cangjie
Right
```

**功能：** 文本右对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Start

```cangjie
Start
```

**功能：** 文本对齐界线开始的地方。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum TextBaseline

```cangjie
public enum TextBaseline {
    | Alphabetic
    | Ideographic
    | Top
    | Bottom
    | Middle
    | Hanging
}
```

**功能：** 设置文本绘制中的水平对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Alphabetic

```cangjie
Alphabetic
```

**功能：** 文本基线是标准的字母基线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Bottom

```cangjie
Bottom
```

**功能：** 文本基线在文本块的底部。 与ideographic基线的区别在于ideographic基线不需要考虑下行字母。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Hanging

```cangjie
Hanging
```

**功能：** 文本基线是悬挂基线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Ideographict

```cangjie
Ideographict
```

**功能：** 文字基线是表意字基线；如果字符本身超出了alphabetic基线，那么ideograhpic基线位置在字符本身的底部。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Middle

```cangjie
Middle
```

**功能：** 文本基线在文本块的中间。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Top

```cangjie
Top
```

**功能：** 文本基线在文本块的顶部。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum TextCase

```cangjie
public enum TextCase {
    | Normal
    | LowerCase
    | UpperCase
}
```

**功能：** 文本大小写格式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### LowerCase

```cangjie
LowerCase
```

**功能：** 文本采用全小写。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Normal

```cangjie
Normal
```

**功能：** 保持文本原有大小写。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### UpperCase

```cangjie
UpperCase
```

**功能：** 文本采用全大写。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum TextContentStyle

```cangjie
public enum TextContentStyle {
    | DEFAULT
    | INLINE
}
```

**功能：** 文本框多态样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### DEFAULT

```cangjie
DEFAULT
```

**功能：** 默认风格，光标宽1.5vp，光标高度与文本选中底板高度和字体大小相关。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### INLINE

```cangjie
INLINE
```

**功能：** 内联输入风格。文本选中底板高度与输入框高度相同。
内联输入是在有明显的编辑态/非编辑态的区分场景下使用，例如：文件列表视图中的重命名。
不支持showError属性。
内联模式下，不支持拖入文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19