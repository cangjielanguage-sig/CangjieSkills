### func enableScrollInteraction(Bool)

```cangjie
public func enableScrollInteraction(value: Bool): This
```

**功能：** 设置是否支持滚动手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否支持滚动手势，当设置为false时，无法通过手指或者鼠标滚动，但不影响控制器[Scroller](./cj-scroll-swipe-scroll.md#class-scroller)的滚动接口。<br>初始值：true。|

### func fadingEdge(Bool)

```cangjie
public func fadingEdge(enabled: Bool): This
```

**功能：** 设置是否开启边缘渐隐效果及设置边缘渐隐长度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enabled|Bool|是|-|fadingEdge生效时，会覆盖原组件的.overlay()属性。<br/>fadingEdge生效时，建议不在该组件上设置background相关属性，会影响渐隐的显示效果。<br>fadingEdge生效时，组件会裁剪到边界，设置组件的clip属性为false不生效。<br/>初始值：false，不开启边缘渐隐效果。|

### func fadingEdge(Bool, FadingEdgeOptions)

```cangjie
public func fadingEdge(enabled: Bool, options: FadingEdgeOptions): This
```

**功能：** 设置是否开启边缘渐隐效果及设置边缘渐隐长度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enabled|Bool|是|-|fadingEdge生效时，会覆盖原组件的.overlay()属性。<br/>fadingEdge生效时，建议不在该组件上设置background相关属性，会影响渐隐的显示效果。<br>fadingEdge生效时，组件会裁剪到边界，设置组件的clip属性为false不生效。<br/>初始值：false，不开启边缘渐隐效果。|
|options|[FadingEdgeOptions](#class-fadingedgeoptions)|是|-|边缘渐隐参数对象。可以通过该对象定义边缘渐隐效果属性，比如设置渐隐长度。|

### func flingSpeedLimit(Float64)

```cangjie
public func flingSpeedLimit(speedLimit: Float64): This
```

**功能：** 限制跟手滑动结束后，Fling动效开始时的最大初始速度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|speedLimit|Float64|是|-|Fling动效开始时的最大初始速度。<br> 初始值：9000.0 <br> 单位：vp/s <br> 取值范围：(0, +∞)，设置为小于等于0的值时，按初始值处理。|

### func friction(Float64)

```cangjie
public func friction(value: Float64): This
```

**功能：** 设置摩擦系数，手动划动滚动区域时生效，只对惯性滚动过程有影响，对惯性滚动过程中的链式效果有间接影响。设置为小于等于0的值时，按初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|摩擦系数。<br>初始值：非可穿戴设备为0.75，可穿戴设备为0.9。<br> 取值范围：(0, +∞)，设置为小于等于0的值时，按初始值处理。|

### func nestedScroll(NestedScrollOptions)

```cangjie
public func nestedScroll(value: NestedScrollOptions): This
```

**功能：** 设置向前和向后两个方向上的嵌套滚动模式，实现与父组件的滚动联动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[NestedScrollOptions](#class-nestedscrolloptions)|是|-|嵌套滚动选项。|