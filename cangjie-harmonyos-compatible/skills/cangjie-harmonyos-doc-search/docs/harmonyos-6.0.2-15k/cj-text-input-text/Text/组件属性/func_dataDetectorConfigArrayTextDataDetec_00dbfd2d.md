### func dataDetectorConfig(Array\<TextDataDetectorType>, (String) -> Unit, ResourceColor, TextDecorationType, ResourceColor, TextDecorationStyle)

```cangjie
public func dataDetectorConfig(textType: Array<TextDataDetectorType>, onDetectResultUpdate!: (String)->Unit = {_ =>},
    color!: ResourceColor = Color(0xff0a59f7), decorationType!: TextDecorationType = TextDecorationType.Underline,
    decorationColor!: ResourceColor = Color(0xff0a59f7), decorationStyle!: TextDecorationStyle = TextDecorationStyle.SOLID): This
```

**功能：** 设置文本识别配置。

> **说明：**
>
> 需配合[enableDataDetector](#func-enabledatadetectorbool)一起使用，设置enableDataDetector为true时，dataDetectorConfig的配置才能生效。当有两个实体A、B重叠时，按以下规则保留实体：
>
> - 若A ⊂ B，则保留B，反之则保留A。
> - 当A ⊄ B且B ⊄ A时，若A.start < B.start，则保留A，反之则保留B。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|textType|Array\<[TextDataDetectorType](#enum-textdatadetectortype)>|是|-|文本识别的实体类型。|
|onDetectResultUpdate|(String)->Unit|否|{ _ => }| **命名参数。** 回调函数，文本识别成功后触发。|
|color|[ResourceColor](cj-common-types.md#interface-resourcecolor)|否|Color(0xff0a59f7)| **命名参数。** 文本识别成功后的实体颜色。|
|decorationType|[TextDecorationType](cj-common-types.md#enum-textdecorationtype)|否|TextDecorationType.Underline| **命名参数。** 文本识别成功后的实体装饰线类型。|
|decorationColor|[ResourceColor](cj-common-types.md#interface-resourcecolor)|否|Color(0xff0a59f7)| **命名参数。** 文本识别成功后的实体装饰线颜色。|
|decorationStyle|[TextDecorationStyle](cj-common-types.md#enum-textdecorationstyle)|否|TextDecorationStyle.SOLID| **命名参数。** 文本识别成功后的实体装饰线样式。|