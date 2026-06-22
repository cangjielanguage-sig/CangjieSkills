# 菜单控制（Menu）

Menu是菜单接口，一般用于鼠标右键弹窗、点击弹窗等。具体用法请参见[菜单控制](../../cj-universal-attribute-menu/.overview.md)。

使用[bindContextMenu](../../cj-universal-attribute-menu/.overview.md)并设置预览图，菜单弹出时有蒙层，此时为模态。

使用[bindMenu](../../cj-universal-attribute-menu/.overview.md)或bindContextMenu未设置预览图时，菜单弹出无蒙层，此时为非模态。

## 生命周期

|名称|类型|说明|
|:---|:---|:---|
|aboutToAppear|() -> Unit|菜单显示动效前的事件回调。|
|onAppear|() -> Unit|菜单弹出时的事件回调。|
|aboutToDisappear|() -> Unit|菜单退出动效前的事件回调。|
|onDisappear|() -> Unit|菜单消失时的事件回调。|