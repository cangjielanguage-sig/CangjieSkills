### class RichEditorParagraphStyle

```cangjie
public class RichEditorParagraphStyle {
    public var textAlign: ?TextAlign
    public var leadingMargin: ?LeadingMarginType
    public init(textAlign!: ?TextAlign = None)
    public init(textAlign!: ?TextAlign = None, leadingMargin!: ?Length)
    public init(textAlign!: ?TextAlign = None, leadingMargin!: ?LeadingMarginPlaceholder)
}
```

**功能：** 定义段落样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var textAlign

```cangjie
public var textAlign: ?TextAlign
```

**功能：** 文本对齐。

**类型：** ?[TextAlign](./cj-common-types.md#enum-textalign)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var leadingMargin

```cangjie
public var leadingMargin: ?LeadingMarginType
```

**功能：** 首行缩进。

**类型：** ?[LeadingMarginType](#enum-leadingmargintype)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?TextAlign)

```cangjie
public init(textAlign!: ?TextAlign = None)
```

**功能：** RichEditorParagraphStyle构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|textAlign|?[TextAlign](./cj-common-types.md#enum-textalign)|否|None|**命名参数。** 文本对齐。初始值：TextAlign.Start。|

#### init(?TextAlign, ?Length)

```cangjie
public init(textAlign!: ?TextAlign = None, leadingMargin!: ?Length)
```

**功能：** RichEditorParagraphStyle构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|textAlign|?[TextAlign](./cj-common-types.md#enum-textalign)|否|None|**命名参数。** 文本对齐。初始值：TextAlign.Start。|
|leadingMargin|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 首行缩进。|

#### init(?TextAlign, ?LeadingMarginPlaceholder)

```cangjie
public init(textAlign!: ?TextAlign = None, leadingMargin!: ?LeadingMarginPlaceholder)
```

**功能：** RichEditorParagraphStyle构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|textAlign|?[TextAlign](./cj-common-types.md#enum-textalign)|否|None|**命名参数。** 文本对齐。初始值：TextAlign.Start。|
|leadingMargin|?[LeadingMarginPlaceholder](#class-leadingmarginplaceholder)|是|-|**命名参数。** 首行缩进。|