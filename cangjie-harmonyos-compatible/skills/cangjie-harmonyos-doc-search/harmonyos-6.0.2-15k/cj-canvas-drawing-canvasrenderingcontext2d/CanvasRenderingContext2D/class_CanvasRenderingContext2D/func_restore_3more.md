### func restore()

```cangjie
public func restore(): Unit
```

**功能：** 对保存的绘图上下文进行恢复。

> **说明：**
>
> - 当restore()次数未超出save()次数时，从栈中弹出存储的绘制状态并恢复CanvasRenderingContext2D对象的属性、剪切路径和变换矩阵的值。
> - 当restore()次数超出save()次数时，此方法不做任何改变。
> - 当没有保存状态时，此方法不做任何改变。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**示例：**

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    private let settings: RenderingContextSettings = RenderingContextSettings(antialias: true)
    private let context: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)
    @State
    var toDataUrl: String = ""

    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.context.save() // save the default state
                    this.context.fillStyle(0x00ff00)
                    this.context.fillRect(20, 20, 100, 100)
                    this.context.restore() // restore to the default state
                    this.context.fillRect(150, 75, 100, 100)
                }
            )
            Text(this.toDataUrl)
        }.width(100.percent).height(100.percent)
    }
}
```

![restore](./figures/canvasrenderingcontext_38.png)

### func restoreLayer()

```cangjie
public func restoreLayer(): Unit
```

**功能：** 恢复图像变换和裁剪状态至saveLayer前的状态，并将图层绘制在canvas上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**示例：**

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    private let settings: RenderingContextSettings = RenderingContextSettings(antialias: true)
    private let context: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)
    @State
    var message: String = ""
    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.context.fillStyle(0x0000ff)
                    this.context.fillRect(50, 100, 300, 100)
                    this.context.fillStyle(0x00ffff)
                    this.context.fillRect(50, 150, 300, 100)
                    this.context.globalCompositeOperation(CompositeOperation.DestinationOver)
                    this.context.saveLayer()
                    this.context.globalCompositeOperation(CompositeOperation.SourceOver)
                    this.context.fillStyle(0xff0000)
                    this.context.fillRect(100, 50, 100, 300)
                    this.context.fillStyle(0x00ff00)
                    this.context.fillRect(150, 50, 100, 300)
                    this.context.restoreLayer()
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![restoreLayer](./figures/canvasrenderingcontext_40.png)

### func rotate(Float64)

```cangjie
public func rotate(angle: Float64): Unit
```

**功能：** 针对当前坐标轴进行顺时针旋转。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|angle|Float64|是|-|设置顺时针旋转的弧度值，可以通过Float64.PI / 180将角度转换为弧度值。<br>单位：弧度。|