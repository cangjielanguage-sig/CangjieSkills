### class ScrollAnimationOptions

```cangjie
public class ScrollAnimationOptions {
    public var duration: ?Float64
    public var curve: ?Curve
    public var canOverScroll: ?Bool
    public init(
        duration!: ?Float64 = None,
        curve!: ?Curve = None,
        canOverScroll!: ?Bool = None
    )
}
```

**功能：** 提供自定义滚动动画的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var duration

```cangjie
public var duration: ?Float64
```

**功能：** 滚动持续时间。

**类型：** ?Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var curve

```cangjie
public var curve: ?Curve
```

**功能：** 滚动曲线。

**类型：** ?[Curve](./cj-common-types.md#enum-curve)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var canOverScroll

```cangjie
public var canOverScroll: ?Bool
```

**功能：** 是否启用越界滚动。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Float64, ?Curve, ?Bool)

```cangjie
public init(
    duration!: ?Float64 = None,
    curve!: ?Curve = None,
    canOverScroll!: ?Bool = None
)
```

**功能：** 构造一个自定义滚动动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|duration|?Float64|否|None|**命名参数。** 滚动持续时间。初始值：1000.0。|
|curve|?[Curve](./cj-common-types.md#enum-curve)|否|None|**命名参数。** 滚动曲线。初始值：Curve.Ease。|
|canOverScroll|?Bool|否|None|**命名参数。** 是否启用越界滚动。初始值：false。|

### class NestedScrollOptions

```cangjie
public class NestedScrollOptions {
    public var scrollForward: ?NestedScrollMode
    public var scrollBackward: ?NestedScrollMode
    public init(scrollForward: ?NestedScrollMode, scrollBackward: ?NestedScrollMode)
}
```

**功能：** 提供自定义滚动嵌套的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var scrollForward

```cangjie
public var scrollForward: ?NestedScrollMode
```

**功能：** 自定义滚动嵌套中的向前方向。

**类型：** ?[NestedScrollMode](./cj-common-types.md#enum-nestedscrollmode)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var scrollBackward

```cangjie
public var scrollBackward: ?NestedScrollMode
```

**功能：** 自定义滚动嵌套中的向后方向。

**类型：** ?[NestedScrollMode](./cj-common-types.md#enum-nestedscrollmode)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?NestedScrollMode, ?NestedScrollMode)

```cangjie
public init(scrollForward: ?NestedScrollMode, scrollBackward: ?NestedScrollMode)
```

**功能：** 提供自定义滚动嵌套的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scrollForward|?[NestedScrollMode](./cj-common-types.md#enum-nestedscrollmode)|是|-|自定义滚动嵌套中的向前方向。初始值：NestedScrollMode.SelfOnly。|
|scrollBackward|?[NestedScrollMode](./cj-common-types.md#enum-nestedscrollmode)|是|-|自定义滚动嵌套中的向后方向。初始值：NestedScrollMode.SelfOnly。|