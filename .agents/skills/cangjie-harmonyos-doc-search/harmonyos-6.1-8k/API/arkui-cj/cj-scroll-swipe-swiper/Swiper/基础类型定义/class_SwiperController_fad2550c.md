### class SwiperController

```cangjie
public class SwiperController {
    public init()
}
```

**功能：** SwiperController是Swiper容器组件的控制器，可以定义该类型的对象并绑定至Swiper组件，实现控制子组件的翻页。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init()

```cangjie
public init()
```

**功能：** SwiperController的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### func finishAnimation()

```cangjie
public func finishAnimation(): Unit
```

**功能：** 停止播放动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### func finishAnimation(?VoidCallback)

```cangjie
public func finishAnimation(callback: ?VoidCallback): Unit
```

**功能：** 停止播放动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[VoidCallback](./cj-common-types.md#type-voidcallback)|是|-|回调函数，动画结束时触发。<br>初始值：{ => }。|

#### func showNext()

```cangjie
public func showNext(): Unit
```

**功能：** 翻至下一页。翻页带动效切换过程，时长通过Swiper的[duration](#func-durationuint32)属性设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### func showPrevious()

```cangjie
public func showPrevious(): Unit
```

**功能：** 翻至上一页。翻页带动效切换过程，时长通过Swiper的[duration](#func-durationuint32)属性设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22