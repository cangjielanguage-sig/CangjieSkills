|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|?String|是|-|**命名参数。** 设置弹窗信息内容。|
|placement|?[Placement](#enum-placement)|否|Option.None|**命名参数。** 设置popup组件相对于目标的显示位置。|
|primaryButton|?[PopupButton](#class-popupbutton)|否|None|**命名参数。** 设置第一个按钮。初始值为PopupButton(value: "", action: {=>})。|
|secondaryButton|?[PopupButton](#class-popupbutton)|否|None|**命名参数。** 设置第二个按钮。初始值为PopupButton(value: "", action: {=>})。|
|onStateChange|Option<([PopupStateChangeParam](#class-popupstatechangeparam)) -> Unit>|否|Option.None|**命名参数。** 设置弹窗状态变化事件回调。|
|arrowOffset|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 设置popup箭头在弹窗处的偏移。初始值为0.vp。|
|showInSubWindow|?Bool|否|None|**命名参数。** 设置是否在子窗口显示气泡。初始值为false。|
|mask|?[Color](./cj-common-types.md#class-color)|否|None|**命名参数。** 设置遮罩层的颜色。初始值为Color(0x1000000)。|
|messageOptions|?[PopupMessageOptions](#class-popupmessageoptions)|否|None|**命名参数。** 设置弹窗信息文本参数。初始值为PopupMessageOptions()。|
|targetSpace|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 设置popup与目标的间隙。初始值为0.vp。|
|enableArrow|?Bool|否|None|**命名参数。** 是否启用箭头，初始值为true。|
|offset|?[Position](#class-position)|否|None|**命名参数。** 设置popup组件相对于placement设置的显示位置的偏移。初始值为Position(x:0.0, y: 0.0)。|
|popupColor|?[Color](./cj-common-types.md#class-color)|否|None|**命名参数。** 设置提示气泡的颜色。初始值为Color(0x1000000)。|
|autoCancel|?Bool|否|None|**命名参数。** 页面有操作时，设置是否自动关闭气泡。初始值为true。|
|width|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 设置弹窗宽度。初始值为0.vp。|
|arrowPointPosition|?[ArrowPointPosition](./cj-common-types.md#enum-arrowpointposition)|否|None|**命名参数。** 设置气泡尖角相对于父组件显示位置。|
|arrowWidth|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 箭头宽度。初始值为16.vp。|
|arrowHeight|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 箭头高度。初始值为8.vp。|
|radius|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 设置气泡圆角半径。初始值为20.vp。|
|shadow|?[ShadowStyle](./cj-common-types.md#enum-shadowstyle)|否|None|**命名参数。** 设置气泡阴影。初始值为ShadowStyle.OuterDefaultMD。|
|backgroundBlurStyle|?[BlurStyle](#enum-blurstyle)|否|Option.None|**命名参数。** 设置气泡模糊背景参数。初始值为BlurStyle.ComponentUltraThick。|
|transition|?[TransitionEffect](./cj-animation-transition.md#class-transitioneffect)|否|Option.None|**命名参数。** 自定义设置popup弹窗显示和退出的动画效果。|
|onWillDismiss|Option\<([DismissPopupAction](#class-dismisspopupaction)) -> Unit>|否|None|**命名参数。**设置拦截退出事件且执行回调函数。|
|followTransformOfTarget|?Bool|否|None|**命名参数。** 气泡绑定的宿主组件或其宿主组件的父容器添加了旋转、缩放等变换时，设置气泡是否能显示在对应变化后的位置上。|