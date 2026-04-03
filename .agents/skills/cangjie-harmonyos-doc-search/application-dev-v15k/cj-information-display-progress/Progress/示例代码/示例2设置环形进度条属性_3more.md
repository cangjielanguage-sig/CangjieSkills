### 示例2（设置环形进度条属性）

该示例通过style接口的strokeWidth、shadow属性，实现了环形进度条视觉属性设置功能。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    let colorStop0 = ColorStop(0X02fd03, 0.5)
    let colorStop1 = ColorStop(Color.BLUE, 1.0)
    let ringStyle0 = RingStyleOptions(strokeWidth: 20.vp)
    let ringStyle1 = RingStyleOptions(strokeWidth: 20.vp, shadow: true)
    func build() {
        Column(15) {
            Text("Gradient Color").fontSize(20).fontColor(0xCCCCCC).width(90.percent)
            Row(40) {
                Progress(value: 70.0, `type`: ProgressType.Ring).width(100).style(ringStyle0).color(
                    [colorStop0, colorStop1])
            }
            Text("Shadow").fontSize(20).fontColor(0xCCCCCC).width(90.percent)
            Row(40) {
                Progress(value: 70.0, `type`: ProgressType.Ring).width(120).color(Color.BLUE).style(ringStyle1)
            }
        }
    }
}
```

![progress2](figures/progress2.jpg)

### 示例3（设置环形进度条动画）

该示例通过style接口的status、enableScanEffect属性，实现了环形进度条动效的开关功能。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import ohos.state_manage.*
import ohos.state_macro_manage.*
import ohos.component.*
import ohos.base.*
import ohos.resource_manager.*

@Entry
@Component
class EntryView {
    let ringStyle0 = RingStyleOptions(strokeWidth: 20.vp, status: ProgressStatus.LOADING)
    let ringStyle1 = RingStyleOptions(strokeWidth: 20.vp, enableScanEffect: true)
    func build() {
        Column(15) {
            Text("Loading Effect").fontSize(20).fontColor(0xCCCCCC).width(90.percent)
            Row(40) {
                Progress(value: 0.0, `type`: ProgressType.Ring).width(100).style(ringStyle0).color(Color.BLUE)
            }
            Text("Shadow").fontSize(20).fontColor(0xCCCCCC).width(90.percent)
            Row(40) {
                Progress(value: 30.0, `type`: ProgressType.Ring).width(100).color(0X02fd03).style(ringStyle1)
            }
        }
    }
}
```

![progress3](figures/progress3.gif)

### 示例4（设置胶囊形进度条属性）

该示例通过style接口的borderColor、borderWidth、content、font、fontColor、enableScanEffect、showDefaultPercentage属性，实现了胶囊形进度条视觉属性设置功能。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Column(15) {
            Row(40) {
                Progress(value: 100.0, total: 100.0, `type`: ProgressType.Capsule).width(100).height(50).style(
                    CapsuleStyleOptions(
                        content: 'Installing...',
                        font: Fonts(size: 13, style: FontStyle.Normal),
                        borderColor: Color.BLUE,
                        borderWidth: 1,
                        fontColor: Color.GRAY,
                        enableScanEffect: false,
                        showDefaultPercentage: false
                    )
                )
            }
        }.width(100.percent).padding(top: 5)
    }
}
```

![progress4](figures/progress4.png)