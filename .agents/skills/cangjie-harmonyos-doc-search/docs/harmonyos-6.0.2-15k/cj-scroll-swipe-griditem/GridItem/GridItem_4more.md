# GridItem

网格容器中单项内容容器。

> **说明：**
>
> - 仅支持作为[Grid](./cj-scroll-swipe-grid.md)组件的子组件使用。
> - 当GridItem配合[LazyForEach](./cj-state-rendering-lazyforeach.md)使用时，GridItem子组件在GridItem创建时创建。配合[if/else](../../../Dev_Guide/arkui-cj/rendering_control/cj-rendering-control-ifelse.md)、[ForEach](./cj-state-rendering-foreach.md)使用时，或父组件为Grid时，GridItem子组件在GridItem布局时创建。

## 子组件

可以包含单个子组件。

## 创建组件

### init()

```cangjie
public init()
```

**功能：** 创建网格容器中单项内容组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(() -> Unit)

```cangjie
public init(child: () -> Unit)
```

**功能：** 创建一个可包含子组件的网格容器中单项内容组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|child|()->Unit|是|-|GridItem 容器的子组件。|

### init(GridItemOptions)

```cangjie
public init(value: GridItemOptions)
```

**功能：** 创建一个不包含子组件的GridItem容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[GridItemOptions](#class-griditemoptions)|是|-|为GridItem提供可选参数， 该对象内含有[GridItemStyle](cj-common-types.md#enum-griditemstyle)枚举类型的style参数。|

### init(GridItemOptions, () -> Unit)

```cangjie
public init(value: GridItemOptions, child: () -> Unit)
```

**功能：** 创建一个可包含子组件的GridItem容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[GridItemOptions](#class-griditemoptions)|是|-|为GridItem提供可选参数， 该对象内含有[GridItemStyle](cj-common-types.md#enum-griditemstyle)枚举类型的style参数。|
|child|()->Unit|是|-|GridItem 容器的子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。