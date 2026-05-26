### 示例1（加载基本类型图片）

加载png、gif、svg和jpg等基本类型的图片。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import kit.LocalizationKit.__GenerateResource__

@Entry
@Component
class EntryView {
    func build() {
        Flex(FlexParams(direction: FlexDirection.Column, alignItems: ItemAlign.Start)) {
            Row() {
                // 加载png格式图片
                Image(@r(app.media.startIcon)).width(110).height(110).margin(15).overlay(title: "png",
                    align: Alignment.Bottom, offset: ContentOffset(x: 0, y: 20))
                // 加载gif格式图片
                Image(@r(app.media.list)).width(110).height(110).margin(15).overlay(title: "gif",
                    align: Alignment.Bottom, offset: ContentOffset(x: 0, y: 20))
            }
            Row() {
                // 加载svg格式图片
                Image(@r(app.media.svg)).width(110).height(110).margin(15).overlay(title: "svg", align: Alignment.Bottom,
                    offset: ContentOffset(x: 0, y: 20))
                // 加载jpg格式图片
                Image(@r(app.media.startIcon_jpg)).width(110).height(110).margin(15).overlay(title: "jpg",
                    align: Alignment.Bottom, offset: ContentOffset(x: 0, y: 20))
            }
        }.height(320).width(360).padding(right: 10, top: 10)
    }
}
```

![image1](figures/image1.gif)

### 示例2（为图片添加事件）

为图片添加onClick和onFinish事件。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import kit.LocalizationKit.AppResource
import kit.LocalizationKit.__GenerateResource__

@Entry
@Component
class EntryView {
    let imageOne: AppResource = @r(app.media.startIcon)
    let imageTwo = @r(app.media.background)
    let imageThree = @r(app.media.svg_move)
    @State
    var src: AppResource = this.imageOne
    @State
    var src2: AppResource = this.imageThree

    func build() {
        Column() {
            // 为图片添加点击事件，点击完成后加载特定图片
            Image(this.src).width(100).height(100).onClick {
                evt => this.src = this.imageTwo
            }
            // 当加载图片为SVG格式时
            Image(this.src2).width(100).height(100).onFinish {
                // SVG动效播放完成时加载另一张图片
                => this.src2 = this.imageOne
            }
        }
    }
}
```

![image2](figures/image2.gif)

### 示例3（图像设置颜色滤镜效果）

该示例通过colorFilter实现了给图像设置颜色滤镜效果。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import kit.LocalizationKit.AppResource
import kit.LocalizationKit.__GenerateResource__

@Entry
@Component
class EntryView {
    let blueColor = ColorFilter([0.38, 0.0, 0.0, 0.0, 0.0, 0.0, 0.81, 0.0, 0.0, 0.0, 0.0, 0.0, 0.43, 0.0, 0.0, 0.0, 0.0,
        0.0, 1.0, 0.0])
    let colorFilter = ColorFilter([1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0,
        0.0, 1.0, 0.0])

    @State
    var DrawingColorFilterFirst: ColorFilter = blueColor
    @State
    var DrawingColorFilterSecond: ColorFilter = colorFilter

    func build() {
        Column(5) {
            Image(@r(app.media.startIcon)).width(100).height(100).colorFilter(this.DrawingColorFilterFirst).onClick {
                evt => this.DrawingColorFilterFirst = colorFilter
            }
            Image(@r(app.media.startIcon)).width(110).height(110).margin(15).colorFilter(this.DrawingColorFilterSecond).
                onClick {
                evt => this.DrawingColorFilterSecond = blueColor
            }
        }
    }
}
```

![image3](figures/image3.gif)