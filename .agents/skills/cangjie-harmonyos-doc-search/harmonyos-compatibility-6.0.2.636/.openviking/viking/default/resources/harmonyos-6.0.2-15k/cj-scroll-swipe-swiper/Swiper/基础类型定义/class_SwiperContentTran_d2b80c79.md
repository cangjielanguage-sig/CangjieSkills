### class SwiperContentTransitionProxy

```cangjie
public class SwiperContentTransitionProxy {
    public let selectedIndex: Int32
    public let index: Int32
    public let position: Float64
    public let mainAxisLength: Float64
}
```

**功能：** Swiper自定义切换动画执行过程中，返回给开发者的proxy对象。开发者可通过该对象获取自定义动画视窗内的页面信息，同时，也可以通过调用该对象的finishTransition接口通知Swiper组件页面自定义动画已结束。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let index

```cangjie
public let index: Int32
```

**功能：** 视窗内页面的索引。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let mainAxisLength

```cangjie
public let mainAxisLength: Float64
```

**功能：** index对应页面在主轴方向上的长度，单位vp。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let position

```cangjie
public let position: Float64
```

**功能：** index页面相对于Swiper主轴起始位置（selectedIndex对应页面的起始位置）的移动比例。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let selectedIndex

```cangjie
public let selectedIndex: Int32
```

**功能：** 当前选中页面的索引。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### func finishTransition()

```cangjie
public func finishTransition(): Unit
```

**功能：** 通知Swiper组件，此页面的自定义动画已结束。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19