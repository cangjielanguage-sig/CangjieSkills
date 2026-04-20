# SideBarContainer

提供可以显示和隐藏的侧边栏容器，通过子组件定义侧边栏和内容区，第一个子组件表示侧边栏，第二个子组件表示内容区。

## 子组件

可以包含子组件。

> **说明：**
>
> - 子组件类型：系统组件和自定义组件，不支持支持渲染控制类型（[if/else](../../../Dev_Guide/arkui-cj/rendering_control/cj-rendering-control-ifelse.md)、[ForEach](cj-state-rendering-foreach.md)、[LazyForEach](cj-state-rendering-lazyforeach.md)）。
> - 子组件个数：必须且仅包含2个子组件。
> - 子组件个数异常时：3个或以上子组件，显示第一个和第二个。1个子组件，显示侧边栏，内容区为空白。

## 创建组件

### init(SideBarContainerType, () -> Unit)

```cangjie
public init(`type`: SideBarContainerType, content: () -> Unit)
```

**功能：** 创建一个侧边栏容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|'`type`'|[SideBarContainerType](./cj-common-types.md#enum-sideBarcontainertype)|是|-|设置侧边栏的显示类型。<br>初始值：SideBarContainerType.Embed。|
|content|()->Unit|是|-|定义侧边栏和内容区。|

### init(() -> Unit)

```cangjie
public init(content: () -> Unit)
```

**功能：** 创建一个侧边栏容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|()->Unit|是|-|定义侧边栏和内容区。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。