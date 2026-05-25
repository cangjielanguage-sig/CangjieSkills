### func onWillDisappear(() -> Unit)

```cangjie
public func onWillDisappear(callback: ()->Unit): This
```

**功能：** 当该Destination卸载之前触发的生命周期(有转场动画时，在转场动画开始之前触发)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|() -> Unit|是|-|回调函数，当该Destination卸载之前触发此回调。|