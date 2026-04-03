## class PageTransitionEnter

```cangjie
public class PageTransitionEnter <: PageTransition {
    public init(value: PageTransitionOptions)
}
```

**功能：** 当前页面的自定义入场动效类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- [PageTransition](#class-pagetransition)

### init(PageTransitionOptions)

```cangjie
public init(value: PageTransitionOptions)
```

**功能：** 创建当前页面的自定义入场动效对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[PageTransitionOptions](#class-pagetransitionoptions)|是|-|配置入场动效的参数。|

### func onEnter((RouteType, Float64) -> Unit)

```cangjie
public func onEnter(event: (RouteType, Float64)->Unit)
```

**功能：** 逐帧回调，直到入场动画结束，progress从0变化到1。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|([RouteType](#enum-routetype),Float64)->Unit|是|-|入场动画的逐帧回调直到入场动画结束，progress从0变化到1。|

## class PageTransitionExit

```cangjie
public class PageTransitionExit <: PageTransition {
    public init(value: PageTransitionOptions)
}
```

**功能：** 当前页面的自定义退场动效类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- [PageTransition](#class-pagetransition)

### init(PageTransitionOptions)

```cangjie
public init(value: PageTransitionOptions)
```

**功能：** 创建当前页面的自定义退场动效对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[PageTransitionOptions](#class-pagetransitionoptions)|是|-|配置退场动效的参数。|

### func onExit((RouteType,Float64) -> Unit)

```cangjie
public func onExit(event: (RouteType, Float64)->Unit)
```

**功能：** 逐帧回调，直到出场动画结束，progress从0变化到1。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|([RouteType](#enum-routetype),Float64)->Unit|是|-|出场动画的逐帧回调直到入场动画结束，progress从0变化到1。|