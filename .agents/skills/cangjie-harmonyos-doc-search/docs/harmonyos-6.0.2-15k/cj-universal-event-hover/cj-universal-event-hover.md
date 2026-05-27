# 悬浮事件

光标滑动或手写笔在屏幕上悬浮移动扫过组件时触发。

> **说明：**
>
> 目前支持通过外接鼠标、手写笔以及触控板触发。

## func onHover((Bool) -> Unit)

```cangjie
public func onHover(callback: (Bool)->Unit): This
```

**功能：** 鼠标进入或退出组件时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Bool)->Unit|是|-|回调函数，鼠标进入或退出组件时触发的回调。<br>鼠标进入时为true，退出时为false。|
