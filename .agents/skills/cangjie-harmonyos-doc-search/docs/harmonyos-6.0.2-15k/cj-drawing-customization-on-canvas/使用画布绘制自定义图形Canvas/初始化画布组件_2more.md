## 初始化画布组件

onReady(() -> Unit)是Canvas组件初始化完成时或者Canvas组件发生大小变化时的事件回调。调用该事件后，可获取Canvas组件的确定宽高，进一步使用CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象调用相关API进行图形绘制。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    //settings用来配置CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象的参数，包括是否开启抗锯齿。antialias赋值为true表明开启抗锯齿。
    private let settings: RenderingContextSettings = RenderingContextSettings(antialias: true)
    private let context: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)

    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            //在Canvas中使用CanvasRenderingContext2D对象。
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0XF5DC62).onReady(
                {
                    =>
                    this.context.fillStyle(0X0097D4)
                    this.context.fillRect(50, 50, 100, 100)
                }
            )
        }.width(100.percent).height(100.percent)
    }
}
```

![Canvas1](figures/Canvas1.jpg)

## 画布组件绘制方式

调用Canvas组件生命周期接口onReady()之后，开发者可以直接使用Canvas组件进行绘制。或者可以脱离Canvas组件和onReady()生命周期，单独定义Path2d对象构造理想的路径，并在onReady()调用之后使用Canvas组件进行绘制。

- 通过CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象直接调用相关API进行绘制。

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

      func build() {
          Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
          ) {
              Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0XF5DC62).onReady(
                  {
                      =>
                      this.context.beginPath()
                      this.context.moveTo(50, 50)
                      this.context.lineTo(280, 160)
                      this.context.stroke()
                  }
              )
          }.width(100.percent).height(100.percent)
      }
  }
  ```

  ![Canvas2](figures/Canvas2.jpg)

- 先单独定义path2d对象构造理想的路径，再通过调用CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象的stroke接口或者fill接口进行绘制，具体使用可以参考path2d。

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

      var region: Path2D = Path2D()
      func build() {
          Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
          ) {
              Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0XF5DC62).onReady(
                  {
                      =>
                      this.region.arc(100.0, 75.0, 50.0, 0.0, 6.28)
                      this.context.stroke(this.region)
                  }
              )
          }.width(100.percent).height(100.percent)
      }
  }
  ```

  ![Canvas3](figures/Canvas3.jpg)