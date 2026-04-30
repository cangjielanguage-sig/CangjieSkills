## enum LengthMetricsUnit

```cangjie
public enum LengthMetricsUnit {
    | DEFAULT
    | PX
}
```

**功能：** 长度属性单位枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### DEFAULT

```cangjie
DEFAULT
```

**功能：** 长度类型，用于描述以默认的vp像素单位为单位的长度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### PX

```cangjie
PX
```

**功能:** 长度类型，用于描述以px像素单位为单位的长度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum LengthType

```cangjie
public enum LengthType {
    | px
    | vp
    | fp
    | percent
    | lpx
}
```

**功能：** 长度类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- [Length](#interface-length)

### fp

```cangjie
fp
```

**功能：** 字体像素单位。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### lpx

```cangjie
lpx
```

**功能：** 逻辑像素单位。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### percent

```cangjie
percent
```

**功能：** 百分比。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### px

```cangjie
px
```

**功能：** 基本像素单位。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### vp

```cangjie
vp
```

**功能：** 屏幕密度单位。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum LineBreakStrategy

```cangjie
public enum LineBreakStrategy {
    | GREEDY
    | HIGH_QUALITY
    | BALANCED
}
```

**功能：** 文本的折行规则。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### BALANCED

```cangjie
BALANCED
```

**功能：** 尽可能保证在不拆词的情况下，使一个段落中每一行的宽度相同。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### GREEDY

```cangjie
GREEDY
```

**功能：** 使每一行尽量显示多的字符，直到这一行不能显示更多字符再进行折行。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### HIGH_QUALITY

```cangjie
HIGH_QUALITY
```

**功能：** 在BALANCED的基础上，尽可能填满行，在最后一行的权重上比较低，可能会出现最后一行留白比较多。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum LineCapStyle

```cangjie
public enum LineCapStyle {
    | Butt
    | Round
    | Square
}
```

**功能：** 线条样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Butt

```cangjie
Butt
```

**功能：** 线条两端为平行线，不额外扩展。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Round

```cangjie
Round
```

**功能：** 在线条两端延伸半个圆，直径等于线宽。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Square

```cangjie
Square
```

**功能：** 在线条两端延伸半个圆，直径等于线宽。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum LineJoinStyle

```cangjie
public enum LineJoinStyle {
    | Miter
    | Round
    | Bevel
}
```

**功能：** 路径段连接方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Bevel

```cangjie
Bevel
```

**功能：** 使用斜角连接路径段。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Miter

```cangjie
Dotted
```

**功能：** 使用尖角连接路径段。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Round

```cangjie
Round
```

**功能：** 使用圆角连接路径段。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12