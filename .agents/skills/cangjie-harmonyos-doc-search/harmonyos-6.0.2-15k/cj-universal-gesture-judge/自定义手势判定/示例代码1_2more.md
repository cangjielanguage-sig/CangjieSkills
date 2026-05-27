## 示例代码1

该示例通过配置onGestureJudgeBegin实现了对长按、滑动和拖动手势的自定义判定。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var message: String = ""

    func build() {
        Column() {
            Row() {
                Text(message).width(200).height(80).backgroundColor(Color.GRAY)
            }.margin(20.vp)
        }.width(100.percent).height(200).borderWidth(2).gesture(TapGesture().onAction({
            evt => message = "tap1"
        })).gesture(LongPressGesture().onAction({
            evt => message = "longPress"
        })).gesture(SwipeGesture().onAction({
            evt => message = "swipe1"
        })).gesture(PanGesture().onActionStart({
            evt => message = "pan1"
        })).onGestureJudgeBegin(
            {
                gestureInfo: GestureInfo, event: BaseGestureEvent =>
                // 若该手势类型为长按手势，转换为长按手势事件
                if (event is LongPressGestureEvent) {
                    let longPressEvent = (event as LongPressGestureEvent).getOrThrow()
                    AppLog.info("repeat = ${longPressEvent.repeat}")
                }
                // 若该手势类型为滑动手势，转换为滑动手势事件
                if (event is SwipeGestureEvent) {
                    let swipeGesture = (event as SwipeGestureEvent).getOrThrow()
                    AppLog.info("angle = ${swipeGesture.angle }")
                }
                // 若该手势类型为拖动手势，转换为拖动手势事件
                if (event is PanGestureEvent) {
                    let panGesture = (event as PanGestureEvent).getOrThrow()
                    AppLog.info("velocity = ${panGesture.velocity  }")
                }
                match (gestureInfo.`type`) {
                    // 返回 REJECT 会使拖动手势失败
                    case GestureTypes.PAN_GESTURE => return GestureJudgeResult.REJECT
                    // 返回 CONTINUE 将保持系统判定。
                    case _ => return GestureJudgeResult.CONTINUE
                }
            }
        )
    }
}
```

![judge1](figures/gesture_judge_1.gif)

## 示例代码2

该示例通过配置onGestureJudgeBegin判定区域决定长按手势和拖拽是否响应。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.prompt_action.PromptAction
import ohos.resource_manager.*

@Entry
@Component
class EntryView {
    var scroller: Scroller = Scroller()

    func build() {
        Scroll(this.scroller) {
            Column(8) {
                Text(
                    "Drag 上下两层 上层绑定长按，下层绑定拖拽。先长按后平移上半区只会响应长按，先长按后平移下半区只会响应拖拽"
                ).width(100.percent).fontSize(20)
                Stack(Alignment.Center) {
                    // Stack的下半区是绑定了拖动手势的图像区域
                    Image(@r(app.media.startIcon)).draggable(true).onDragStart(
                        {
                        _ => PromptAction.showToast(message: "Drag 下半区，Image响应")
                    }).width(200).height(200)
                    // Stack的上半区是绑定了长按手势的浮动区域
                    Stack {
                    }.width(200).height(200).hitTestBehavior(HitTestMode.Transparent).onGestureJudgeBegin(
                        {
                            gestureInfo: GestureInfo, event: BaseGestureEvent =>
                            // 确定tag标志是否有值
                            if (gestureInfo.tag.isEmpty()) {
                                AppLog.info("gestureInfo tag" + gestureInfo.tag.toString())
                            }
                            //如果是长按类型手势，判断点击的位置是否在上半区
                            var isLongPressGesture = match (gestureInfo.`type`) {
                                case GestureTypes.LONG_PRESS_GESTURE => true
                                case _ => false
                            }
                            AppLog.info("gestureInfo type" + isLongPressGesture.toString())
                            if (isLongPressGesture) {
                                if (event.fingerList.size > 0 && event.fingerList[0].localY < 100.0) {
                                    return GestureJudgeResult.CONTINUE
                                } else {
                                    return GestureJudgeResult.REJECT
                                }
                            }
                            return GestureJudgeResult.REJECT
                        }
                    ).gesture(
                        GestureGroup(
                            GestureMode.Parallel,
                            LongPressGesture().onAction(
                                {
                                event: GestureEvent => PromptAction.showToast(
                                    message: "LongPressGesture 长按上半区 上半区响应")
                            }).tag("tap111")
                        )
                    )
                }.width(100.percent)
            }.width(100.percent)
        }
    }
}
```

![judge2](figures/gesture_judge_2.gif)