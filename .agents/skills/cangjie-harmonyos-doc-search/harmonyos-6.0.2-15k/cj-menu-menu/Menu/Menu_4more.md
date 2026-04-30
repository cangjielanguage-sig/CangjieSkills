# Menu

以垂直列表形式显示的菜单。

> **说明：**
>
> Menu组件需配合[bindMenu](cj-universal-attribute-menu.md#func-bindmenu---unit)或[bindContextMenu](cj-universal-attribute-menu.md#func-bindcontextmenu---unit-responsetype)方法使用，不支持作为普通组件单独使用。

## 子组件

包含[MenuItem](cj-menu-menuitem.md)、[MenuItemGroup](cj-menu-menuitemgroup.md)子组件。

## 创建组件

### init(() -> Unit)

```cangjie
public init(child: () -> Unit)
```

**功能：** 创建一个存在子组件的菜单。

> **说明：**
>
> 菜单和菜单项宽度计算规则：<br/>布局过程中，期望每个菜单项的宽度一致。若子组件设置了宽度，则以[尺寸计算规则](./cj-universal-attribute-size.md#func-constraintsizelength-length-length-length)为准。<br/>不设置宽度的情况：菜单组件会对子组件MenuItem、MenuItemGroup设置默认2栅格的宽度，若菜单项内容区比2栅格宽，则会自适应撑开。<br/>设置宽度的情况：菜单组件会对子组件MenuItem、MenuItemGroup设置减去padding后的固定宽度。<br/>设置Menu边框[width](./cj-universal-attribute-size.md#func-widthlength)时，支持设置的最小宽度为64vp。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|child|()->Unit|是|-|声明容器内的子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。