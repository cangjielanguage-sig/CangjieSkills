### func displayMode(?SwiperDisplayMode)

```cangjie
public func displayMode(value: ?SwiperDisplayMode): This
```

**功能：** 设置主轴方向上元素排列的模式，优先以displayCount设置的个数显示，displayCount未设置时本属性生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[SwiperDisplayMode](./cj-common-types.md#enum-swiperdisplaymode)|是|-|主轴方向上元素排列的模式。<br>初始值：SwiperDisplayMode.Stretch。|

### func duration(?UInt32)

```cangjie
public func duration(value: ?UInt32): This
```

**功能：** 设置子组件切换的动画时长。

duration需要和[curve](#func-curvecurve)一起使用。

curve默认曲线为[interpolatingSpring](./cj-apis-curves.md#static-func-interpolatingspringfloat32-float32-float32-float32)，此时动画时长只受曲线自身参数影响，不再受duration的控制。不受duration控制的曲线可以查阅[插值计算](./cj-apis-curves.md)模块，比如，[springMotion](./cj-apis-curves.md#static-func-springmotionfloat32-float32-float32)、[responsiveSpringMotion](./cj-apis-curves.md#static-func-responsivespringmotionfloat32-float32-float32)和interpolatingSpring类型的曲线不受duration控制。如果希望动画时长受到duration控制，需要给curve设置其他曲线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?UInt32|是|-|子组件切换的动画时长，单位为毫秒。设置小于0的值时，按照初始值处理。<br>初始值：400。<br>取值范围：[0, +∞)，设置小于0的值时，按照初始值处理。|

### func effectMode(?EdgeEffect)

```cangjie
public func effectMode(value: ?EdgeEffect): This
```

**功能：** 设置边缘滑动效果，[loop](#func-loopbool) = false时生效。调用SwiperController.changeIndex()、SwiperController.showNext()和SwiperController.showPrevious()接口跳转至首尾页时不生效回弹。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[EdgeEffect](./cj-common-types.md#enum-edgeeffect)|是|-|边缘滑动效果。<br>初始值：EdgeEffect.Spring。|

### func index(?UInt32)

```cangjie
public func index(value: ?UInt32): This
```

**功能：** 设置当前在容器中显示的子组件的索引值。设置大于等于子组件数量时，按照初始值0处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?UInt32|是|-|当前在容器中显示的子组件的索引值。<br> **说明：**<br>设置的值小于0或大于最大页面索引时，取0。<br>初始值：0。|

### func indicator(?Bool)

```cangjie
public func indicator(indicator: ?Bool): This
```

**功能：** 设置可选导航点指示器样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|indicator|?Bool|是|-|可选导航点指示器样式。<br>- boolean：是否启用导航点指示器。设置为true启用，false不启用。<br>初始值：true。|

### func indicator(?DotIndicator)

```cangjie
public func indicator(indicator: ?DotIndicator): This
```

**功能：** 设置外部绑定的导航点组件控制器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|indicator|?[DotIndicator](#class-dotindicator)|是|-|可选导航点指示器样式。<br>- DotIndicator：圆点指示器样式。<br>初始值：DigitIndicator()。|