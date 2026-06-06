# NavDestination

作为子页面的根容器，用于显示[Navigation](./cj-navigation-switching-navigation.md)的内容区。

> **说明：**
>
> - NavDestination组件必须配合Navigation使用，作为Navigation目的页面的根节点，单独使用只能作为普通容器组件，不具备路由相关属性能力。
> - 如果页面栈中间页面的生命周期发生变化，跳转之前的栈顶Destination的生命周期(onWillShow, onShown, onHidden, onWillDisappear)与跳转之后的栈顶Destination的生命周期(onWillShow, onShown, onHidden, onWillDisappear)均在最后触发。
> - NavDestination未设置主副标题并且没有返回键时，不显示标题栏。

## 子组件

可以包含子组件。

## 创建组件

### init()

```cangjie
public init()
```

**功能：** 构造一个不包含子组件的NavDestination容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### init(() -> Unit)

```cangjie
public init(child: () -> Unit)
```

**功能：** 构造一个包含子组件的NavDestination容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|child|()->Unit|是|-|NavDestination容器的子组件。|

## 通用属性/通用事件

通用属性：支持通用属性。

不推荐设置位置、大小等布局相关属性，可能会造成页面显示异常。

通用事件：全部支持。