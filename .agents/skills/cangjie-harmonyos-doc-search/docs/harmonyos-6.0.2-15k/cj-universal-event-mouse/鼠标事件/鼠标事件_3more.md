# 鼠标事件

在单个动作触发多个事件时，事件的顺序是固定的，鼠标事件默认透传。

> 说明：
>
> 目前仅支持通过外接鼠标触发。

## 权限列表

无

## func onMouse(MouseEvent)

```cangjie
public func onMouse(callback: (MouseEvent)->Unit): This
```

**功能：** 当前组件被鼠标按键点击时或者鼠标在组件上移动时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([MouseEvent](#class-mouseevent))->Unit|是|-|组件被鼠标按键点击时或者鼠标在组件上移动时触发该回调。MouseEvent参数包含触发事件时的时间戳、鼠标按键、动作、点击触点在整个屏幕上的坐标和点击触点相对于当前组件的坐标。|