## class EdgeStyle

```cangjie
public class EdgeStyle {
    public EdgeStyle(
        public var top: BorderStyle,
        public var right: BorderStyle,
        public var bottom: BorderStyle,
        public var left: BorderStyle
    ) {}
}
```

**功能：** 边框样式，用于描述组件边框四条边的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### static let DASHED

```cangjie
public static let DASHED = EdgeStyle(
    BorderStyle.Dashed,
    BorderStyle.Dashed,
    BorderStyle.Dashed,
    BorderStyle.Dashed
)
```

**功能：** 显示为一系列短的方形虚线。

**类型：** dashed边框样式。

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### static let DOTTED

```cangjie
public static let DOTTED = EdgeStyle(
    BorderStyle.Dotted,
    BorderStyle.Dotted,
    BorderStyle.Dotted,
    BorderStyle.Dotted
)
```

**功能：** 显示为一系列圆点，圆点半径为borderWidth的一半。

**类型：** dotted边框样式。

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### static let SOILD

```cangjie
public static let SOILD = EdgeStyle(
        BorderStyle.Solid,
        BorderStyle.Solid,
        BorderStyle.Solid,
        BorderStyle.Solid
)
```

**功能：** 显示为一条实线。

**类型：** solid边框样式。

**读写能力：** 只读

**起始版本：** 19

### var bottom

```cangjie
public var bottom: BorderStyle
```

**功能：** 组件下边框样式。

**类型：** [BorderStyle](./cj-common-types.md#enum-borderstyle)

**读写能力：** 可读写

**起始版本：** 19

### var left

```cangjie
public var left: BorderStyle
```

**功能：** 组件左边框样式。

**类型：** [BorderStyle](./cj-common-types.md#enum-borderstyle)

**读写能力：** 可读写

**起始版本：** 19

### var right

```cangjie
public var right: BorderStyle
```

**功能：** 组件右边框样式。

**类型：** [BorderStyle](./cj-common-types.md#enum-borderstyle)

**读写能力：** 可读写

**起始版本：** 19

### var top

```cangjie
public var top: BorderStyle
```

**功能：** 组件上边框样式。

**类型：** [BorderStyle](./cj-common-types.md#enum-borderstyle)

**读写能力：** 可读写

**起始版本：** 19

### EdgeStyle(BorderStyle, BorderStyle, BorderStyle, BorderStyle)

```cangjie
public EdgeStyle(
    public var top: BorderStyle,
    public var right: BorderStyle,
    public var bottom: BorderStyle,
    public var left: BorderStyle
)
```

**功能：** EdgeStyle构造方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数:**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| top    | [BorderStyle](./cj-common-types.md#enum-borderstyle) | 是   | \-   | 组件上边框样式。 |
| right  | [BorderStyle](./cj-common-types.md#enum-borderstyle) | 是   | \-   | 组件右边框样式。 |
| bottom | [BorderStyle](./cj-common-types.md#enum-borderstyle) | 是   | \-   | 组件下边框样式。 |
| left   | [BorderStyle](./cj-common-types.md#enum-borderstyle) | 是   | \-   | 组件左边框样式。 |