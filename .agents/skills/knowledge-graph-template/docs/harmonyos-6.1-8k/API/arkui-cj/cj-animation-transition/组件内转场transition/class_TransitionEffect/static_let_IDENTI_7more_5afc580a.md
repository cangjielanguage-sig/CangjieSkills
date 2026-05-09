### static let IDENTITY

```cangjie
public static let IDENTITY: TransitionEffect
```

**功能：** 禁用转场效果。

**类型：** [TransitionEffect](#class-transitioneffect)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### static let OPACITY

```cangjie
public static let OPACITY: TransitionEffect = TransitionEffect.opacity(0.0)
```

**功能：** 为组件添加透明度转场效果，出现时透明度从0到1、消失时透明度从1到0，相当于TransitionEffect.opacity(0.0)。

**类型：** [TransitionEffect](#class-transitioneffect)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### static let SLIDE

```cangjie
public static let SLIDE: TransitionEffect = TransitionEffect.asymmetric(TransitionEffect.move(TransitionEdge.Start),
        TransitionEffect.move(TransitionEdge.End))
```

**功能：** 相当于TransitionEffect.asymmetric(TransitionEffect.move(TransitionEdge.Start), TransitionEffect.move(TransitionEdge.End))。从Start边滑入，End边滑出。即在LTR模式下，从左侧滑入，右侧滑出；在RTL模式下，从右侧滑入，左侧滑出。

**类型：** [TransitionEffect](#class-transitioneffect)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### static let SLIDE_SWITCH

```cangjie
public static let SLIDE_SWITCH: TransitionEffect
```

**功能：** 指定出现时从右侧先缩小再放大滑入、消失时从左侧先缩小再放大滑出的转场效果。自带动画参数，也可覆盖动画参数，自带的动画参数时长600ms，指定动画曲线cubicBezierCurve(0.24, 0.0, 0.50, 1.0)，最小缩放比例为0.8。

**类型：** [TransitionEffect](#class-transitioneffect)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### static func opacity(Float64)

```cangjie
public static func opacity(alpha: Float64): TransitionEffect
```

**功能：** 设置组件转场时的透明度效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|alpha|Float64|是|-|设置组件转场时的透明度效果，为插入时起点和删除时终点的值。<br>取值范围：[0.0, 1.0]。<br> **说明：** <br>设置小于0.0的非法值按0.0处理，大于1.0的非法值按1.0处理。|

**返回值：**

|类型|说明|
|:----|:----|
|[TransitionEffect](#class-transitioneffect)|返回转场效果。|

### static func translate(TranslateOptions)

```cangjie
public static func translate(options: TranslateOptions): TransitionEffect
```

**功能：** 设置组件转场时的平移效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[TranslateOptions](#class-translateoptions)|是|-|设置组件转场时的平移效果，为插入时起点和删除时终点的值。|

**返回值：**

|类型|说明|
|:----|:----|
|[TransitionEffect](#class-transitioneffect)|返回转场效果。|

### static func scale(?ScaleOptions)

```cangjie
public static func scale(options: ?ScaleOptions): TransitionEffect
```

**功能：** 设置组件转场时的缩放效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|?[ScaleOptions](#class-scaleoptions)|是|-|	组件转场时的缩放效果，为插入时起点和删除时终点的值。设置的缩放值在组件当前的scale属性上进行叠加，如组件当前scale值为0.8，当转场缩放值设置为0.5时，组件入场动画的缩放值将从0.4开始执行。|

**返回值：**

|类型|说明|
|:----|:----|
|[TransitionEffect](#class-transitioneffect)|返回转场效果。|