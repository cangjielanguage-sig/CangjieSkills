# LoadingProgress

用于显示加载动效的组件。

加载动效在组件不可见时停止，组件的可见状态基于[onVisibleAreaChange](../../source_zh_cn/arkui-cj/cj-universal-event-visibleareachange.md#func-onvisibleareachangearrayfloat64-bool-float64-unit---unit)处理，可见阈值ratios大于0即视为可见状态。

## 子组件

无

## 创建组件

### init()

```cangjie
public init()
```

**功能：** 创建加载进展组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## 通用属性/通用事件

通用属性：除文本样式外，其余全部支持。

> **说明：**
>
> 组件应设置合理的宽高，当组件宽高设置过大时加载动效可能不符合预期效果。

通用事件：全部支持。