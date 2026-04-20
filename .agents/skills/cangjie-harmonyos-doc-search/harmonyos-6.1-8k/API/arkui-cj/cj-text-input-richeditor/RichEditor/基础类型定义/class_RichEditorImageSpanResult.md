### class RichEditorImageSpanResult

```cangjie
public class RichEditorImageSpanResult <: RichEditorSpanResult {
    public var spanPosition: ?RichEditorSpanPosition
    public var valuePixelMap: Option<PixelMap>
    public var valueResourceStr: ?String
    public var imageStyle: ?RichEditorImageSpanStyleResult
    public var offsetInSpan: ?(Int32, Int32)
    public init(
        spanPosition!: ?RichEditorSpanPosition = Option.None,
        valuePixelMap!: Option<PixelMap> = Option.None,
        valueResourceStr!: ?String = None,
        imageStyle!: ?RichEditorImageSpanStyleResult = None,
        offsetInSpan!: ?(Int32, Int32) = None
    )
}
```

**功能：** 定义图像span。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [RichEditorSpanResult](#interface-richeditorspanresult)

#### var spanPosition

```cangjie
public var spanPosition: ?RichEditorSpanPosition
```

**功能：** 图像span的位置。

**类型：** ?[RichEditorSpanPosition](#class-richeditorspanposition)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var valuePixelMap

```cangjie
public var valuePixelMap: Option<PixelMap>
```

**功能：** 图像span的像素图。

**类型：** Option\<[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var valueResourceStr

```cangjie
public var valueResourceStr: ?String
```

**功能：** 图像span的资源字符串。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var imageStyle

```cangjie
public var imageStyle: ?RichEditorImageSpanStyleResult
```

**功能：** 图像属性。

**类型：** ?[RichEditorImageSpanStyleResult](#class-richeditorimagespanstyleresult)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var offsetInSpan

```cangjie
public var offsetInSpan: ?(Int32, Int32)
```

**功能：** span中的偏移量。

**类型：** ?(Int32, Int32)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?RichEditorSpanPosition, Option\<PixelMap>, ?String, ?RichEditorImageSpanStyleResult, ?(Int32, Int32))

```cangjie
public init(
    spanPosition!: ?RichEditorSpanPosition = Option.None,
    valuePixelMap!: Option<PixelMap> = Option.None,
    valueResourceStr!: ?String = None,
    imageStyle!: ?RichEditorImageSpanStyleResult = None,
    offsetInSpan!: ?(Int32, Int32) = None
)
```

**功能：** RichEditorImageSpanResult构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|spanPosition|?[RichEditorSpanPosition](#class-richeditorspanposition)|否|Option.None|**命名参数。** 图像span的位置。初始值：RichEditorSpanPosition(0, (0, 0))。|
|valuePixelMap|Option\<[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)>|否|Option.None|**命名参数。** 图像span的像素图。|
|valueResourceStr|?String|否|None|**命名参数。** 图像span的资源字符串。初始值：""。|
|imageStyle|?[RichEditorImageSpanStyleResult](#class-richeditorimagespanstyleresult)|否|None|**命名参数。** 图像属性。初始值：RichEditorImageSpanStyleResult()。|
|offsetInSpan|?(Int32, Int32)|否|None|**命名参数。** span中的偏移量。初始值：(0, 0)。|