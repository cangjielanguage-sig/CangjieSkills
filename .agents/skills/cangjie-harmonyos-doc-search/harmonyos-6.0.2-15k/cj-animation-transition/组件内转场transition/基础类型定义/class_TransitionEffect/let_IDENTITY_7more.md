#### let IDENTITY

```cangjie
public static let IDENTITY: TransitionEffect
```

**功能：** 禁用转场效果。

**类型：** [TransitionEffect](#class-transitioneffect)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### let OPACITY

```cangjie
public static let OPACITY: TransitionEffect
```

**功能：** 为组件添加透明度转场效果，出现时透明度从0到1、消失时透明度从1到0，相当于TransitionEffect.opacity(0.0)。

**类型：** [TransitionEffect](#class-transitioneffect)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### let SLIDE

```cangjie
public static let SLIDE: TransitionEffect
```

**功能：** 设置从START边滑入，END边滑出。即在LTR模式下，从左侧滑入，右侧滑出；在RTL模式下，从右侧滑入，左侧滑出。相当于TransitionEffect.asymmetric(TransitionEffect.move(TransitionEdge.START), TransitionEffect.move(TransitionEdge.END))。

**类型：** [TransitionEffect](#class-transitioneffect)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### let SLIDE_SWITCH

```cangjie
public static let SLIDE_SWITCH: TransitionEffect
```

**功能：** 指定出现时从右先缩小再放大侧滑入、消失时从左侧先缩小再放大滑出的转场效果。自带动画参数，也可覆盖动画参数，自带的动画参数时长600ms，指定动画曲线cubicBezierCurve(0.24, 0.0, 0.50, 1.0)，最小缩放比例为0.8。

**类型：** [TransitionEffect](#class-transitioneffect)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func animation(AnimateParam)

```cangjie
public func animation(param: AnimateParam): TransitionEffect
```

**功能：** 指定该TransitionEffect的动画参数。

> **说明：**
>
> 该参数只用来指定动画参数，其入参AnimateParam的onFinish回调不生效。如果通过combine进行TransitionEffect的组合，前一TransitionEffect的动画参数也可用于后一TransitionEffect。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|param|[AnimateParam](./cj-animation-animateto.md#class-animateparam)|是|-|动画效果参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[TransitionEffect](#class-transitioneffect)|组件转场效果。|

#### static func asymmetric(TransitionEffect, TransitionEffect)

```cangjie
public static func asymmetric(appear: TransitionEffect, disappear: TransitionEffect): TransitionEffect
```

**功能：** 用于指定非对称的转场效果。

> **说明：**
>
> 如不通过asymmetric函数构造TransitionEffect，则表明该效果在组件出现和消失时均生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|appear|[TransitionEffect](#class-transitioneffect)|是|-|指定出现的转场效果。|
|disappear|[TransitionEffect](#class-transitioneffect)|是|-|指定消失的转场效果。|

**返回值：**

|类型|说明|
|:----|:----|
|[TransitionEffect](#class-transitioneffect)|组件转场效果。|

#### func combine(TransitionEffect)

```cangjie
public func combine(effect: TransitionEffect): TransitionEffect
```

**功能：** 用于对TransitionEffect进行链式组合，以形成包含多种转场效果的TransitionEffect。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|effect|[TransitionEffect](#class-transitioneffect)|是|-|用于链式组合的组件转场效果。|

**返回值：**

|类型|说明|
|:----|:----|
|[TransitionEffect](#class-transitioneffect)|组件转场效果。|