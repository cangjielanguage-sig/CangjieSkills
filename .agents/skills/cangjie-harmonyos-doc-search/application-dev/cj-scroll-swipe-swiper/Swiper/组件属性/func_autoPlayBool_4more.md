### func autoPlay(?Bool)

```cangjie
public func autoPlay(value: ?Bool): This
```

**功能：** 设置子组件是否自动播放。[loop](#func-loopbool)为false时，自动轮播到最后一页时停止轮播。手势切换后不是最后一页时继续播放。当Swiper不可见时会停止轮播。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|子组件是否自动播放。<br>初始值：false，不自动轮播。|

### func cachedCount(?Int32)

```cangjie
public func cachedCount(value: ?Int32): This
```

**功能：** 设置预加载子组件个数，以当前页面为基准，加载当前显示页面的前后个数。例如cachedCount=1时，会将当前显示的页面的前面一页和后面一页的子组件都预加载。如果设置为按组翻页，即displayCount的swipeByGroup参数设为true，预加载时会以组为基本单位。例如cachedCount=1，swipeByGroup=true时，会将当前组的前面一组和后面一组的子组件都预加载。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Int32|是|-|预加载子组件个数。<br>初始值：1。<br>取值范围：[0, +∞)，设置小于0的值时，按照初始值处理。|

### func curve(?Curve)

```cangjie
public func curve(value: ?Curve): This
```

**功能：** 设置Swiper的动画曲线，默认为弹簧插值曲线。常用曲线参考[Curve枚举说明](./cj-common-types.md#enum-curve)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[Curve](./cj-common-types.md#enum-curve)|是|-|Swiper的动画曲线。<br>初始值：Curve.Linear。|

### func disableSwipe(?Bool)

```cangjie
public func disableSwipe(value: ?Bool): This
```

**功能：** 设置禁用组件滑动切换功能。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|是否禁用组件滑动切换功能。设置为true禁用，false不禁用。<br>初始值：false。|