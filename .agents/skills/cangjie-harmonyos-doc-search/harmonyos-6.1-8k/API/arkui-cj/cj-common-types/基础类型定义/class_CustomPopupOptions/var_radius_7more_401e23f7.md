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

**功能：** 弹出窗口阴影的样式。

**类型：** ?[ShadowStyle](#enum-shadowstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var backgroundBlurStyle

```cangjie
public var backgroundBlurStyle: ?BlurStyle
```

**功能：** 弹出窗口的背景模糊样式。

**类型：** ?[BlurStyle](#enum-blurstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var focusable

```cangjie
public var focusable: ?Bool
```

**功能：** 设置气泡弹出后是否获焦。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var transition

```cangjie
public var transition: Option<TransitionEffect>
```

**功能：** 自定义设置popup弹窗显示和退出的动画效果。

**类型：** Option<[TransitionEffect](./cj-animation-transition.md#class-transitioneffect)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var onWillDismiss

```cangjie
public var onWillDismiss: Option<(DismissPopupAction) -> Unit>
```

**功能：** 设置拦截退出事件且执行回调函数。

> **说明：**
>
> 在onWillDismiss回调中，不能再做onWillDismiss拦截。

**类型：** Option<([DismissPopupAction](#class-dismisspopupaction)) -> Unit>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var followTransformOfTarget

```cangjie
public var followTransformOfTarget: ?Bool
```

**功能：** 气泡绑定的宿主组件或其宿主组件的父容器添加了旋转、缩放等变换时，气泡是否能显示在对应变化后的位置上。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22