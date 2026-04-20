### var arrowWidth

```cangjie
public var arrowWidth: ?Length
```

**功能：** 箭头的宽度。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var arrowHeight

```cangjie
public var arrowHeight: ?Length
```

**功能：** 箭头的高度。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var radius

```cangjie
public var radius: ?Length
```

**功能：** 弹出窗口的圆角。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var shadow

```cangjie
public var shadow: ?ShadowStyle
```

**功能：** 设置气泡阴影。

**类型：** ?[ShadowStyle](#enum-shadowstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var backgroundBlurStyle

```cangjie
public var backgroundBlurStyle: ?BlurStyle
```

**功能：** 设置气泡模糊背景参数。

**类型：** ?[BlurStyle](#enum-blurstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var transition

```cangjie
public var transition: ?TransitionEffect
```

**功能：** 自定义设置popup弹窗显示和退出的动画效果。

> **说明：**
>
> - 如果不设置，则使用默认的显示/退出动效。
> - 显示动效中按back键，打断显示动效，执行退出动效，动画效果为显示动效与退出动效的曲线叠加后的效果。
> - 退出动效中按back键，不会打断退出动效，退出动效继续执行，back键不被响应。

**类型：** ?[TransitionEffect](./cj-animation-transition.md#class-transitioneffect)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var onWillDismiss

```cangjie
public var onWillDismiss: ?(DismissPopupAction) -> Unit
```

**功能：** 设置拦截退出事件且执行回调函数。

> **说明：**
>
> 在onWillDismiss回调中，不能再做onWillDismiss拦截。

**类型：** ?([DismissPopupAction](#class-dismisspopupaction)) -> Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var followTransformOfTarget

```cangjie
public var followTransformOfTarget: ?Bool
```

**功能：** 气泡绑定的宿主组件或其宿主组件的父容器添加了旋转、缩放等变换时，设置气泡是否能显示在对应变化后的位置上。默认值：false。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22