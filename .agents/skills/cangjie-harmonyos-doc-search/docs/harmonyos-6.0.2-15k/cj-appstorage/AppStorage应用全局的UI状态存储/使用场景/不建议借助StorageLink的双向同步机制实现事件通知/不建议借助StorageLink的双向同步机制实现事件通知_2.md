@Entry
@Component
class EntryView {
    // 此处"app.media.startIcon"仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
    let dataList: Array<ViewData> = [ViewData("flower", @r(app.media.startIcon)), ViewData("OMG", @r(app.media.image))]
    var gridScroller: Scroller = Scroller()
    var preIndex: Int64 = -1
    func build() {
        Column() {
            Grid(this.gridScroller) {
                ForEach(
                    this.dataList,
                    itemGeneratorFunc: {
                        item: ViewData, idx: Int64 => GridItem() {
                            TapImage(index: idx, uri: item.uri)
                        }.aspectRatio(1).onClick(
                            {
                                evt =>
                                if (this.preIndex >= 0 && idx == this.preIndex) {
                                    Hilog.info(0, "EmitterTest", "preIndex: ${this.preIndex}, index: ${idx}, red")
                                    let innerEvent: InnerEvent = InnerEvent(UInt32(this.preIndex))
                                    let p = HashMap<String, EventDataType>()
                                    p.add("red", INT64(0))
                                    let eventData = EventData(p)
                                    Emitter.emit(innerEvent, data: eventData)
                                } else if (this.preIndex >= 0 && idx != this.preIndex) {
                                    Hilog.info(0, "EmitterTest", "preIndex: ${this.preIndex}, index: ${idx}, black")
                                    let innerEvent: InnerEvent = InnerEvent(UInt32(this.preIndex))
                                    let p = HashMap<String, EventDataType>()
                                    p.add("black", INT64(0))
                                    let eventData = EventData(p)
                                    Emitter.emit(innerEvent, data: eventData)
                                }
                                this.preIndex = idx
                            }
                        )
                    }
                )
            }
        }
    }
}

@Component
class TapImage {
    @State
    var tapColor: Color = Color.BLACK
    var index: Int64
    var uri: AppResource
    func onTapIndexChange(colorTag: EventData) {
        if (colorTag.data.contains("red")) {
            this.tapColor = Color.RED
        } else {
            this.tapColor = Color.BLACK
        }
    }
    public func aboutToAppear() {
        let innerEvent: InnerEvent = InnerEvent(UInt32(this.index), priority: EventPriority.IMMEDIATE)
        let f = EventCallback(
            "on",
            {
                data: EventData => this.onTapIndexChange(data)
            }
        )
        Emitter.on(innerEvent, f)
    }
    func build() {
        Column() {
            Image(this.uri).objectFit(ImageFit.Cover).border(width: 5, color: this.tapColor)
        }
    }
}
```