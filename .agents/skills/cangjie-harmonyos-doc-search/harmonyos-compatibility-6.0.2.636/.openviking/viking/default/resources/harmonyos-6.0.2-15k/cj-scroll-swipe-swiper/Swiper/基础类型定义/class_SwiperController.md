### class SwiperController

```cangjie
public class SwiperController {
    public init()
}
```

**功能：** SwiperController是Swiper容器组件的控制器，可以定义该类型的对象并绑定至Swiper组件，实现控制子组件的翻页。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init()

```cangjie
public init()
```

**功能：** SwiperController的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func changeIndex(Int32, Bool)

```cangjie
public func changeIndex(index: Int32, useAnimation: Bool): Unit
```

**功能：** 翻页至指定页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|指定页面在Swiper中的索引值。<br> **说明：**<br>设置的值小于0或大于最大页面索引时，取0。|
|useAnimation|Bool|是|-|设置翻至指定页面时是否有动效，true表示有动效，false表示没有动效。<br>初始值：false。|

#### func changeIndex(Int32)

```cangjie
public func changeIndex(index: Int32): Unit
```

**功能：** 翻页至指定页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|指定页面在Swiper中的索引值。<br> **说明：**<br>设置的值小于0或大于最大页面索引时，取0。|

#### func finishAnimation()

```cangjie
public func finishAnimation(): Unit
```

**功能：** 停止播放动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func finishAnimation(() -> Unit)

```cangjie
public func finishAnimation(callback: () -> Unit): Unit
```

**功能：** 停止播放动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，动画结束时触发。|

#### func showNext()

```cangjie
public func showNext(): Unit
```

**功能：** 翻至下一页。翻页带动效切换过程，时长通过Swiper的[duration](#func-durationuint32)属性设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func showPrevious()

```cangjie
public func showPrevious(): Unit
```

**功能：** 翻至上一页。翻页带动效切换过程，时长通过Swiper的[duration](#func-durationuint32)属性设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12