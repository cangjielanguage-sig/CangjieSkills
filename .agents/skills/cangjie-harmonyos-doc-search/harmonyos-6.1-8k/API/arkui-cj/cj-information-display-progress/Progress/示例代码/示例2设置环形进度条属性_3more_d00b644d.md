### 示例2（设置环形进度条属性）

该示例通过style接口的strokeWidth、shadow属性，实现了环形进度条视觉属性设置功能。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*

@Entry
@Component
class EntryView {
    let ringStyle0 = RingStyleOptions(strokeWidth: 20.vp)
    let ringStyle1 = RingStyleOptions(strokeWidth: 20.vp, shadow: true)
    func build() {
        Column(space: 15) {
            Text("Gradient Color").fontSize(20).fontColor(0xCCCCCC).width(90.percent)
            Row(space: 40) {
                Progress(value: 70.0, progressType: ProgressType.Ring)
                    .width(100)
                    .style(ringStyle0)
                    .color(0X02fd03)
            }
            Text("Shadow").fontSize(20).fontColor(0xCCCCCC).width(90.percent)
            Row(space: 40) {
                Progress(value: 70.0, progressType: ProgressType.Ring).width(120).color(Color.Blue).style(ringStyle1)
            }
        }
    }
}
```

![progress2](./figures/progress2.PNG)

### 示例3（设置环形进度条动画）

该示例通过style接口的status、enableScanEffect属性，实现了环形进度条动效的开关功能。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import ohos.arkui.state_management.*
import ohos.arkui.state_macro_manage.*
import ohos.arkui.component.*
import ohos.base.*
import ohos.resource_manager.*

@Entry
@Component
class EntryView {
    let ringStyle0 = RingStyleOptions(strokeWidth: 20.vp, status: ProgressStatus.Loading)
    let ringStyle1 = RingStyleOptions(strokeWidth: 20.vp, enableScanEffect: true)
    func build() {
        Column(space: 15) {
            Text("Loading Effect").fontSize(20).fontColor(0xCCCCCC).width(90.percent)
            Row(space: 40) {
                Progress(value: 0.0, progressType: ProgressType.Ring).width(100).style(ringStyle0).color(Color.Blue)
            }
            Text("Shadow").fontSize(20).fontColor(0xCCCCCC).width(90.percent)
            Row(space: 40) {
                Progress(value: 30.0, progressType: ProgressType.Ring).width(100).color(0X02fd03).style(ringStyle1)
            }
        }
    }
}
```

![progress3](figures/progress3.gif)

### 示例4（设置进度平滑动效）

该示例通过style接口的enableSmoothEffect属性，实现了进度平滑动效开关的功能。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var value: Float64 = 0.0

    func build() {
        Column(space: 10) {
            Text('enableSmoothEffect: true').fontSize(9).fontColor(0xCCCCCC).width(90.percent).margin(5).margin( top: 20 )
            Progress( value: this.value, total: 100.0, progressType: ProgressType.Linear ).style(RingStyleOptions(strokeWidth: 10, enableSmoothEffect: true ))
            Text('enableSmoothEffect: false').fontSize(9).fontColor(0xCCCCCC).width(90.percent).margin(5)
            Progress( value: this.value, total: 100.0, progressType: ProgressType.Linear ).style(RingStyleOptions(strokeWidth: 10, enableSmoothEffect: false ))
            Button('value +10')
                .onClick({ evt =>
                    this.value += 10.0
            }).width(75).height(15).fontSize(9)
        }.width(50.percent).height(100.percent).margin( left: 20 )
    }
}
```

![progress5](figures/progress5.gif)