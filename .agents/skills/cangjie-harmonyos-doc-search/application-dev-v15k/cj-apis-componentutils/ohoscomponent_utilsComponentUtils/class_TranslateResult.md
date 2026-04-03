## class TranslateResult

```cangjie
public class TranslateResult {
    public TranslateResult(
        public let x: Float32,
        public let y: Float32,
        public let z: Float32
    )
}
```

**功能：** 组件平移信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let x

```cangjie
public let x: Float32
```

**功能：** 设置x轴平移距离。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 19

### let y

```cangjie
public let y: Float32
```

**功能：** 设置y轴平移距离。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 19

### let z

```cangjie
public let z: Float32
```

**功能：** 设置z轴平移距离。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 19

### TranslateResult(Float32, Float32, Float32)

```cangjie
public TranslateResult(
    public let x: Float32,
    public let y: Float32,
    public let z: Float32
)
```

**功能：** 构建一个TranslateResult类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|x轴平移距离。<br>单位: px。|
|y|Float32|是|-|y轴平移距离。<br>单位: px。|
|z|Float32|是|-|z轴平移距离。<br>单位: px。|

**示例：**

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.component_utils.ComponentUtils
import ohos.resource_manager.__GenerateResource__

@Entry
@Component
class EntryView {
    @State
    var message1: String = ""
    @State
    var message2: String = ""
    @State
    var message3: String = ""
    @State
    var x = 120
    @State
    var y = 10
    @State
    var z = 100
    func build() {
        Column {
            Image(@r(app.media.startIcon)).width(300).height(100).scale(x: 0.5, y: 0.5, z: 1.0).translate(x: 20, y: 20,
                z: 20).rotate(
                x: 1.0,
                y: 1.0,
                z: 1.0,
                centerX: 50,
                centerY: 50,
                angle: 300.0
            ).id("image")
            Button("getRectangleById").onClick {
                let info = ComponentUtils.getRectangleById("image")
                message1 = info.size.width.toString()
                message2 = info.scale.x.toString()
                message3 = info.rotate.angle.toString()
            }
            Text(this.message1 + this.message2 + this.message3).margin(20).width(300).height(300).borderWidth(2)
        }
    }
}
```

![componentutils](figures/componentutils.gif)