### func imageSmoothingEnabled(Bool)

```cangjie
public func imageSmoothingEnabled(enabled: Bool): Unit
```

**功能：** 用于设置绘制图片时是否进行图像平滑度调整。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enabled|Bool|是|-|用于设置绘制图片时是否进行图像平滑度调整，true为启用，false为不启用。|

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
                    this.context.imageSmoothingEnabled(false)
                    this.context.drawImage(this.img, 0, 0, 400, 200)
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

![imageSmoothingEnabled](./figures/canvasrenderingcontext_32.png)