### class Indicator

```cangjie
public open class Indicator {}
```

**功能：** 设置导航点距离Swiper组件距离。由于导航点有默认交互区域，交互区域高度为32.vp，所以无法让显示部分完全贴底。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### static func digit()

```cangjie
public static func digit(): DigitIndicator
```

**功能：** 返回一个DigitIndicator对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DigitIndicator](#class-digitindicator)|数字指示器。|

#### static func dot()

```cangjie
public static func dot(): DotIndicator
```

**功能：** 返回一个DotIndicator对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DotIndicator](#class-dotindicator)|圆点指示器。|

#### func bottom(Length)

```cangjie
public func bottom(value: Length): This
```

**功能：** 导航点底部相对于Swiper的位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|设置导航点底部相对于Swiper的位置。<br>未设置top和bottom时，进行自适应大小布局，按照指示器本身大小和Swiper的大小，在交叉轴方向上，位于底部，效果与设置bottom=0一致。<br>设置为0时：按照0位置布局计算。<br>优先级：低于top属性。<br>取值范围：[0,Swiper高度-导航点区域高度]，超出该范围时，取最近的边界值。|

#### func end(Length)

```cangjie
public func end(value: Length): This
```

**功能：** 在RTL模式下为导航点距离Swiper组件左边的距离，在LTR模式下为导航点距离Swiper组件右边的距离。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|在RTL模式下为导航点距离Swiper组件左边的距离，在LTR模式下为导航点距离Swiper组件右边的距离。<br>初始值：0。<br>单位：vp。|

#### func left(Length)

```cangjie
public func left(value: Length): This
```

**功能：** 导航点左侧相对于Swiper的位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|设置导航点左侧相对于Swiper的位置。<br>未设置left和right时，进行自适应大小布局，按照指示器本身大小和Swiper的大小在主轴方向上进行居中对齐。<br>设置为0时：按照0位置布局计算。<br>优先级：高于right属性。<br>取值范围：[0,Swiper宽度-导航点区域宽度]，超出该范围时，取最近的的边界值。|

#### func right(Length)

```cangjie
public func right(value: Length): This
```

**功能：** 导航点右侧相对于Swiper的位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|设置导航点右侧相对于Swiper的位置。<br>未设置left和right时，进行自适应大小布局，按照指示器本身大小和Swiper的大小在主轴方向上进行居中对齐。设置为0时：按照0位置布局计算。<br>优先级：低于left属性。<br>取值范围：[0,Swiper宽度-导航点区域宽度]，超出该范围时，取最近的的边界值。|