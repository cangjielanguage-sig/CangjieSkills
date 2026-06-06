### 图片插值

当原图分辨率较低并且放大显示时，图片会模糊出现锯齿。这时可以使用interpolation属性对图片进行插值，使图片显示得更清晰。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.*

@Entry
@Component
class EntryView {
    func build() {
        Column() {
            Row() {
                Image(@r(app.media.grass)).width(40.percent).interpolation(ImageInterpolation.None).borderWidth(1).
                    overlay(title: "Interpolation.None", align: Alignment.Bottom, offset: ContentOffset(x: 0.0, y: 20.0)
                ).margin(10)
                Image(@r(app.media.grass)).width(40.percent).interpolation(ImageInterpolation.Low).borderWidth(1).
                    overlay(title: "Interpolation.Low", align: Alignment.Bottom, offset: ContentOffset(x: 0.0, y: 20.0)).
                    margin(10)
            }.width(100.percent).justifyContent(FlexAlign.Center)

            Row() {
                Image(@r(app.media.grass)).width(40.percent).interpolation(ImageInterpolation.Medium).borderWidth(1).
                    overlay(title: "Interpolation.Medium", align: Alignment.Bottom,
                    offset: ContentOffset(x: 0.0, y: 20.0)).margin(10)
                Image(@r(app.media.grass)).width(40.percent).interpolation(ImageInterpolation.High).borderWidth(1).
                    overlay(title: "Interpolation.High", align: Alignment.Bottom, offset: ContentOffset(x: 0.0, y: 20.0)
                ).margin(10)
            }.width(100.percent).justifyContent(FlexAlign.Center)
        }.height(100.percent)
    }
}
```

![image2](figures/image2.png)

### 设置图片重复样式

通过objectRepeat属性设置图片的重复样式方式，重复样式请参考[ImageRepeat](../../API_Reference/source_zh_cn/arkui-cj/cj-common-types.md#enum-imagerepeat)枚举说明。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.*

@Entry
@Component
class EntryView {
    func build() {
        Column(10) {
            Row(5) {
                Image(@r(app.media.ic_public_favor_filled_1)).width(110).height(115).border(width: 1).objectRepeat(
                    ImageRepeat.XY).objectFit(ImageFit.ScaleDown)
                        // 在水平轴和竖直轴上同时重复绘制图片
                        .overlay(title: 'ImageRepeat.XY',
                    align: Alignment.Bottom, offset: ContentOffset(x: 0.0, y: 20.0))
                Image(@r(app.media.ic_public_favor_filled_1)).width(110).height(115).border(width: 1).objectRepeat(
                    ImageRepeat.Y).objectFit(ImageFit.ScaleDown)
                        // 只在竖直轴上重复绘制图片
                        .overlay(title: 'ImageRepeat.Y', align: Alignment.Bottom,
                    offset: ContentOffset(x: 0.0, y: 20.0))
                Image(@r(app.media.ic_public_favor_filled_1)).width(110).height(115).border(width: 1).objectRepeat(
                    ImageRepeat.X).objectFit(ImageFit.ScaleDown)
                        // 只在水平轴上重复绘制图片
                        .overlay(title: 'ImageRepeat.X', align: Alignment.Bottom,
                    offset: ContentOffset(x: 0.0, y: 20.0))
            }
        }.height(150).width(100.percent).padding(8)
    }
}
```

![image3](figures/image3.png)