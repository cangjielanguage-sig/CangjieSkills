## 多语种场景

当对朗读内容进行标注时，须对标注字符串进行多语种翻译，具体支持的语种和应用本身界面支持的语种保持一致。若采用多个字符串进行朗读内容的拼接，需考虑多语种的情况，避免拼接后朗读错误，例如阿拉伯语从右到左。

```cangjie
import kit.UIKit.*

@Entry
@Component
class EntryView {
    private var multilingual: String = 'It is convenient: 屏幕朗读已开启 and use'
    func build() {
        NavDestination() {
            Column() {
                Flex(
                    FlexParams(
                        direction: FlexDirection.Column,
                        alignItems: ItemAlign.Center,
                        justifyContent: FlexAlign.Center
                    )
                ) {
                    Row() {
                        Text(this.multilingual).fontSize(30).fontColor(Color.BLUE)
                    }.width(80.percent)
                }.width(100.percent).height(100.percent).backgroundColor(Color.WHITE)
            }
        }
    }
}
```

## 控件位置调整场景

移动过程中需要实时播报即将移动到的位置，新位置的播报会打断老位置的播报，放置到确定位置后，需要再播报已经放置的位置信息，尽量保证视障用户耳朵听到的信息和我们通过眼睛看到的信息是一致的。例如，网页书签被托起时，会播报已托起，移动的过程中，根据即将放置的位置播报“移至第几行，第几列”，放置后播报“已放至第几行，第几列”。应用可调用主动播报的接口来进行主动播报。

![图10](./figures/graph10.png)

## 重新设置新焦点位置的场景

1. 适用场景：当前焦点所在的控件消失或者隐藏后，需要重新设置新的焦点位置
2. 说明：一般情况下，新焦点应该在原控件位置的下一个控件上，不应该跳变到前面的控件。应用可以调用主动聚焦的接口对想要聚焦的组件进行主动聚焦。
3. 示例代码：

```cangjie
func build() {
    Column() {
        Button(`待聚焦组件`).id("abc345")
    }
}
```

```cangjie
import kit.AccessibilityKit.*
import ohos.base.AppLog

var eventInfo: EventInfo = EventInfo(
    `type`: EventType.EVENTTYPE_REQUESTFOCUSFORACCESSIBILITY,
    bundleName: "com.example.pagesrouter", triggerAction: Action.ACTION_COMMON)
eventInfo.customId = "abc345"
sendAccessibilityEvent(eventInfo)
AppLog.info("sendAccessibilityEvent")
```

**表2** EventInfo 说明

|属性|类型|说明|例|
|:---|:---|:---|:---|
|\`type`|EventType|主动播报事件类型|announceForAccessibility|
|bundleName|String|目标应用名|当前应用包名|
|triggerAction|Action|触发事件的Action|click或其他都不会有任何影响|
|customId|String|组件id|abc345|