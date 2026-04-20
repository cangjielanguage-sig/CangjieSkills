## class DismissContentCoverAction

```cangjie
public class DismissContentCoverAction {
    public let reason: DismissReason
}
```

**功能：** 用于处理全屏模态页面关闭逻辑的核心回调类，负责在用户触发关闭操作时，通过回调机制拦截关闭行为。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### let reason

```cangjie
public let reason: DismissReason
```

**功能：** 关闭原因类型。

**类型：** [DismissReason](#enum-dismissreason)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func dismiss()

```cangjie
public func dismiss(): Unit
```

**功能：** 显式触发模态页面关闭操作，是唯一控制关闭的入口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22