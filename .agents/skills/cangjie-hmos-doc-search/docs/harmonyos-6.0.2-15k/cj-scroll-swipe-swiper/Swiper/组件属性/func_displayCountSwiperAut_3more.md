### func displayCount(SwiperAutoFill)

```cangjie
public func displayCount(value: SwiperAutoFill): This
```

**功能：** 设置Swiper视窗内元素显示个数。

使用SwiperAutoFill类型时，通过设置一个子组件最小宽度值minSize，会根据Swiper当前宽度和minSize值自动计算并更改一页内元素显示个数。当minSize为空或者小于等于0时，Swiper显示1列。

当按组进行翻页时，判定翻页的拖拽距离阈值将调整为Swiper宽度的50%（若按子元素翻页，该阈值为子元素宽度的50%）。若最后一组的子元素数量少于displayCount，将利用占位子元素进行填充，占位子元素仅用于布局定位，不显示任何内容，其位置将直接显示Swiper的背景样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[SwiperAutoFill](#class-swiperautofill)|是|-|视窗内显示的子元素个数。|

> **说明：**
>
> 当Swiper子组件个数小于等于Swiper组件内容区内显示的节点总个数(totalDisplayCount = DisplayCount + prevMargin? (1 : 0) + nextMargin? (1 : 0))时，一般按照非循环模式布局处理，此时，前后边距对应子组件不显示，但依然会在视窗内占位。Swiper组件按照totalDisplayCount个数判断测算规格。例外情况如下：
>
> - 当Swiper子组件个数等于Swiper组件内容区内显示的节点总个数且prevMargin和nextMargin都生效时，设置loop为true支持循环。
> - 当Swiper子组件个数等于Swiper组件DisplayCount数 + 1，且prevMargin和nextMargin至少一个生效时，设置loop为true会生成截图占位组件(如果使用图片异步加载等显示耗时较长的组件可能不能正确生成截图，不建议在该场景开启循环)，支持循环。

### func displayMode(SwiperDisplayMode)

```cangjie
public func displayMode(value: SwiperDisplayMode): This
```

**功能：** 设置主轴方向上元素排列的模式，优先以displayCount设置的个数显示，displayCount未设置时本属性生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[SwiperDisplayMode](#enum-swiperdisplaymode)|是|-|主轴方向上元素排列的模式。<br>初始值：SwiperDisplayMode.STRETCH。|

### func duration(UInt32)

```cangjie
public func duration(value: UInt32): This
```

**功能：** 设置子组件切换的动画时长。

duration需要和[curve](#func-curvecurve)一起使用。

curve默认曲线为[interpolatingSpring](./cj-apis-curves.md#static-func-interpolatingspringfloat32-float32-float32-float32)，此时动画时长只受曲线自身参数影响，不再受duration的控制。不受duration控制的曲线可以查阅[插值计算](./cj-apis-curves.md)模块，比如，[springMotion](./cj-apis-curves.md#static-func-springmotionfloat32-float32-float32)、[responsiveSpringMotion](./cj-apis-curves.md#static-func-responsivespringmotionfloat32-float32-float32)和interpolatingSpring类型的曲线不受duration控制。如果希望动画时长受到duration控制，需要给curve设置其他曲线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|UInt32|是|-|子组件切换的动画时长，单位为毫秒。设置小于0的值时，按照初始值处理。<br>初始值：400。<br>取值范围：[0, +∞)，设置小于0的值时，按照初始值处理。|