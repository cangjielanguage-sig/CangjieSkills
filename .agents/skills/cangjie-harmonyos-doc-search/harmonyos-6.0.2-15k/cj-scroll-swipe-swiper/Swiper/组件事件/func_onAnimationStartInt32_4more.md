### func onAnimationStart((Int32, Int32, SwiperAnimationEvent) -> Unit)

```cangjie
public func onAnimationStart(callback: (Int32, Int32, SwiperAnimationEvent) -> Unit): This
```

**功能：** 切换动画开始时触发该事件。参数为动画开始前的index值（不是最终结束动画的index值），多列Swiper时，index为最左侧组件的索引。

> **说明：**
>
> 当翻页动画时长为0时，只有以下场景会触发该回调：滑动翻页、自动轮播、调用SwiperController.showNext()和SwiperController.showPrevious()接口以及手指点击导航点翻页。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32,Int32,[SwiperAnimationEvent](#class-swiperanimationevent))->Unit|是|-|回调函数，切换动画开始时触发。<br/> 参数一：当前显示元素的索引。<br/> 参数二：切换动画目标元素的索引。<br/> 参数三：动画相关信息，包括主轴方向上当前显示元素和目标元素相对Swiper起始位置的位移，以及离手速度。|

### func onChange((Int32) -> Unit)

```cangjie
public func onChange(callback: (Int32) -> Unit): This
```

**功能：** 当前显示的子组件索引变化时触发该事件，返回值为当前显示的子组件的索引值。

Swiper组件结合LazyForEach使用时，不能在onChange事件里触发子页面UI的刷新。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32)->Unit|是|-|回调函数，当前显示的子组件索引变化时触发该事件。<br>参数一：当前显示元素的索引。|

### func onContentDidScroll((Int32, Int32, Float64, Float64) -> Unit)

```cangjie
public func onContentDidScroll(callback: (Int32, Int32, Float64, Float64) -> Unit): This
```

**功能：** 监听Swiper页面滑动事件。

> **说明：**
>
> - 循环场景下，设置prevMargin和nextMargin属性，使得Swiper前后端显示同一页面时，该接口不生效。
> - 在页面滑动过程中，会对视窗内所有页面逐帧触发onContentDidScroll事件的回调函数。例如，当视窗内有下标为0、1的两个页面时，会每帧触发两次index值分别为0和1的回调。
> - 设置displayCount属性的swipeByGroup参数为true时，若同组中至少有一个页面在视窗内时，则会对同组中所有页面触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32,Int32,Float64,Float64)->Unit|是|-|回调函数，Swiper滑动时触发。<br/> 参数一：当前显示元素的索引。<br/> 参数二：视窗内页面的索引。<br/> 参数三：index页面相对于Swiper主轴起始位置（selectedIndex对应页面的起始位置）的移动比例。<br/> 参数四：index对应页面在主轴方向上的长度。|

### func onGestureSwipe((Int32, SwiperAnimationEvent) -> Unit)

```cangjie
public func onGestureSwipe(callback: (Int32, SwiperAnimationEvent) -> Unit): This
```

**功能：** 在页面跟手滑动过程中，逐帧触发该事件。多列Swiper时，index为最左侧组件的索引。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32,[SwiperAnimationEvent](#class-swiperanimationevent))->Unit|是|-|回调函数，切页面跟手滑动过程中，逐帧触发。<br/> 参数一：当前显示元素的索引。<br/> 参数二：动画相关信息，只返回主轴方向上当前显示元素相对于Swiper起始位置的位移。|