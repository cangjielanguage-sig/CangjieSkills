### func arrowPosition(ArrowPosition)

```cangjie
public func arrowPosition(value: ArrowPosition): This
```

**功能：** 设置下拉菜单项的文本与箭头之间的对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ArrowPosition](./cj-common-types.md#enum-arrowpointposition)|是|-|下拉菜单项的文本与箭头之间的对齐方式。<br>初始值：ArrowPosition.END。|

### func controlSize(ControlSize)

```cangjie
public func controlSize(value: ControlSize): This
```

**功能：** 设置Select组件的尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ControlSize](./cj-common-types.md#enum-controlsize)|是|-|Select组件的尺寸。<br>初始值：ControlSize.NORMAL。|

### func divider(Option\<DividerOptions>)

```cangjie
public func divider(options!: Option<DividerOptions> = Option.None): This
```

**功能：** 设置分割线样式，不设置该属性则按初始值展示分割线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|Option\<[DividerOptions](#class-divideroptions)>|否|Option.None| **命名参数。** 1.设置为DividerOptions，则按DividerOptions参数的样式显示分割线。<br>初始值：strokeWidth:1.px，color:0x33182431<br>2.设置为Option.None时，不显示分割线。<br>3.strokeWidth设置过宽时，会覆盖文字。分割线会从每一个Item底部开始，同时向上向下画分割线。<br>4.startMargin和endMargin的默认值与不设置divider属性时的分割线样式保持一致。startMargin和endMargin的和与optionWidth的值相等时，不显示分割线。 startMargin和endMargin的和超过optionWidth的值时，按照初始样式显示分割线。|

### func font(FontStyle, FontWeight, Length, String)

```cangjie
public func font(
    style!: FontStyle = FontStyle.Normal,
    weight!: FontWeight = FontWeight.Medium,
    size!: Length = 16.vp,
    family!: String = "sans-serif"
): This
```

**功能：** 设置下拉按钮本身的文本样式。当size为0的时候，文本不显示，当size为负值的时候，文本的size按照初始值显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 用于指定字体样式。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Medium| **命名参数。** 用于指定字体的粗细。|
|size|[Length](./cj-common-types.md#interface-length)|否|16.vp| **命名参数。** 指定字号和行高，不支持百分比设置。|
|family|String|否|"sans-serif"| **命名参数。** 指定字体系列。|

### func fontColor(ResourceColor)

```cangjie
public func fontColor(value: ResourceColor): This
```

**功能：** 根据指定的Color，设置下拉按钮本身的文本颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|下拉按钮本身的文本颜色。<br>初始值：@r(sys.color.ohos_id_color_text_primary)混合@r(sys.color.ohos_id_alpha_content_primary)的透明度。|