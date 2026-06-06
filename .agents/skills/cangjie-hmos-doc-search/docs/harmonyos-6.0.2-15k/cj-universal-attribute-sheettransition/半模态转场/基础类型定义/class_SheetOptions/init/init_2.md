|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| backgroundColor | Option\<[Color](./cj-common-types.md#color)> | 否 | Color.WHITE  | **命名参数。**  半模态页面的背板颜色，默认为白色。 |
| onAppear | Option\<() -> Unit> | 否 | Option.None  | **命名参数。**  半模态页面显示（动画结束后）回调函数。 |
| onDisappear | Option\<() -> Unit> | 否 | Option.None | **命名参数。**  半模态页面回退（动画结束后）回调函数。 |
| onWillAppear | Option\<() -> Unit> | 否 | Option.None | **命名参数。**  半模态页面显示（动画开始前）回调函数。 |
| onWillDisappear | Option\<() -> Unit> | 否 | Option.None | **命名参数。**  半模态页面回退（动画开始前）回调函数。<br>**说明：**<br>不允许在onWillDisappear函数中修改状态变量，可能会导致组件行为不稳定。 |
| height | Option\<() -> Unit> | 否 | Option.None  | **命名参数。**  半模态高度。<br>**说明：**<br>底部弹窗竖屏时，当设置detents时，该属性设置无效。<br>底部弹窗竖屏时，最大高度为距离信号栏8vp。<br>底部弹窗横屏时，该属性设置无效，高度为距离屏幕顶部8vp。<br>居中弹窗和跟手弹窗设置类型为SheetSize.LARGE和SheetSize.MUDIUM无效，显示默认高度560vp。居中弹窗和跟手弹窗最小高度为320vp，最大高度为窗口短边的90%。当使用Length设置的高度和使用SheetSize.FIT\_CONTENT自适应的高度大于最大高度，则显示最大高度，小于最小高度，则显示最小高度。 |
| detents | Option\<Array\<[SheetSize](#enum-sheetsize)>> | 否 | Option.None | **命名参数。**  半模态页面的切换高度档位。<br>**说明：**<br>底部弹窗竖屏生效，元组中第一个高度为初始高度。<br>面板可跟手滑动切换档位，松手后是否滑动至目标档位有两个判断条件：速度和距离。速度超过阈值，则执行滑动至与手速方向一致的目标档位；速度小于阈值，则引入距离判断条件，当位移距离>当前位置与目标位置的1/2，滑动至与手速方向一致的目标档位，位移距离当前位置与目标位置的1/2，返回至当前档位。速度阈值：1000，距离阈值：50%。 |
| preferType | Option\<[SheetType](#enum-sheettype)> | 否 | Option.None | **命名参数。**  半模态页面的样式。<br>**说明：**<br>preferType不可设置为SheetType.BOTTOM。 |
| showClose | Option\<Bool> | 否 | Option.None | **命名参数。**  是否显示关闭图标，默认显示关闭图标。使用关闭图标关闭半模态页面时，需要在onDisappear回调函数中将isShow参数置为false。参考示例代码。<br>**说明：**<br>Resource需要为Bool类型。 |
| dragBar | Option\<Bool> | 否  | Option.None | **命名参数。**  是否显示控制条。<br>**说明：**<br>半模态面板的dentents属性设置多个不同高度并且设置生效时，默认显示控制条。否则不显示控制条。 |
| blurStyle | Option\<BlurStyle> | 否  | Option.None | **命名参数。**  半模态面板的模糊背景。 |
| maskColor | Option\<[Color](./cj-common-types.md#color)> | 否  | \- | **命名参数。**  半模态页面的背景蒙层颜色。 |
| title | Option\<() -> Unit> | 否  | Option.None | **命名参数。**  半模态面板的标题。在使用时结合@Builder使用。 |
| enableOutsideInteractive | Option\<Bool> | 否  | Option.None | **命名参数。**  半模态所在页面是否允许交互。<br>**说明：**<br>设置为true时允许交互，不显示蒙层；设置为false时不允许交互，显示蒙层；若不进行设置，默认底部弹窗与居中弹窗不允许交互，跟手弹窗允许交互。当设置为true时，maskColor设置无效。 |
| shouldDismiss | Option\<([SheetDismiss](#class-sheetdismiss)) -> Unit> | 否  | Option.None  | **命名参数。**  半模态页面交互式关闭回调函数。<br>**说明：**<br>当用户执行下拉关闭/back事件/点击蒙层关闭/关闭按钮关闭交互操作时，如果注册该回调函数，则不会立刻关闭。 |
| onWillDismiss | Option\<([DismissSheetAction](#class-dismisssheetaction)) -> Unit> | 否  | Option.None  | **命名参数。**  半模态页面的交互式关闭回调函数允许开发者注册，以获取关闭操作的类型，并决定是否关闭半模态状态。<br>**说明：**<br>当用户触发关闭操作时，若已注册回调函数，则不会立即关闭页面，而是由开发者通过回调函数中的reason参数判断关闭操作的类型，进而根据具体原因自主选择是否关闭半模态页面。如果不注册该回调函数，则用户执行关闭操作时，正常关闭半模态，无其他行为。在onWillDismiss回调中，不能再做onWillDismiss拦截。建议在二次确认场景使用。 |
| onWillSpringBackWhenDismiss | Option\<([SpringBackAction](#springbackaction)) -> Unit> | 否  | Option.None  | **命名参数。**  半模态页面交互式关闭前控制回弹函数允许开发者注册，以控制半模态页面交互式关闭时的回弹效果。<br>**说明：**<br>当用户触发执行下拉关闭操作并同时注册该回调函数与shouldDimiss或onWillDismiss时，由开发者控制下滑关闭时是否回弹。在回调函数中可以通过调用springBack来实现回弹效果。也可以通过不调用springBack来取消