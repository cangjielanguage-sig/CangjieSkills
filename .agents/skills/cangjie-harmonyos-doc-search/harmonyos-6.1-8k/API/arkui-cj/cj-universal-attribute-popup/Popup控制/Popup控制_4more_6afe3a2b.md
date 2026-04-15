# Popup控制

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

给组件绑定popup弹窗，并设置弹窗内容，交互逻辑和显示状态。

> **说明：**
>
> popup弹窗的显示状态在onStateChange事件回调中反馈，其显隐与组件的创建或销毁无强对应关系。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## func bindPopup(?Bool, ?PopupOptions)

```cangjie
func bindPopup(show: ?Bool, popup: ?PopupOptions): T
```

**功能：** 给组件绑定Popup弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| show | ?Bool | 是 | - | 弹窗显示状态。popup弹窗必须等待页面全部构建完成才能展示，因此show不能在页面构建中设置为true，否则会导致popup弹窗显示位置及形状错误。<br>初始值：false。|
| popup | ?[PopupOptions](./cj-common-types.md#class-popupoptions) | 是 | - | 配置当前弹窗提示的参数。 |

**返回值：**

|类型|说明|
|:---|:---|
|T|返回调用此接口的组件实例本身。|

## func bindPopup(?Bool, ?CustomPopupOptions)

```cangjie
func bindPopup(show: ?Bool, popup: ?CustomPopupOptions): T
```

**功能：** 给组件绑定Popup弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| show | ?Bool | 是 | - | 弹窗显示状态。popup弹窗必须等待页面全部构建完成才能展示，因此show不能在页面构建中设置为true，否则会导致popup弹窗显示位置及形状错误。<br>初始值：false。|
| popup | ?[CustomPopupOptions](./cj-common-types.md#class-custompopupoptions) | 是 | - | 配置当前弹窗提示的参数。 |

**返回值：**

|类型|说明|
|:---|:---|
|T|返回调用此接口的组件实例本身。|