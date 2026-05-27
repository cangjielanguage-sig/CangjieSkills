|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| message | String | 是 | \- | 弹窗内容。 |
| title | Option\<String> | 否 | None | **命名参数。**  弹窗标题。 |
| subtitle | Option\<String> | 否 | None | **命名参数。**  弹窗副标题。 |
| autoCancel | Option\<Bool> | 否 | true | **命名参数。**  点击遮障层时是否关闭弹窗。true表示关闭弹窗,false表示不关闭弹窗。 |
| cancel | Option\<()->Unit> | 否 | None | **命名参数。**  点击遮障层关闭dialog时的回调。 |
| alignment | Option\<[DialogAlignment](./cj-common-types.md#enum-dialogalignment)> | 否 | DialogAlignment.Bottom | **命名参数。**  弹窗在竖直方向上的对齐方式。|
| offset | Option\<[Offset](./cj-common-types.md#class-offset)> | 否 | None | **命名参数。**  弹窗相对alignment所在位置的偏移量。|
| gridCount | Option\<UInt32> | 否 | 4 | **命名参数。**  弹窗容器宽度所占用栅格数。|
| maskRect | Option\<[Rectangle](./cj-common-types.md#class-rectangle)> | 否 | Rectangle(x: 0.vp, y: 0.vp, height: 100.percent, width: 100.percent) | **命名参数。**  弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。<br/>**说明：**<br/>showInSubWindow为true时，maskRect不生效。 |
| showInSubWindow | Option\<Bool> | 否 | false | **命名参数。**  某弹框需要显示在主窗口之外时，是否在子窗口显示此弹窗。<br/>初始值：false，弹窗显示在应用内，而非独立子窗口。<br/>**说明**：showInSubWindow为true的弹窗无法触发显示另一个showInSubWindow为true的弹窗。 |
| isModal | Option\<Bool> | 否 | true | **命名参数。**  弹窗是否为模态窗口。模态窗口有蒙层，非模态窗口无蒙层。<br/>初始值：true，此时弹窗有蒙层。 |
| backgroundColor | Option\<[Color](./cj-common-types.md#class-color)> | 否 | Color.TRANSPARENT | **命名参数。**  弹窗背板颜色。<br/>**说明：** <br/>当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则颜色显示将不符合预期效果。 |
| backgroundBlurStyle | Option\<[BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)> | 否 | BlurStyle.COMPONENT_ULTRA_THICK | **命名参数。**  弹窗背板模糊材质。<br/>**说明：** <br/>设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。 |
| onWillDismiss | Option\<([DismissDialogAction](./cj-dialog-actionsheet.md#class-dismissdialogaction)) -> Unit> | 否 | None | **命名参数。**  交互式关闭回调函数。<br/>**说明：**<br/>1.当用户执行点击遮障层关闭、左滑/右滑、三键back、键盘ESC关闭交互操作时，如果注册该回调函数，则不会立刻关闭弹窗。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗。当前组件返回的reason中，暂不支持CLOSE_BUTTON的枚举值。<br/>2.在onWillDismiss回调中，不能再做onWillDismiss拦截。 |
| cornerRadius | Option\<[BorderRadiuses](./cj-common-types.md#class-borderradiuses)> | 否 | BorderRadiuses(topLeft: 32.vp, topRight: 32.vp, bottomLeft: 32.vp, bottomRight: 32.vp) | **命名参数。**  设置背板的圆角半径。<br />可分别设置4个圆角的半径。<br /> 圆角大小受组件尺寸限制，最大值为组件宽或高的一半，若值为负，则按照默认值处理。 <br /> 百分比参数方式：以父元素弹窗宽和高的百分比来设置弹窗的圆角。<br/>**说明：**<br/>当cornerRadius属性类型为LocalizedBorderRadiuses时，支持随语言习惯改变布局顺序。 |
| transition | Option\<[TransitionEffect](./cj-animation-transition.md#class-transitioneffect)> | 否 | None| **命名参数。**  设置弹窗显示和退出的过渡效果。<br/>**说明：**<br/> 1.如果不设置，则使用默认的显示/退出动效。<br/> 2.显示动效中按back键，打断显示动效，执行退出动效，动画效果为显示动效与退出动效的曲线叠加后的效果。<br/> 3.退出动效中按back键，不会打断退出动效，退出动效继续执行，继续按back键退出应用。 |
| width | Option\<[Length](./cj-common-types.md#interface-length)> | 否 | None | **命名参数。**  设置弹窗背板的宽度。<br />**说明：**<br>- 弹窗宽度默认最大值：None。<br />- 百分比参数方式：弹窗参考宽度为所在窗口的宽度，在此基础上调小或调大。 |
| height | Option\<[Length](./cj-common-types.md#interface-length)> | 否 | N