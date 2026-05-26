### func labelStyle(TextOverflow, UInt32, Option\<Length>, AppResource, TextHeightAdaptivePolicy, Fonts)

```cangjie
public func labelStyle(
    overflow!: TextOverflow = TextOverflow.Ellipsis,
    maxLines!: UInt32 = 1,
    minFontSize!: Option<Length> = None,
    maxFontSize!: AppResource,
    heightAdaptivePolicy!: TextHeightAdaptivePolicy = TextHeightAdaptivePolicy.MAX_LINES_FIRST,
    font!: Fonts = Fonts()
): This
```

**功能：** 设置Button组件label文本和字体的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|overflow|[TextOverflow](./cj-common-types.md#enum-textoverflow)|否|TextOverflow.Ellipsis| **命名参数。** 设置label文本超长时的显示方式。文本截断是按字截断。例如，英文以单词为最小单位进行截断，若需要以字母为单位进行截断，可在字母间添加零宽空格。|
|maxLines|UInt32|否|1| **命名参数。** 设置label文本的最大行数。默认情况下，文本是自动折行的，如果指定此参数，则文本最多不会超过指定的行。如果有多余的文本，可以通过overflow来指定截断方式。|
|minFontSize|Option\<[Length](./cj-common-types.md#interface-length)>|否|None| **命名参数。** 设置label文本最小显示字号。需配合maxFontSize以及maxLines或布局大小限制使用。<br/>**说明**：<br/>minFontSize小于或等于0时，自适应字号不生效。|
|maxFontSize|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 设置label文本最大显示字号。需配合minFontSize以及maxLines或布局大小限制使用。|
|heightAdaptivePolicy|[TextHeightAdaptivePolicy](./cj-common-types.md#enum-textheightadaptivepolicy)|否|TextHeightAdaptivePolicy.MAX_LINES_FIRST| **命名参数。** 设置label文本自适应高度的方式。|
|font|[Fonts](./cj-common-types.md#class-fonts)|否|Fonts()| **命名参数。** 设置label文本字体样式。|