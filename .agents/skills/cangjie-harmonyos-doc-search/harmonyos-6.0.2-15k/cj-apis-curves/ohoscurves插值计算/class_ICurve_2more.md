## class ICurve

```cangjie
public class ICurve {}
```

**功能：** 曲线对象类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### func interpolate(Float32)

```cangjie
public func interpolate(fraction: Float32): Float32
```

**功能：** 插值曲线的插值计算函数，可以通过传入的归一化时间参数返回当前的插值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fraction|Float32|是|-|当前的归一化时间参数。<br>取值范围：[0，1]。<br>**说明：**<br>设置的值小于0时，按0处理；设置的值大于1时，按1处理。|

**返回值：**

|类型|说明|
|:----|:----|
|Float32|返回归一化time时间点对应的曲线插值。|

**示例：**

```cangjie
import kit.UIKit.*
// 创建一个默认先慢后快插值曲线
let curve: ICurve = Curves.initCurve(curve: Curve.EaseIn)
// 计算得到时间到一半时的插值
let value: Float32 = curve.interpolate(0.5)
```

## 示例代码

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

let animateOpt1 = AnimateParam(
    duration: 1200,
    curve: Curve.EaseOut
)

@Entry
@Component
class EntryView {
    @State
    var widthSize: Float64 = 200.0
    @State
    var heightSize: Float64 = 200.0
    func build() {
        Column {
            Column().margin(top: 100).width(this.widthSize).height(this.heightSize).backgroundColor(Color.RED).onClick(
                {
                    evt =>
                    let curve = Curves.cubicBezierCurve(0.25, 0.1, 0.25, 1.0)
                    this.widthSize = Float64(curve.interpolate(0.5)) * this.widthSize
                    this.heightSize = Float64(curve.interpolate(0.5)) * this.heightSize
                }
            ).animationStart(animateOpt1)
        }
    }
}
```

![curves](figures/curves_api.gif)