# TextTimer

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

通过文本显示计时信息并控制其计时器状态的组件。

在组件不可见时时间变动将停止，组件的可见状态基于[onVisibleAreaChange](./cj-universal-event-visibleareachange.md#func-onvisibleareachangearrayfloat64-bool-float64---unit)处理，可见阈值ratios大于0即视为可见状态。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

无

## 创建组件

### init(?Bool, ?Int64, ?TextTimerController)

```cangjie
public init(isCountDown!: ?Bool = None, count!: ?Int64 = None,
    controller!: ?TextTimerController = None)
```

**功能：** 创建一个包含倒计时设置、计时时间和控制器的TextTimer对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isCountDown|?Bool|否|None| **命名参数。** 是否倒计时。<br>初始值：false。|
|count|?Int64|否|None| **命名参数。** 计时器时间（isCountDown为true时生效），单位为毫秒。<br>初始值：60000。|
|controller|?[TextTimerController](#class-texttimercontroller)|否|None| **命名参数。** TextTimer控制器。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。