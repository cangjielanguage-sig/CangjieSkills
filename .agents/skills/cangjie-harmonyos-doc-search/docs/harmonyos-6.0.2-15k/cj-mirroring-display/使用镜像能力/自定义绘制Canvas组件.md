## 自定义绘制Canvas组件

Canvas组件的绘制内容和坐标均不支持镜像能力。已绘制到Canvas组件上的内容并不会跟随系统语言的切换自动做镜像效果。

[CanvasRenderingContext2D](../../API_Reference/source_zh_cn/arkui-cj/cj-canvas-drawing-canvasrenderingcontext2d.md)的文本绘制支持镜像能力，在使用时需要与Canvas组件的通用属性direction（组件显示方向）和CanvasRenderingContext2D的属性direction（文本绘制方向）协同使用。具体规格如下：

1. 优先级：CanvasRenderingContext2D的direction属性 > Canvas组件通用属性direction > 系统语言决定的水平显示方向。
2. Canvas组件本身不会自动跟随系统语言切换镜像效果，需要应用监听到系统语言切换后自行重新绘制。
3. CanvasRenderingContext2D绘制文本时，只有符号等文本会对绘制方向生效，英文字母和数字不响应绘制方向的变化。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.BasicServicesKit.*
import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    private let settings: RenderingContextSettings = RenderingContextSettings(antialias: true)
    private let context: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)

    public func aboutToAppear() {
        let subscriber: CommonEventSubscriber
        let support = Support.COMMON_EVENT_LOCALE_CHANGED
        let subscribeInfo: CommonEventSubscribeInfo = CommonEventSubscribeInfo([support])
        func callback(c: CommonEventData): Unit {
            this.drawText()
        }
        try {
            subscriber = CommonEventManager.createSubscriber(subscribeInfo)
            try {
                // 订阅
                CommonEventManager.subscribe(subscriber, callback)
                AppLog.info("成功订阅语言地区状态变化公共事件")
            } catch (e: BusinessException) {
                AppLog.info("订阅语言地区状态变化公共事件失败. errorCode = ${e.code}, errorMsg = ${e.message}")
            }
        } catch (e: BusinessException) {
            AppLog.info("Failed to create subscriber. errorCode = ${e.code}, errorMsg = ${e.message}")
        }
    }
    public func drawText() {
        this.context.reset()
        this.context.direction(CanvasDirection.inherit)
        this.context.font(size: 30.px, family: "sans-serif")
        this.context.fillText("ab%123&*@", 50, 50)
    }
    func build() {
        Row() {
            Canvas(this.context).direction(Direction.Auto).width(100.percent).height(100.percent).backgroundColor(
                Color.PINK).onReady({
                => this.drawText()
            })
        }.width(100.percent).height(100.percent)
    }
}
```

|**镜像前**|**镜像后**|
|:---|:---|
| ![mirroring-capability](./figures/mirroring_capability3.jpg) | ![mirroring-capability](./figures/mirroring_capability4.jpg) |