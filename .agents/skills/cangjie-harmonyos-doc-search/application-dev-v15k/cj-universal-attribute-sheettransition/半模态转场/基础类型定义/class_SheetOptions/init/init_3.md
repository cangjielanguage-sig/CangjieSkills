回弹效果。<br>若不注册该回调函数，但注册shouldDimiss或onWillDismiss时，则默认在下滑关闭时，会触发回弹效果，回弹后再根据shouldDimiss或onWillDismiss内的回调行为决定半模态是否关闭。<br>如果不注册该回调函数，且未注册shouldDimiss或onWillDismiss时，默认在下滑关闭时，触发半模态关闭。|
| onHeightDidChange | Option\<(Float32) -> Unit> | 否  | Option.None  | **命名参数。**  半模态页面高度变化回调函数。<br>**说明：**<br>底部弹窗时，只有档位变化和拖拽跟手才返回每一帧高度，拉起半模态和避让软键盘只返回最后的高度，其他弹窗只在半模态拉起返回最后高度。返回值为px。 |
| onDetentsDidChange | Option\<(Float32) -> Unit> | 否  | Option.None  | **命名参数。**  半模态页面档位变化回调函数。<br>**说明：**<br>底部弹窗时，档位变化返回最后的高度。返回值为px。 |
| onWidthDidChange | Option\<(Float32) -> Unit> | 否  | Option.None  | **命名参数。**  半模态页面宽度变化回调函数。<br>**说明：**<br>宽度变化时返回最后的宽度。返回值为px。 |
| onTypeDidChange | Option\<(Float32) -> Unit> | 否  | Option.None  | **命名参数。**  半模态页面形态变化回调函数。<br>**说明：**<br>形态变化时返回最后的形态。 |
| borderWidth | Option\<Length> | 否  | 0.vp  | **命名参数。**  设置半模态页面的边框宽度。可分别设置4个边框宽度。<br>百分比参数方式：以父元素半模态页面宽的百分比来设置半模态页面的边框宽度。<br>当半模态页面左边框和右边框大于半模态页面宽度，半模态页面上边框和下边框大于半模态页面高度，显示可能不符合预期。<br>**说明：**<br>底部弹窗时，底部边框宽度设置无效。 |
| borderColor | Option\<Color> | 否  | Color.BLACK  | **命名参数。**  设置半模态页面的边框颜色。如果使用borderColor属性，需要和borderWidth属性一起使用。<br>**说明：**<br>底部弹窗时，底部边框颜色设置无效。 |
| borderStyle | Option\<[EdgeStyles](./cj-common-types.md#class-edgestyles)> | 否  | BorderStyle.Solid  | **命名参数。**  设置半模态页面的边框样式。如果使用borderStyle属性，需要和borderWidth属性一起使用。<br>**说明：**<br>底部弹窗时，底部边框样式设置无效。 |
| width | Option\<Length> | 否  | Option.None  | **命名参数。**  设置半模态页面的宽度。百分比参数方式：以父元素宽的百分比来设置半模态页面的宽度。 |
| shadow | Option\<[ShadowOptions](./cj-text-input-text.md#class-shadowoptions)> | 否  | Option.None | **命名参数。**  设置半模态页面的阴影。 |
| mode | Option\<[SheetMode](#enum-sheetmode)> | 否  | SheetMode.OVERLAY  | **命名参数。**  设置半模态页面的显示层级。<br>**说明：**<br>半模态显示期间mode属性不支持动态切换，两种模式的显示层级完全不同，无法做到显示期间同一个半模态从一个层级变换到另一个层级。建议在使用时明确诉求固定mode值。 |
| scrollSizeMode | Option\<[ScrollSizeMode](#enum-scrollsizemode)> | 否  | ScrollSizeMode.FOLLOW_DETENT | **命名参数。**  设置半模态面板滑动时，内容区域刷新时机。 |