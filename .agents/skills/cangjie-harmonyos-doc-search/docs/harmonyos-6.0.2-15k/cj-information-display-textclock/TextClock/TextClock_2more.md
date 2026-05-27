# TextClock

TextClock 组件通过文本将当前系统时间显示在设备上。支持不同时区的时间显示，最高精度到秒级。

在组件不可见时时间变动将停止，组件的可见状态基于[onVisibleAreaChange](./cj-universal-event-visibleareachange.md#func-onvisibleareachangearrayfloat64-bool-float64-unit---unit)处理，可见阈值ratios大于0即视为可见状态。

## 子组件

无