# SaveButton

安全控件的保存控件，用户通过点击该保存按钮，可以临时获取存储权限，而不需要权限弹框授权确认。

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

**功能：** 默认创建带有图标、文本、背景的保存按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

### init(?SaveIconStyle, ?SaveDescription, ButtonType)

```cangjie
public init(icon!: ?SaveIconStyle = None, text!: ?SaveDescription = None, buttonType!: ButtonType = ButtonType.Capsule)
```

**功能：** 创建包含指定元素的保存按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|?[SaveIconStyle](#enum-saveiconstyle)|否|None|**命名参数。** 设置保存按钮的图标风格。<br/>不传入该参数表示没有图标。|
|text|?[SaveDescription](#enum-savedescription)|否|None|**命名参数。** 设置保存按钮的文本描述。<br/>不传入该参数表示没有文字描述。|
|buttonType|[ButtonType](./cj-button-picker-button.md#enum-buttontype)|否|ButtonType.Capsule|**命名参数。** 设置保存按钮的背景样式。<br/>不传入该参数，系统默认提供Capsule类型按钮。|

> **说明：**
>
> - icon或text需至少传入一个。
> - 如果icon、text都不传入，buttonType参数不起效，创建的SaveButton为默认样式，默认样式：
>     - SaveIconStyle默认样式为Lines；
>     - SaveDescription默认样式为Paste；
>     - ButtonType默认样式为Capsule。
> - icon、text、buttonType不支持动态修改。

## 组件事件

### func onClick((ClickEvent, SaveButtonOnClickResult) -> Unit)

```cangjie
public func onClick (callback: (ClickEvent, SaveButtonOnClickResult) -> Unit): This
```

**功能：** 点击动作触发该回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback |([ClickEvent](../../source_zh_cn/arkui-cj/cj-universal-event-click.md#class-clickevent), [SaveButtonOnClickResult](#enum-savebuttononclickresult)) -> Unit | 是| - | 点击动作触时，触发该回调函数。<br> 参数一：点击事件对象；<br>参数二：存储权限的授权结果。|