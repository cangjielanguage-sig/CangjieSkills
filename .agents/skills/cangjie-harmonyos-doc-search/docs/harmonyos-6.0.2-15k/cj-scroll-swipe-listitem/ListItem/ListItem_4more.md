# ListItem

用来展示列表具体item，必须配合List来使用。

> **说明：**
>
> * 该组件的父组件只能是[List](./cj-scroll-swipe-list.md)或者[ListItemGroup](./cj-scroll-swipe-listgroup.md)。
> * 当ListItem配合LazyForEach使用时，ListItem子组件在ListItem创建时创建。配合if/else、ForEach使用时，或父组件为List/ListItemGroup时，ListItem子组件在ListItem布局时创建。

## 子组件

可以包含单个子组件。

## 创建组件

### init(() -> Unit)

```cangjie
public init(child: () -> Unit)
```

**功能：** 创建ListItem组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|child|()->Unit|是|-|容器内的ListItem子组件。|

### init(ListItemOptions, () -> Unit)

```cangjie
public init(value: ListItemOptions, deepRender: () -> Unit)
```

**功能：** 创建ListItem组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ListItemOptions](#class-listitemoptions)|是|-|为ListItem提供可选参数， 该对象内含有ListItemStyle枚举类型的style参数。|
|deepRender|()->Unit|是|-|容器内的ListItem子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。