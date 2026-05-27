# TextTimer

通过文本显示计时信息并控制其计时器状态的组件。

在组件不可见时时间变动将停止，组件的可见状态基于[onVisibleAreaChange](./cj-universal-event-visibleareachange.md#func-onvisibleareachangearrayfloat64-bool-float64-unit---unit)处理，可见阈值ratios大于0即视为可见状态。

## 子组件

无

## 创建组件

### init(Bool, Int64, TextTimerController)

```cangjie
public init(isCountDown!: Bool = false, count!: Int64 = 60000, controller!: TextTimerController = TextTimerController())
```

**功能：** 创建一个TextTimer组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isCountDown|Bool|否|false| **命名参数。**  是否倒计时。值为true时，计时器开启倒计时，例如从30秒 ~ 0秒。值为false时，计时器开始计时，例如从0秒 ~ 30秒。 |
|count|Int64|否|60000| **命名参数。**  计时器时间（isCountDown为true时生效），单位为毫秒。最长不超过86400000毫秒（24小时）。 0<count<86400000时，count值为计时器初始值。否则，使用默认值为计时器初始值。 |
|controller|[TextTimerController](#class-texttimercontroller)|否|TextTimerController()| **命名参数。** TextTimer控制器。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。