# Badge

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

信息标记组件，可以附加在单个组件上用于信息提醒的容器组件。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

支持单个子组件。

> **说明：**
>
> 子组件类型：系统组件和自定义组件，支持渲染控制类型（[if/else](../../arkui-cj/rendering_control/cj-rendering-control-ifelse.md)、[ForEach](cj-state-rendering-foreach.md)、[LazyForEach](cj-state-rendering-lazyforeach.md)）。

## 创建组件

### init(Int32, ?BadgeStyle, ?BadgePosition, ?Int32, () -> Unit)

```cangjie
public init(count!: Int32, style!: ?BadgeStyle, position!: ?BadgePosition = None,
    maxCount!: ?Int32 = None, child!: () -> Unit)
```

**功能：** 根据数字创建标记组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|count|Int32|是|-|**命名参数。** 设置提醒消息数。小于等于0时不显示信息标记。|
|style|?[BadgeStyle](#class-badgestyle)|是|-|**命名参数。** Badge组件可设置的样式，支持设置文本颜色、尺寸、圆点颜色和尺寸。|
|position|?[BadgePosition](#enum-badgeposition)|否|None|**命名参数。** 提示点显示位置。初始值：BadgePosition.RightTop|
|maxCount|?Int32|否|None|**命名参数。** 最大消息数，超过最大消息时仅显示 maxCount+。初始值：99|
|child|() -> Unit|是|-|**命名参数。** 容器的子组件。|

### init(String, ?BadgeStyle, ?BadgePosition, () -> Unit)

```cangjie
public init(value!: String, style!: ?BadgeStyle, position!: ?BadgePosition = None, child!: () -> Unit)
```

**功能：** 根据字符串创建标记组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|**命名参数。** 文本标记组件参数。|
|style|?[BadgeStyle](#class-badgestyle)|是|-|**命名参数。** Badge组件可设置的样式，支持设置文本颜色、尺寸、圆点颜色和尺寸。|
|position|?[BadgePosition](#enum-badgeposition)|否|None|**命名参数。** 提示点显示位置。初始值：BadgePosition.RightTop|
|child|() -> Unit|是|-|**命名参数。** 容器的子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。