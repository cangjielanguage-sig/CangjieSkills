# TextClock

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

TextClock 组件通过文本将当前系统时间显示在设备上。支持不同时区的时间显示，最高精度到秒级。

在组件不可见时时间变动将停止，组件的可见状态基于[onVisibleAreaChange](./cj-universal-event-visibleareachange.md#func-onvisibleareachangearrayfloat64-bool-float64---unit)处理，可见阈值ratios大于0即视为可见状态。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

无

## 创建组件

### init(?Float32, ?TextClockController)

```cangjie
public init(timeZoneOffset!: ?Float32 = None, controller!: ?TextClockController = None)
```

**功能：** 创建一个包含时区偏移和控制器的TextClock对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|timeZoneOffset|?Float32|否|None| **命名参数。** 时区偏移。|
|controller|?[TextClockController](#class-textclockcontroller)|否|None| **命名参数。** TextClock组件的控制器。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。