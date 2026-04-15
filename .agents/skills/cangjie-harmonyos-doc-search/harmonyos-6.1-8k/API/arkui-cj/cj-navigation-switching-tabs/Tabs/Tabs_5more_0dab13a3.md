# Tabs

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

不支持自定义组件作为子组件，仅可包含子组件[TabContent](./cj-navigation-switching-tabcontent.md)，以及渲染控制类型[if/else](../../arkui-cj/rendering_control/cj-rendering-control-ifelse.md)和[ForEach](cj-state-rendering-foreach.md)，并且if/else和ForEach下也仅支持TabContent，不支持自定义组件。

> **说明：**
>
> Tabs子组件的visibility属性设置为None，或者visibility属性设置为Hidden时，对应子组件不显示，但依然会在视窗内占位。

## 创建组件

### init(?BarPosition, ?TabsController, ?Int32, () -> Unit)

```cangjie
public init(
    barPosition!: ?BarPosition = None,
    controller!: ?TabsController = None,
    index!: ?Int32 = None,
    child!: () -> Unit = {=>}
)
```

**功能：** 创建一个Tabs容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|barPosition|?[BarPosition](./cj-common-types.md#enum-barposition)|否|None|**命名参数。** 设置Tabs的页签位置。<br> 初始值: BarPosition.Start|
|controller|?[TabsController](#class-tabscontroller)|否|None|**命名参数。** 设置Tabs控制器。<br> 初始值：TabsController()|
|index|?Int32|否|None|**命名参数。** 设置当前显示页签的索引。<br> 初始值：0 <br> **说明：**<br> 设置为小于0的值时按初始值显示。可选值为[0, TabContent子节点数量-1]。直接修改index跳页时，切换动效不生效。 使用TabController的changeIndex时，默认生效切换动效，可以设置animationDuration为0关闭动画。|
|child|()->Unit|否|{=>}|**命名参数。** 声明容器内的子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。