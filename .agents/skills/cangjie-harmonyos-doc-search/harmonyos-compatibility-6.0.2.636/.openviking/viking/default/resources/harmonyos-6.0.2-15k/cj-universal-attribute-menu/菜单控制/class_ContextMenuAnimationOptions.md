## class ContextMenuAnimationOptions

```cangjie
public open class ContextMenuAnimationOptions {
    public ContextMenuAnimationOptions(
        public var scale!: ?(Float64, Float64) = None,
        public var transition!: ?TransitionEffect = None,
        public var hoverScale!: ?(Float64, Float64) = None
    )
}
```

**功能：** 控制长按预览显示动画开始倍率和结束倍率（相对预览原图比例）参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var hoverScale

```cangjie
public var hoverScale: ?(Float64, Float64) = None
```

**功能：** 设置预览自定义长按场景下，浮起原组件截图的缩放动画开始和结束时相对预览原图缩放比例，且有与预览图的切换的过渡动效。

**类型：** ?(Float64, Float64)

**读写能力：** 可读写

**起始版本：** 19

### var scale

```cangjie
public var scale: ?(Float64, Float64) = None
```

**功能：** 动画开始和结束时相对预览原图缩放比例。

**类型：** ?(Float64, Float64)

**读写能力：** 可读写

**起始版本：** 19

### var transition

```cangjie
public var transition: ?TransitionEffect = None
```

**功能：** 设置菜单显示和退出的过渡效果。

**类型：** ?[TransitionEffect](./cj-animation-transition.md#class-transitioneffect)

**读写能力：** 可读写

**起始版本：** 19

### ContextMenuAnimationOptions(?(Float64,Float64), ?TransitionEffect, ?(Float64,Float64))

```cangjie
public ContextMenuAnimationOptions(
    public var scale!: ?(Float64, Float64) = None,
    public var transition!: ?TransitionEffect = None,
    public var hoverScale!: ?(Float64, Float64) = None
)
```

**功能：** 创建 ContextMenuAnimationOptions 对象。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scale|?(Float64, Float64)|否|None| **命名参数。** 动画开始和结束时相对预览原图缩放比例。<br> **说明：** 缩放比例需要根据实际开发场景设置，建议设置值为小于预览图宽度或布局的最大限制。|
|transition|?[TransitionEffect](./cj-animation-transition.md#class-transitioneffect)|否|None| **命名参数。** 菜单显示和退出的过渡效果。<br> **说明：** 菜单退出动效过程中，进行横竖屏切换，菜单会避让。二级菜单不继承自定义动效。弹出过程可以点击二级菜单，退出动效执行过程不允许点击二级菜单。详细描述见TransitionEffect对象说明。|
|hoverScale|?(Float64, Float64)|否|None| **命名参数。** 预览自定义长按场景下，浮起原组件截图的缩放动画开始和结束时相对预览原图缩放比例，且有与预览图的切换的过渡动效。<br> **说明：** 倍率设置参数小于等于0时，不生效。<br> 设置transition接口时，不生效。<br>使用此接口且同时使用scale接口时，scale接口起始值不生效。<br> 为保障最佳体验，最终预览图尺寸不建议小于原组件截图尺寸。当前预览动效宽高会受组件截图和自定义预览大小影响，请根据实际使用情况自行保障展示效果。|