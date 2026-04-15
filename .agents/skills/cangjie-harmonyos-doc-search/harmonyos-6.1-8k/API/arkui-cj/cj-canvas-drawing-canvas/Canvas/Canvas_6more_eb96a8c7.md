# Canvas

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

提供画布组件，用于自定义绘制图形。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

不支持子组件。

## 创建组件

### init(?CanvasRenderingContext2D)

```cangjie
public init(context: ?CanvasRenderingContext2D)
```

**功能：** 构造一个Canvas组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|?[CanvasRenderingContext2D](./cj-canvas-drawing-canvasrenderingcontext2d.md#class-canvasrenderingcontext2d)|是|-|Canvas上下文对象。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。

## 组件事件

### func onReady(?() -> Unit)

```cangjie
public func onReady(callback: ?() -> Unit): This
```

**功能：** Canvas组件构造完成后的事件通知。此时可以开始绘制Canvas。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?() -> Unit|是|-|事件回调。<br>初始值：{ => }。|