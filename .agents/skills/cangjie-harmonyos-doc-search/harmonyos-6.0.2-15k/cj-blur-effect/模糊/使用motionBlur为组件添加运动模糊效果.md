## 使用motionBlur为组件添加运动模糊效果

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.__GenerateResource__

@Entry
@Component
class EntryView {
    @State
    var widthSize: Int64 = 400
    @State
    var heightSize: Int64 = 320
    @State
    var flag: Bool = true
    @State
    var radius: Float64 = 0.0
    @State
    var x: Float64 = 0.0
    @State
    var y: Float64 = 0.0

    func build() {
        Column() {
            Column() {
                Image(@r(app.media.share)).onClick(
                    {
                        evt =>
                        this.radius = 5.0
                        this.x = 0.5
                        this.y = 0.5
                        if (this.flag) {
                            this.widthSize = 100
                            this.heightSize = 80
                        } else {
                            this.widthSize = 400
                            this.heightSize = 320
                        }
                        this.flag = !this.flag
                    }
                ).animationStart(AnimateParam(duration: 2000, curve: Curve.EaseInOut, onFinish: {=> this.radius = 0.0})).
                    width(this.widthSize).height(this.heightSize).animationEnd().motionBlur(
                    MotionBlurOptions(radius: this.radius, anchor: MotionBlurAnchor(x: this.x, y: this.y)))
            }
        }
    }
}
```

![motionBlurTest](./figures/motionBlurTest.gif)