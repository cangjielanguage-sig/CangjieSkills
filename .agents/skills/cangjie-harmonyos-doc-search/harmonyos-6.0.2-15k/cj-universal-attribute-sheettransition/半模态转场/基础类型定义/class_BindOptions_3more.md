### class BindOptions

```cangjie
public class BindOptions {
    public init(
        backgroundColor!: Option<Color> = Option.None,
        onAppear!: Option<() -> Unit> = Option.None,
        onDisappear!: Option<() -> Unit> = Option.None,
        onWillAppear!: Option<() -> Unit> = Option.None,
        onWillDisappear!: Option<() -> Unit> = Option.None
    )
}
```

**功能：** 配置半模态页面的可选属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(Option\<Color>, Option\<() -> Unit>, Option\<() -> Unit>, Option\<() -> Unit>, Option\<() -> Unit>)

```cangjie
public init(
    backgroundColor!: Option<Color> = Option.None,
    onAppear!: Option<() -> Unit> = Option.None,
    onDisappear!: Option<() -> Unit> = Option.None,
    onWillAppear!: Option<() -> Unit> = Option.None,
    onWillDisappear!: Option<() -> Unit> = Option.None
)
```

**功能：** 配置半模态页面的可选属性构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| backgroundColor | Option\<[Color](./cj-common-types.md#class-color)> | 否 | Option.None | **命名参数。**  半模态页面的背板颜色，默认白色。 |
| onAppear | Option\<() -> Unit> | 否 | Option.None | **命名参数。**  半模态页面显示（动画结束后）回调函数。 |
| onDisappear | Option\<() -> Unit> | 否 | Option.None | **命名参数。**  半模态页面回退（动画结束后）回调函数。 |
| onWillAppear | Option\<() -> Unit> | 否 |  Option.None | **命名参数。**  半模态页面显示（动画开始前）回调函数。 |
| onWillDisappear | Option\<() -> Unit> | 否 | Option.None | **命名参数。**  半模态页面回退（动画开始前）回调函数。<br>**说明：** 不允许在onWillDisappear函数中修改状态变量，可能会导致组件行为不稳定。 |

### class DismissSheetAction

```cangjie
public class DismissSheetAction {
    public DismissSheetAction(reason: DismissReason)
}
```

**功能：** 半模态页面关闭回调函数类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### DismissSheetAction(DismissReason)

```cangjie
public DismissSheetAction(reason: DismissReason)
```

**功能：** 半模态页面关闭回调函数类型的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| reason | [DismissReason](./cj-dialog-actionsheet.md#enum-dismissreason) | 是 | \-  | 返回本次半模态页面退出的操作类型。|

#### func dismiss()

```cangjie
public func dismiss()
```

**功能：** 半模态页面关闭回调函数。开发者需要退出页面时调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### class SheetDismiss

```cangjie
public class SheetDismiss {
    public SheetDismiss()
}
```

**功能：** 控制半模态的关闭类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### SheetDismiss()

```cangjie
public SheetDismiss()
```

**功能：** 控制半模态的关闭类型的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### func dismiss()

```cangjie
public func dismiss()
```

**功能：** 半模态面板关闭回调函数。开发者需要退出时调用，不需要退出时无需调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19