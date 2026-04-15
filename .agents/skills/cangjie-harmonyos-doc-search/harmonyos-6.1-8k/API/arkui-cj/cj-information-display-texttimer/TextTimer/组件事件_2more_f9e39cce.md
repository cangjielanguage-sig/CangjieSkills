## 组件事件

### func onTimer(?(Int64, Int64) -> Unit)

```cangjie
public func onTimer(event: ?(Int64, Int64) -> Unit): This
```

**功能：** 时间文本变化时触发该回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|?(Int64, Int64) -> Unit|是|-|时间文本变化时的回调函数。初始值: { _, _ => }。|

## 基础类型定义

### class TextTimerController

```cangjie
public class TextTimerController {
    public init()
}
```

**功能：** TextTimerController是TextTimer组件的控制器，可以定义该类型的对象并绑定至TextTimer组件，实现对TextTimer组件的控制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init()

```cangjie
public init()
```

**功能：** TextTimerController的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### func pause()

```cangjie
public func pause(): Unit
```

**功能：** 提供计时器的暂停事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### func reset()

```cangjie
public func reset(): Unit
```

**功能：** 提供重置计时器的事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### func start()

```cangjie
public func start(): Unit
```

**功能：** 提供计时器的启动事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22