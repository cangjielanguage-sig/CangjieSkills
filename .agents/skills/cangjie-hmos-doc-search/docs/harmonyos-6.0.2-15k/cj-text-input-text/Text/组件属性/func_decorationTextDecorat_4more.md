### func decoration(TextDecorationType, ResourceColor, TextDecorationStyle)

```cangjie
public func decoration(decorationType!: TextDecorationType, color!: ResourceColor, decorationStyle!: TextDecorationStyle = TextDecorationStyle.SOLID): This
```

**功能：** 设置文本装饰线样式及其颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|decorationType|[TextDecorationType](cj-common-types.md#enum-textdecorationtype)|是|-| **命名参数。** 文本装饰线类型。<br>初始值：TextDecorationType.None。|
|color|[ResourceColor](cj-common-types.md#interface-resourcecolor)|是|-| **命名参数。** 文本装饰线颜色。<br>初始值：Color.Black。|
|decorationStyle|[TextDecorationStyle](cj-common-types.md#enum-textdecorationstyle)|否|TextDecorationStyle.SOLID| **命名参数。** 文本装饰线样式。|

### func draggable(Bool)

```cangjie
public func draggable(value: Bool): This
```

**功能：** 设置选中文本拖拽效果。

> **说明：**
>
> - 不能和[onDragStart](./cj-universal-event-drag.md)事件同时使用。
> - 需配合[CopyOptions](./cj-common-types.md#enum-copyoptions)一起使用，设置copyOptions为CopyOptions.InApp或者CopyOptions.LocalDevice，并且draggable设置为true时，支持对选中文本的拖拽以及选中内容复制到输入框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|选中文本拖拽效果。<br>初始值：false。|

### func editMenuOptions((Array\<TextMenuItem>) -> Array\<TextMenuItem>, (TextMenuItem, Int32, Int32) -> Bool)

```cangjie
public func editMenuOptions(
    onCreateMenu: (Array<TextMenuItem>)->Array<TextMenuItem>,
    onMenuItemClick: (TextMenuItem, Int32, Int32)->Bool
): This
```

**功能：** 设置自定义菜单扩展项，允许用户设置扩展项的文本内容、图标、回调方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onCreateMenu|(Array\<[TextMenuItem](#class-textmenuitem)>)->Array\<[TextMenuItem](#class-textmenuitem)>|是|-|菜单数据模版编辑能力。|
|onMenuItemClick|([TextMenuItem](#class-textmenuitem), Int32, Int32)->Bool|是|-|菜单项功能函数。|

### func ellipsisMode(EllipsisMode)

```cangjie
public func ellipsisMode(value: EllipsisMode): This
```

**功能：** 设置省略位置。

> **说明：**
>
> - ellipsisMode属性需要配合[TextOverflow](./cj-common-types.md#enum-textoverflow)设置为TextOverflow.Ellipsis以及maxLines使用，单独设置ellipsisMode属性不生效。
> - EllipsisMode.START和EllipsisMode.CENTER仅在单行超长文本生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[EllipsisMode](cj-common-types.md#enum-ellipsismode)|是|-|省略位置。<br>初始值：EllipsisMode.END。|