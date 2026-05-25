## class ContentCoverOptions

```cangjie
public class ContentCoverOptions <: BindOptions {
    public init(
        modalTransition!: ?ModalTransition = Option.None,
        onWillDismiss!: ?(DismissContentCoverAction) -> Unit = Option.None,
        transition!: ?TransitionEffect = Option.None,
        backgroundColor!: ?ResourceColor = Option.None,
        onAppear!: ?() -> Unit = Option.None,
        onDisappear!: ?() -> Unit = Option.None,
        onWillAppear!: ?() -> Unit = Option.None,
        onWillDisappear!: ?() -> Unit = Option.None
    )
}
```

**功能：** 全屏模态页面转场

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [BindOptions](#class-bindoptions)

### init(?ModalTransition, ?(DismissContentCoverAction) -> Unit, ?TransitionEffect, ?ResourceColor, ?() -> Unit, ?() -> Unit, ?() -> Unit, ?() -> Unit)

```cangjie
public init(
    modalTransition!: ?ModalTransition = Option.None,
    onWillDismiss!: ?(DismissContentCoverAction) -> Unit = Option.None,
    transition!: ?TransitionEffect = Option.None,
    backgroundColor!: ?ResourceColor = Option.None,
    onAppear!: ?() -> Unit = Option.None,
    onDisappear!: ?() -> Unit = Option.None,
    onWillAppear!: ?() -> Unit = Option.None,
    onWillDisappear!: ?() -> Unit = Option.None
)
```

**功能：** 构造一个ContentCoverOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|modalTransition|?[ModalTransition](./cj-common-types.md#enum-modaltransition)|否|Option.None|**命名参数。** 全屏模态页面的转场方式。|
|onWillDismiss|?([DismissContentCoverAction](#class-dismisscontentcoveraction))-> Unit|否|Option.None|**命名参数。** 内容覆盖交互式关闭时的回调函数。|
|transition|?[TransitionEffect](./cj-animation-transition.md#class-transitioneffect)|否|Option.None|**命名参数。** 全屏模态页面交互式关闭回调函数。|
|backgroundColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Option.None|**命名参数。** sheet的背景色。默认值：**Color.White**。|
|onAppear|?() -> Unit|否|Option.None|**命名参数。** 全模态页面显示（动画结束后）回调函数。|
|onDisappear|?() -> Unit|否|Option.None|**命名参数。** 全模态页面回退（动画结束后）回调函数。|
|onWillAppear|?() -> Unit|否|Option.None|**命名参数。** 全模态页面显示（动画开始前）回调函数。|
|onWillDisappear|?() -> Unit|否|Option.None|**命名参数。** 全模态页面回退（动画开始前）回调函数。|