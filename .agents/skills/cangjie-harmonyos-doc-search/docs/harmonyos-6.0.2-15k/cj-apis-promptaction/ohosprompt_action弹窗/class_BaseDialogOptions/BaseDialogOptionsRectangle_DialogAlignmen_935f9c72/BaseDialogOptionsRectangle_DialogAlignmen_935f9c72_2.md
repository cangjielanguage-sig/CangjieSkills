| 参数名称            | 参数类型        | 必填 | 默认值               | 描述                     |
|:----------------|:---------------|:---|:------------|:------------------|
| maskRect        | [Rectangle](./cj-common-types.md#class-rectangle)                | 否  | Rectangle(x: 0.vp, y: 0.vp, width: 100.percent, height: 100.percent)          | **命名参数。**  弹窗遮蔽层区域。<br> **说明：**  <br> - showInSubWindow为true时，maskRect不生效。<br> - maskRect在设置部分属性值后，其余属性值默认为0。     |
| alignment       | [DialogAlignment](./cj-common-types.md#enum-dialogalignment) | 否  | DialogAlignment.Default     | **命名参数。**  弹窗在竖直方向上的对齐方式。 |
| offset          | [Offset](./cj-common-types.md#class-offset)   | 否  | Offset(0.vp, 0.vp)            | **命名参数。**  弹窗相对alignment所在位置的偏移量。 |
| isModal         | Bool     | 否  | true                          | **命名参数。**  弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。默认弹窗有蒙层。|
| showInSubWindow | Bool     | 否  | false                         | **命名参数。**  某弹框需要显示在主窗口之外时，是否在子窗口显示此弹窗。默认弹窗显示在应用内，而非独立子窗口。 |
|autoCancel|Bool|否|true| 点击遮障层时，是否关闭弹窗，true表示关闭弹窗。false表示不关闭弹窗。<br> 初始值： true|
| maskColor | [Color](./cj-common-types.md#class-color)      | 否  | Color(0x33000000) | **命名参数。**  自定义蒙层颜色。 |
| transition | [TransitionEffect](./cj-animation-transition.md#class-transitioneffect)     | 否  | TransitionEffect.OPACITY | **命名参数。**  设置弹窗显示和退出的过渡效果。<br />**说明：** <br />1.显示动效中按back键，打断显示动效，执行退出动效，动画效果为显示动效与退出动效的曲线叠加后的效果。<br />2.退出动效中按back键，不会打断退出动效，退出动效继续执行，继续按back键退出应用。 |
| onDidAppear | () -> Unit     | 否  | { => } | **命名参数。**  弹窗弹出时的事件回调。<br />**说明：** <br />1.正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。<br />2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。<br />3.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。<br />4.当弹窗入场动效未完成时关闭弹窗，该回调不会触发。|
| onDidDisappear | () -> Unit     | 否  | { => } | **命名参数。**  弹窗消失时的事件回调。<br />**说明：** <br /> 正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。|
| onWillAppear | () -> Unit     | 否  | { => } | **命名参数。**  弹窗显示动效前的事件回调。<br />**说明：** <br /> 1.正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。<br />2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。|
| onWillDisappear | () -> Unit     | 否  | { => } | **命名参数。**  弹窗退出动效前的事件回调。<br />**说明：** <br />1.正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。<br />2.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。 |
| keyboardAvoidMode | [KeyboardAvoidMode](#enum-keyboardavoidmode)     | 否  | KeyboardAvoidMode.DEFAULT | **命名参数。**  用于设置弹窗是否在拉起软键盘时进行自动避让。 |
| enableHoverMode | Bool     | 否  | false  | **命名参数。**   是否响应悬停态。 |
| hoverModeArea | [HoverModeAreaType](#enum-hovermodeareatype)     | 否  | HoverModeAreaType.BOTTOM_SCREEN | **命名参数。**   悬停态下弹窗默认展示区域。 |