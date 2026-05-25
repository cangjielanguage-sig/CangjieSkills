# ListItemGroup

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

该组件用来展示列表item分组，宽度默认充满[List](cj-scroll-swipe-list.md)组件，必须配合List组件来使用。

> **说明：**
>
> - 该组件的父组件只能是[List](cj-scroll-swipe-list.md)。
> - ListItemGroup组件不支持设置[通用属性aspectRatio](./cj-universal-attribute-size.md#func-aspectratiofloat64)。
> - 当ListItemGroup的父组件List的listDirection属性为Axis.Vertical时，设置[通用属性height](cj-universal-attribute-size.md#func-heightoptionlength)属性不生效。ListItemGroup的高度为header高度、footer高度和所有ListItem布局后总高度之和。
> - 当父组件List的listDirection属性为Axis.Horizontal时，设置[通用属性width](cj-universal-attribute-size.md#func-widthoptionlength)属性不生效。ListItemGroup的宽度为header宽度、footer宽度和所有ListItem布局后总宽度之和。
> - 当前ListItemGroup内部的ListItem组件不支持编辑、拖拽功能，即ListItem组件的editable属性不生效。
> - ListItemGroup使用direction属性设置布局方向不生效，ListItemGroup组件布局方向跟随父容器List组件的布局方向。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

包含[ListItem](./cj-scroll-swipe-listitem.md)子组件。

## 创建组件

### init(?CustomBuilder, ?CustomBuilder, ?Length, ?ListItemGroupStyle, () -> Unit)

```cangjie
public init(
    header!: ?CustomBuilder = None,
    footer!: ?CustomBuilder = None,
    space!: ?Length = None,
    style!: ?ListItemGroupStyle = Option.None,
    child!: () -> Unit
)
```

**功能：**  创建ListItemGroup组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

| 参数名    | 类型              | 必填  | 默认值        | 说明                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:------ |:--------------- |:--- |:---------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| header | ?[CustomBuilder](./cj-common-types.md#type-custombuilder)  | 否   | None       | **命名参数。** 设置ListItemGroup头部组件。                                                                                                                                                                                                                                                                                                                                                                                                                        |
| footer | ?[CustomBuilder](./cj-common-types.md#type-custombuilder)  | 否   | None       | **命名参数。** 设置ListItemGroup尾部组件。                                                                                                                                                                                                                                                                                                                                                                                                                        |
| space  | ?[Length](./cj-common-types.md#interface-length)         | 否   | None       | **命名参数。** 列表项间距。只作用于ListItem与ListItem之间，不作用于header与ListItem、footer与ListItem之间。                                                                                                                                                                                                                                                                                                                                                   |
| style  | ?[ListItemGroupStyle](#enum-listitemgroupstyle) | 否   | Option.None | **命名参数。** 设置List组件卡片样式。                                                                                                                                                                                                                                                                                                                                                                                                                      |
| child  | ()->Unit        | 是   | -          | 声明容器子组件。                                                                                                                                                                                                                                                                                                                                                                                                                             |

## 通用属性/通用事件

通用属性：全部支持。

> **说明：**
>
> 不支持[设置通用属性aspectRatio](./cj-universal-attribute-size.md#func-aspectratiofloat64)。

通用事件：全部支持。

## 组件属性

### func divider(Option\<ListDividerOptions>)

```cangjie
public func divider(value: Option<ListDividerOptions>): This
```

**功能：** 设置ListItem分割线样式，默认无分割线。strokeWidth，startMargin和endMargin不支持设置百分比。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Option<[ListDividerOptions](#class-listdivideroptions)>|是|-|ListItem分割线样式。设置为Option.None时表示无分割线。|