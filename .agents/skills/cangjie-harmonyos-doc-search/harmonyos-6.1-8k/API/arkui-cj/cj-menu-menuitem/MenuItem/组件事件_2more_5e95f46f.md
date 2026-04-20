## 组件事件

### func onChange(?(Bool) -> Unit)

```cangjie
public func onChange(callback: ?(Bool) -> Unit): This
```

**功能：** 当选中状态发生变化时，触发该事件。只有手动触发且MenuItem状态改变时才会触发onChange事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?(Bool) -> Unit|是|-|选中状态发生变化时，触发该回调。初始值：{ res: Bool => }。|

## 示例代码

详见[Menu](cj-menu-menu.md#示例代码)组件示例。