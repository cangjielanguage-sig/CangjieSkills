### func drawImage(PixelMap, Int64, Int64, Int64, Int64, Int64, Int64, Int64, Int64)

```cangjie
public func drawImage(
    pixelMap: PixelMap,
    sx: Int64,
    sy: Int64,
    sWidth: Int64,
    sHeight: Int64,
    dx: Int64,
    dy: Int64,
    dWidth: Int64,
    dHeight: Int64
): Unit
```

**功能：** 进行图像绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pixelMap|[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)|是|-|图片资源，请参考[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)。|
|sx|Int64|是|-|裁切源图像时距离源图像左上角的x坐标值。<br>单位：px。|
|sy|Int64|是|-|裁切源图像时距离源图像左上角的y坐标值。<br>单位：px。|
|sWidth|Int64|是|-|裁切源图像时需要裁切的宽度。<br>单位：px。|
|sHeight|Int64|是|-|裁切源图像时需要裁切的高度。<br>单位：px。|
|dx|Int64|是|-|绘制区域左上角在 x 轴的位置。<br>默认单位：vp。|
|dy|Int64|是|-|绘制区域左上角在 y 轴的位置。<br>默认单位：vp。|
|dWidth|Int64|是|-|绘制区域的宽度。当绘制区域的宽度和裁剪图像的宽度不一致时，将图像宽度拉伸或压缩为绘制区域的宽度。<br>默认单位：vp。|
|dHeight|Int64|是|-|绘制区域的高度。当绘制区域的高度和裁剪图像的高度不一致时，将图像高度拉伸或压缩为绘制区域的高度。<br>默认单位：vp。|

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
                    this.context.drawImage(this.img, 0, 0)
                    this.context.drawImage(this.img, 0, 150, 300, 100)
                    this.context.drawImage(this.img, 0, 0, 500, 500, 0, 300, 400, 200)
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

![drawImage](./figures/canvasrenderingcontext_19.png)