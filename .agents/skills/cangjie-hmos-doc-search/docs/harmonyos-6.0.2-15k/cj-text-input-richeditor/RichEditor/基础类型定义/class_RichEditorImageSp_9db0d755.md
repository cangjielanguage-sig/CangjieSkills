### class RichEditorImageSpanStyleResult

```cangjie
public class RichEditorImageSpanStyleResult {
    public var size: (Float64, Float64) = (0.0, 0.0)
    public var verticalAlign: ImageSpanAlignment = ImageSpanAlignment.CENTER
    public var objectFit: ImageFit = ImageFit.Auto
    public var layoutStyle: RichEditorLayoutStyleResult = RichEditorLayoutStyleResult()
}
```

**功能：** 后端返回的图片样式信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var layoutStyle

```cangjie
public var layoutStyle: RichEditorLayoutStyleResult
```

**功能：** 表示图片布局风格。

**类型：** [RichEditorLayoutStyleResult](#class-richeditorlayoutstyleresult)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var objectFit

```cangjie
public var objectFit: ImageFit
```

**功能：** 表示图片缩放类型。

**类型：** [ImageFit](./cj-common-types.md#enum-imagefit)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var size

```cangjie
public var size:(Float64, Float64)
```

**功能：** 表示图片的宽度和高度。

> **说明：**
>
> 初始值：size的初始值与objectFit的值有关，不同的objectFit值对应的size初始值也不同。objectFit的值为Cover时，图片高度为组件高度减去组件上下内边距，图片宽度为组件宽度减去组件左右内边距。

**类型：** (Float64,Float64)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var verticalAlign

```cangjie
public var verticalAlign: ImageSpanAlignment
```

**功能：** 表示图片垂直对齐方式。

**类型：** [ImageSpanAlignment](./cj-common-types.md#enum-imagespanalignment)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19