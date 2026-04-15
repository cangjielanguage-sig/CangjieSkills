## class CustomPopupOptions

```cangjie
public class CustomPopupOptions {
    public var builder: CustomBuilder
    public var placement: ?Placement
    public var backgroundColor: ?Color
    public var enableArrow: ?Bool
    public var autoCancel: ?Bool
    public var onStateChange: Option<(PopupStateChangeParam) -> Unit>
    public var popupColor: ?Color
    public var arrowOffset: ?Length
    public var showInSubWindow: ?Bool
    public var mask: ?Color
    public var targetSpace: ?Length
    public var offset: ?Position
    public var width: ?Length
    public var arrowPointPosition: Option<ArrowPointPosition>
    public var arrowWidth: ?Length
    public var arrowHeight: ?Length
    public var radius: ?Length
    public var shadow: ?ShadowStyle
    public var backgroundBlurStyle: ?BlurStyle
    public var focusable: ?Bool
    public var transition: Option<TransitionEffect>
    public var onWillDismiss: Option<(DismissPopupAction) -> Unit>
    public var followTransformOfTarget: ?Bool
    public init(
        builder!: () -> Unit,
        placement!: ?Placement = Option.None,
        popupColor!: ?Color = None,
        enableArrow!: ?Bool = None,
        autoCancel!: ?Bool = None,
        onStateChange!: Option<(PopupStateChangeParam) -> Unit> = Option.None,
        showInSubWindow!: ?Bool = None,
        backgroundColor!: ?Color = None,
        arrowOffset!: ?Length = None,
        mask!: ?Color = None,
        targetSpace!: ?Length = None,
        offset!: ?Position = None,
        width!: ?Length = None,
        arrowPointPosition!: ?ArrowPointPosition = None,
        arrowWidth!: ?Length = None,
        arrowHeight!: ?Length = None,
        radius!: ?Length = None,
        shadow!: ?ShadowStyle = None,
        backgroundBlurStyle!: ?BlurStyle = Option.None,
        focusable!: ?Bool = None,
        transition!: Option<TransitionEffect> = Option.None,
        onWillDismiss!: Option<(DismissPopupAction) -> Unit> = None,
        followTransformOfTarget!: ?Bool = None
    )
}
```

**功能：** 弹出弹窗的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var builder

```cangjie
public var builder: CustomBuilder
```

**功能：** 提示气泡内容的构造器。

> **说明：**
>
> popup为通用属性，自定义popup中不支持再次弹出popup。对builder下的第一层容器组件不支持使用position属性，如果使用将导致气泡不显示。builder中若使用自定义组件，自定义组件的aboutToAppear和aboutToDisappear生命周期与popup弹窗的显隐无关，不能使用其生命周期判断popup弹窗的显隐。

**类型：** [CustomBuilder](#type-custombuilder)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var placement

```cangjie
public var placement: ?Placement
```

**功能：** 设置气泡组件优先显示的位置，当前位置显示不下时，会自动调整位置

**类型：** ?[Placement](#enum-placement)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var backgroundColor

```cangjie
public var backgroundColor: ?Color
```

**功能：** 设置提示气泡背景颜色。

**类型：** ?[Color](./cj-common-types.md#class-color)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var enableArrow

```cangjie
public var enableArrow: ?Bool
```

**功能：** 设置是否显示箭头。如果箭头所在方位侧的气泡长度不足以显示下箭头，则会默认不显示箭头。例如placement设置为Left，此时如果气泡高度小于箭头的宽度（32.vp）与气泡圆角两倍（48.vp）之和（80.vp），则实际不会显示箭头。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var autoCancel

```cangjie
public var autoCancel: ?Bool
```

**功能：** 页面有操作时，设置是否自动关闭气泡。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22