值处理。 <br>百分比参数方式：以父元素弹窗宽和高的百分比来设置弹窗的圆角。 |
|width|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。**  设置弹窗背板的宽度。<br>**说明:**<br>1. 弹窗宽度默认最大值：400.vp。<br>2. 百分比参数方式：弹窗参考宽度为所在窗口的宽度，在此基础上调小或调大。 |
|height|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。**  设置弹窗背板的高度。<br>**说明:**<br>1. 弹窗高度默认最大值：0.9 *（窗口高度 - 安全区域） 。<br>2. 百分比参数方式：弹窗参考高度为（窗口高度 - 安全区域），在此基础上调小或调大。 |
|borderWidth|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。**  设置弹窗背板的边框宽度。<br>百分比参数方式：以父元素弹窗宽和高的百分比来设置弹窗的圆角。<br>当弹窗左边框和右边框大于弹窗宽度，弹窗上边框和下边框大于弹窗高度，显示可能不符合预期。|
|borderColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None|**命名参数。**  设置弹窗背板的边框颜色。如果使用borderColor属性，需要和borderWidth属性一起使用。 |
|borderStyle|?[EdgeStyles](./cj-common-types.md#class-edgestyles)|否|None|**命名参数。**  设置弹窗背板的边框样式 。 如果使用borderStyle属性，需要和borderWidth属性一起使用。 |
|shadow|?[ShadowOptions](./cj-common-types.md#class-shadowoptions)|否|None|**命名参数。** 设置弹窗背板的阴影。|