# 菜单控制

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

为组件绑定弹出式菜单，弹出式菜单以垂直列表形式显示菜单项，可通过长按、点击或鼠标右键触发。

> **说明：**
>
> - CustomBuilder里不支持再使用bindMenu、bindContextMenu弹出菜单。多级菜单可使用[Menu](./cj-menu-menu.md)组件。
> - 弹出菜单的文本内容不支持长按选中。
> - 若组件是可拖动节点，绑定bindContextMenu未指定preview时，菜单弹出会浮起拖拽预览图且菜单选项和预览图不会发生避让。对此，开发者可根据使用场景设置preview或者将目标节点设置成不可拖动节点。
> - 菜单支持长按500ms弹出子菜单，支持按压态跟随手指移动。仅支持使用[Menu](./cj-menu-menu.md)组件且子组件包含[MenuItem](./cj-menu-menuitem.md)或[MenuItemGroup](./cj-menu-menuitemgroup.md)的场景。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## func bindContextMenu(?CustomBuilder, ?ResponseType, ?ContextMenuOptions)

```cangjie
func bindContextMenu(builder!: ?CustomBuilder, responseType!: ?ResponseType,
    options!: ?ContextMenuOptions): T
```

**功能：** 绑定上下文菜单到组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
| :--- | :--- | :--- | :--- | :--- |
| builder | ?[CustomBuilder](./cj-common-types.md#type-custombuilder) | 是 | - | **命名参数。** 自定义构建器。<br>初始值：{ => }。|
| responseType | ?[ResponseType](./cj-common-types.md#enum-responsetype) |是|-| **命名参数。** 响应类型。<br>初始值：ResponseType.LongPress。|
| options | ?[ContextMenuOptions](./cj-common-types.md#class-contextmenuoptions) | 是 | - | **命名参数。** 上下文菜单选项。<br>初始值：ContextMenuOptions()。|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回调用此接口的组件实例本身。|

## func bindMenu(?Array\<MenuElement>)

```cangjie
func bindMenu(content: ?Array<MenuElement>): T
```

**功能：** 绑定菜单到组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
| :--- | :--- | :--- | :--- | :--- |
| content | ?Array\<[MenuElement](./cj-common-types.md#class-menuelement)> | 是 | - | 菜单元素数组。|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回调用此接口的组件实例本身。|

## func bindMenu(?CustomBuilder)

```cangjie
func bindMenu(builder!: ?CustomBuilder): T
```

**功能：** 绑定自定义菜单到组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
| :--- | :--- | :--- | :--- | :--- |
| builder | ?[CustomBuilder](./cj-common-types.md#type-custombuilder) | 是 | - | **命名参数。** 自定义构建器。<br>初始值：{ => }。|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回通用方法接口类型。|