## class GestureHandler

```cangjie
public open class GestureHandler {}
```

**功能：** 手势对象的基型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### func tag(String)

```cangjie
public func tag(tag: String): This
```

**功能：** 设置手势处理器的标志。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|tag|String|是|-|设置手势处理器标志。|

## class TapGestureHandler

```cangjie
public class TapGestureHandler <: GestureHandler {}
```

**功能：** 点击手势处理器对象类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [GestureHandler](#class-gesturehandler)

### init(Int32, Int32)

```cangjie
public init(count!: Int32 = 1, fingers!: Int32 = 1)
```

**功能：** 创建一个点击手势处理器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|count|Int32|否|1| **命名参数。** 识别的连续点击次数。当设置的值小于1或不设置时，会被转化为默认值。<br/>**说明：** <br/> 1. 当配置多击时，上一次的最后一根手指抬起和下一次的第一根手指按下的超时时间为300毫秒。<br/> 2. 当上次点击的位置与当前点击的位置距离超过60vp时，手势识别失败。|
|fingers|Int32|否|1| **命名参数。** 触发点击的手指数，最小为1指， 最大为10指。当设置小于1的值或不设置时，会被转化为默认值。<br/>**说明：** <br/> 1. 当配置多指时，第一根手指按下后300毫秒内未有足够的手指数按下，手势识别失败；手指抬起时，抬起后剩余的手指数小于阈值时开始计时，如300ms内未全部抬起则手势识别失败。<br/>2. 实际点击手指数超过配置值，手势识别成功。|

### func onAction((GestureEvent) -> Unit)

```cangjie
public func onAction(callback: (GestureEvent) -> Unit): This
```

**功能：** Tap手势识别成功触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureEvent](./cj-universal-gesture-bind.md#class-gestureevent))->Unit|是|-|Tap手势识别成功触发该回调。|