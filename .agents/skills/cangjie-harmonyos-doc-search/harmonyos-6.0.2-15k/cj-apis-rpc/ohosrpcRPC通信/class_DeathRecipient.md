## class DeathRecipient

```cangjie
public abstract class DeathRecipient {}
```

**功能：** 用于订阅远端对象的死亡通知。当被订阅该通知的远端对象死亡时，本端可收到消息，调用[onRemoteDied](#func-onremotedied)接口。远端对象死亡可以为远端对象所在进程死亡，远端对象所在设备关机或重启，当远端对象与本端对象属于不同设备时，也可为远端对象离开组网时。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

### func onRemoteDied()

```cangjie
public open func onRemoteDied(): Unit
```

**功能：** 在成功添加死亡通知订阅后，当远端对象死亡时，将自动调用本方法。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

// 此处代码可添加在依赖项定义中
class MyDeathRecipient <: DeathRecipient {
    public func onRemoteDied(): Unit {
    }
}
```