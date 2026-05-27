# ListItemGroup

该组件用来展示列表item分组，宽度默认充满[List](cj-scroll-swipe-list.md)组件，必须配合List组件来使用。

> **说明：**
>
> - 该组件的父组件只能是[List](cj-scroll-swipe-list.md)。
> - ListItemGroup组件不支持设置[通用属性aspectRatio](cj-universal-attribute-layoutconstraints.md)。
> - 当ListItemGroup的父组件List的listDirection属性为Axis.Vertical时，设置[通用属性height](cj-universal-attribute-size.md)属性不生效。ListItemGroup的高度为header高度、footer高度和所有ListItem布局后总高度之和。
> - 当父组件List的listDirection属性为Axis.Horizontal时，设置[通用属性width](cj-universal-attribute-size.md)属性不生效。ListItemGroup的宽度为header宽度、footer宽度和所有ListItem布局后总宽度之和。
> - 当前ListItemGroup内部的ListItem组件不支持编辑、拖拽功能，即ListItem组件的editable属性不生效。
> - ListItemGroup使用direction属性设置布局方向不生效，ListItemGroup组件布局方向跟随父容器List组件的布局方向。

## 子组件

包含[ListItem](./cj-scroll-swipe-listitem.md)子组件。

## 创建组件

### init(ListItemGroupParams, () -> Unit)

```cangjie
public init(value: ListItemGroupParams, child: () -> Unit)
```

**功能：** 创建ListItemGroup组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ListItemGroupParams](#class-listitemgroupparams)|是|-|列表item分组组件参数。|
|child|()->Unit|是|-|声明容器子组件。|

## 通用属性/通用事件

通用属性：全部支持。

> **说明：**
>
> 不支持[设置通用属性aspectRatio](./cj-universal-attribute-layoutconstraints.md#func-aspectratiofloat64)

通用事件：全部支持。

## 组件属性

### func divider(Length, ResourceColor, Length, Length)

```cangjie
public func divider(strokeWidth!: Length, color!: ResourceColor = Color.BLACK, startMargin!: Length = 0.vp, endMargin!: Length = 0.vp): This
```

**功能：** 用于设置ListItem分割线样式，默认无分割线。

strokeWidth、startMargin和endMargin不支持设置百分比。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|strokeWidth|[Length](cj-common-types.md#interface-length)|是|-| **命名参数。** 设置分割线的线宽。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color.BLACK| **命名参数。** 设置分割线的颜色。|
|startMargin|[Length](cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 设置分割线距离列表侧边起始端的距离。|
|endMargin|[Length](cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 设置分割线距离列表侧边结束端的距离。|