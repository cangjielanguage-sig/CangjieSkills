### func indicatorStyle(Length, Length, Length, Length, Length, ResourceColor, ResourceColor, Bool)<sup>deprecated</sup>

```cangjie
public func indicatorStyle(
    left!: Length = (-1.0).vp,
    top!: Length = (-1.0).vp,
    right!: Length = (-1.0).vp,
    bottom!: Length = (-1.0).vp,
    size!: Length = (10.0).vp,
    color!: ResourceColor = Color(0x0c000000),
    selectedColor!: ResourceColor = Color(0xff0a59f7),
    mask!: Bool = false
): This
```

**功能：** 设置导航点样式。建议使用[indicator](#func-indicatorbool)代替。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|left|[Length](./cj-common-types.md#interface-length)|否|(- 1.0).vp| **命名参数。** 设置导航点距离Swiper组件左边的距离。<br>未设置left和right时，进行自适应大小布局，按照指示器本身大小和Swiper的大小在主轴方向上进行居中对齐。设置为0时，按照0位置布局计算。<br>优先级：高于right属性<br>取值范围：[0,Swiper宽度-导航点区域宽度]，超出该范围时，取最近的的边界值。|
|top|[Length](./cj-common-types.md#interface-length)|否|(- 1.0).vp| **命名参数。** 设置导航点距离Swiper组件顶部的距离。<br>未设置top和bottom时，进行自适应大小布局，按照指示器本身大小和Swiper的大小，在交叉轴方向上，位于底部，效果与设置bottom=0一致。设置为0时：按照0位置布局计算。<br>优先级：高于bottom属性<br>取值范围：[0,Swiper高度-导航点区域高度]，超出该范围时，取最近的边界值。|
|right|[Length](./cj-common-types.md#interface-length)|否|(- 1.0).vp| **命名参数。** 设置导航点距离Swiper组件右边的距离。<br>未设置left和right时，进行自适应大小布局，按照指示器本身大小和Swiper的大小在主轴方向上进行居中对齐。设置为0时：按照0位置布局计算。<br>优先级：低于left属性<br>取值范围：[0,Swiper宽度-导航点区域宽度]，超出该范围时，取最近的边界值。|
|bottom|[Length](./cj-common-types.md#interface-length)|否|(- 1.0).vp| **命名参数。** 设置导航点距离Swiper组件底部的距离。<br>未设置top和bottom时，进行自适应大小布局，按照指示器本身大小和Swiper的大小，在交叉轴方向上，位于底部，效果与设置bottom=0一致。设置为0时：按照0位置布局计算。<br>优先级：低于top属性<br>取值范围：[0,Swiper高度-导航点区域高度]，超出该范围时，取最近的边界值。|
|size|[Length](./cj-common-types.md#interface-length)|否|(10.0).vp| **命名参数。** 设置导航点的直径，不支持设置百分比。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color(0x0c000000)| **命名参数。** 设置导航点的颜色。|
|selectedColor|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color(0xff0a59f7)| **命名参数。** 设置选中的导航点的颜色。|
|mask|Bool|否|false| **命名参数。** 设置是否显示导航点蒙层样式。设置为true时显示导航点蒙层样式，为false时不显示。|