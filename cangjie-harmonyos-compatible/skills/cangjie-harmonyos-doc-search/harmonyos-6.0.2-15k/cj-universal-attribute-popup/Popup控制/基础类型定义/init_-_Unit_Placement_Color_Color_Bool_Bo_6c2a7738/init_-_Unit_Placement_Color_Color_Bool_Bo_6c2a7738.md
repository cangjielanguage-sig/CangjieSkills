### init(() -> Unit, Placement, Color, Color, Bool, Bool, Option\<(StateChangeEvent) -> Unit>)

```cangjie
public init(
    builder!: () -> Unit,
    placement!: Placement = Placement.Bottom,
    maskColor!: Color = Color(0x1000000),
    popupColor!: Color = Color(0x1000000),
    enableArrow!: Bool = true,
    autoCancel!: Bool = true,
    onStateChange!: Option<(StateChangeEvent) -> Unit> = Option.None
)
```

**功能：** 创建CustomPopupOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| builder | ()->Unit | 是 |  - | **命名参数。**  提示气泡内容的构造器。使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。 |
| placement | [Placement](./cj-common-types.md#enum-placement) | 否 | Placement.Bottom | **命名参数。**  气泡组件优先显示的位置。<br>**说明：** 当前位置显示不下时，会自动调整位置。 |
| maskColor  | [Color](./cj-common-types.md#class-color) | 否 | Color(0x1000000) | **命名参数。**   提示气泡遮障层的颜色。 |
| popupColor | [Color](./cj-common-types.md#class-color) | 否 | Color(0x1000000) | **命名参数。**  提示气泡的颜色。 |
| arrowOffset | [Length](cj-common-types.md#interface-length) | 否 | 0.vp | **命名参数。**  popup箭头在弹窗处的偏移。<br>**说明：** 箭头在气泡上下方时，数值为0表示箭头居最左侧，偏移量为箭头至最左侧的距离，默认居中。箭头在气泡左右侧时，偏移量为箭头至最上侧的距离，默认居中。如果显示在屏幕边缘，气泡会自动左右偏移，数值为0时箭头始终指向绑定组件。 |
| enableArrow | Bool | 否 | true | **命名参数。**  是否显示箭头。<br>**说明：** 如果箭头所在方位侧的气泡长度不足以显示下箭头，则会默认不显示箭头。比如：placement设置为Left，但气泡高度小于箭头的宽度（32vp），则实际不会显示箭头。 |
| autoCancel | Bool | 否 | true | **命名参数。**  页面有操作时，是否自动关闭气泡。 |
| onStateChange | ?([StateChangeEvent](#class-statechangeevent))->Unit | 否 | None | **命名参数。**  弹窗状态变化事件回调，参数为弹窗当前的显示状态。 |