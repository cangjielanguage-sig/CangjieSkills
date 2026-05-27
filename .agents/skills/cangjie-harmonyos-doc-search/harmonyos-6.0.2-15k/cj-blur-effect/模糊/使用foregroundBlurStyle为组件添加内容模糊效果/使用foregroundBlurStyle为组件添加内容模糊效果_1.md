## 使用foregroundBlurStyle为组件添加内容模糊效果

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.__GenerateResource__

@Entry
@Component
class EntryView {
    func build() {
        Grid() {
            GridItem() {
                Column() {
                    Column() {
                        Text('原图').fontSize(20).fontColor(Color.WHITE).textAlign(TextAlign.Center).width(100.percent).
                            height(100.percent)
                    }.height(100).aspectRatio(1).borderRadius(10).backgroundImage(src: @r(app.media.scene))

                    Text('原图').fontSize(12).fontColor(Color.BLACK)
                }.height(100.percent).justifyContent(FlexAlign.Start)
            }.height(200).width(200)

            GridItem() {
                Column() {
                    Column() {
                        Text('Thin').fontSize(20).fontColor(Color.WHITE).textAlign(TextAlign.Center).width(100.percent).
                            height(100.percent)
                    }.height(100).aspectRatio(1).borderRadius(10).backgroundImage(src: @r(app.media.scene))
                        // ForegroundBlurStyle.Thin: 为组件添加轻薄材质模糊效果
                        // ThemeColorMode.LIGHT: 固定使用浅色模式效果
                        // AdaptiveColor.DEFAULT: 不使用取色模糊，使用默认的颜色作为蒙版颜色
                        // scale: 背景材质模糊效果程度，默认值是1
                        .
                        foregroundBlurStyle(
                        ForegroundBlurStyle.THIN,
                        options: ForegroundBlurStyleOptions(colorMode: ThemeColorMode.LIGHT,
                            adaptiveColor: AdaptiveColor.DEFAULT, scale: 0.1)
                    )

                    Text('Thin').fontSize(12).fontColor(Color.BLACK)
                }.height(100.percent).justifyContent(FlexAlign.Start)
            }.height(200).width(200)

            GridItem() {
                Column() {
                    Column() {
                        Text('Regular').fontSize(20).fontColor(Color.WHITE).textAlign(TextAlign.Center).width(
                            100.percent).height(100.percent)
                    }.height(100).aspectRatio(1).borderRadius(10).backgroundImage(src: @r(app.media.scene)).
                        foregroundBlurStyle(
                        ForegroundBlurStyle.REGULAR,
                        options: ForegroundBlurStyleOptions(colorMode: ThemeColorMode.LIGHT,
                            adaptiveColor: AdaptiveColor.DEFAULT, scale: 0.1)
                    )

                    Text('Regular').fontSize(12).fontColor(Color.BLACK)
                }.height(100.percent).justifyContent(FlexAlign.Start)
            }.height(200).width(200)

            GridItem() {
                Column() {
                    Column() {
                        Text('Thick').fontSize(20).fontColor(Color.WHITE).textAlign(TextAlign.Center).width(100.percent).
                            height(100.percent)
                    }.height(100).aspectRatio(1).borderRadius(10).backgroundImage(src: @r(app.media.scene)).
                        foregroundBlurStyle(
                        ForegroundBlurStyle.THICK,
                        options: ForegroundBlurStyleOptions(colorMode: ThemeColorMode.LIGHT,
                            adaptiveColor: AdaptiveColor.DEFAULT, scale: 0.1)
                    )

                    Text('Thick').fontSize(12).fontColor(Color.BLACK)
                }.height(100.percent).justifyContent(FlexAlign.Start)
            }.height(200).width(200)

            GridItem() {
                Column() {
                    Column() {
                        Text('BACKGROUND_THIN').fontSize(20).fontColor(Color.WHITE).textAlign(TextAlign.Center).width(
                            100.percent).height(100.percent)
                    }.height(100).aspectRatio(1).borderRadius(10).backgroundImage(src: @r(app.media.scene)).
                        foregroundBlurStyle(
                        ForegroundBlurStyle.BACKGROUND_THIN,
                        options: ForegroundBlurStyleOptions(colorMode: ThemeColorMode.LIGHT,
                            adaptiveColor: AdaptiveColor.DEFAULT, scale: 0.1)
                    )

                    Text('BACKGROUND_THIN').fontSize(12).fontColor(Color.BLACK)
                }.height(100.percent).justifyContent(FlexAlign.Start)
            }.height(200).width(200)

            GridItem() {
                Column() {
                    Column() {
                        Text('BACKGROUND_REGULAR').fontSize(20).fontColor(Color.WHITE).textAlign(TextAlign.Center).width(
                            100.percent).height(100.percent)
                    }.height(100).aspectRatio(1).borderRadius(10).backgroundImage(src: @r(app.media.scene)).
                        foregroundBlurStyle(
                        ForegroundBlurStyle.BACKGROUND_REGULAR,
                        options: ForegroundBlurStyleOptions(colorMode: ThemeColorMode.LIGHT,
                            adaptiveColor: AdaptiveColor.DEFAULT, scale: 0.1)
                    )