### class DismissPopupAction

```cangjie
public class DismissPopupAction {
    public DismissPopupAction(public let reason!: DismissReason)
}
```

**功能：** 设置popup交互式关闭拦截开关及拦截回调函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let reason

```cangjie
public let reason: DismissReason
```

**功能：** 关闭原因，返回本次拦截popup消失的事件原因。

**类型：** [DismissReason](./cj-dialog-actionsheet.md#enum-dismissreason)

**读写能力：** 只读

**起始版本：** 19

#### DismissPopupAction(DismissReason)

```cangjie
public DismissPopupAction(public let reason!: DismissReason)
```

**功能：** 构建一个DismissPopupAction的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|reason|  [DismissReason](./cj-dialog-actionsheet.md#enum-dismissreason)| 是 | - | **命名参数。**  关闭原因，返回本次拦截popup消失的事件原因。 |

#### func dismiss()

```cangjie
public func dismiss()
```

**功能：** popup交互式关闭拦截开关及拦截结果类型。开发者需要退出时调用，不需要退出时无需调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### struct PopupMessageOptions

```cangjie
public struct PopupMessageOptions {
    public PopupMessageOptions(
        public let textColor!: Color = Color(0x000000),
        public let font!: Fonts = Fonts()
    )
}
```

**功能：** 弹窗信息文本参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let font

```cangjie
public let font: Fonts = Fonts()
```

**功能：** 设置弹窗信息字体属性。不支持设置family。

**类型：** [Fonts](./cj-common-types.md#class-fonts)

**读写能力：** 只读

**起始版本：** 19

#### let textColor

```cangjie
public let textColor: Color = Color(0x000000)
```

**功能：** 设置弹窗信息文本颜色。

**类型：** [Color](./cj-common-types.md#class-color)

**读写能力：** 只读

**起始版本：** 19

#### PopupMessageOptions(Color, Fonts)

```cangjie
public PopupMessageOptions(
    public let textColor!: Color = Color(0x000000),
    public let font!: Fonts = Fonts()
)
```

**功能：** 创建一个PopupMessageOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|textColor| [Color](./cj-common-types.md#class-color) | 否 | Color(0x000000) | **命名参数。**  弹窗信息文本颜色。 |
| font |[Fonts](./cj-common-types.md#class-fonts) | 否 | Fonts() | **命名参数。** 弹窗信息字体属性。 |