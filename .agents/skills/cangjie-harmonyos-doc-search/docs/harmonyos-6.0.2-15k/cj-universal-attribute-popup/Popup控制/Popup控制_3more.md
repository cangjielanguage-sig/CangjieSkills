# Popup控制

给组件绑定popup弹窗，并设置弹窗内容，交互逻辑和显示状态。

> **说明：**
>
> popup弹窗的显示状态在onStateChange事件回调中反馈，其显隐与组件的创建或销毁无强对应关系。

## func bindPopup(Bool, CustomPopupOptions)

```cangjie
public func bindPopup(
    show!: Bool,
    popup!: CustomPopupOptions
)
```

**功能：** 给组件绑定Popup弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| show | Bool | 是 | - | **命名参数。**  弹窗显示状态。<br/>初始值：false，表示隐藏弹窗。popup弹窗必须等待页面全部构建完成才能展示，因此show不能在页面构建中设置为true，否则会导致popup弹窗显示位置及形状错误。|
| popup | [CustomPopupOptions](#class-custompopupoptions) | 是 | -  | **命名参数。**  配置当前弹窗提示的参数。 |

## func bindPopup(Bool, PopupOptions)

```cangjie
public func bindPopup(
    show!: Bool,
    popup!: PopupOptions
)
```

**功能：** 给组件绑定Popup弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| show | Bool | 是 | -| **命名参数。**  弹窗显示状态。<br/>初始值：false，表示隐藏弹窗。popup弹窗必须等待页面全部构建完成才能展示，因此show不能在页面构建中设置为true，否则会导致popup弹窗显示位置及形状错误。|
| popup | [PopupOptions](#class-popupoptions) | 是 | - | **命名参数。**  配置当前弹窗提示的参数。 |