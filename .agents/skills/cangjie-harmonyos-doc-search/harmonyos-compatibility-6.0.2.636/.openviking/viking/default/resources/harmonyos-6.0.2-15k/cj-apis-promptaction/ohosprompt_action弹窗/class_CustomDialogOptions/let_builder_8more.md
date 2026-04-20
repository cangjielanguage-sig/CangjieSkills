### let builder

```cangjie
public let builder: () -> Unit = {=>}
```

**功能：** 表示自定义弹窗的内容。

**类型：** ()->Unit

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let backgroundColor

```cangjie
public let backgroundColor: UInt32 = Color.TRANSPARENT.toUInt32()
```

**功能：** 表示弹窗背板颜色。

> **说明：**
>
> 当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则颜色显示将不符合预期效果。

**类型：** UInt32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let cornerRadius

```cangjie
public let cornerRadius: BorderRadiuses = BorderRadiuses(topLeft: 32.vp, topRight: 32.vp, bottomLeft: 32.vp,
    bottomRight: 32.vp)
```

**功能：** 表示背板的圆角半径。可分别设置4个圆角的半径。圆角大小受组件尺寸限制，最大值为组件宽或高的一半，若值为负，则按照默认值处理。百分比参数方式：以父元素弹窗宽和高的百分比来设置弹窗的圆角。

**类型：** [BorderRadiuses](./cj-common-types.md#class-borderradiuses)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let borderWidth

```cangjie
public let borderWidth: EdgeWidths = EdgeWidths()
```

**功能：** 表示弹窗背板的边框宽度。可分别设置4个边框宽度。百分比参数方式：以父元素弹窗宽的百分比来设置弹窗的边框宽度。当弹窗左边框和右边框大于弹窗宽度，弹窗上边框和下边框大于弹窗高度，显示可能不符合预期。

**类型：** [EdgeWidths](./cj-universal-attribute-border.md#class-edgewidths)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let borderColor

```cangjie
public let borderColor: EdgeColor = EdgeColor()
```

**功能：** 表示弹窗背板的边框颜色。如果使用borderColor属性，需要和borderWidth属性一起使用。

**类型：** [EdgeColor](#class-edgecolor)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let borderStyle

```cangjie
public let borderStyle: Option<BorderStyle> = None
```

**功能：** 表示弹窗背板的边框样式。如果使用borderStyle属性，需要和borderWidth属性一起使用。

> **说明：**
>
> - borderStyle与borderEdgeStyle同时设置为非NONE时，仅borderEdgeStyle生效。
> - borderEdgeStyle设置为NONE时，borderStyle设置值生效。
> - borderStyle与borderEdgeStyle同时设置为NONE时，使用默认值BorderStyle.Solid。

**类型：** Option\<[BorderStyle](./cj-common-types.md#enum-borderstyle)>

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let borderEdgeStyle

```cangjie
public let borderEdgeStyle: Option<EdgeStyles> = None
```

**功能：** 表示弹窗背板的边框样式。如果使用borderStyle属性，需要和borderWidth属性一起使用。

> **说明：**
>
> - borderStyle与borderEdgeStyle同时设置为非NONE时，仅borderEdgeStyle生效。
> - borderEdgeStyle设置为NONE时，borderStyle设置值生效。
> - borderStyle与borderEdgeStyle同时设置为NONE时，使用默认值BorderStyle.Solid。

**类型：** Option\<[EdgeStyles](./cj-common-types.md#class-edgestyles)>

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let width

```cangjie
public let width: Length = 400.vp
```

**功能：** 表示弹窗背板的宽度。

> **说明：**
>
> 百分比参数方式：弹窗参考宽度为所在窗口的宽度，在此基础上调小或调大。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19