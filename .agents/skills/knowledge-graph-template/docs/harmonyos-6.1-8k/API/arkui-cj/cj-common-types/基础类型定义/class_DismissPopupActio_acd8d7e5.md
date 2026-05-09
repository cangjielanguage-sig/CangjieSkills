## class DismissPopupAction

```cangjie
public class DismissPopupAction {
    public let reason: DismissReason
}
```

**功能：** 设置popup交互式关闭拦截开关及拦截回调函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### let reason

```cangjie
public let reason: DismissReason
```

**功能：** 关闭原因，返回本次拦截popup消失的事件原因。

**类型：** [DismissReason](#enum-dismissreason)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func dismiss()

```cangjie
public func dismiss(): Unit
```

**功能：** 半模态页面关闭回调函数。开发者需要退出页面时调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22