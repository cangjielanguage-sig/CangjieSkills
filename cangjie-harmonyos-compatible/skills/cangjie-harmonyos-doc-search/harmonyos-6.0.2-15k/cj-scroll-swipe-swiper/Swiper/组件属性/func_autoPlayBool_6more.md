### func autoPlay(Bool)

```cangjie
public func autoPlay(value: Bool): This
```

**功能：** 设置子组件是否自动播放。[loop](#func-loopbool)为false时，自动轮播到最后一页时停止轮播。手势切换后不是最后一页时继续播放。当Swiper不可见时会停止轮播。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|子组件是否自动播放。<br>初始值：false，不自动轮播。|

### func cachedCount(Int32)

```cangjie
public func cachedCount(value: Int32): This
```

**功能：** 设置预加载子组件个数，以当前页面为基准，加载当前显示页面的前后个数。例如cachedCount=1时，会将当前显示的页面的前面一页和后面一页的子组件都预加载。如果设置为按组翻页，即displayCount的swipeByGroup参数设为true，预加载时会以组为基本单位。例如cachedCount=1，swipeByGroup=true时，会将当前组的前面一组和后面一组的子组件都预加载。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|预加载子组件个数。<br>初始值：1。<br>取值范围：[0, +∞)，设置小于0的值时，按照初始值处理。|

### func curve(Curve)

```cangjie
public func curve(value: Curve): This
```

**功能：** 设置Swiper的动画曲线，默认为弹簧插值曲线。常用曲线参考[Curve枚举说明](./cj-common-types.md#enum-curve)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Curve](./cj-common-types.md#enum-curve)|是|-|Swiper的动画曲线。|

### func disableSwipe(Bool)

```cangjie
public func disableSwipe(value: Bool): This
```

**功能：** 设置禁用组件滑动切换功能。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否禁用组件滑动切换功能。设置为true禁用，false不禁用。<br>初始值：false。|

### func displayArrow(Bool, Bool)

```cangjie
public func displayArrow(value: Bool, isHoverShow!: Bool = false): This
```

**功能：** 设置导航点箭头样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|支持设置箭头和底板样式。设置为false不显示箭头和底板，true显示默认的箭头和底板样式。<br>初始值：false。|
|isHoverShow|Bool|否|false| **命名参数。** 设置鼠标悬停时是否显示箭头。<br> **说明：**<br>1、isHoverShow为false时，常驻显示箭头。<br>2、isHoverShow为true时，有导航点时鼠标悬停在导航点和箭头范围内显示箭头，无导航点时鼠标悬停在Swiper显示范围内显示箭头。<br>3、箭头显示时，支持点击翻页。|

### func displayArrow(ArrowStyle, Bool)

```cangjie
public func displayArrow(value: ArrowStyle, isHoverShow!: Bool = false): This
```

**功能：** 设置导航点箭头样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ArrowStyle](#class-arrowstyle)|是|-|支持设置箭头和底板样式。|
|isHoverShow|Bool|否|false| **命名参数。** 设置鼠标悬停时是否显示箭头。<br> **说明：**<br>1、isHoverShow为false时，常驻显示箭头。<br>2、isHoverShow为true时，有导航点时鼠标悬停在导航点和箭头范围内显示箭头，无导航点时鼠标悬停在Swiper显示范围内显示箭头。<br>3、箭头显示时，支持点击翻页。|