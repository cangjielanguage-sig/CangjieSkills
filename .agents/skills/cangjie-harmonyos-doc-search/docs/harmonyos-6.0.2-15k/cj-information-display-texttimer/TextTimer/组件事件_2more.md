## 组件事件

### func onTimer((Int64, Int64) -> Unit)

```cangjie
public func onTimer(callback: (Int64, Int64) -> Unit): This
```

**功能：** 时间文本发生变化时触发。锁屏状态和应用后台状态下不会触发该事件。设置高精度的format（SSS、SS）时，回调间隔可能会出现波动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int64,Int64)->Unit|是|-| 第一个Int64类型的参数为Linux时间戳，即自1970年1月1日起经过的时间，单位为设置格式的最小单位。<br/>第二个Int64类型的参数为计时器经过的时间，单位为设置格式的最小单位。 |

## 基础类型定义

### class TextTimerController

```cangjie
public class TextTimerController {
    public init()
}
```

**功能：** TextTimer组件的控制器，用于控制文本计时器。一个TextTimer组件仅支持绑定一个控制器，组件创建完成后相关指令才能被调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init()

```cangjie
public init()
```

**功能：** 创建一个TextTimerController对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func pause()

```cangjie
public func pause()
```

**功能：** 计时暂停。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func reset()

```cangjie
public func reset()
```

**功能：** 重置计时器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func start()

```cangjie
public func start()
```

**功能：** 计时开始。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12