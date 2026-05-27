#### init(String, Float64, FontStyle, Int32, String, TextDecorationResult)

```cangjie
public init(
    fontColor: String,
    fontSize: Float64,
    fontStyle: FontStyle,
    fontWeight: Int32,
    fontFamily: String,
    decoration: TextDecorationResult
)
```

**功能：** 创建RichEditorTextStyleResult。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fontColor|String|是|-|文本颜色。|
|fontSize|Float64|是|-|字体大小。|
|fontStyle|[FontStyle](./cj-common-types.md#enum-fontstyle)|是|-|字体样式。|
|fontWeight|Int32|是|-|字体粗细。|
|fontFamily|String|是|-|字体列表。|
|decoration|[TextDecorationResult](#class-textdecorationresult)|是|-|文本装饰线样式及其颜色。|

#### init(String, Float64, FontStyle, Int32, String, TextDecorationResult)

```cangjie
public init(
    fontColor: String,
    fontSize: Float64,
    fontStyle: FontStyle,
    fontWeight: Int32,
    fontFamily: String,
    decoration: TextDecorationResult,
    textShadow: Array<ShadowOptionsResult>,
    lineHeight: Float64,
    letterSpacing: Float64,
    fontFeature: String
)
```

**功能：** 创建RichEditorTextStyleResult。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fontColor|String|是|-|文本颜色。|
|fontSize|Float64|是|-|字体大小。|
|fontStyle|[FontStyle](./cj-common-types.md#enum-fontstyle)|是|-|字体样式。|
|fontWeight|Int32|是|-|字体粗细。|
|fontFamily|String|是|-|字体列表。|
|decoration|[TextDecorationResult](#class-textdecorationresult)|是|-|文本装饰线样式及其颜色。|
|textShadow|Array\<[ShadowOptionsResult](#class-shadowoptionsresult)>|是|-|文字阴影效果。|
|lineHeight|Float64|是|-|文本行高。|
|letterSpacing|Float64|是|-|文本字符间距。|
|fontFeature|String|是|-|文字特性效果。|