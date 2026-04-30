## class EdgeStyles

```cangjie
public class EdgeStyles {
    public var top: BorderStyle
    public var right: BorderStyle
    public var bottom: BorderStyle
    public var left: BorderStyle
    public init(top!: BorderStyle = BorderStyle.Solid, right!: BorderStyle = BorderStyle.Solid, bottom!: BorderStyle = BorderStyle.Solid, left!: BorderStyle = BorderStyle.Solid)
}
```

**功能：** 边框样式，用于描述组件边框四条边的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var bottom

```cangjie
public var bottom: BorderStyle
```

**功能：** 设置组件下边框样式。

**类型：** [BorderStyle](#enum-borderstyle)

**读写能力：** 可读写

**起始版本：** 12

### var left

```cangjie
public var left: BorderStyle
```

**功能：** 设置组件左边框样式。

**类型：** [BorderStyle](#enum-borderstyle)

**读写能力：** 可读写

**起始版本：** 12

### var right

```cangjie
public var right: BorderStyle
```

**功能：** 设置组件右边框样式。

**类型：** [BorderStyle](#enum-borderstyle)

**读写能力：** 可读写

**起始版本：** 12

### var top

```cangjie
public var top: BorderStyle
```

**功能：** 设置组件上边框样式。

**类型：** [BorderStyle](#enum-borderstyle)

**读写能力：** 可读写

**起始版本：** 12

### init(BorderStyle, BorderStyle, BorderStyle, BorderStyle)

```cangjie
public init(top!: BorderStyle = BorderStyle.Solid, right!: BorderStyle = BorderStyle.Solid, bottom!: BorderStyle = BorderStyle.Solid, left!: BorderStyle = BorderStyle.Solid)
```

**功能：** 构造EdgeColor对象。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|top|[BorderStyle](#enum-borderstyle)|否|BorderStyle.Solid| **命名参数。** 组件上边框样式。|
|right|[BorderStyle](#enum-borderstyle)|否|BorderStyle.Solid| **命名参数。** 组件右边框样式。|
|bottom|[BorderStyle](#enum-borderstyle)|否|BorderStyle.Solid| **命名参数。** 组件下边框样式。|
|left|[BorderStyle](#enum-borderstyle)|否|BorderStyle.Solid| **命名参数。** 组件左边框样式。|