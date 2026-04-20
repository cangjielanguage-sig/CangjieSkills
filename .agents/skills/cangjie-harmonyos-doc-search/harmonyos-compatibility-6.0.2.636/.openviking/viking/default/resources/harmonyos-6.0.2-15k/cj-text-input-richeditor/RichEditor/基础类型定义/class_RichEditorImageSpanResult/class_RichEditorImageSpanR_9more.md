### class RichEditorImageSpanResult

```cangjie
public class RichEditorImageSpanResult {
    public var size: (Float64, Float64) = (0.0, 0.0)
    public var verticalAlign: ImageSpanAlignment = ImageSpanAlignment.TOP
    public var objectFit: ImageFit = ImageFit.Auto
    public var spanPosition: RichEditorSpanPosition = RichEditorSpanPosition(0, (0, 0))
    public var valuePixelMap: Option<PixelMap> = None
    public var valueResourceStr: String = ""
    public var imageStyle: RichEditorImageSpanStyleResult = RichEditorImageSpanStyleResult()
    public var offsetInSpan: (Int32, Int32) = (0, 0)

    public init(size: (Float64, Float64), verticalAlign: ImageSpanAlignment, objectFit: ImageFit)
    public init(
        size: (Float64, Float64),
        verticalAlign: ImageSpanAlignment,
        objectFit: ImageFit,
        spanPosition: RichEditorSpanPosition,
        valuePixelMap: Option<PixelMap>,
        valueResourceStr: String,
        imageStyle: RichEditorImageSpanStyleResult,
        offsetInSpan: (Int32, Int32)
    )
    public init()
}
```

**功能：** 表示后端返回的图片信息的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var imageStyle

```cangjie
public var imageStyle: RichEditorImageSpanStyleResult
```

**功能：** 表示图片样式。

**类型：** [RichEditorImageSpanStyleResult](#class-richeditorimagespanstyleresult)

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

**起始版本：** 12

#### var offsetInSpan

```cangjie
public var offsetInSpan:(Int32, Int32)
```

**功能：** 表示Span里图片的起始和结束位置。

**类型：** (Int32, Int32)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var size

```cangjie
public var size:(Float64, Float64)
```

**功能：** 表示图片的宽度和高度。

**类型：** (Float64, Float64)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var spanPosition

```cangjie
public var spanPosition: RichEditorSpanPosition
```

**功能：** 表示Span位置。

**类型：** [RichEditorSpanPosition](#class-richeditorspanposition)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var valuePixelMap

```cangjie
public var valuePixelMap: Option<PixelMap>
```

**功能：** 表示图片内容。

**类型：** Option\<[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var valueResourceStr

```cangjie
public var valueResourceStr: String
```

**功能：** 表示图片资源id。

**类型：** String

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

**起始版本：** 12