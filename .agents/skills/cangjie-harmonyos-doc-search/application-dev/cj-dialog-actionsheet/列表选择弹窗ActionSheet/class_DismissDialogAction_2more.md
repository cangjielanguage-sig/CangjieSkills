## class DismissDialogAction

```cangjie
public class DismissDialogAction {
    public var reason: DismissReason
    public init(reason: DismissReason)
}
```

**功能：** Dialog关闭的信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var reason

```cangjie
public var reason: DismissReason
```

**功能：** Dialog无法关闭原因。根据开发者需要选择不同操作下，Dialog是否需要关闭。

**类型：** [DismissReason](./cj-common-types.md#enum-dismissreason)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(DismissReason)

```cangjie
public init(reason: DismissReason)
```

**功能：** DismissDialogAction类的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|reason|[DismissReason](./cj-common-types.md#enum-dismissreason)|是|-|Dialog无法关闭原因。根据开发者需要选择不同操作下，Dialog是否需要关闭。|

### func dismiss()

```cangjie
public func dismiss(): Unit
```

**功能：** Dialog关闭回调函数。开发者需要推出时调用，不需要退出时无需调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

## class ActionSheetOffset

```cangjie
public class ActionSheetOffset {
    public var dx: ?Length
    public var dy: ?Length
    public init(
        dx!: ?Length,
        dy!: ?Length
    )
}
```

**功能：** 弹窗的对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var dx

```cangjie
public var dx: ?Length
```

**功能：** 弹出窗口相对于对齐位置dx的偏移量。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var dy

```cangjie
public var dy: ?Length
```

**功能：** 弹出窗口相对于对齐位置dy的偏移量。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?Length, ?Length)

```cangjie
public init(
    dx!: ?Length,
    dy!: ?Length
)
```

**功能：** ActionSheetOffset类的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dx|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 弹出窗口相对于对齐位置dx的偏移量。|
|dy|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 弹出窗口相对于对齐位置dy的偏移量。|