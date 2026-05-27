### 示例8（通过objectRepeat设置图片的重复样式）

该示例通过通过[objectRepeat](#func-objectfitimagefit)接口在竖直轴上重复绘制图片。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import kit.LocalizationKit.AppResource
import kit.LocalizationKit.__GenerateResource__
import ohos.component.ImageFit

@Entry
@Component
class EntryView {
    @State
    var borderRadiusValue: Int64 = 10
    func build() {
        Column() {
            Image(@r(app.media.image)).objectRepeat(ImageRepeat.Y).width(120).height(300).objectFit(ImageFit.Contain).
                borderWidth(1)
        }.height(100.percent).width(100.percent)
    }
}
```

![image8](figures/image8.png)

### 示例9（设置SVG图片的填充颜色）

该示例通过通过[fillColor](#func-fillcolorresourcecolor)接口在竖直轴上重复绘制图片。

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
    @State
    var borderRadiusValue: Int64 = 10
    func build() {
        Column() {
            Text("不设置fillColor")
            Image(@r(app.media.svg)).width(100).height(100).objectFit(ImageFit.Contain).borderWidth(1)
            Text("fillColor传入Color.ORANGE")
            Image(@r(app.media.svg)).width(100).height(100).objectFit(ImageFit.Contain).borderWidth(1).fillColor(
                Color.ORANGE)
            Text("fillColor传入Color.BLUE")
            Image(@r(app.media.svg)).width(100).height(100).objectFit(ImageFit.Contain).borderWidth(1).fillColor(
                Color.BLUE)
            Text("fillColor传入Color.RED")
            Image(@r(app.media.svg)).width(100).height(100).objectFit(ImageFit.Contain).borderWidth(1).fillColor(
                Color.RED)
        }.height(100.percent).width(100.percent)
    }
}
```

![image9](figures/image9.png)