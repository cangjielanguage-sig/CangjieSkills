### var alignment

```cangjie
public var alignment: Option<DialogAlignment> = DialogAlignment.Bottom
```

**功能:** 弹窗在竖直方向上的对齐方式。

**类型:** Option\<[DialogAlignment](./cj-common-types.md#enum-dialogalignment)>

**读写能力:** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var autoCancel

```cangjie
public var autoCancel: Option<Bool> = true
```

**功能:** 点击遮障层时，是否关闭弹窗。

**类型:** Option\<Bool>

**读写能力:** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var backgroundBlurStyle

```cangjie
public var backgroundBlurStyle: Option<BlurStyle> = BlurStyle.COMPONENT_ULTRA_THICK
```

**功能:** 弹窗背板模糊材质。

**类型:** Option\<[BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)>

**读写能力:** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var backgroundColor

```cangjie
public var backgroundColor: Option<Color> = Option.None
```

**功能:** 弹窗背板颜色。

**类型:** Option\<[Color](./cj-common-types.md#class-color)>

**读写能力:** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var borderColor

```cangjie
public var borderColor: Option<Color> = Color.BLACK
```

**功能:** 设置弹窗背板的边框颜色。如果使用borderColor属性，需要和borderWidth属性一起使用。

**类型:** Option\<[Color](./cj-common-types.md#class-color)>

**读写能力:** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var borderStyle

```cangjie
public var borderStyle: Option<EdgeStyle> = EdgeStyle.SOILD
```

**功能:** 设置弹窗背板的边框样式。如果使用borderStyle属性，需要和borderWidth属性一起使用。

**类型:** Option\<[EdgeStyle](cj-dialog-actionsheet.md#class-edgestyle)>

**读写能力:** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var borderWidth

```cangjie
public var borderWidth: Option<Length> = 0.vp
```

**功能:** 设置弹窗背板的边框宽度。

**类型:** Option\<[Length](./cj-common-types.md#interface-length)>

**读写能力:** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var cancel

```cangjie
public var cancel: Option<() -> Unit> = Option.None
```

**功能:** 点击遮障层关闭dialog时的回调。

**类型:** Option\<() -> Unit>

**读写能力:** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var cornerRadius

```cangjie
public var cornerRadius: Option<BorderRadiuses> = BorderRadiuses(topLeft: 32.vp, topRight: 32.vp, bottomLeft: 32.vp,
    bottomRight: 32.vp)
```

**功能:** 设置背板的圆角半径。可分别设置4个圆角的半径。

**类型:** Option\<[BorderRadiuses](./cj-common-types.md#class-borderradiuses)>

**读写能力:** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var gridCount

```cangjie
public var gridCount: Option<UInt32> = 4
```

**功能:** 弹窗容器宽度所占用栅格数。

**类型:** Option\<UInt32>

**读写能力:** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var height

```cangjie
public var height: Option<Length> = Option<Length>.None
```

**功能:** 设置弹窗背板的高度。

**类型:** Option\<[Length](./cj-common-types.md#interface-length)>

**读写能力:** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var isModal

```cangjie
public var isModal: Option<Bool> = true
```

**功能:** 弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。

**类型:** Option\<Bool>

**读写能力:** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12