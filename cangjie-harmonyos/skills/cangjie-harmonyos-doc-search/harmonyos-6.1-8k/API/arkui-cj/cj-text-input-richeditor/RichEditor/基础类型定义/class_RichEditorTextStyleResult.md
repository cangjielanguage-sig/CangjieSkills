### class RichEditorTextStyleResult

```cangjie
public class RichEditorTextStyleResult {
    public var fontColor: String
    public var fontSize: Float64
    public var fontStyle: FontStyle
    public var fontWeight: Int32
    public var fontFamily: String
    public var decoration: DecorationStyleResult
    public init(
        fontColor: String,
        fontSize: Float64,
        fontStyle: FontStyle,
        fontWeight: Int32,
        fontFamily: String,
        decoration: DecorationStyleResult
    )
}
```

**功能：** 定义文本样式结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var fontColor

```cangjie
public var fontColor: String
```

**功能：** 字体颜色。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var fontSize

```cangjie
public var fontSize: Float64
```

**功能：** 字体大小。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var fontStyle

```cangjie
public var fontStyle: FontStyle
```

**功能：** 字体样式。

**类型：** [FontStyle](./cj-common-types.md#enum-fontstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var fontWeight

```cangjie
public var fontWeight: Int32
```

**功能：** 字体粗细。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var fontFamily

```cangjie
public var fontFamily: String
```

**功能：** 字体族。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var decoration

```cangjie
public var decoration: DecorationStyleResult
```

**功能：** 字体装饰。

**类型：** [DecorationStyleResult](#class-decorationstyleresult)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(String, Float64, FontStyle, Int32, String, DecorationStyleResult)

```cangjie
public init(
    fontColor: String,
    fontSize: Float64,
    fontStyle: FontStyle,
    fontWeight: Int32,
    fontFamily: String,
    decoration: DecorationStyleResult
)
```

**功能：** RichEditorTextStyleResult构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fontColor|String|是|-|字体颜色。|
|fontSize|Float64|是|-|字体大小。|
|fontStyle|[FontStyle](./cj-common-types.md#enum-fontstyle)|是|-|字体样式。|
|fontWeight|Int32|是|-|字体粗细。|
|fontFamily|String|是|-|字体族。|
|decoration|[DecorationStyleResult](#class-decorationstyleresult)|是|-|字体装饰。|