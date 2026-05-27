### func customContentTransition(SwiperContentAnimatedTransition)

```cangjie
public func customContentTransition(transition: SwiperContentAnimatedTransition): This
```

**功能：** 自定义Swiper页面切换动画。在页面跟手滑动和离手后执行切换动画的过程中，会对视窗内所有页面逐帧触发回调，开发者可以在回调中设置透明度、缩放比例、位移等属性来自定义切换动画。

> **说明：**
>
> - 循环场景下，设置prevMargin和nextMargin属性，使得Swiper前后端显示同一页面时，该接口不生效。
> - 在页面跟手滑动和离手后执行切换动画的过程中，会对视窗内所有页面逐帧触发[SwiperContentTransitionProxy](#class-swipercontenttransitionproxy)回调。例如，当视窗内有下标为0、1的两个页面时，会每帧触发两次index值分别为0和1的回调。
> - 设置displayCount属性的swipeByGroup参数为true时，若同组中至少有一个页面在视窗内时，则会对同组中所有页面触发回调，若同组所有页面均不在视窗内时，则会一起下渲染树。
> - 在页面跟手滑动和离手后执行切换动画的过程中，默认动画（页面滑动）依然会发生，若希望页面不滑动，可以设置主轴方向上负的位移（translate属性）来抵消页面滑动。例如：当displayCount属性值为2，视窗内有下标为0、1的两个页面时，页面水平滑动过程中，可以逐帧设置第0页的translate属性在x轴上的值为-position * mainAxisLength来抵消第0页的位移，设置第1页的translate属性在x轴上的值为-(position - 1) * mainAxisLength来抵消第1页的位移。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|transition|[SwiperContentAnimatedTransition](#class-swipercontentanimatedtransition)|是|-|Swiper自定义切换动画相关信息。|

### func onAnimationEnd((Int32, SwiperAnimationEvent) -> Unit)

```cangjie
public func onAnimationEnd(callback: (Int32, SwiperAnimationEvent) -> Unit): This
```

**功能：** 当Swiper切换动效结束时触发该事件，包括动画过程中手势中断，通过SwiperController调用finishAnimation。参数为动画结束后的index值，多列Swiper时，index为最左侧组件的索引。

> **说明：**
>
> 当翻页动画时长为0时，只有以下场景会触发该回调：滑动翻页、自动轮播、调用SwiperController.showNext()和SwiperController.showPrevious()接口以及手指点击导航点翻页。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32,[SwiperAnimationEvent](#class-swiperanimationevent))->Unit|是|-|回调函数，切换动画结束时触发。<br/> 参数一：当前显示元素的索引。<br/> 参数二：动画相关信息，只返回主轴方向上当前显示元素相对于Swiper起始位置的位移。|