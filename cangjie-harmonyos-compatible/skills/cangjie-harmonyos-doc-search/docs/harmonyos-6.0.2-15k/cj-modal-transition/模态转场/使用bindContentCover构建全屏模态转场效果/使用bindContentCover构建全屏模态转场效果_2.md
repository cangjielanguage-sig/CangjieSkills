func build() {
        Column {
            Row {
                Text("确认订单").fontSize(20.vp).fontColor(Color.WHITE).width(100.percent).textAlign(TextAlign.Center).
                    padding(top: 30.vp, bottom: 60.vp)
            }.backgroundColor(0x007dfe)

            Column {
                Row {
                    Column {
                        Text("00:25")
                        Text("始发站")
                    }.width(30.percent)

                    Column {
                        Text("G1234")
                        Text("8时1分")
                    }.width(30.percent)

                    Column {
                        Text("08:26")
                        Text("终点站")
                    }.width(30.percent)
                }
            }.width(92.percent).padding(15.percent).margin(top: -30).backgroundColor(Color.WHITE).shadow(radius: 30,
                color: 0xaaaaaa).borderRadius(10.vp)

            Column {
                Text("+ 选择乘车人").fontSize(18.vp).fontColor(Color.ORANGE).fontWeight(FontWeight.Bold).padding(
                    top: 10.vp, bottom: 10.vp).width(60.percent).textAlign(TextAlign.Center).borderRadius(15.vp).
                    bindContentCover(
                    this.isPresent,
                    this.MyBuilder,
                    ContentCoverOptions(
                        modalTransition: ModalTransition.DEFAULT,
                        onDisappear: {
                            => if (this.isPresent) {
                                this.isPresent = !this.isPresent
                            }
                        }
                    )
                ).onClick({
                    evt => this.isPresent = !this.isPresent
                })
            }.padding(top: 60.vp)
        }
    }
}
```

![bindContentCover](./figures/bindContentCover.gif)