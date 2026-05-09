|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|() -> Unit|是|-|**命名参数。** 提示气泡内容的构造器。|
|placement|?[Placement](#enum-placement)|否|Option.None|**命名参数。** 气泡组件优先显示的位置。<br>**说明：** 当前位置显示不下时，会自动调整位置。初始值为Placement.Bottom。|
|popupColor|?[Color](./cj-common-types.md#class-color)|否|None|**命名参数。** 提示气泡的背景颜色。初始值为Color(0x1000000)。|
|enableArrow|?Bool|否|None|**命名参数。** 是否显示箭头。<br>**说明：** 如果箭头所在方位侧的气泡长度不足以显示下箭头，则会默认不显示箭头。比如：placement设置为Left，但气泡高度小于箭头的宽度（32vp），则实际不会显示箭头。初始值为true。|
|autoCancel|?Bool|否|None|**命名参数。** 页面有操作时，是否自动关闭气泡。初始值为true。|
|onStateChange|Option<([PopupStateChangeParam](#class-popupstatechangeparam)) -> Unit>|否|Option.None|**命名参数。** 弹窗状态变化事件回调，参数为弹窗当前的显示状态。|
|showInSubWindow|?Bool|否|None|**命名参数。** 是否在子窗口显示气泡。初始值为false。|
|backgroundColor|?[Color](./cj-common-types.md#class-color)|否|None|**命名参数。** 提示气泡的背景颜色。初始值为Color(0x1000000)。|
|arrowOffset|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** popup箭头在弹窗处的偏移。<br>**说明：** 箭头在气泡上下方时，数值为0表示箭头居最左侧，偏移量为箭头至最左侧的距离，默认居中。箭头在气泡左右侧时，偏移量为箭头至最上侧的距离，默认居中。如果显示在屏幕边缘，气泡会自动左右偏移，数值为0时箭头始终指向绑定组件。初始值为0.vp。|
|mask|?[Color](./cj-common-types.md#class-color)|否|None|**命名参数。** 提示气泡遮障层的颜色。|
|targetSpace|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 设置popup与目标的间隙。初始值为0.vp。|
|offset|?[Position](#class-position)|否|None|**命名参数。** popup组件相对于placement设置的显示位置的偏移。<br>**说明：** 不支持设置百分比。 |
|width|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 弹窗宽度。<br>**说明：**  showInSubWindow=true时最大高度为设备屏幕高度，showInSubWindow=false时最大高度为应用窗口高度。高度限定逻辑=最大高度-状态栏高度（没有时高度为0）-dock栏高度（没有时高度为0）-40VP-40VP。初始值为0.vp。|
|arrowPointPosition|?[ArrowPointPosition](./cj-common-types.md#enum-arrowpointposition)|否|None|**命名参数。** 气泡尖角相对于父组件显示位置，气泡尖角在垂直和水平方向上有 ”Start“、”Center“、”End“三个位置点可选。以上所有位置点均位于父组件区域的范围内，不会超出父组件的边界范围。|
|arrowWidth|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 箭头宽度。<br>**说明：** 若所设置的箭头宽度超过所在边的长度减去两倍的气泡圆角大小，则不绘制气泡箭头。初始值为16.vp。|
|arrowHeight|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 箭头高度。<br>**说明：** 不支持设置百分比。初始值为16.vp。|