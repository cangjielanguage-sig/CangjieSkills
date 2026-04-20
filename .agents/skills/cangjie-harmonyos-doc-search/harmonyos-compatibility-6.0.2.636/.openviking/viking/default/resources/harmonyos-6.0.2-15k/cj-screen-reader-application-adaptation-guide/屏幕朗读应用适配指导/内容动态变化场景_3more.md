## 内容动态变化场景

1. 适用场景：界面上重要内容在动态变化后，需要实时发送变化后的朗读内容
2. 说明：如果界面上内容发生动态变化且其内容对用户具有必要的提示/告知/指导作用，则其发生变化后需对其变化内容进行朗读，可调用无障碍提供的主动朗读接口进行播报。

![图7](./figures/graph7.png)

```cangjie
import kit.AccessibilityKit.*

var eventInfo: EventInfo = EventInfo(
    `type`: EventType.EVENTTYPE_ANNOUNCEFORACCESSIBILITY,
    bundleName: 'com.example.pagesrouter',
    triggerAction: Action.ACTION_COMMON
)

eventInfo.textAnnouncedForAccessibility = 'test123 text'
sendAccessibilityEvent(eventInfo)
AppLog.info("test123 Succeeded in send event")
```

**表1** EventInfo 说明

|属性|类型|说明|例|
|:---|:---|:---|:---|
|\`type`|EventType|主动播报事件类型|announceForAccessibility|
|bundleName|String|目标应用名|当前应用包名|
|triggerAction|Action|触发事件的Action|click或其他都不会有任何影响|
|textAnnouncedForAccessibility|String|主动播报的内容|test123 text|

## 控件状态变化场景

例如下图，播放暂停按钮对应着两种状态，在状态切换时需要实时变化对应的标注信息。

![图8](./figures/graph8.png)

```cangjie
import ohos.component.*
import ohos.resource_manager.__GenerateResource__
import ohos.prompt_action.PromptAction
import ohos.base.Color

@Entry
@Component
class EntryView {
    @State
    var isPlaying = true
    func play() {
        // play audio file
    }
    func pause() {
        // pause playing of audio file
    }
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
                        Image(if (this.isPlaying) {
                            @r(app.media.play)
                        } else {
                            @r(app.media.pause)
                        }).width(50).height(50).onClick {
                            evt =>
                            PromptAction.showToast(message: if (this.isPlaying) {
                                "Play"
                            } else {
                                "Pause"
                            })
                            this.isPlaying = !this.isPlaying
                            if (this.isPlaying) {
                                this.play()
                            } else {
                                this.pause()
                            }
                        }.accessibilityText(if (this.isPlaying) {
                            "Play"
                        } else {
                            "Pause"
                        }) // 设置可访问性框架的注释信息
                    }
                }.width(100.percent).height(100.percent).backgroundColor(Color.WHITE)
            }
        }
    }
}
```

## 操作错误场景

比如网络连接错误，或者其他警告信息，不能仅仅以颜色区分，需要实时告诉用户错误提示和改进方法。

<img src="./figures/graph9.png" style="zoom:58%">

如下是一个将连接中断播报出来的例子。

```cangjie
import kit.UIKit.*

@Entry
@Component
class EntryView {
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
                        Text('Connection state').fontSize(30)
                    }
                    Row() {
                        Radio(value: 'Radio1', group: 'radioGroup').checked(true).radioStyle(
                            checkedBackgroundColor: Color.RED).height(50).width(50).onChange(
                            {
                            isChecked: Bool => AppLog.info('Radio1 status is ${isChecked}')
                        })
                        Text('Connection interrupted').fontColor(Color.RED)
                    }.width(80.percent).accessibilityGroup(true) //将单选和文本合并到单个对象中
                }.width(100.percent).height(100.percent).backgroundColor(Color.WHITE)
            }
        }
    }
}
```