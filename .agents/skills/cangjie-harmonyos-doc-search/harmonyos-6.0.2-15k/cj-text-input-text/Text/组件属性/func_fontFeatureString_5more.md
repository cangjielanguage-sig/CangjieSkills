### func fontFeature(String)

```cangjie
public func fontFeature(value: String): This
```

**功能：** 设置文字特性效果，比如数字等宽的特性。

> **说明：**
>
> - 格式为：normal | \<feature-tag-value>。
> - \<feature-tag-value>的格式为：\<string> [ \<integer> | on | off ]。
> - \<feature-tag-value>的个数可以有多个，中间用','隔开。
> - 例如，使用等宽数字的输入格式为："ss01" on。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|文字特性效果。|

**fontFeature属性列表**

![text](figures/fontFeatureList.png)

设置 Font Feature 属性，Font Feature 是 OpenType 字体的高级排版能力，如支持连字、数字等宽等特性，一般用在自定义字体中，其能力需要字体本身支持。

更多 Font Feature 能力介绍可参考 [https://www.w3.org/TR/css-fonts-3/#font-feature-settings-prop](https://www.w3.org/TR/css-fonts-3/#font-feature-settings-prop) 和 [https://sparanoid.com/lab/opentype-features/](https://sparanoid.com/lab/opentype-features/)

> **说明：**
>
> - 不支持Text内同时存在文本内容和Span或ImageSpan子组件。如果同时存在，只显示Span或ImageSpan内的内容。
> - 字体排版引擎会对开发者传入的宽度[width](./cj-universal-attribute-size.md#func-widthlength)进行向下取整，保证是整型像素后进行排版。如果字体排版引擎向上取整，可能会出现文字右侧被截断。
> - 当多个Text组件在[Row](./cj-row-column-stack-row.md#row)容器内布局且没有设置具体的布局分配信息时，Text会以Row的最大尺寸进行布局。如果需要子组件主轴累加的尺寸不超过Row容器主轴的尺寸，可以设置[layoutWeight](./cj-universal-attribute-size.md#func-layoutweightint32)或者是以[Flex](./cj-row-column-stack-flex.md#flex)布局来约束子组件的主轴尺寸。

### func fontSize(Length)

```cangjie
public func fontSize(value: Length): This
```

**功能：** 设置字体大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](cj-common-types.md#interface-length)|是|-|字体大小。不支持百分比单位。<br>初始值：16.fp。|

### func fontStyle(FontStyle)

```cangjie
public func fontStyle(value: FontStyle): This
```

**功能：** 设置字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FontStyle](cj-common-types.md#enum-fontstyle)|是|-|字体样式。<br>初始值：FontStyle.Normal。|

### func fontWeight(FontWeight)

```cangjie
public func fontWeight(value: FontWeight): This
```

**功能：** 设置文本的字体粗细，设置过大可能会在不同字体下有截断。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FontWeight](cj-common-types.md#enum-fontweight)|是|-|文本的字体粗细。<br>初始值：FontWeight.Normal。|

### func halfLeading(Bool)

```cangjie
public func halfLeading(value: Bool): This
```

**功能：** 设置文本是否将行间距平分至行的顶部与底部。

> **说明：**
>
> 组件侧设置halfLeading优先级高于module.json5配置文件中的halfLeading配置项。默认使用false不平分。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|文本是否将行间距平分至行的顶部与底部。<br>初始值：false。|