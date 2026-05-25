# Grid

网格容器，由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。

## 子组件

仅支持[GridItem](cj-scroll-swipe-griditem.md)子组件，支持渲染控制类型（[if/else](../../../Dev_Guide/arkui-cj/rendering_control/cj-rendering-control-ifelse.md)、[ForEach](cj-state-rendering-foreach.md)、[LazyForEach](cj-state-rendering-lazyforeach.md)）。

> **说明：**
>
> - Grid子组件的索引值计算规则：
> - 按子组件的顺序依次递增。
> - if/else语句中，只有条件成立分支内的子组件会参与索引值计算，条件不成立分支内的子组件不计算索引值。
> - ForEach/LazyForEach语句中，会计算展开所有子节点索引值。
> - [if/else](../../../Dev_Guide/arkui-cj/rendering_control/cj-rendering-control-ifelse.md)、[ForEach](cj-state-rendering-foreach.md)、[LazyForEach](cj-state-rendering-lazyforeach.md)发生变化以后，会更新子节点索引值。
> - Grid子组件的visibility属性设置为Hidden或None时依然会计算索引值。
> - Grid子组件的visibility属性设置为None时不显示，但依然会占用子组件对应的网格。
> - Grid子组件设置position属性，会占用子组件对应的网格，子组件将显示在相对Grid左上角偏移position的位置。该子组件不会随其对应网格滚动，在对应网格滑出Grid显示范围外后不显示。
> - 当Grid子组件之间留有空隙时，会根据当前的展示区域尽可能填补空隙，因此GridItem可能会随着网格滚动而改变相对位置。

## 创建组件

### init()

```cangjie
public init()
```

**功能：** 创建网格容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(Scroller)

```cangjie
public init(scroller: Scroller)
```

**功能：** 创建包含滚动控制器的网格容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scroller|[Scroller](cj-scroll-swipe-scroll.md)|是|-|可滚动组件的控制器，与可滚动组件绑定。<br> **说明：** <br>不允许和其他滚动类组件，如：[List](cj-scroll-swipe-list.md)、[Grid](cj-scroll-swipe-grid.md)、[Scroll](cj-scroll-swipe-scroll.md)等绑定同一个滚动控制对象。|

### init(() -> Unit)

```cangjie
public init(child: () -> Unit)
```

**功能：** 创建包含子组件的网格容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|child|()->Unit|是|-|网格容器的子组件。|

### init(Scroller, () -> Unit)

```cangjie
public init(scroller: Scroller, child: () -> Unit)
```

**功能：** 创建包含滚动控制器和子组件的网格容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scroller|[Scroller](cj-scroll-swipe-scroll.md)|是|-|可滚动组件的控制器，与可滚动组件绑定。<br> **说明：** <br>不允许和其他滚动类组件，如：[List](cj-scroll-swipe-list.md)、[Grid](cj-scroll-swipe-grid.md)、[Scroll](cj-scroll-swipe-scroll.md)等绑定同一个滚动控制对象。|
|child|()->Unit|是|-|网格容器的子组件。|

## 通用属性/通用事件

通用属性：除支持通用属性外，还支持[滚动组件通用属性](./cj-scroll-swipe-common.md)。

通用事件：全部支持。