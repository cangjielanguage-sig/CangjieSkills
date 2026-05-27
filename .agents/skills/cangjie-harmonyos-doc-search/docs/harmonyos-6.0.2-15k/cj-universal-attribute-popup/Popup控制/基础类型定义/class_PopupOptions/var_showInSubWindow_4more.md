#### var showInSubWindow

```cangjie
public var showInSubWindow: Bool = false
```

**功能：** 设置是否在子窗口显示气泡，默认值为false。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var targetSpace

```cangjie
public var targetSpace: Length = 0.vp
```

**功能：** 设置popup与目标的间隙。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var transition

```cangjie
public var transition: Option<TransitionEffect> = Option.None
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

**起始版本：** 19

#### var width

```cangjie
public var width: Length = 0.vp
```

**功能：** 设置弹窗宽度。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19