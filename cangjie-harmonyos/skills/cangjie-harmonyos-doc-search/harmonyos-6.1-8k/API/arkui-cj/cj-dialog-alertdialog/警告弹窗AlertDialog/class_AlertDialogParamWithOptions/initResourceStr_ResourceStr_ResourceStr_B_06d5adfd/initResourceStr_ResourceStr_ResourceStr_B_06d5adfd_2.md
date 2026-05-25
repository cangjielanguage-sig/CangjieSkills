|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None| **命名参数。** 弹窗标题。初始值: "" |
|subtitle|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None| **命名参数。** 弹窗副标题。初始值: "" |
|message|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-| 弹窗内容。 |
|autoCancel|?Bool|否|None| **命名参数。** 点击遮障层时是否关闭弹窗。true表示关闭弹窗,false表示不关闭弹窗。初始值: true |
|cancel|?[VoidCallback](./cj-common-types.md#type-voidcallback)|否|None| **命名参数。** 点击遮障层关闭dialog时的回调。初始值: {=>} |
|alignment|?[DialogAlignment](./cj-common-types.md#enum-dialogalignment)|否|None| **命名参数。** 弹窗在竖直方向上的对齐方式。初始值: DialogAlignment.Default |
|offset|?[Offset](./cj-common-types.md#class-offset)|否|None| **命名参数。** 弹窗相对alignment所在位置的偏移量。初始值: Offset(0, 0) |
|gridCount|?UInt32|否|None| **命名参数。** 弹窗容器宽度所占用栅格数。初始值: 4 |
|maskRect|?[Rectangle](./cj-common-types.md#class-rectangle)|否|None| **命名参数。** 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。**说明：** showInSubWindow为true时，maskRect不生效。初始值: Rectangle(x: 0, y: 0, width: 100.percent, height: 100.percent) |
|showInSubWindow|?Bool|否|None| **命名参数。** 某弹框需要显示在主窗口之外时，是否在子窗口显示此弹窗。初始值：false，弹窗显示在应用内，而非独立子窗口。**说明**：showInSubWindow为true的弹窗无法触发显示另一个showInSubWindow为true的弹窗。 |
|isModal|?Bool|否|None| **命名参数。** 弹窗是否为模态窗口。模态窗口有蒙层，非模态窗口无蒙层。初始值：true，此时弹窗有蒙层。 |
|backgroundColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None| **命名参数。** 弹窗背板颜色。**说明：** 当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则颜色显示将不符合预期效果。初始值: Color.Transparent |
|backgroundBlurStyle|?[BlurStyle](./cj-common-types.md#enum-blurstyle)|否|None| **命名参数。** 弹窗背板模糊材质。**说明：** 设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。初始值: BlurStyle.ComponentUltraThick |
|onWillDismiss|?[Callback](./cj-common-types.md#type-callbackt-v)\<[DismissDialogAction](./cj-dialog-actionsheet.md#class-dismissdialogaction), Unit>|否|None| **命名参数。** 交互式关闭回调函数。**说明：** 1.当用户执行点击遮障层关闭、左滑/右滑、三键back、键盘ESC关闭交互操作时，如果注册该回调函数，则不会立刻关闭弹窗。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗。当前组件返回的reason中，暂不支持CLOSE_BUTTON的枚举值。2.在onWillDismiss回调中，不能再做onWillDismiss拦截。 |
|cornerRadius|?[BorderRadiuses](./cj-common-types.md#class-borderradiuses)|否|None| **命名参数。** 设置背板的圆角半径。可分别设置4个圆角的半径。圆角大小受组件尺寸限制，最大值为组件宽或高的一半，若值为负，则按照默认值处理。 百分比参数方式：以父元素弹窗宽和高的百分比来设置弹窗的圆角。**说明：** 当cornerRadius属性类型为LocalizedBorderRadiuses时，支持随语言习惯改变布局顺序。初始值: BorderRadiuses(topLeft: 32.vp, topRight: 32.vp, bottomLeft: 32.vp, bottomRight: 32.vp) |
|transition|?[TransitionEffect](./cj-animation-transition.md#class-transitioneffect)|否|None| **命名参数。** 设置弹窗显示和退出的过渡效果。**说明：** 1.如果不设置，则使用默认的显示/退出动效。 2.显示动效中按back键，打断显示动效，执行退出动效，动画效果为显示动效与退出动效的曲线叠加后的效果。 3.退出动效中按back键，不会打断退出动效，退出动效继续执行，继续按back键退出应用。 |
|width|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 设置弹窗背板的宽度。**说明：** - 弹窗宽度默认最大值：None。 - 百分比参数方式：弹窗参考宽度为所在窗口的宽度，在此基础上调小或调大。 |
|height|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 设置弹窗背板的高度。**说明：** - 弹窗高度默认最大值：None。 - 百分比参数方式：弹窗参考高度为（窗口高度 - 安全区域），在此基础上调小或调大。 |
|borderWidth|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 可分别设置4个边框宽度。 百分比参数方式：以父元素弹窗宽的百分比来设置弹窗的边框宽度。当弹窗左边框和右边框大于弹窗宽度，弹窗上边框和下边框大于弹窗高度，显示可能不符合预期。**说明：** 当borderWidth属性类型为LocalizedEdgeWidths时，支持随语言习惯改变布局顺序。初始值: 0 |
|borderColor|?[BorderColor](#class-bordercolor)|否|None| **命名参数。** 设置弹窗背板的边框颜色。 如果使用borderColor属性，需要和borderWidth属性一起使用。**说明：** 当borderColor属性类型为LocalizedEdgeColors时，支持随语言习惯改变布局顺序。初始值: BorderColor(color: Color.Black) |
|borderStyle|?[EdgeStyles](./cj-common-types.md#class-edgestyles)|否|None| **命名参数。** 设置弹窗背板的边框样式。如果使用borderStyle属性，需要和borderWidth属性一起使用。初始值: EdgeStyles() |
|shadow|?[ShadowOptions](./cj-common-types.md#class-shadowoptions)|否|None| **命名参数。** 设置弹窗背板的阴影。初始值: ShadowOptions(radius: 0.0) |
|textStyle|?[WordBreak](./cj-common-types.md#enum-wordbreak)|否|None| **命名参数。** 设置弹窗message内容的文本样式。初始值: WordBreak.BreakAll |
|buttons|?Array\<[AlertDialogButtonOptions](#class-alertdialogbuttonoptions)>|是|-| **命名参数。** 弹窗容器中的多个按钮。 |
|buttonDirection|?[DialogButtonDirection](#enum-dialogbuttondirection)|否|None| **命名参数。** 按钮排布方向默认值为DialogButtonDirection.Auto，建议3个以上按钮使用Auto模式（两个以上按钮会切换为纵向模式，通常能显示更多按钮），非Auto模式下，3个以上按钮可能会显示不全，超出显示范围的按钮会被截断。初始值: DialogButtonDirection.Auto |