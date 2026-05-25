## 并行识别

并行识别组合手势对应的GestureMode为Parallel。并行识别组合手势中注册的手势将同时进行识别，直到所有手势识别结束。并行识别手势组合中的手势进行识别时互不影响。

以在一个Column组件上绑定点击手势和双击手势组成的并行识别手势为例，由于单击手势和双击手势是并行识别，因此两个手势可以同时进行识别，二者互不干涉。

<!--run-->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import kit.LocalizationKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var count1: Int = 0;
    @State
    var count2: Int = 0;

    func build() {
        Column() {
            Text(
                'Parallel gesture\n' + 'tapGesture count is 1:' + this.count1.toString() + '\ntapGesture count is 2:' +
                this.count2.toString() + '\n').fontSize(28)
        }.height(200).width(200)
            // 以下组合手势为并行并别，单击手势识别成功后，若在规定时间内再次点击，双击手势也会识别成功
            .gesture(
            GestureGroup(
                GestureMode.Parallel,
                [TapGesture(count: 1).onAction({
                    event: GestureEvent => this.count1++
                }), TapGesture(count: 2).onAction({
                    event: GestureEvent => this.count2++
                })]
            )
        )
    }
}
```

![Parallel](figures/combinedGestureParallel.gif)

> **说明：**
>
> - 当由单击手势和双击手势组成一个并行识别组合手势后，在区域内进行点击时，单击手势和双击手势将同时进行识别。
> - 当只有单次点击时，单击手势识别成功，双击手势识别失败。
> - 当有两次点击时，若两次点击相距时间在规定时间内（默认规定时间为300毫秒），触发两次单击事件和一次双击事件。
> - 当有两次点击时，若两次点击相距时间超出规定时间，触发两次单击事件不触发双击事件。

## 互斥识别

互斥识别组合手势对应的GestureMode为Exclusive。互斥识别组合手势中注册的手势将同时进行识别，若有一个手势识别成功，则结束手势识别，其他所有手势识别失败。

以在一个Column组件上绑定单击手势和双击手势组合而成的互斥识别组合手势为例。若先绑定单击手势后绑定双击手势，由于单击手势只需要一次点击即可触发而双击手势需要两次，每次的点击事件均被单击手势消费而不能积累成双击手势，所以双击手势无法触发。若先绑定双击手势后绑定单击手势，则触发双击手势不触发单击手势。

<!--run-->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import kit.LocalizationKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var count1: Int = 0;
    @State
    var count2: Int = 0;

    func build() {
        Column() {
            Text(
                'Exclusive gesture\n' + 'tapGesture count is 1:' + this.count1.toString() + '\ntapGesture count is 2:' +
                this.count2.toString() + '\n').fontSize(28)
        }.height(200).width(200)
            //以下组合手势为互斥并别，单击手势识别成功后，双击手势会识别失败
            .gesture(
            GestureGroup(
                GestureMode.Exclusive,
                [TapGesture(count: 1).onAction({
                    event: GestureEvent => this.count1++
                }), TapGesture(count: 2).onAction({
                    event: GestureEvent => this.count2++
                })]
            )
        )
    }
}
```

![Exclusive](figures/combinedGestureExclusive.gif)

> **说明：**
>
> - 当由单击手势和双击手势组成一个互斥识别组合手势后，在区域内进行点击时，单击手势和双击手势将同时进行识别。
> - 当只有单次点击时，单击手势识别成功，双击手势识别失败。
> - 当有两次点击时，手势响应取决于绑定手势的顺序。若先绑定单击手势后绑定双击手势，单击手势在第一次点击时即宣告识别成功，此时双击手势已经失败。即使在规定时间内进行了第二次点击，双击手势事件也不会进行响应，此时会触发单击手势事件的第二次识别成功。若先绑定双击手势后绑定单击手势，则会响应双击手势不响应单击手势。