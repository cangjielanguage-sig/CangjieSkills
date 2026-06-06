### init(String, Bool, Action, Action, Option<(StateChangeEvent) -> Unit>)

```cangjie
public init(
    message!: String,
    placementOnTop!: Bool = false,
    primaryButton!: Action = Action(value: "", action: { => }),
    secondaryButton!: Action = Action(value: "", action: { => }),
    onStateChange!: Option<(StateChangeEvent) -> Unit> = Option.None
)
```

**功能：** 构建一个PopupOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| message | string | 是 |  | **命名参数。**  弹窗信息内容。 |
| placementOnTop | Bool | 否 | false | **命名参数。**  是否在组件上方显示。 |
| primaryButton| [Action](#class-action) | 否 | Action(value: "", action: {=>}) | **命名参数。**  第一个按钮。 <br/>value:&nbsp;弹窗里主按钮的文本。<br/>action:&nbsp;点击主按钮的回调函数。|
| secondaryButton| [Action](#class-action) | 否 | Action(value: "", action: {=>}) | **命名参数。**  第二个按钮。<br/>value:&nbsp;弹窗里主按钮的文本。<br/>action:&nbsp;点击主按钮的回调函数。 |
| onStateChange | ?([StateChangeEvent](#class-statechangeevent))->Unit | 否 | None | **命名参数。**  弹窗状态变化事件回调，参数为弹窗当前的显示状态。 |