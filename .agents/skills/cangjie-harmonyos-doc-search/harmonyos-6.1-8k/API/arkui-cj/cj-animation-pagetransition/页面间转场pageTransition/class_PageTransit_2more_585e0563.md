## class PageTransitionEnter

```cangjie
public class PageTransitionEnter <: CommonTransition {
    public init(
        routeType!: ?RouteType = Option.None,
        duration!: ?Int32 = None,
        curve!: ?Curve = None,
        delay!: ?Int32 = None
    )
}
```

**功能：** 当前页面的自定义入场动效类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [CommonTransition](#class-commontransition)

### init(?RouteType, ?Int32, ?Curve, ?Int32)

```cangjie
public init(
    routeType!: ?RouteType = Option.None,
    duration!: ?Int32 = None,
    curve!: ?Curve = None,
    delay!: ?Int32 = None
)
```

**功能：** 创建当前页面的自定义入场动效对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|routeType|?[RouteType](#enum-routetype) |否|Option.None|**命名参数。** 页面转场效果生效的路由类型。<br>初始值：RouteType.None。|
|duration|?Int32|否|None|**命名参数。** 动画的时长。<br>单位：毫秒。<br>取值范围：[0, +∞)。<br>初始值：1000。|
|curve|?[Curve](./cj-common-types.md#enum-curve)|否|None|**命名参数。** 动画曲线。<br>Curve.Linear|
|delay|?Int32|否|None|**命名参数。** 动画延迟时长。<br>单位：毫秒。<br>初始值：1000。|

### func onEnter(?PageTransitionCallback)

```cangjie
public func onEnter(event: ?PageTransitionCallback)
```

**功能：** 逐帧回调，直到入场动画结束，转场进度从0变化到1。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|?[PageTransitionCallback](#type-pagetransitioncallback)|是|-|入场动画的逐帧回调直到入场动画结束，转场进度从0变化到1。|

## class PageTransitionExit

```cangjie
public class PageTransitionExit <: CommonTransition {
    public init(
        routeType!: ?RouteType = Option.None,
        duration!: ?Int32 = None,
        curve!: ?Curve = None,
        delay!: ?Int32 = None
    )
}
```

**功能：** 当前页面的自定义退场动效类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [CommonTransition](#class-commontransition)

### init(?RouteType, ?Int32, ?Curve, ?Int32)

```cangjie
public init(
    routeType!: ?RouteType = Option.None,
    duration!: ?Int32 = None,
    curve!: ?Curve = None,
    delay!: ?Int32 = None
)
```

**功能：** 创建当前页面的自定义退场动效对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|routeType|?[RouteType](#enum-routetype) |否|Option.None|**命名参数。** 页面转场效果生效的路由类型。<br>初始值：RouteType.None。|
|duration|?Int32|否|None|**命名参数。** 动画的时长。<br>单位：毫秒。<br>取值范围：[0, +∞)。<br>初始值：1000。|
|curve|?[Curve](./cj-common-types.md#enum-curve)|否|None|**命名参数。** 动画曲线。<br>Curve.Linear|
|delay|?Int32|否|None|**命名参数。** 动画延迟时长。<br>单位：毫秒。<br>初始值：1000。|

### func onExit(?PageTransitionCallback)

```cangjie
public func onExit(event: ?PageTransitionCallback)
```

**功能：** 逐帧回调，直到出场动画结束，转场进度从0变化到1。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|?[PageTransitionCallback](#type-pagetransitioncallback)|是|-|出场动画的逐帧回调直到出场动画结束，转场进度从0变化到1。|