（窗口高度 - 安全区域），在此基础上调小或调大。 |
|borderWidth|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 可分别设置4个边框宽度。 百分比参数方式：以父元素弹窗宽的百分比来设置弹窗的边框宽度。当弹窗左边框和右边框大于弹窗宽度，弹窗上边框和下边框大于弹窗高度，显示可能不符合预期。**说明：** 当borderWidth属性类型为LocalizedEdgeWidths时，支持随语言习惯改变布局顺序。初始值: 0 |
|borderColor|?[BorderColor](#class-bordercolor)|否|None| **命名参数。** 设置弹窗背板的边框颜色。 如果使用borderColor属性，需要和borderWidth属性一起使用。**说明：** 当borderColor属性类型为LocalizedEdgeColors时，支持随语言习惯改变布局顺序。初始值: BorderColor(color: Color.Black) |
|borderStyle|?[EdgeStyles](./cj-common-types.md#class-edgestyles)|否|None| **命名参数。** 设置弹窗背板的边框样式。如果使用borderStyle属性，需要和borderWidth属性一起使用。初始值: EdgeStyles() |
|shadow|?[ShadowOptions](./cj-common-types.md#class-shadowoptions)|否|None| **命名参数。** 设置弹窗背板的阴影。初始值: ShadowOptions(radius: 0.0) |
|textStyle|?[WordBreak](./cj-common-types.md#enum-wordbreak)|否|None| **命名参数。** 设置弹窗message内容的文本样式。初始值: WordBreak.BreakAll |
|buttons|?Array\<[AlertDialogButtonOptions](#class-alertdialogbuttonoptions)>|是|-| **命名参数。** 弹窗容器中的多个按钮。 |
|buttonDirection|?[DialogButtonDirection](#enum-dialogbuttondirection)|否|None| **命名参数。** 按钮排布方向默认值为DialogButtonDirection.Auto，建议3个以上按钮使用Auto模式（两个以上按钮会切换为纵向模式，通常能显示更多按钮），非Auto模式下，3个以上按钮可能会显示不全，超出显示范围的按钮会被截断。初始值: DialogButtonDirection.Auto |