### init(Rectangle, DialogAlignment, Offset, Bool, Bool, Bool, ResourceColor, TransitionEffect, () -> Unit, () -> Unit, () -> Unit, () -> Unit, KeyboardAvoidMode, Bool, HoverModeAreaType)

```cangjie
public init(
    maskRect!: Rectangle = Rectangle(x: 0.vp, y: 0.vp, width: 100.percent, height: 100.percent),
    alignment!: DialogAlignment = DialogAlignment.Default,
    offset!: Offset = Offset(0.vp, 0.vp),
    isModal!: Bool = true,
    showInSubWindow!: Bool = false,
    autoCancel!: Bool = true,
    maskColor!: ResourceColor = Color(0x33000000),
    transition!: TransitionEffect = TransitionEffect.OPACITY,
    onDidAppear!: () -> Unit = {=>},
    onDidDisappear!: () -> Unit = {=>},
    onWillAppear!: () -> Unit = {=>},
    onWillDisappear!: () -> Unit = {=>},
    keyboardAvoidMode!: KeyboardAvoidMode = KeyboardAvoidMode.Default,
    enableHoverMode!: Bool = false,
    hoverModeArea!: HoverModeAreaType = HoverModeAreaType.BottomScreen
)
```

**功能：** BaseDialogOptions构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|maskRect|[Rectangle](./cj-common-types.md#class-rectangle)|否|Rectangle(x: 0.vp, y: 0.vp, width: 100.percent, height: 100.percent)| **命名参数。** 对话框遮罩区域。|
|alignment|[DialogAlignment](./cj-common-types.md#enum-dialogalignment)|否|DialogAlignment.Default| **命名参数。** 对话框在屏幕上的对齐方式。|
|offset|[Offset](./cj-common-types.md#class-offset)|否|Offset(0.vp, 0.vp)| **命名参数。** 对话框偏移量。|
|isModal|Bool|否|true| **命名参数。** 是否为模态对话框。|
|showInSubWindow|Bool|否|false| **命名参数。** 是否在子窗口中显示。|
|autoCancel|Bool|否|true| **命名参数。** 是否允许用户点击遮罩层退出。|
|maskColor|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color(0x33000000)| **命名参数。** 自定义对话框遮罩颜色。|
|transition|[TransitionEffect](./cj-animation-transition.md#class-transitioneffect)|否|TransitionEffect.OPACITY| **命名参数。** 自定义对话框打开/关闭时的过渡参数。|
|onDidAppear|() -> Unit|否|{=>}| **命名参数。** 对话框出现时的回调函数。|
|onDidDisappear|() -> Unit|否|{=>}| **命名参数。** 对话框消失时的回调函数。|
|onWillAppear|() -> Unit|否|{=>}| **命名参数。** 对话框打开动画开始前的回调函数。|
|onWillDisappear|() -> Unit|否|{=>}| **命名参数。** 对话框关闭动画开始前的回调函数。|
|keyboardAvoidMode|[KeyboardAvoidMode](#enum-keyboardavoidmode)|否|KeyboardAvoidMode.Default| **命名参数。** 自定义对话框的键盘避免模式。|
|enableHoverMode|Bool|否|false| **命名参数。** 是否响应悬停模式。|
|hoverModeArea|[HoverModeAreaType](#enum-hovermodeareatype)|否|HoverModeAreaType.BottomScreen| **命名参数。** 悬停模式下对话框的显示区域。|