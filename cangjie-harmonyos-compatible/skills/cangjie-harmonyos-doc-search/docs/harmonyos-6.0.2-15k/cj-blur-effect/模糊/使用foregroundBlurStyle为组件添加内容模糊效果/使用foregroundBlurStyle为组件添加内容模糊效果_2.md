Text('BACKGROUND_REGULAR').fontSize(12).fontColor(Color.BLACK)
                }.height(100.percent).justifyContent(FlexAlign.Start)
            }.height(200).width(200)

            GridItem() {
                Column() {
                    Column() {
                        Text('BACKGROUND_THICK').fontSize(20).fontColor(Color.WHITE).textAlign(TextAlign.Center).width(
                            100.percent).height(100.percent)
                    }.height(100).aspectRatio(1).borderRadius(10).backgroundImage(src: @r(app.media.scene)).
                        foregroundBlurStyle(
                        ForegroundBlurStyle.BACKGROUND_THICK,
                        options: ForegroundBlurStyleOptions(colorMode: ThemeColorMode.LIGHT,
                            adaptiveColor: AdaptiveColor.DEFAULT, scale: 0.1)
                    )

                    Text('BACKGROUND_THICK').fontSize(12).fontColor(Color.BLACK)
                }.height(100.percent).justifyContent(FlexAlign.Start)
            }.height(200).width(200)

            GridItem() {
                Column() {
                    Column() {
                        Text('BACKGROUND_ULTRA_THICK').fontSize(20).fontColor(Color.WHITE).textAlign(TextAlign.Center).
                            width(100.percent).height(100.percent)
                    }.height(100).aspectRatio(1).borderRadius(10).backgroundImage(src: @r(app.media.scene)).
                        foregroundBlurStyle(
                        ForegroundBlurStyle.BACKGROUND_ULTRA_THICK,
                        options: ForegroundBlurStyleOptions(colorMode: ThemeColorMode.LIGHT,
                            adaptiveColor: AdaptiveColor.DEFAULT, scale: 0.1)
                    )

                    Text('BACKGROUND_ULTRA_THICK').fontSize(12).fontColor(Color.BLACK)
                }.height(100.percent).justifyContent(FlexAlign.Start)
            }.height(200).width(200)
        }.columnsTemplate("1fr 1fr").rowsTemplate("1fr 1fr 1fr 1fr").width(100.percent).height(100.percent).margin(
            top: 40)
    }
}
```

![blur4](./figures/blur4.png)