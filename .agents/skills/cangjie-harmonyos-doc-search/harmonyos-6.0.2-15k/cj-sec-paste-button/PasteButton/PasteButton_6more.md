# PasteButton

安全控件的粘贴按钮，用户通过点击该粘贴按钮，可以临时获取读取剪贴板权限。

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

### init(?PasteIconStyle, ?PasteDescription, ButtonType)

```cangjie
public init(icon!: ?PasteIconStyle = None, text!: ?PasteDescription = None, buttonType!: ButtonType = ButtonType.Capsule)
```

**功能：** 创建包含指定元素的保存按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|?[PasteIconStyle](#enum-pasteiconstyle)|否|None|**命名参数。** 设置保存按钮的图标风格。<br/>不传入该参数表示没有图标。|
|text|?[PasteDescription](#enum-pastedescription)|否|None|**命名参数。** 设置保存按钮的文本描述。<br/>不传入该参数表示没有文字描述。|
|buttonType|[ButtonType](./cj-button-picker-button.md#enum-buttontype)|否|ButtonType.Capsule|**命名参数。** 设置保存按钮的背景样式。<br/>不传入该参数，系统默认提供Capsule类型按钮。|

> **说明：**
>
> - icon或text需至少传入一个。
> - 如果icon、text都不传入，buttonType参数不起效，创建的PasteButton为默认样式，默认样式：
>     - PasteIconStyle默认样式为Lines；
>     - PasteDescription默认样式为Paste；
>     - ButtonType默认样式为Capsule。
> - icon、text、buttonType不支持动态修改。

## 组件事件

### func onClick((ClickEvent, PasteButtonOnClickResult) -> Unit)

```cangjie
public func onClick(callback: (ClickEvent, PasteButtonOnClickResult) -> Unit): This
```

**功能：** 点击动作触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback |([ClickEvent](../../source_zh_cn/arkui-cj/cj-universal-event-click.md#class-clickevent), [PasteButtonOnClickResult](#enum-pastebuttononclickresult)) -> Unit | 是| - | 点击动作触时，触发该回调函数。参数一：点击事件对象；参数二： 剪贴板权限的授权结果，授权后可以读取当前剪贴板内容。|

## 基础类型定义

### enum PasteIconStyle

```cangjie
public enum PasteIconStyle {
    | Lines
}
```

**功能：** 设置粘贴按钮的图标风格。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### Lines

```cangjie
Lines
```

**功能：** 粘贴按钮展示线条样式图标。

**起始版本：** 20

### enum PasteDescription

```cangjie
public enum PasteDescription {
    | Paste
}
```

**功能：** 设置粘贴按钮的文本描述。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### Paste

```cangjie
Paste
```

**功能：** 粘贴按钮的文字描述为“粘贴”。

**起始版本：** 20

### enum PasteButtonOnClickResult

```cangjie
public enum PasteButtonOnClickResult {
    | Success
    | TemporaryAuthorizationFailed
}
```

**功能：** 粘贴按钮点击后权限授权结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### Success

```cangjie
Success
```

**功能：** 粘贴按钮点击后权限授权成功。

**起始版本：** 20

#### TemporaryAuthorizationFailed

```cangjie
TemporaryAuthorizationFailed
```

**功能：** 粘贴按钮点击后权限授权失败。

**起始版本：** 20