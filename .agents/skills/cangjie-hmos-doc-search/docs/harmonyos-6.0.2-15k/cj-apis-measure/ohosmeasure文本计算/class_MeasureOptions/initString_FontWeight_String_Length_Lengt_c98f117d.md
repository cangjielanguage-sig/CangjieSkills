### init(String, FontWeight, String, ?Length, ?Length, ?Length, ?Length, ?Length, ?Length, UInt32, TextAlign, FontStyle, TextOverflow, TextCase, WordBreak)

```cangjie
public init(
    textContent!: String,
    fontWeight!: FontWeight = FontWeight.Normal,
    fontFamily!: String = "HarmonyOS Sans",
    constraintWidth!: ?Length = None,
    fontSize!: ?Length = 16.fp,
    lineHeight!: ?Length = None,
    baselineOffset!: ?Length = 0.0.vp,
    letterSpacing!: ?Length = None,
    textIndent!: ?Length = None,
    maxLines!: UInt32 = 0,
    textAlign!: TextAlign = TextAlign.Start,
    fontStyle!: FontStyle = FontStyle.Normal,
    overflow!: TextOverflow = TextOverflow.Clip,
    textCase!: TextCase = TextCase.Normal,
    wordBreak!: WordBreak = WordBreak.BreakWord
)
```

**功能：** 创建被计算文本的描述信息结构体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|textContent|String|是|-| **命名参数。** 设置被计算文本内容。|
|fontWeight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Normal| **命名参数。** 设置被计算文本的字体粗细，可以使用FontWeight中相应的枚举值。|
|fontFamily|String|否|"HarmonyOS Sans"| **命名参数。** 设置被计算文本字体列表。默认字体'HarmonyOS Sans'，且当前只支持这种字体。|
|constraintWidth|Option\<[Length](./cj-common-types.md#interface-length)>|否|None| **命名参数。** 设置被计算文本布局宽度。<br>**说明：** <br>默认单位为vp，不支持百分比设置。若不设置，则文本SizeOption宽度为单行布局所占最大宽度值，若设置则为设置值。|
|fontSize|Option\<[Length](./cj-common-types.md#interface-length)>|否|16.fp| **命名参数。** 设置被计算文本字体大小。<br>**说明：** <br>不支持设置百分比设置，为数字类型时，使用fp单位。|
|lineHeight|Option\<[Length](./cj-common-types.md#interface-length)>|否|None| **命名参数。** 设置被计算文本行高，使用vp单位。|
|baselineOffset|Option\<[Length](./cj-common-types.md#interface-length)>|否|0.0.vp| **命名参数。** 设置被计算文本基线的偏移量。|
|letterSpacing|Option\<[Length](./cj-common-types.md#interface-length)>|否|None| **命名参数。** 设置被计算文本字符间距，使用vp单位。|
|textIndent|Option\<[Length](./cj-common-types.md#interface-length)>|否|None| **命名参数。** 设置首行文本缩进，使用vp单位。|
|maxLines|UInt32|否|0| **命名参数。** 设置被计算文本最大行数。|
|textAlign|[TextAlign](./cj-common-types.md#enum-textalign)|否|TextAlign.Start| **命名参数。** 设置被计算文本水平方向的对齐方式。|
|fontStyle|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 设置被计算文本字体样式。|
|overflow|[TextOverflow](./cj-common-types.md#enum-textoverflow)|否|TextOverflow.Clip| **命名参数。** 设置被计算文本超长时的截断方式。|
|textCase|[TextCase](./cj-common-types.md#enum-textcase)|否|TextCase.Normal| **命名参数。** 设置被计算文本大小写。|
|wordBreak|[WordBreak](./cj-common-types.md#enum-wordbreak)|否|WordBreak.BreakWord| **命名参数。** 设置断行规则。|