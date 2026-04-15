## class SheetOptions

```cangjie
public class SheetOptions <: BindOptions {
    public init(backgroundColor!: Option<ResourceColor> = Option.None, onAppear!: Option<() -> Unit> = Option.None, onDisappear!: Option<() -> Unit> = Option.None, onWillAppear!: Option<() -> Unit> = Option.None, onWillDisappear!: Option<() -> Unit> = Option.None, height!: Option<SheetSize> = Option.None, detents!: Option<Array<SheetSize>> = Option.None, preferType!: Option<SheetType> = Option.None, showClose!: Option<Bool> = Option.None, dragBar!: Option<Bool> = Option.None, blurStyle!: Option<BlurStyle> = Option.None, maskColor!: Option<Color> = Option.None, title!: Option<() -> Unit> = Option.None, enableOutsideInteractive!: Option<Bool> = Option.None, shouldDismiss!: Option<(SheetDismiss) -> Unit> = Option.None, onWillDismiss!: Option<(DismissSheetAction) -> Unit> = Option.None, onWillSpringBackWhenDismiss!: Option<(SpringBackAction) -> Unit> = Option.None, onHeightDidChange!: Option<(Float32) -> Unit> = Option.None, onDetentsDidChange!: Option<(Float32) -> Unit> = Option.None, onWidthDidChange!: Option<(Float32) -> Unit> = Option.None, onTypeDidChange!: Option<(Float32) -> Unit> = Option.None, borderWidth!: Option<Length> = None, borderColor!: Option<Color> = None, borderStyle!: Option<EdgeStyles> = None, width!: Option<Length> = None, shadow!: Option<ShadowOptions> = None, mode!: Option<SheetMode> = None, scrollSizeMode!: Option<ScrollSizeMode> = None)
}
```

**功能：** 配置半模态页面的可选属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [BindOptions](#class-bindoptions)