### 示例1（加载基本类型图片）

加载png、gif、svg和jpg等基本类型的图片。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry
import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*
import ohos.i18n.*
import ohos.resource.*

@Entry
@Component
class EntryView {
    func build() {
        Flex(direction: FlexDirection.Column, alignItems: ItemAlign.Start) {
                Row() {
                    // 加载png格式图片
                    Image(@r(app.media.startIcon))
                    .width(110)
                    .height(110)
                    .margin(15)
                    .overlay(value: "png", align: Alignment.Bottom, offset: OverlayOffset(x: 0.0, y: 20.0))
                    // 加载gif格式图片
                    Image(@r(app.media.list))
                    .width(110).height(110).margin(15)
                    .overlay(value: "gif", align: Alignment.Bottom, offset: OverlayOffset(x: 0.0, y: 20.0))
                }
                Row() {
                    // 加载svg格式图片
                    Image(@r(app.media.svg))
                    .width(110)
                    .height(110)
                    .margin(15)
                    .overlay(value: "svg", align: Alignment.Bottom, offset: OverlayOffset(x: 0.0, y: 20.0))
                    // 加载jpg格式图片
                    Image(@r(app.media.startIcon_jpg))
                    .width(110)
                    .height(110)
                    .margin(15)
                    .overlay(value: "jpg", align: Alignment.Bottom, offset: OverlayOffset(x: 0.0, y: 20.0))
                }
            }
            .height(320)
            .width(360)
            .padding(right: 10, top: 10)
    }
}
```

![image1](figures/image1.gif)

### 示例2（为图片添加事件）

为图片添加onClick和onFinish事件。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry
import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*
import ohos.i18n.*
import ohos.resource.*

@Entry
@Component
class EntryView {
    let imageOne: AppResource= @r(app.media.startIcon)
    let imageTwo = @r(app.media.background)
    let imageThree = @r(app.media.svg_move)
    @State var src: AppResource = this.imageOne
    @State var src2: AppResource = this.imageThree

    func build() {
        Column(){
            // 为图片添加点击事件，点击完成后加载特定图片
            Image(this.src)
            .width(100)
            .height(100)
            .onClick({
                    evt =>
                    this.src =this.imageTwo
            })
            // 当加载图片为SVG格式时
            Image(this.src2)
            .width(100)
            .height(100)
            .onFinish({
                    // SVG动效播放完成时加载另一张图片
                    =>
                    this.src2 =this.imageOne
            })
        }
    }
}
```

![image2](figures/image2.gif)