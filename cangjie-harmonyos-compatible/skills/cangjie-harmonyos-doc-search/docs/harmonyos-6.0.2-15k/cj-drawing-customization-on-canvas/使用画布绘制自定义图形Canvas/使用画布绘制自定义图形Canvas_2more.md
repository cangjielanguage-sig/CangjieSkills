# 使用画布绘制自定义图形（Canvas）

Canvas提供画布组件，用于自定义绘制图形，开发者使用CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象在Canvas组件上进行绘制，绘制对象可以是基础形状、文本、图片等。

## 使用画布组件绘制自定义图形

可以由以下三种形式在画布绘制自定义图形：

- 使用[CanvasRenderingContext2D](../../API_Reference/source_zh_cn/arkui-cj/cj-canvas-drawing-canvasrenderingcontext2d.md)对象在Canvas画布上绘制。

  <!-- run -->

  ```cangjie
  package ohos_app_cangjie_entry

  import kit.UIKit.*
  import ohos.state_macro_manage.*

  @Entry
  @Component
  class EntryView {
      //用来配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿，true表明开启抗锯齿。
      var settings: RenderingContextSettings = RenderingContextSettings(antialias: true)
      //用来创建CanvasRenderingContext2D对象，通过在canvas中调用CanvasRenderingContext2D对象来绘制。
      var context: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)
      func build() {
          Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
          ) {
              //在canvas中调用CanvasRenderingContext2D对象。
              Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0XF5DC62).onReady(
                  {
                      =>
                      //可以在这里绘制内容。
                      this.context.lineWidth(0.6)
                      this.context.strokeRect(50, 50, 200, 150);
                  }
              )
          }.width(100.percent).height(100.percent)
      }
  }
  ```

  ![Canvas](figures/Canvas.jpg)

- 离屏绘制是指将需要绘制的内容先绘制在缓存区，再将其转换成图片，一次性绘制到Canvas上，加快了绘制速度。过程为：

  1. 通过transferToImageBitmap方法将离屏画布最近渲染的图像创建为一个ImageBitmap对象。
  2. 通过CanvasRenderingContext2D对象的transferFromImageBitmap方法显示给定的ImageBitmap对象。

  具体使用参考[OffscreenCanvasRenderingContext2D](../../API_Reference/source_zh_cn/arkui-cj/cj-canvas-drawing-canvasrenderingcontext2d.md#class-canvasrenderingcontext2d)对象。

  <!-- run -->

  ```cangjie
  package ohos_app_cangjie_entry

  import kit.UIKit.*
  import ohos.state_macro_manage.*

  @Entry
  @Component
  class EntryView {
      //用来配置CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象的参数，包括是否开启抗锯齿。true表明开启抗锯齿
      private let settings: RenderingContextSettings = RenderingContextSettings(antialias: true)
      private let context: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)
      //用来创建OffscreenCanvas对象，width为离屏画布的宽度，height为离屏画布的高度。通过在canvas中调用OffscreenCanvasRenderingContext2D对象来绘制。
      private let offCanvas: OffscreenCanvas = OffscreenCanvas(600.0, 600.0)
      func build() {
          Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
          ) {
              //在canvas中调用CanvasRenderingContext2D对象。
              Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0XF5DC62).onReady(
                  {
                      =>
                      let offContext = this.offCanvas.getContext(contextType: ContextType.type_2d, options: this.settings)
                      //可以在这里绘制内容
                      offContext.strokeRect(50, 50, 200, 150)
                      //将离屏绘值渲染的图像在普通画布上显示
                      let image = this.offCanvas.transferToImageBitmap()
                      this.context.lineWidth(5)
                      this.context.transferFromImageBitmap(image)
                  }
              )
          }.width(100.percent).height(100.percent)
      }
  }
  ```

  ![Canvas](figures/Canvas.jpg)

  > **说明：**
  >
  > 在画布组件中，通过CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象在Canvas组件上进行绘制时调用的接口相同，接口参数如无特别说明，单位均为vp。