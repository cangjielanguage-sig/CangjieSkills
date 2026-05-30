### func getImageData(Int64, Int64, Int64, Int64)

```cangjie
public func getImageData(sx: Int64, sy: Int64, sw: Int64, sh: Int64): ImageData
```

**功能：** 以当前canvas指定区域内的像素创建ImageData对象，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sx|Int64|是|-|需要输出的区域的左上角x坐标。<br> 默认单位：vp。|
|sy|Int64|是|-|需要输出的区域的左上角y坐标。<br> 默认单位：vp。|
|sw|Int64|是|-|需要输出的区域的宽度。<br> 默认单位：vp。|
|sh|Int64|是|-|需要输出的区域的高度。<br> 默认单位：vp。|

**返回值：**

|类型|说明|
|:----|:----|
|[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)|新的ImageData对象。|

**示例：**

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.image.*
import ohos.resource_manager.*
import ohos.ability.getStageContext

@Entry
@Component
class EntryView {
    private let settings: RenderingContextSettings = RenderingContextSettings(antialias: true)
    private let context: CanvasRenderingContext2D = CanvasRenderingContext2D(this.settings)
    private let buffer: Array<UInt8> = loadMedia(
        AppResource("com.example.myapplication", "entry", Int32(@r(app.media.icon).id)))
    private let imageSource: ImageSource = createImageSource(buffer)
    private let pix: PixelMap = imageSource.createPixelMap()
    private let img: ImageBitmap = ImageBitmap(pix)
    @State
    var message: String = ""
    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center)
        ) {
            Canvas(this.context).width(100.percent).height(100.percent).backgroundColor(0xffff00).onReady(
                {
                    =>
                    this.context.drawImage(this.img, 0, 0, 130, 130)
                    let imagedata = this.context.getImageData(50, 50, 130, 130)
                    this.context.putImageData(imagedata, 150, 150)
                }
            )
        }.width(100.percent).height(100.percent)
    }

    // abilityContext需要先在MainAbility中声明，然后在onCreate时初始化。具体如下
    // MainAbility中定义abilityContext：
    //     public static var abilityContext: Option<UIAbilityContext> = Option<UIAbilityContext>.None
    // MainAbility.onCreate方法中插入：
    //     abilityContext = Option<UIAbilityContext>.Some(this.context)
    public static func loadMedia(res: AppResource): Array<UInt8> {
        let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
        let resourceManager = ResourceManager.getResourceManager(stageContext)
        resourceManager.getMediaContent(res, 0)
    }
}
```

![getImageData](./figures/canvasrenderingcontext_25.png)