# 按键事件

按键事件指组件与键盘、遥控器等按键设备交互时触发的事件，适用于所有可获焦组件，例如Button。对于Text和Image等默认不可获焦的组件，当前暂不支持，后续可以设置focusable属性为true后使用按键事件。

## 权限列表

无

## func onKeyEvent((KeyEvent)->Unit)

```cangjie
public open func onKeyEvent(callback: (KeyEvent)->Unit): This
```

**功能：** 绑定该方法的组件获焦后，按键动作触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([KeyEvent](#class-keyevent))->Unit|是|-|绑定该方法的组件获焦后，按键动作触发该回调。|