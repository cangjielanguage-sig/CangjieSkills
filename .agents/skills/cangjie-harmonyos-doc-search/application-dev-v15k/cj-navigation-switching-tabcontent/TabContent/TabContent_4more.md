# TabContent

仅在Tabs中使用，对应一个切换页签的内容视图。

## 子组件

支持单个子组件。

> **说明：**
>
> 可内置系统组件和自定义组件，支持渲染控制类型（[if/else](../../../Dev_Guide/arkui-cj/rendering_control/cj-rendering-control-ifelse.md)、[ForEach](cj-state-rendering-foreach.md)和[LazyForEach](cj-state-rendering-lazyforeach.md)）。

## 创建组件

### init()

```cangjie
public init()
```

**功能：** 创建一个不包含子组件的TabContent容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(() -> Unit)

```cangjie
public init(child: () -> Unit)
```

**功能：** 创建一个包含子组件的TabContent容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|child|()->Unit|是|-|声明容器内的子组件。|

## 通用属性/通用事件

通用属性：全部支持。

> **说明：**
>
> - TabContent组件不支持设置通用宽度属性，其宽度默认撑满Tabs父组件。
> - TabContent组件不支持设置通用高度属性，其高度由Tab父组件与TabBar组件高度决定。
> - vertical属性为false值，交换上述2个限制。
> - TabContent组件不支持内容过长时页面的滑动，如需页面滑动，可嵌套List使用。
> - 建议对Tabs组件的所有TabContent子组件的tabBar属性，采用统一的参数类型。
> - 若TabContent内部有可获焦组件，Tabs组件内TabContent组件和TabBar组件之间的走焦，仅支持通过键盘的方向键控制。

通用事件：全部支持。