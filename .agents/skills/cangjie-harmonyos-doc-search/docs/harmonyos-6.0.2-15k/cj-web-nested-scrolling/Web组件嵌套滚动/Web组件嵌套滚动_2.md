func build() {
        Flex() {
            Scroll(this.scrollerForScroll) {
                Column(5) {
                    Row() {
                        Text('切换前滚动模式').fontSize(5)
                        Button("SELF_ONLY").onClick {
                            evt => this.nestedScrollModeF = this.nestedScrollMode0
                        }.fontSize(5)
                        Button("SELF_FIRST").onClick {
                            evt => this.nestedScrollModeF = this.nestedScrollMode1
                        }.fontSize(5)
                        Button("PARENT_FIRST").onClick {
                            evt => this.nestedScrollModeF = this.nestedScrollMode2
                        }.fontSize(5)
                        Button("PARALLEL").onClick {
                            evt => this.nestedScrollModeF = this.nestedScrollMode3
                        }.fontSize(5)
                    }
                    Row() {
                        Text('切换后滚动模式').fontSize(5)
                        Button("SELF_ONLY").onClick {
                            evt => this.nestedScrollModeB = this.nestedScrollMode0
                        }.fontSize(5)
                        Button("SELF_FIRST").onClick {
                            evt => this.nestedScrollModeB = this.nestedScrollMode1
                        }.fontSize(5)
                        Button("PARENT_FIRST").onClick {
                            evt => this.nestedScrollModeB = this.nestedScrollMode2
                        }.fontSize(5)
                        Button("PARALLEL").onClick {
                            evt => this.nestedScrollModeB = this.nestedScrollMode3
                        }.fontSize(5)
                    }
                    Text('当前内嵌前滚动模式 scrollForward ---nestedScrollModeF').fontSize(10)
                    Text('当前内嵌后滚动模式  scrollBackward ---nestedScrollModeB').fontSize(10)
                    Text("Scroll Area").width(100.percent).height(10.percent).backgroundColor(0X330000FF).fontSize(16).
                        textAlign(TextAlign.Center)
                    Text("Scroll Area").width(100.percent).height(10.percent).backgroundColor(0X330000FF).fontSize(16).
                        textAlign(TextAlign.Center)
                    Text("Scroll Area").width(100.percent).height(10.percent).backgroundColor(0X330000FF).fontSize(16).
                        textAlign(TextAlign.Center)
                    // src改为有效地址或者资源文件
                    Web(src: "www.example.com", controller: this.controller).nestedScroll(
                        scrollForward: this.nestedScrollModeF,
                        scrollBackward: this.nestedScrollModeB
                    ).height(40.percent).width(100.percent)

                    Text("Scroll Area").width(100.percent).height(20.percent).backgroundColor(0X330000FF).fontSize(16).
                        textAlign(TextAlign.Center)
                    Text("Scroll Area").width(100.percent).height(20.percent).backgroundColor(0X330000FF).fontSize(16).
                        textAlign(TextAlign.Center)
                    // src改为有效地址或者资源文件
                    Web(src: "www.example.com", controller: this.controller2).nestedScroll(
                        scrollForward: this.nestedScrollModeF,
                        scrollBackward: this.nestedScrollModeB
                    ).height(40.percent).width(90.percent)
                    Text("Scroll Area").width(100.percent).height(20.percent).backgroundColor(0X330000FF).fontSize(16).
                        textAlign(TextAlign.Center)
                }.width(95.percent).border(width: 5)
            }.width(100.percent).height(120.percent).border(width: 5).scrollable(this.scrollDirection)
        }.width(100.percent).height(100.percent).backgroundColor(0xDCDCDC).padding(20)
    }
}
```

![web-nested-scrolling](figures/web-nested-scrolling.gif)