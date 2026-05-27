### 示例1（ScrollEvent）

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import ohos.state_macro_manage.*
import kit.UIKit.*

class ScrollEventCallback1 <: Callback1Argument<ScrollEventInfo> {
    public init() {}
    public open func invoke(val: ScrollEventInfo): Unit {
        AppLog.info("ScrollEvent1 id:${val.id}")
        AppLog.info("ScrollEvent1 uniqueId:${val.uniqueId}")
        match (val.scrollEvent) {
            case SCROLL_START => AppLog.info("ScrollEvent1 SCROLL_START")
            case SCROLL_STOP => AppLog.info("ScrollEvent1 SCROLL_STOP")
            case _ => throw Exception()
        }
        AppLog.info("ScrollEvent1 offset:${val.offset}")
    }
}

class ScrollEventCallback2 <: Callback1Argument<ScrollEventInfo> {
    public init() {}
    public open func invoke(val: ScrollEventInfo): Unit {
        AppLog.info("ScrollEvent2 id:${val.id}")
        AppLog.info("ScrollEvent2 uniqueId:${val.uniqueId}")
        match (val.scrollEvent) {
            case SCROLL_START => AppLog.info("ScrollEvent2 SCROLL_START")
            case SCROLL_STOP => AppLog.info("ScrollEvent2 SCROLL_STOP")
            case _ => throw Exception()
        }
        AppLog.info("ScrollEvent2 offset:${val.offset}")
    }
}

@Entry
@Component
class EntryView {
    let scrollEvent1 = ScrollEventCallback1()
    let scrollEvent2 = ScrollEventCallback2()

    func build() {
        Column {
            Column {
                Button("observer Callback1 on").onClick({
                    => on(ObserverType.OBSERVER_SCROLL_EVENT, scrollEvent1)
                })
                Button("observer Callback2 on").onClick({
                    => on(ObserverType.OBSERVER_SCROLL_EVENT, scrollEvent2)
                })
                Button("observer Callback1 off").onClick({
                    => off(ObserverType.OBSERVER_SCROLL_EVENT, scrollEvent1)
                })
                Button("observer Callback2 off").onClick({
                    => off(ObserverType.OBSERVER_SCROLL_EVENT, scrollEvent2)
                })
                Button("observer Callback all off").onClick({
                    => off(ObserverType.OBSERVER_SCROLL_EVENT)
                })
                Button("observer with Scroll1 Callback1 on").onClick(
                    {
                    => on(ObserverType.OBSERVER_SCROLL_EVENT, ObserverOptions("Scroll1"), scrollEvent1)
                })
                Button("observer with Scroll2 Callback1 on").onClick(
                    {
                    => on(ObserverType.OBSERVER_SCROLL_EVENT, ObserverOptions("Scroll2"), scrollEvent1)
                })
                Button("observer with Scroll2 Callback2 on").onClick(
                    {
                    => on(ObserverType.OBSERVER_SCROLL_EVENT, ObserverOptions("Scroll2"), scrollEvent2)
                })
                Button("observer with Scroll1 Callback1 off").onClick(
                    {
                    => off(ObserverType.OBSERVER_SCROLL_EVENT, ObserverOptions("Scroll1"), scrollEvent1)
                })
                Button("observer with Scroll2 Callback all off").onClick(
                    {
                    => off(ObserverType.OBSERVER_SCROLL_EVENT, ObserverOptions("Scroll2"))
                })
            }.width(100.percent)

            Scroll() {
                Column {
                    Text("Text").fontSize(100)
                    Text("Text").fontSize(100)
                    Text("Text").fontSize(100)
                    Text("Text").fontSize(100)
                    Text("Text").fontSize(100)
                    Text("Text").fontSize(100)
                    Text("Text").fontSize(100)
                    Text("Text").fontSize(100)
                    Text("Text").fontSize(100)
                    Text("Text").fontSize(100)
                }
            }.height(40.percent).width(100.percent).id("Scroll1")

            Scroll() {
                Column {
                    Text("Text").fontSize(100)
                    Text("Text").fontSize(100)
                    Text("Text").fontSize(100)
                    Text("Text").fontSize(100)
                    Text("Text").fontSize(100)
                    Text("Text").fontSize(100)
                    Text("Text").fontSize(100)
                    Text("Text").fontSize(100)
                    Text("Text").fontSize(100)
                    Text("Text").fontSize(100)
                }
            }.height(40.percent).width(100.percent).id("Scroll2")
        }.height(100.percent)
    }
}
```