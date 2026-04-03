|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|CustomView|是|-| **命名参数。** 自定义弹窗内容构造器。|
|cancel|?[VoidCallback](./cj-common-types.md#type-voidcallback)|否|None| **命名参数。** 返回、ESC键和点击遮障层弹窗退出时的回调。初始值: { => }|
|autoCancel|?Bool|否|None| **命名参数。** 是否允许点击遮障层退出，true表示关闭弹窗。false表示不关闭弹窗。初始值: true|
|alignment|?[DialogAlignment](./cj-common-types.md#enum-dialogalignment)|否|None| **命名参数。** 弹窗在竖直方向上的对齐方式。初始值: DialogAlignment.Default|
|offset|?[Offset](./cj-common-types.md#class-offset)|否|None| **命名参数。** 弹窗相对alignment所在位置的偏移量。初始值: Offset(0.vp, 0.vp)|
|customStyle|?Bool|否|None| **命名参数。**  弹窗容器样式是否自定义。初始值: false<br>设置为false时（默认值）：<br/>1、圆角为32.vp。<br/>2、未设置弹窗宽度高度：弹窗容器的宽度根据栅格系统自适应。高度自适应自定义的内容节点。<br/>3、设置弹窗宽度高度：弹窗容器的宽度不超过默认样式下的最大宽度（自定义节点设置100%的宽度），弹窗容器的高度不超过默认样式下的最大高度（自定义节点设置100%的高度）。<br/>设置为true时：<br/>1、圆角为0，弹窗背景色为透明色。<br/>2、不支持设置弹窗宽度、高度、边框宽度、边框样式、边框颜色以及阴影宽度。|
|gridCount|?UInt32|否|None| **命名参数。** 弹窗宽度占栅格宽度的个数。<br>默认为按照窗口大小自适应，异常值按默认值处理，最大栅格数为系统最大栅格数。|
|maskColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None| **命名参数。** 自定义蒙层颜色。初始值: Color(0x33000000)|
|maskRect|?[Rectangle](./cj-common-types.md#class-rectangle)|否|None| **命名参数。** 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。初始值: Rectangle() <br/>**说明：**<br/>showInSubWindow为true时，maskRect不生效。|
|openAnimation|?[AnimateParam](./cj-common-types.md#class-animateparam)|否|None| **命名参数。** 自定义设置弹窗弹出的动画效果相关参数。<br>**说明**：<br>tempo默认值为1，当设置小于等于0的值时按默认值处理。<br/>iterations默认值为1，默认播放一次，设置为其他数值时按默认值处理。<br>playMode控制动画播放模式，默认值为PlayMode.Normal，设置为其他数值时按照默认值处理。|
|closeAnimation|?[AnimateParam](./cj-common-types.md#class-animateparam)|否|None| **命名参数。** 自定义设置弹窗关闭的动画效果相关参数。<br>**说明**：<br>tempo默认值为1，当设置小于等于0的值时按默认值处理。<br/>iterations默认值为1，默认播放一次，设置为其他数值时按默认值处理。<br>playMode控制动画播放模式，默认值为PlayMode.Normal，设置为其他数值时按照默认值处理。<br/>页面转场切换时，建议使用默认关闭动效。|
|showInSubWindow|?Bool|否|None| **命名参数。** 某弹框需要显示在主窗口之外时，是否在子窗口显示此弹窗。初始值: false<br>初始值：false，弹窗显示在应用内，而非独立子窗口。<br>**说明**：showInSubWindow为true的弹窗无法触发显示另一个showInSubWindow为true的弹窗。|
|backgroundColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None| **命名参数。** 设置弹窗背板填充。初始值: Color.Transparent<br/>**说明：** 如果同时设置了内容构造器的背景色，则backgroundColor会被内容构造器的背景色覆盖。<br/>当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则颜色显示将不符合预期效果。|
|cornerRadius|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 设置背板的圆角半径。初始值: 32.vp<br/>可分别设置4个圆角的半径。<br/>**说明**：自定义弹窗默认的背板圆角半径为32.vp，如果需要使用cornerRadius属性，请和[borderRadius](./cj-universal-attribute-border.md#func-borderradiuslength-length-length-length)属性一起使用。|
|isModal|?Bool|否|None| **命名参数。** 弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。初始值: true|
|onWillDismiss|?[Callback](./cj-common-types.md#type-callbackt-v)\<[DismissDialogAction](./cj-dialog-actionsheet.md#class-dismissdialogaction),Unit>|否|None| **命名参数。** 交互式关闭回调函数。<br/>**说明：**<br/>1.当用户执行点击遮障层关闭、左滑/右滑、三键back、键盘ESC关闭交互操作时，如果注册该回调函数，则不会立刻关闭弹窗。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗。当前组件返回的reason中，暂不支持CloseButton的枚举值。<br/>2.在onWillDismiss回调中，不能再做onWillDismiss拦截。|
|width|?[Length](.