### static func rotate(?RotateOptions)

```cangjie
public static func rotate(options: ?RotateOptions): TransitionEffect
```

**功能：** 设置组件转场时的旋转效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|?[RotateOptions](#class-rotateoptions)|是|-|设置组件转场时的旋转效果，为插入时起点和删除时终点的值。|

**返回值：**

|类型|说明|
|:----|:----|
|[TransitionEffect](#class-transitioneffect)|返回转场效果。|

### static func move(TransitionEdge)

```cangjie
public static func move(edge: TransitionEdge): TransitionEffect
```

**功能：** 指定组件转场时从屏幕边缘滑入和滑出的效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|edge|[TransitionEdge](#enum-transitionedge)|是|-|指定组件转场时从屏幕边缘滑入和滑出的效果，本质为平移效果，为插入时起点和删除时终点的值。|

**返回值：**

|类型|说明|
|:----|:----|
|[TransitionEffect](#class-transitioneffect)|返回转场效果。|

### static func asymmetric(TransitionEffect, TransitionEffect)

```cangjie
public static func asymmetric(appear: TransitionEffect, disappear: TransitionEffect): TransitionEffect
```

**功能：** 用于指定非对称的转场效果。

> **说明：**
>
> 如不通过asymmetric函数构造TransitionEffect，则表明该效果在组件出现和消失时均生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|appear|[TransitionEffect](#class-transitioneffect)|是|-|指定出现的转场效果。<br>如不通过asymmetric函数构造TransitionEffect，则表明该效果在组件出现和消失时均生效。|
|disappear|[TransitionEffect](#class-transitioneffect)|是|-|指定消失的转场效果。<br>如不通过asymmetric函数构造TransitionEffect，则表明该效果在组件出现和消失时均生效。|

**返回值：**

|类型|说明|
|:----|:----|
|[TransitionEffect](#class-transitioneffect)|返回转场效果。|

### func animation(?AnimateParam)

```cangjie
public func animation(value: ?AnimateParam): TransitionEffect
```

**功能：** 指定该TransitionEffect的动画参数。

> **说明：**
>
> 该参数只用来指定动画参数，其入参AnimateParam的onFinish回调不生效。如果通过combine进行TransitionEffect的组合，前一TransitionEffect的动画参数也可用于后一TransitionEffect。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[AnimateParam](./cj-common-types.md#class-animateparam)|是|-|动画效果参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[TransitionEffect](#class-transitioneffect)|返回转场效果。|

### func combine(TransitionEffect)

```cangjie
public func combine(transitionEffect: TransitionEffect): TransitionEffect
```

**功能：** 用于对TransitionEffect进行链式组合，以形成包含多种转场效果的TransitionEffect。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|transitionEffect|[TransitionEffect](#class-transitioneffect)|是|-|被组合的过渡效果。|

**返回值：**

|类型|说明|
|:----|:----|
|[TransitionEffect](#class-transitioneffect)|返回转场效果。|