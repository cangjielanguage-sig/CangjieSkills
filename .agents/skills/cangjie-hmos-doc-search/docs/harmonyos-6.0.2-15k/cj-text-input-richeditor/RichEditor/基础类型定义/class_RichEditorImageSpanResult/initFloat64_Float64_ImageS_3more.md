#### init((Float64, Float64), ImageSpanAlignment, ImageFit)

```cangjie
public init(size: (Float64, Float64), verticalAlign: ImageSpanAlignment, objectFit: ImageFit)
```

**功能：** 创建RichEditorImageSpanResult类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|(Float64, Float64)|是|-|图片的宽度和高度。单位：px。<br>初始值：size的初始值与objectFit的值有关，不同的objectFit值对应的size初始值也不同。objectFit的值为Cover时，图片高度为组件高度减去组件上下内边距，图片宽度为组件宽度减去组件左右内边距。 |
|verticalAlign|[ImageSpanAlignment](./cj-common-types.md#enum-imagespanalignment)|是|-|图片垂直对齐方式。 |
|objectFit|[ImageFit](./cj-common-types.md#enum-imagefit)|是|-|图片缩放类型。|

#### init((Float64, Float64), ImageSpanAlignment, ImageFit, RichEditorSpanPosition, Option\<PixelMap>, String, RichEditorImageSpanStyleResult, (Int32, Int32))

```cangjie
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
```

**功能：** 创建RichEditorImageSpanResult类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|(Float64, Float64)|是|-|图片的宽度和高度。单位：px。<br>初始值：size的初始值与objectFit的值有关，不同的objectFit值对应的size初始值也不同。objectFit的值为Cover时，图片高度为组件高度减去组件上下内边距，图片宽度为组件宽度减去组件左右内边距。 |
|verticalAlign|[ImageSpanAlignment](./cj-common-types.md#enum-imagespanalignment)|是|-|图片垂直对齐方式。 |
|objectFit|[ImageFit](./cj-common-types.md#enum-imagefit)|是|-|图片缩放类型。|
|spanPosition|[RichEditorSpanPosition](#class-richeditorspanposition)|是|-|Span位置。|
|valuePixelMap|Option\<PixelMap>|是|-|图片内容。|
|valueResourceStr|String|是|-|图片资源id。|
|imageStyle|[RichEditorImageSpanStyleResult](#class-richeditorimagespanstyleresult)|是|-|图片样式。|
|offsetInSpan|(Int32, Int32)|是|-|Span里图片的起始和结束位置。|

#### init()

```cangjie
public init()
```

**功能：** 创建RichEditorImageSpanResult类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19