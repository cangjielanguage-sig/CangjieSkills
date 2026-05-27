|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| title | String | 是 | \-| 弹窗标题。<br/>当文本内容过长无法显示时，用省略号代替未显示的部分。|
| message | String | 是 | \- | 弹窗内容。<br/>文本超长时会触发滚动条。 |
| sheets | Array\<[SheetInfo](#class-sheetinfo)> | 是 | \- | 设置选项内容，每个选择项支持设置图片、文本和选中的回调。 |
| subtitle | Option\<String> | 否 | Option.None | **命名参数。**  弹窗副标题。<br/>当文本内容过长无法显示时，用省略号代替未显示的部分。|
| confirm | Option\<[Confirm](#class-confirm)> | 否 | Option.None | **命名参数。**  确认Button的使能状态、默认焦点、按钮风格、文本内容和点击回调。在弹窗获焦且未进行tab键走焦时，该按钮默认响应Enter键，且多重弹窗可自动获焦连续响应。默认响应Enter键能力在defaultFocus为true时不生效。<br/>enabled：点击Button是否响应，true表示Button可以响应，false表示Button不可以响应。<br/>初始值：true。<br/>defaultFocus：设置Button是否是默认焦点，true表示Button是默认焦点，false表示Button不是默认焦点。<br/>初始值：false。<br/>style：设置Button的风格样式。<br/>初始值：DialogButtonStyle.DEFAULT。<br/>value：Button文本内容。当文本内容过长无法显示时，用省略号代替未显示的部分。<br/>action: Button选中时的回调。|
| cancel | Option\< () -> Unit> | 否 | Option.None | **命名参数。**  点击遮障层关闭dialog时的回调。 |
| autoCancel | Option\<boolean> | 否 | true | **命名参数。**  点击遮障层时，是否关闭弹窗。<br/>值为true时，点击遮罩层关闭弹窗，值为false时，点击遮罩层不关闭弹窗。|
| alignment | Option\<[DialogAlignment](./cj-common-types.md#enum-dialogalignment)> | 否 | DialogAlignment.Bottom | **命名参数。**  弹窗在竖直方向上的对齐方式。 |
| offset | Option\<[Offset](./cj-common-types.md#class-offset)> | 否 |Option.None| **命名参数。**  需要显式指定像素单位，如10.vp，也可设置百分比字符串，如100.percent。<br/>不指定像素单位时，默认单位vp，如10，等同于10.vp。<br/>弹窗相对alignment所在位置的偏移量。<br/>初始值：<br/>1.alignment设置为Top、TopStart、TopEnd时默认值为{dx: 0,dy: 40.vp}<br/>2.alignment设置为其他时默认值为{dx: 0,dy: -40.vp}|
| maskRect | Option\<[Rectangle](./cj-common-types.md#class-rectangle)> | 否 |Rectangle(x: 0, y: 0, width: 100.percent, height: 100.percent)| **命名参数。**  弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。 <br>**说明:**<br> showInSubWindow为true时，maskRect不生效。 |
| showInSubWindow | Option\<boolean> | 否 | false | **命名参数。**  某弹框需要显示在主窗口之外时，是否在子窗口显示此弹窗。<br>初始值：false，弹窗显示在应用内，而非独立子窗口。<br>**说明:**<br> showInSubWindow为true的弹窗无法触发显示另一个showInSubWindow为true的弹窗。 |
| isModal| Option\<boolean> | 否 | true | **命名参数。**  弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。<br/>初始值：true，此时弹窗有蒙层。|
| backgroundColor | Option\<[Color](./cj-common-types.md#class-color)> | 否 | Color.TRANSPARENT | **命名参数。**  弹窗背板颜色。<br>**说明:**<br> 当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则颜色显示将不符合预期效果。 |
| backgroundBlurStyle | Option\<[BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)> | 否 | BlurStyle.COMPONENT_ULTRA_THICK | **命名参数。**  弹窗背板模糊材质。<br>**说明:**<br>设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。 |
| onWillDismiss | Option\<( [DismissDialogAction](#class-dismissdialogaction) ) -> Unit> | 否   | Option.None | **命名参数。**  交互式关闭回调函数。 <br>**说明:**<br> 1.当用户执行点击遮障层关闭、左滑/右滑、三键back、键盘ESC关闭交互操作时，如果注册该回调函数，则不会立刻关闭弹窗。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗。当前组件返回的reason中，暂不支持CLOSE_BUTTON的枚举值。<br> 2.在onWillDismiss回调中，不能再做onWillDismiss拦截。 |
| cornerRadius | Option\<[BorderRadiuses](./cj-common-types.md#class-borderradiuses)>| 否 | BorderRadiuses(topLeft: 32.vp, topRight: 32.