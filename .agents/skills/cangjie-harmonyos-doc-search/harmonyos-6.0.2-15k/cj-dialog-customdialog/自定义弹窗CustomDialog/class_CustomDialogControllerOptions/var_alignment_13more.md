### var alignment

```cangjie
public var alignment: DialogAlignment
```

**功能：** 弹窗在竖直方向上的对齐方式。

**类型：** [DialogAlignment](./cj-common-types.md#enum-dialogalignment)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var autoCancel

```cangjie
public var autoCancel: Bool
```

**功能：** 是否允许点击遮障层退出。true表示关闭弹窗，false表示不关闭弹窗。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var backgroundBlurStyle

```cangjie
public var backgroundBlurStyle: Option<BlurStyle>
```

**功能：** 弹窗背板模糊材质。

**类型：** Option\<[BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var backgroundColor

```cangjie
public var backgroundColor: Option<ResourceColor>
```

**功能：** 设置弹窗背板填充。

**类型：** Option\<[ResourceColor](./cj-common-types.md#interface-resourcecolor)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var borderColor

```cangjie
public var borderColor: Option<ResourceColor>
```

**功能：** 设置弹窗背板的边框颜色。

**类型：** Option\<[ResourceColor](./cj-common-types.md#interface-resourcecolor)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var borderStyle

```cangjie
public var borderStyle: Option<EdgeStyle>
```

**功能：** 设置弹窗背板的边框样式。

**类型：** Option\<[EdgeStyle](cj-dialog-actionsheet.md#class-edgestyle)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var borderWidth

```cangjie
public var borderWidth: Option<Length>
```

**功能：** 设置弹窗背板的边框宽度。

**类型：** Option\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var cancel

```cangjie
public var cancel:() -> Unit
```

**功能：** 返回、ESC键和点击遮障层弹窗退出时的回调。

**类型：** ()->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var closeAnimation

```cangjie
public var closeAnimation: Option<AnimateParam>
```

**功能：** 自定义设置弹窗关闭的动画效果相关参数。

**类型：** Option\<[AnimateParam](./cj-common-types.md#class-animateparam)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var cornerRadius

```cangjie
public var cornerRadius: Length
```

**功能：** 设置背板的圆角半径。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var customStyle

```cangjie
public var customStyle: Bool
```

**功能：** 弹窗容器样式是否自定义。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var gridCount

```cangjie
public var gridCount: Option<Int32>
```

**功能：** 弹窗宽度占栅格宽度的个数。

**类型：** Option\<Int32>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var height

```cangjie
public var height: Option<Length>
```

**功能：** 设置弹窗背板的高度。

**类型：** Option\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19