### func filter(String)

```cangjie
public func filter(filterStr: String): Unit
```

**功能：** 设置图像的滤镜，可以组合任意数量的滤镜。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|filterStr|String|是|-|用于设置图像的滤镜，可以组合任意数量的滤镜。<br>支持的滤镜效果如下： <br> - "none": 无滤镜效果 <br> - "blur"：给图像设置高斯模糊 <br> - "brightness"：给图片应用一种线性乘法，使其看起来更亮或更暗 <br> - "contrast"：调整图像的对比度 <br> - "grayscale"：将图像转换为灰度图像 <br> - "hue-rotate"：给图像应用色相旋转 <br> - "invert"：反转输入图像 <br> - "opacity"：转化图像的透明程度 <br> - "saturate"：转换图像饱和度 <br> - "sepia"：将图像转换为深褐色 <br> 初始值："none"。|

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
                    let ctx = this.context
                    let img = this.img

                    ctx.drawImage(img, 0, 0, 100, 100)

                    ctx.filter('grayscale(50%)')
                    ctx.drawImage(img, 100, 0, 100, 100)

                    ctx.filter('sepia(60%)')
                    ctx.drawImage(img, 200, 0, 100, 100)

                    ctx.filter('saturate(30%)')
                    ctx.drawImage(img, 0, 100, 100, 100)

                    ctx.filter('hue-rotate(90deg)')
                    ctx.drawImage(img, 100, 100, 100, 100)

                    ctx.filter('invert(100%)')
                    ctx.drawImage(img, 200, 100, 100, 100)

                    ctx.filter('opacity(25%)')
                    ctx.drawImage(img, 0, 200, 100, 100)

                    ctx.filter('brightness(0.4)')
                    ctx.drawImage(img, 100, 200, 100, 100)

                    ctx.filter('contrast(200%)')
                    ctx.drawImage(img, 200, 200, 100, 100)

                    ctx.filter('blur(5px)')
                    ctx.drawImage(img, 0, 300, 100, 100)

                    message = ctx.toDataURL()
                }
            )
            Text(this.message)
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

![filter](./figures/canvasrenderingcontext_23.png)