# Canvas

提供画布组件，用于自定义绘制图形。

## 子组件

不支持子组件。

## 创建组件

### init(CanvasRenderingContext2D)

```cangjie
public init(context: CanvasRenderingContext2D)
```

**功能：** 初始化一个绘制画布组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[CanvasRenderingContext2D](./cj-canvas-drawing-canvasrenderingcontext2d.md#canvasrenderingcontext2d)|是|-|不支持多个Canvas共用一个[CanvasRenderingContext2D](./cj-canvas-drawing-canvasrenderingcontext2d.md#canvasrenderingcontext2d)对象，具体描述见[CanvasRenderingContext2D](./cj-canvas-drawing-canvasrenderingcontext2d.md#class-canvasrenderingcontext2d)对象。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。

## 组件事件

### func onReady(() -> Unit)

```cangjie
public func onReady(callback: () -> Unit): This
```

**功能：** Canvas组件初始化完成时或者Canvas组件发生大小变化时的事件回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|Canvas组件初始化完成时或者Canvas组件发生大小变化时的事件回调。<br>当该事件被触发时画布被清空，该事件之后Canvas组件宽高确定且可获取，可使用Canvas相关API进行绘制。当Canvas组件仅发生位置变化时，只触发[onAreaChange](./cj-universal-event-areachange.md#func-onareachangearea-area---unit)事件、不触发onReady事件。[onAreaChange](./cj-universal-event-areachange.md#func-onareachangearea-area---unit)事件在onReady事件后触发。|

## 示例代码

### 示例1（使用CanvasRenderingContext2D中的方法）

该示例实现了如何在Canvas组件使用CanvasRenderingContext2D中的方法进行绘制。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    var settings: RenderingContextSettings = RenderingContextSettings(antialias: true)
    var context: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)

    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                => this.context.fillRect(0, 30, 100, 100)
            })
        }.width(100.percent).height(100.percent)
    }
}
```

![canvas1](figures/canvas.png)
