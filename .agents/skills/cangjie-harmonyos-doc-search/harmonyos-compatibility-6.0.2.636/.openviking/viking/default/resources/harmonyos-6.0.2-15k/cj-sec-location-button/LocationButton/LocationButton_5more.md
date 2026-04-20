# LocationButton

安全控件的位置控件，用户通过点击该位置按钮，可以临时获取精准定位权限，而不需要权限弹框授权确认。

## 子组件

无

## 通用属性/通用事件

通用属性：仅支持[安全控件通用属性](./cj-sec-button.md)。

通用事件：不支持。

## 创建组件

### init()

```cangjie
public init()
```

**功能：** 默认创建带有图标、文本、背景的位置按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

### init(?LocationIconStyle, ?LocationDescription, ButtonType)

```cangjie
public init(icon!: ?LocationIconStyle = None, text!: ?LocationDescription = None, buttonType!: ButtonType = ButtonType.Capsule)
```

**功能：** 创建包含指定元素的位置按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|?[LocationIconStyle](#enum-locationiconstyle)|否|None|**命名参数。** 设置位置按钮的图标风格。不传入该参数表示没有图标。|
|text|?[LocationDescription](#enum-locationdescription)|否|None|**命名参数。** 设置位置按钮的文本描述。不传入该参数表示没有文字描述。|
|buttonType|[ButtonType](./cj-common-types.md#enum-buttontype)|否| ButtonType.Capsule|**命名参数。** 设置位置按钮的背景样式。不传入该参数，系统默认提供Capsule类型按钮。|

> **说明：**
>
> - icon或text需至少传入一个。
> - 如果icon、text都不传入，buttonType参数不起效，创建的LocationButton为默认样式，默认样式：
>     - LocationIconStyle默认样式为LINES；
>     - LocationDescription默认样式为CURRENT_LOCATION；
>     - ButtonType默认样式为Capsule。
> - icon、text、buttonType不支持动态修改。

## 组件事件

### func onClick((ClickEvent, LocationButtonOnClickResult) -> Unit)

**功能：** 点击动作触发该回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback |([ClickEvent](../../source_zh_cn/arkui-cj/cj-universal-event-click.md#class-clickevent), [LocationButtonOnClickResult](#enum-locationbuttononclickresult)) -> Unit | 是| - | 点击动作触时，触发该回调函数。参数一：点击事件对象；参数二：位置权限的授权结果。|