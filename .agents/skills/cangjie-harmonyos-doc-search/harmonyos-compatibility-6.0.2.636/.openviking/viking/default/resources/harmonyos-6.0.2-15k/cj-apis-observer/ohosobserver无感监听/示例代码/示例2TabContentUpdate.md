### 示例2（TabContentUpdate）

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import ohos.state_macro_manage.*
import kit.UIKit.*

class TabContentInfoCallback1 <: Callback1Argument<TabContentInfo> {
    public init() {}
    public open func invoke(val: TabContentInfo): Unit {
        AppLog.info("TabContentUpdate1 tabContentId: ${val.tabContentId}")
        AppLog.info("TabContentUpdate1 tabContentUniqueId: ${val.tabContentUniqueId}")
        match (val.state) {
            case ON_SHOW => AppLog.info("TabContentUpdate1 ON_SHOW")
            case ON_HIDE => AppLog.info("TabContentUpdate1 ON_HIDE")
            case _ => throw Exception()
        }
        AppLog.info("TabContentUpdate1 id:${val.id}")
        AppLog.info("TabContentUpdate1 uniqueId:${val.uniqueId}")
    }
}

class TabContentInfoCallback2 <: Callback1Argument<TabContentInfo> {
    public init() {}
    public open func invoke(val: TabContentInfo): Unit {
        AppLog.info("TabContentUpdate2 tabContentId: ${val.tabContentId}")
        AppLog.info("TabContentUpdate2 tabContentUniqueId: ${val.tabContentUniqueId}")
        match (val.state) {
            case ON_SHOW => AppLog.info("TabContentUpdate2 ON_SHOW")
            case ON_HIDE => AppLog.info("TabContentUpdate2 ON_HIDE")
            case _ => throw Exception()
        }
        AppLog.info("TabContentUpdate2 id:${val.id}")
        AppLog.info("TabContentUpdate2 uniqueId:${val.uniqueId}")
    }
}

@Entry
@Component
class EntryView {
    let tabContentUpdate1 = TabContentInfoCallback1()
    let tabContentUpdate2 = TabContentInfoCallback2()

    func build() {
        Column {
            Button("observer Callback1 on").onClick({
                => on(ObserverType.OBSERVER_TAB_CONTENT_UPDATE, tabContentUpdate1)
            })
            Button("observer Callback2 on").onClick({
                => on(ObserverType.OBSERVER_TAB_CONTENT_UPDATE, tabContentUpdate2)
            })
            Button("observer Callback1 off").onClick(
                {
                => off(ObserverType.OBSERVER_TAB_CONTENT_UPDATE, tabContentUpdate1)
            })
            Button("observer Callback2 off").onClick(
                {
                => off(ObserverType.OBSERVER_TAB_CONTENT_UPDATE, tabContentUpdate2)
            })
            Button("observer Callback all off").onClick({
                => off(ObserverType.OBSERVER_TAB_CONTENT_UPDATE)
            })

            Button("observer with Tabs1 Callback1 on").onClick(
                {
                => on(ObserverType.OBSERVER_TAB_CONTENT_UPDATE, ObserverOptions("Tabs1"), tabContentUpdate1)
            })
            Button("observer with Tabs2 Callback1 on").onClick(
                {
                => on(ObserverType.OBSERVER_TAB_CONTENT_UPDATE, ObserverOptions("Tabs2"), tabContentUpdate1)
            })
            Button("observer with Tabs2 Callback2 on").onClick(
                {
                => on(ObserverType.OBSERVER_TAB_CONTENT_UPDATE, ObserverOptions("Tabs2"), tabContentUpdate2)
            })
            Button("observer with Tabs1 Callback1 off").onClick(
                {
                => off(ObserverType.OBSERVER_TAB_CONTENT_UPDATE, ObserverOptions("Tabs1"), tabContentUpdate1)
            })
            Button("observer with Tabs2 Callback all off").onClick(
                {
                => off(ObserverType.OBSERVER_TAB_CONTENT_UPDATE, ObserverOptions("Tabs2"))
            })

            Tabs() {
                TabContent() {
                    Column {
                        Text("TabContent1")
                    }
                }.id("TabContent1-1")

                TabContent() {
                    Column {
                        Text("TabContent2")
                    }
                }.id("TabContent1-2")

                TabContent() {
                    Column {
                        Text("TabContent3")
                    }
                }.id("TabContent1-3")
            }.width(100.percent).height(20.percent).id("Tabs1")

            Tabs() {
                TabContent() {
                    Column {
                        Text("TabContent1")
                    }
                }.id("TabContent2-1")

                TabContent() {
                    Column {
                        Text("TabContent2")
                    }
                }.id("TabContent2-2")

                TabContent() {
                    Column {
                        Text("TabContent3")
                    }
                }.id("TabContent2-3")
            }.width(100.percent).height(20.percent).id("Tabs2")
        }.height(100.percent)
    }
}
```