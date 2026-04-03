# Badge

信息标记组件，可以附加在单个组件上用于信息提醒的容器组件。

## 子组件

支持单个子组件。

> **说明：**
>
> 子组件类型：系统组件和自定义组件，支持渲染控制类型（[if/else](../../../Dev_Guide/arkui-cj/rendering_control/cj-rendering-control-ifelse.md)、[ForEach](cj-state-rendering-foreach.md)、[LazyForEach](cj-state-rendering-lazyforeach.md)）。

## 创建组件

### init(BadgeParams, () -> Unit)

```cangjie
public init(value: BadgeParams, child: () -> Unit)
```

**功能：** 根据数字创建标记组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[BadgeParams](#class-badgeparams)|是|-|数字标记组件参数。|
|child|()->Unit|是|-|容器的子组件。|

## 通用属性/通用事件

通用属性：除文本样式外，其余全部支持。

通用事件：全部支持。