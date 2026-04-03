### class SwiperContentAnimatedTransition

```cangjie
public class SwiperContentAnimatedTransition {
    public SwiperContentAnimatedTransition(
        public var timeout: Int32,
        public var transition: (SwiperContentTransitionProxy) -> Unit
    )
}
```

**功能：** Swiper自定义切换动画相关信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var timeout

```cangjie
public var timeout: Int32
```

**功能：** Swiper自定义切换动画超时时间。从页面执行默认动画（页面滑动）至移出视窗外的第一帧开始计时，如果到达该时间后，开发者仍未调用[SwiperContentTransitionProxy](#class-swipercontenttransitionproxy)的finishTransition接口通知Swiper组件此页面的自定义动画已结束，那么组件就会认为此页面的自定义动画已结束，立即将该页面节点下渲染树。单位ms。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

#### var transition

```cangjie
public var transition:(SwiperContentTransitionProxy) -> Unit
```

**功能：** 自定义切换动画具体内容。

**类型：** ([SwiperContentTransitionProxy](#class-swipercontenttransitionproxy))->Unit

**读写能力：** 可读写

**起始版本：** 19

#### SwiperContentAnimatedTransition(Int32, (SwiperContentTransitionProxy) -> Unit)

```cangjie
public SwiperContentAnimatedTransition(
    public var timeout: Int32,
    public var transition: (SwiperContentTransitionProxy) -> Unit
)
```

**功能：** SwiperContentAnimatedTransition的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|timeout|Int32|是|-|Swiper自定义切换动画超时时间。从页面执行默认动画（页面滑动）至移出视窗外的第一帧开始计时，如果到达该时间后，开发者仍未调用[SwiperContentTransitionProxy](#class-swipercontenttransitionproxy)的finishTransition接口通知Swiper组件此页面的自定义动画已结束，那么组件就会认为此页面的自定义动画已结束，立即将该页面节点下渲染树。单位ms，初始值为0。|
|transition|([SwiperContentTransitionProxy](#class-swipercontenttransitionproxy))->Unit|是|-|自定义切换动画具体内容。|