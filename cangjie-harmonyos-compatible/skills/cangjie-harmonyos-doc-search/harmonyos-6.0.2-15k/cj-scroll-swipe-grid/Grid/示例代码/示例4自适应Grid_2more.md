### 示例4（自适应Grid）

layoutDirection、maxcount、minCount、cellLength的使用。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import ohos.state_macro_manage.Entry
import ohos.state_macro_manage.Component
import ohos.state_macro_manage.State
import ohos.state_macro_manage.r
import ohos.base.*
import ohos.component.*
import ohos.state_manage.*
import ohos.state_macro_manage.*
import std.collection.{ArrayList, HashMap}

@Entry
@Component
class EntryView {
    @State
    var numbers: ArrayList<String> = ArrayList<String>()

    protected override func aboutToAppear() {
        for (i in 1..31) {
            this.numbers.add("${i}")
        }
    }

    func build() {
        Scroll() {
            Column(5) {
                Blank()
                Text("rowsTemplate、columnsTemplate都不设置layoutDirection、maxcount、minCount、cellLength才生效").
                    fontSize(15).fontColor(0xCCCCCC).width(90.percent)
                Grid() {
                    ForEach(
                        this.numbers,
                        itemGeneratorFunc: {
                            day: String, idx: Int64 => GridItem() {
                                Text(day).fontSize(16).backgroundColor(0xF9CF93)
                            }.width(40).height(80).borderWidth(2).borderColor(Color.RED)
                        }
                    )
                }.height(300).columnsGap(10).rowsGap(10).backgroundColor(0xFAEEE0).maxCount(6).minCount(2).cellLength(0).
                    layoutDirection(GridDirection.Row)
            }.width(90.percent).margin(top: 5, left: 5, right: 5).align(Alignment.Center)
        }
    }
}
```

![griditem](figures/grid3.gif)

### 示例5（双指缩放修改Grid列数）

双指缩放修改Grid列数。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import ohos.state_macro_manage.Entry
import ohos.state_macro_manage.Component
import ohos.state_macro_manage.State
import ohos.state_macro_manage.r
import ohos.base.*
import ohos.component.*
import ohos.state_manage.*
import ohos.state_macro_manage.*
import std.collection.{ArrayList, HashMap}

@Entry
@Component
class EntryView {
    @State
    var numbers: Array<String> = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
        '16', '17', '18', '19']
    @State
    var columns: Int64 = 2

    protected override func aboutToAppear() {
        let lastCount = AppStorage.get<Int64>("columnsCount")
        if (let Some(v) <- lastCount) {
            this.columns = lastCount.getOrThrow()
        }
    }

    func build() {
        Column(5) {
            Row() {
                Text("双指缩放改变列数").height(5.percent).margin(top: 10, left: 20)
            }

            Grid() {
                ForEach(
                    this.numbers,
                    itemGeneratorFunc: {
                        day: String, idx: Int64 => ForEach(
                            this.numbers,
                            itemGeneratorFunc: {
                                day: String, idx: Int64 => GridItem() {
                                    Text(day).fontSize(16).backgroundColor(0xF9CF93).width(100.percent).height(80).
                                        textAlign(TextAlign.Center)
                                }
                            }
                        )
                    }
                )
            }.columnsTemplate(String.fromUtf8("1fr ".toArray().repeat(this.columns))).columnsGap(10).rowsGap(10).width(
                90.percent).scrollBar(BarState.Off).backgroundColor(0xFAEEE0).height(360.vp).cachedCount(3).transition(
                TransitionEffect.OPACITY.animation(AnimateParam(duration: 300, curve: Curve.Smooth))).priorityGesture(
                PinchGesture().onActionEnd(
                    {
                        event: GestureEvent =>
                        AppLog.info("end scale: ${event.scale}")
                        // 手指分开，减少列数以放大Item，触发阈值可以自定义，示例为2
                        if (event.scale > 2.0) {
                            this.columns--
                        } else if (event.scale < 0.6) {
                            this.columns++
                        }
                        // 可以根据设备屏幕宽度设定最大和最小列数，此处以最小1列最大4列为例
                        this.columns = min(4, max(1, this.columns))
                        AppStorage.setOrCreate<Int64>("columnsCount", this.columns)
                    }
                )
            )
        }.width(100.percent).margin(top: 5)
    }
}
```

![griditem](figures/grid4.gif)