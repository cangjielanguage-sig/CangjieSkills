## enum CanvasFillRule

```cangjie
public enum CanvasFillRule {
    | evenodd
    | nonzero
}
```

**功能：** 指定要填充对象的规则。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### evenodd

```cangjie
evenodd
```

**功能：** 奇偶规则。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### nonzero

```cangjie
nonzero
```

**功能：** 非零规则。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum CheckBoxShape

```cangjie
public enum CheckBoxShape {
    | CIRCLE
    | ROUNDED_SQUARE
}
```

**功能：** 多选框形状类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### CIRCLE

```cangjie
CIRCLE
```

**功能：** 圆形形状。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### ROUNDED_SQUARE

```cangjie
ROUNDED_SQUARE
```

**功能：** 圆角方形形状。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum ClickEffectLevel

```cangjie
public enum ClickEffectLevel {
    | LIGHT
    | MIDDLE
    | HEAVY
}
```

**功能：** 点击回弹动效设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### HEAVY

```cangjie
HEAVY
```

**功能：** 大面积（厚重）。弹簧动效， 刚性：350，阻尼：35，初始速度：0.5。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### LIGHT

```cangjie
LIGHT
```

**功能：** 小面积（轻盈）。弹簧动效， 刚性：410，阻尼：38，初始速度：1。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### MIDDLE

```cangjie
MIDDLE
```

**功能：** 中面积（稳定）。弹簧动效， 刚性：350，阻尼：35，初始速度：0.5。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum ColoringStrategy

```cangjie
public enum ColoringStrategy {
    | INVERT
    | AVERAGE
    | PRIMARY
}
```

**功能：** 智能取色枚举类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### AVERAGE

```cangjie
AVERAGE
```

**功能：** 设置控件背景阴影色为控件背景阴影区域的平均色。仅支持在入参类型为ShadowOptions的shadow中设置该枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### INVERT

```cangjie
INVERT
```

**功能：** 设置前景色为控件背景色的反色。仅支持在foregroundColor中设置该枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### PRIMARY

```cangjie
PRIMARY
```

**功能：** 设置控件背景阴影色为控件背景阴影区域的主色。仅支持在入参类型为ShadowOptions的shadow中设置该枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19