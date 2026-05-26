# 菜单控制

为组件绑定弹出式菜单，弹出式菜单以垂直列表形式显示菜单项，可通过长按、点击或鼠标右键触发。

> **说明：**
>
> - CustomBuilder里不支持再使用bindMenu、bindContextMenu弹出菜单。多级菜单可使用[Menu](./cj-menu-menu.md#menu)组件。
> - 弹出菜单的文本内容不支持长按选中。
> - 若组件是可拖动节点，绑定bindContextMenu未指定preview时，菜单弹出会浮起拖拽预览图且菜单选项和预览图不会发生避让。对此，开发者可根据使用场景设置preview或者将目标节点设置成不可拖动节点。
> - 菜单支持长按500ms弹出子菜单，支持按压态跟随手指移动。<br> a.仅支持使用[Menu](./cj-menu-menu.md#menu)组件且子组件包含[MenuItem](./cj-menu-menuitem.md#menuitem)或[MenuItemGroup](./cj-menu-menuitemgroup.md#menuitemgroup)的场景。<br> b.仅支持[MenuPreviewMode](./cj-common-types.md#enum-menupreviewmode)为NONE的菜单。

## func bindContextMenu(() -> Unit, ResponseType)

```cangjie
public func bindContextMenu(builder!: () -> Unit, responseType!: ResponseType = ResponseType.LongPress): This
```

**功能：** 给组件绑定菜单，触发方式为长按或者右键点击，弹出菜单项需要自定义。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|() -> Unit|是|\-| **命名参数。** 自定义组件。|
|responseType|[ResponseType](./cj-common-types.md#enum-responsetype)|否|ResponseType.LongPress| **命名参数。** 菜单弹出条件，长按或者右键点击。|

## func bindContextMenu(() -> Unit, ResponseType, ContextMenuOptions)

```cangjie
public func bindContextMenu(builder!: () -> Unit, responseType!: ResponseType, options!: ContextMenuOptions): This
```

**功能：** 给组件绑定菜单，触发方式为长按或者右键点击，弹出菜单项需要自定义。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|() -> Unit|是|\-| **命名参数。** 自定义组件。|
|responseType|[ResponseType](./cj-common-types.md#enum-responsetype)|是|\-| **命名参数。** 菜单弹出条件，长按或者右键点击。<br> 初始值：ResponseType.LongPress。|
|options|[ContextMenuOptions](#class-contextmenuoptions)|是|\-| **命名参数。** 配置弹出菜单的参数。|

## func bindMenu(Array\<Action>)

```cangjie
public func bindMenu(menuList: Array<Action>): This
```

**功能：** 给组件绑定菜单，点击后弹出菜单。弹出菜单项支持图标+文本排列和自定义两种功能。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|menuList|Array\<[Action](#class-action)>|是|\-|配置菜单项图标和文本的数组。|

## func bindMenu(Array\<MenuElement>, ?MenuOptions)

```cangjie
public func bindMenu(content: Array<MenuElement>, options!: ?MenuOptions = None): This
```

**功能：** 给组件绑定菜单，点击后弹出菜单。弹出菜单项支持图标+文本排列和自定义两种功能。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|Array\<[MenuElement](#class-menuelement)>|是|\-|配置菜单项图标和文本的数组。|
|options|?[MenuOptions](#class-menuoptions)|否|None| **命名参数。** 配置弹出菜单的参数。|