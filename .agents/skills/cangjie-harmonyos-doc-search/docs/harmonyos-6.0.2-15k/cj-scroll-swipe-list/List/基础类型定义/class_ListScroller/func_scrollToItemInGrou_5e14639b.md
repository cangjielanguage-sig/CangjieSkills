#### func scrollToItemInGroup(Int32, Int32, Bool, ScrollAlign)

```cangjie
public func scrollToItemInGroup(index!: Int32, indexInGroup!: Int32, smooth!: Bool = false,
    align!: ScrollAlign = ScrollAlign.START): Unit
```

**功能：** 滑动到指定的ListItemGroup中指定的ListItem。

开启smooth动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-| **命名参数。** 要滑动到的目标元素所在的ListItemGroup在当前容器中的索引值。<br/>**说明：**<br/>index值设置成负值或者大于当前容器子组件的最大索引值，视为异常值，本次跳转不生效。|
|indexInGroup|Int32|是|-| **命名参数。** 要滑动到的目标元素在index指定的ListItemGroup中的索引值。<br/>**说明：**<br/>indexInGroup值设置成负值或者大于index指定的ListItemGroup容器子组件的最大索引值，视为异常值，本次跳转不生效。|
|smooth|Bool|否|false| **命名参数。** 设置滑动到列表项在列表中的索引值时是否有动效，true表示有动效，false表示没有动效。<br/>初始值：false。<br/>**说明：**<br/>开启动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题。|
|align|[ScrollAlign](./cj-scroll-swipe-scroll.md#enum-scrollalign)|否|ScrollAlign.START| **命名参数。** 指定滑动到的元素与当前容器的对齐方式。<br/>初始值：ScrollAlign.START。|