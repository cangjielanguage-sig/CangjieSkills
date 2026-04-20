## class DismissSheetAction

```cangjie
public class DismissSheetAction {
    public var reason: DismissReason
}
```

**功能：** 半模态页面关闭回调函数类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var reason

```cangjie
public var reason: DismissReason
```

**功能：** 半模态页面关闭原因。

**类型：** [DismissReason](#enum-dismissreason)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func dismiss()

```cangjie
public func dismiss(): Unit
```

**功能：** 半模态页面关闭回调函数。开发者需要退出页面时调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22