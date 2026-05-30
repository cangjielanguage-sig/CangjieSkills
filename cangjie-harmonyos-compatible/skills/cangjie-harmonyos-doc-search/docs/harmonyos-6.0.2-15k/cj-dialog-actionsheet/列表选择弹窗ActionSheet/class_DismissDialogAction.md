## class DismissDialogAction

```cangjie
public class DismissDialogAction {
    public DismissDialogAction(public let reason: DismissReason) {}
}
```

**功能：** Dialog关闭的信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let reason

```cangjie
public let reason: DismissReason
```

**功能：** Dialog无法关闭原因。根据开发者需要选择不同操作下，Dialog是否需要关闭。

**类型：** [DismissReason](cj-dialog-actionsheet.md#enum-dismissreason)

**读写能力：** 只读

**起始版本：** 19

### DismissDialogAction(DismissReason)

```cangjie
public DismissDialogAction(public let reason: DismissReason)
```

**功能：** Dialog关闭的信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|reason|[DismissReason](cj-dialog-actionsheet.md#enum-dismissreason)|是|-|Dialog无法关闭原因。根据开发者需要选择不同操作下，Dialog是否需要关闭。|

### func dismiss()

```cangjie
public func dismiss()
```

**功能：** Dialog关闭回调函数。开发者需要推出时调用，不需要退出时无需调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19