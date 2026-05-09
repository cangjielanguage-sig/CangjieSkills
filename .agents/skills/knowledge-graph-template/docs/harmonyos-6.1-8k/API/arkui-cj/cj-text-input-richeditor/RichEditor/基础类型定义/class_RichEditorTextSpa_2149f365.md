### class RichEditorTextSpanOptions

```cangjie
public class RichEditorTextSpanOptions {
    public var offset: ?Int32
    public var style: ?RichEditorTextStyle
    public init(offset!: ?Int32 = None, style!: ?RichEditorTextStyle = None)
}
```

**功能：** 定义RichEditor的span选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var offset

```cangjie
public var offset: ?Int32
```

**功能：** 添加文本span的偏移量。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var style

```cangjie
public var style: ?RichEditorTextStyle
```

**功能：** 文本样式。

**类型：** ?[RichEditorTextStyle](#class-richeditortextstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Int32, ?RichEditorTextStyle)

```cangjie
public init(offset!: ?Int32 = None, style!: ?RichEditorTextStyle = None)
```

**功能：** RichEditorTextSpanOptions构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|?Int32|否|None|**命名参数。** 添加文本span的偏移量。初始值：Int32.Max。|
|style|?[RichEditorTextStyle](#class-richeditortextstyle)|否|None|**命名参数。** 文本样式。初始值：RichEditorTextStyle()。|