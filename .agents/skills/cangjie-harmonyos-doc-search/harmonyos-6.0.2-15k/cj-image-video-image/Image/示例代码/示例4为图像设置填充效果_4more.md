### 示例4（为图像设置填充效果）

该示例通过objectFit为图像设置填充效果。

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
                    align: Alignment.Bottom, offset: ContentOffset(x: 0, y: 20)).border(width: 2, color: Color.PINK).
                    objectFit(ImageFit.TOP_START)
                // 加载gif格式图片
                Image(@r(app.media.list)).width(110).height(110).margin(15).overlay(title: "gif",
                    align: Alignment.Bottom, offset: ContentOffset(x: 0, y: 20)).border(width: 2, color: Color.PINK).
                    objectFit(ImageFit.BOTTOM_START)
            }
            Row() {
                // 加载svg格式图片
                Image(@r(app.media.svg)).width(110).height(110).margin(15).overlay(title: "svg", align: Alignment.Bottom,
                    offset: ContentOffset(x: 0, y: 20)).border(width: 2, color: Color.PINK).objectFit(ImageFit.TOP_END)
                // 加载jpg格式图片
                Image(@r(app.media.startIcon_jpg)).width(110).height(110).margin(15).overlay(title: "jpg",
                    align: Alignment.Bottom, offset: ContentOffset(x: 0, y: 20)).border(width: 2, color: Color.PINK).
                    objectFit(ImageFit.CENTER)
            }
        }.height(320).width(360).padding(right: 10, top: 10)
    }
}
```

![image4](figures/image4.gif)

### 示例5（切换显示不同类型图片）

该示例展示了png类型与svg类型作为数据源的显示图片效果。

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
    let imageTwo = @r(app.media.svg_move)
    @State
    var imageSrcIndex: Int64 = 0
    @State
    var imageSrcList: Array<AppResource> = [this.imageOne, this.imageTwo]

    func build() {
        Column() {
            Image(this.imageSrcList[this.imageSrcIndex]).width(100).height(100)
            Button("点击切换Image的src").padding(20).onClick {
                evt => this.imageSrcIndex = (this.imageSrcIndex + 1) % 2
            }
        }
    }
}
```

![image5](figures/image5.gif)

### 示例6（通过sourceSize设置图片解码尺寸）

该示例通过[sourceSize](#func-sourcesizelength-length)接口自定义图片的解码尺寸。

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
            Image(@r(app.media.image)).sourceSize(500, 500).width(300).height(300)
            Image(@r(app.media.image)).sourceSize(10, 10).width(300).height(300).borderWidth(1)
        }.height(100.percent).width(100.percent)
    }
}
```

![image6](figures/image6_api.png)

### 示例7（通过renderMode设置图片的渲染模式）

该示例通过通过[renderMode](#func-rendermodeimagerendermode)接口设置图片渲染模式为黑白模式。

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
            Image(@r(app.media.image)).renderMode(ImageRenderMode.Template).width(300).height(300)
        }.height(100.percent).width(100.percent)
    }
}
```

![image7](figures/image7_api.png)