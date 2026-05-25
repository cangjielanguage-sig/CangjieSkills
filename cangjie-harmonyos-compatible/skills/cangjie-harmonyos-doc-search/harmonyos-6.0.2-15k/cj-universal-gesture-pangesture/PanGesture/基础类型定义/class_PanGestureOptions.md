### class PanGestureOptions

```cangjie
public class PanGestureOptions {
    public init(fingers!: Int32 = 1, direction!: PanDirection = PanDirection.All, distance!: Float64 = 5.0)
}
```

**功能：** 通过PanGestureOptions对象接口可以动态修改平移手势识别器的属性，从而避免通过状态变量修改属性（状态变量修改会导致UI刷新）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Int32, PanDirection, Float64)

```cangjie
public init(fingers!: Int32 = 1, direction!: PanDirection = PanDirection.All, distance!: Float64 = 5.0)
```

**功能：** 创建一个PanGestureOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fingers|Int32|否|1| **命名参数。** 用于指定触发滑动的最少手指数，最小为1指，最大取值为10指。<br/> 取值范围：[1,10]。<br/> **说明：** <br/> 当设置的值小于1或不设置时，会被转化为1。|
|direction|[PanDirection](#enum-pandirection)|否|PanDirection.All|用于指定触发滑动的手势方向，此枚举值支持逻辑与（&）和逻辑或（\| **命名参数。** ）运算。|
|distance|Float64|否|5.0| **命名参数。** 用于指定触发滑动手势事件的最小拖动距离，单位为px。 <br/> **说明：** <br/> Tabs组件滑动与该滑动手势事件同时存在时，可将distance的值设为1，使滑动更灵敏，避免造成事件错乱。<br/> 当设定的值小于0时，按5.0处理。|

#### func setDirection(PanDirection)

```cangjie
public func setDirection(value: PanDirection): Unit
```

**功能：** 设置滑动方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[PanDirection](#enum-pandirection)|是|-|用于指定触发滑动的手势方向，此枚举值支持逻辑与和逻辑或运算。|

#### func setDistance(Float64)

```cangjie
public func setDistance(value: Float64): Unit
```

**功能：** 设置触发滑动手势事件的最小滑动距离，单位为px。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|用于指定触发滑动手势事件的最小拖动距离，单位为px。**说明：** <br/> Tabs组件滑动与该滑动手势事件同时存在时，可将distance的值设为1，使滑动更灵敏，避免造成事件错乱。<br/> 当设定的值小于0时，按5.0处理。|

#### func setFingers(Int32)

```cangjie
public func setFingers(value: Int32): Unit
```

**功能：** 设置触发滑动的最少手指数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|用于指定触发滑动的最少手指数，最小为1指，最大取值为10指。 <br/> 取值范围：[1,10]。<br/> **说明：** <br/> 当设置的值小于1或不设置时，会被转化为1。|