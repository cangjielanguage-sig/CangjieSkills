### class ListScroller

```cangjie
public class ListScroller <: BaseScroller {
    public init()
}
```

**功能：** List组件的滚动控制器，通过它控制List组件的滚动，仅支持一对一绑定到List组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

[BaseScroller](./cj-scroll-swipe-scroll.md#class-basescroller)

#### init()

```cangjie
public init()
```

**功能：** 创建ListScroller对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### func closeAllSwipeActions()

```cangjie
public func closeAllSwipeActions(): Unit
```

**功能：** 将EXPANDED状态的[ListItem](cj-scroll-swipe-listitem.md)收起。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### func closeAllSwipeActions(() -> Unit)

```cangjie
public func closeAllSwipeActions(onFinishCallback: () -> Unit): Unit
```

**功能：** 将EXPANDED状态的[ListItem](cj-scroll-swipe-listitem.md)收起，并设置回调事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onFinishCallback|()->Unit|是|-|在收起动画完成后触发。|

#### func getItemRectInGroup(Int32, Int32)

```cangjie
public func getItemRectInGroup(index: Int32, indexInGroup: Int32): RectResult
```

**功能：** 获取[ListItemGroup](./cj-scroll-swipe-listgroup.md#listitemgroup)中的[ListItem](./cj-scroll-swipe-listitem.md#listitem)的大小和相对于List的位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|ListItemGroup在List中的索引值。|
|indexInGroup|Int32|是|-|ListItem在ListItemGroup中的索引值。|

> **说明：**
>
> * index必须是当前显示区域显示的子组件的索引值，否则视index为非法值。
> * 索引值为index的子组件必须是ListItemGroup，否则视index为非法值。
> * indexInGroup必须是当前显示区域内ListItemGroup中显示的ListItem的索引值，否则视indexInGroup为非法值。
> * index或者indexInGroup为非法值时返回的大小和位置均为0。

**返回值：**

|类型|说明|
|:----|:----|
|[RectResult](./cj-common-types.md#class-rectresult)|ListItemGroup中的ListItem的大小和相对于List的位置。<br/>单位：vp。|