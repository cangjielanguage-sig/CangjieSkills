### class ScrollableBarModeOptions

```cangjie
public class ScrollableBarModeOptions {
    public let margin: Length
    public let nonScrollableLayoutStyle: LayoutStyle
    public init( margin!: Length = 0.0.vp, nonScrollableLayoutStyle!: LayoutStyle = LayoutStyle.ALWAYS_CENTER)
}
```

**功能：** Scrollable模式下的TabBar的布局样式对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let margin

```cangjie
public let margin: Length
```

**功能：** Scrollable模式下的TabBar的左右边距（不支持百分比设置）。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let nonScrollableLayoutStyle

```cangjie
public let nonScrollableLayoutStyle: LayoutStyle
```

**功能：** Scrollable模式下不滚动时的页签排布方式。

**类型：** [LayoutStyle](#enum-layoutstyle)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Length, LayoutStyle)

```cangjie
public init( margin!: Length = 0.0.vp, nonScrollableLayoutStyle!: LayoutStyle = LayoutStyle.ALWAYS_CENTER)
```

**功能：** 构造一个ScrollableBarModeOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|margin|[Length](cj-common-types.md#interface-length)|否|0.0.vp| **命名参数。** Scrollable模式下的TabBar的左右边距（不支持百分比设置）。|
|nonScrollableLayoutStyle|[LayoutStyle](#enum-layoutstyle)|否|LayoutStyle.ALWAYS_CENTER| **命名参数。** Scrollable模式下不滚动时的页签排布方式。|

### class TabContentAnimatedTransition

```cangjie
public class TabContentAnimatedTransition {
    public TabContentAnimatedTransition(
        public let timeout!: Int32 = 1000,
        public let transition!: (TabContentTransitionProxy) -> Unit
    )
}
```

**功能：** Tabs自定义切换动画相关信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let timeout

```cangjie
public let timeout: Int32 = 1000
```

**功能：** Tabs自定义切换动画超时时间。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

#### let transition

```cangjie
public let transition:(TabContentTransitionProxy) -> Unit
```

**功能：** 自定义切换动画具体内容。

**类型：** ([TabContentTransitionProxy](#class-tabcontenttransitionproxy))->Unit

**读写能力：** 只读

**起始版本：** 19

#### TabContentAnimatedTransition(Int32, (TabContentTransitionProxy) -> Unit)

```cangjie
public TabContentAnimatedTransition(
    public let timeout!: Int32 = 1000,
    public let transition!: (TabContentTransitionProxy) -> Unit
)
```

**功能：** 构造一个TabContentAnimatedTransition对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|timeout|Int32|否|1000| **命名参数。** Tabs自定义切换动画超时时间。从自定义动画开始切换计时，如果到达该时间后，开发者仍未调用[TabContentTransitionProxy](#class-tabcontenttransitionproxy)的finishTransition接口通知Tabs组件自定义动画结束，那么组件就会认为此次自定义动画已结束，直接执行后续操作。单位ms。初始值：1000。取值范围：[0, +∞)。|
|transition|([TabContentTransitionProxy](#class-tabcontenttransitionproxy))->Unit|是|-| **命名参数。** 自定义切换动画具体内容。|