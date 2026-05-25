|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|String|否|""| **命名参数。** 标题文本。|
|message|String|否|""| **命名参数。** 内容文本。|
|buttons|Array\<[ButtonInfo](#class-buttoninfo)>|否|[ButtonInfo("button", Color(0x31463146))]| **命名参数。** 对话框中按钮的数组，支持大于1个按钮。|
|alignment|[DialogAlignment](./cj-common-types.md#enum-dialogalignment)|否|DialogAlignment.Default| **命名参数。** 弹窗在竖直方向上的对齐方式。|
|offset|[Offset](./cj-common-types.md#class-offset)|否|Offset(0.vp, 0.vp)| **命名参数。** 弹窗相对alignment所在位置的偏移量。|
|maskRect|[Rectangle](./cj-common-types.md#class-rectangle)|否|Rectangle(x: 0.vp, y: 0.vp, width: 100.percent, height: 100.percent)| **命名参数。** 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。<br>**说明：**<br> - showInSubWindow为true时，maskRect不生效。<br> - maskRect在设置部分属性值后，其余属性值默认为0。|
|showInSubWindow|Bool|否|false| **命名参数。** 某弹框需要显示在主窗口之外时，是否在子窗口显示此弹窗。默认弹窗显示在应用内，而非独立子窗口。<br>**说明：**<br>showInSubWindow为true的弹窗无法触发显示另一个showInSubWindow为true的弹窗。|
|isModal|Bool|否|true| **命名参数。** 弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。默认弹窗有蒙层。|
|backgroundColor|[Color](./cj-common-types.md#class-color)|否|Color.TRANSPARENT| **命名参数。** 弹窗背板颜色。<br>**说明：**<br>当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则颜色显示将不符合预期效果。|
|backgroundBlurStyle|[BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)|否|BlurStyle.COMPONENT_ULTRA_THICK| **命名参数。** 弹窗背板模糊材质。<br>**说明：**<br>设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。|
|shadowOption|Option\<[ShadowOptions](./cj-text-input-text.md#class-shadowoptions)>|否|Option.None| **命名参数。** 设置弹窗背板阴影。<br>**说明：**<br>与shadowStyle联合使用。设置shadowOption为非None时，shadowOption设置值生效；shadowOption与shadowStyle均设置为None时，使用默认值ShadowStyle.OUTER_DEFAULT_MD|
|shadowStyle|Option\<[ShadowStyle](#enum-shadowstyle)>|否|Option.None| **命名参数。** 设置弹窗背板阴影。<br>**说明：**<br>与shadowOption联合使用。设置shadowOption为None时，shadowStyle设置值生效；shadowOption与shadowStyle均设置为None时，使用默认值ShadowStyle.OUTER_DEFAULT_MD。|
|enableHoverMode|Bool|否|false| **命名参数。** 是否响应悬停态。默认不响应。|
|hoverModeArea|[HoverModeAreaType](#enum-hovermodeareatype)|否|HoverModeAreaType.BOTTOM_SCREEN| **命名参数。** 悬停态下弹窗默认展示区域。|