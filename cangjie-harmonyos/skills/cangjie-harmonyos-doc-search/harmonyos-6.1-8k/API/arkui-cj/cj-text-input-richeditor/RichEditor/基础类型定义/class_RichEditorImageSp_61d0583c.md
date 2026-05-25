### class RichEditorImageSpanOptions

```cangjie
public class RichEditorImageSpanOptions {
    public var offset: ?Int32
    public var imageStyle: ?RichEditorImageSpanStyle
    public init(
        offset!: ?Int32 = None,
        imageStyle!: ?RichEditorImageSpanStyle = None
    )
}
```

**功能：** 定义RichEditor的图像span选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var offset

```cangjie
public var offset: ?Int32
```

**功能：** 添加图像span的偏移量。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var imageStyle

```cangjie
public var imageStyle: ?RichEditorImageSpanStyle
```

**功能：** 图像样式。

**类型：** ?[RichEditorImageSpanStyle](#class-richeditorimagespanstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Int32, ?RichEditorImageSpanStyle)

```cangjie
public init(
    offset!: ?Int32 = None,
    imageStyle!: ?RichEditorImageSpanStyle = None
)
```

**功能：** RichEditorImageSpanOptions构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|?Int32|否|None|**命名参数。** 添加图像span的偏移量。初始值：Int32.Max。|
|imageStyle|?[RichEditorImageSpanStyle](#class-richeditorimagespanstyle)|否|None|**命名参数。** 图像样式。初始值：RichEditorImageSpanStyle()。|