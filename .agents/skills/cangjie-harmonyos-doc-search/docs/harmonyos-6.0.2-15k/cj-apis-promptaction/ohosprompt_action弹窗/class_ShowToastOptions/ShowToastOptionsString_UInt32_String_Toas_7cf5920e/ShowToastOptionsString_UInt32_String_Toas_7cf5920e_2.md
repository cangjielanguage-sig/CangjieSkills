|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|String|否|"ShowToast"| **命名参数。** 显示的文本信息。<br>**说明：**<br>默认字体为'Harmony Sans'，不支持设置其他字体。|
|duration|UInt32|否|1500| **命名参数。** 弹窗持续时间，取值区间：1500ms-10000ms。若小于1500ms则取默认值，若大于10000ms则取上限值10000ms。|
|bottom|String|否|"80vp"| **命名参数。** 设置弹窗底部边框距离导航条的高度，ToastShowMode.TopMost模式下，软键盘拉起时，如果bottom值过小，toast要被软键盘遮挡时，会自动避让至距离软键盘80.vp处。ToastShowMode.Default模式下，软键盘拉起时，会上移软键盘的高度。<br>**说明：**<br>当底部没有导航条时，bottom为设置弹窗底部边框距离窗口底部的高度。<br>设置对齐方式alignment后，bottom不生效。|
|showMode|[ToastShowMode](#enum-toastshowmode)|否|ToastShowMode.Default| **命名参数。** 设置弹窗是否显示在应用之上。默认显示在应用内。|
|alignment|[Alignment](./cj-common-types.md#enum-alignment)|否|Alignment.Bottom| **命名参数。** 设置弹窗对齐方式。默认底部位置。|
|offset|[Offset](./cj-common-types.md#class-offset)|否|Offset(0.vp, 0.vp)| **命名参数。** 设置弹窗在对齐方式上的偏移。默认没有偏移。|
|backgroundColor|[Color](./cj-common-types.md#class-color)|否|Color.TRANSPARENT| **命名参数。** 设置文本提示框背板颜色。<br>**说明：**<br>当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则颜色显示将不符合预期效果。|
|textColor|[Color](./cj-common-types.md#class-color)|否|Color.BLACK| **命名参数。** 设置文本提示框文本颜色。|
|backgroundBlurStyle|[BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)|否|BlurStyle.COMPONENT_ULTRA_THICK| **命名参数。** 设置文本提示框背板模糊材质。<br>**说明：**<br>设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。|
|shadowOption|Option\<[ShadowOptions](./cj-text-input-text.md#class-shadowoptions)>|否|Option.None| **命名参数。** 设置文本提示框背板阴影。<br>**说明：**<br>与shadowStyle联合使用。设置shadowOption为非None时，shadowOption设置值生效；shadowOption与shadowStyle均设置为None时，使用默认值ShadowStyle.OUTER_DEFAULT_MD。|
|shadowStyle|Option\<[ShadowStyle](#enum-shadowstyle)>|否|Option.None| **命名参数。** 设置文本提示框背板阴影。<br>**说明：**<br>与shadowOption联合使用。设置shadowOption为None时，shadowStyle设置值生效；shadowOption与shadowStyle均设置为None时，使用默认值ShadowStyle.OUTER_DEFAULT_MD。|
|enableHoverMode|Bool|否|false| **命名参数。** 设置弹窗是否响应悬停态。默认不响应。|
|hoverModeArea|[HoverModeAreaType](#enum-hovermodeareatype)|否|HoverModeAreaType.BOTTOM_SCREEN| **命名参数。** 设置响应悬停态时，弹窗的显示区域。默认显示在下半屏。|