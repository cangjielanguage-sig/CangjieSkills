# 点击事件

点击事件指组件被点击时触发的事件。

## func onClick((ClickEvent) -> Unit)

```cangjie
public open func onClick(callback: (ClickEvent)->Unit): This
```

**功能：** 组件被点击时触发的事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([ClickEvent](#class-clickevent))->Unit|是|-|回调函数，组件被点击时触发该回调。|

> **说明：**
>
> 1.手指按下超过800ms后，不能触发点击事件。
> 2.手指按下之后移动位移超过20px，不能触发点击事件。