## struct Size

```cangjie
public struct Size {
    public Size(
        public let width: Float64,
        public let height: Float64
    )
}
```

**功能：** 表示文本所占布局大小。

**起始版本：** 12

### let width

```cangjie
public let width: Float64
```

**功能：** 表示文本布局的宽度。

**类型：** Float64

**读写能力：** 只读。

**起始版本：** 12

### let height

```cangjie
public let height: Float64
```

**功能：** 表示文本布局的高度。

**类型：** Float64

**读写能力：** 只读。

**起始版本：** 12

### Size(Float64, Float64)

```cangjie
public Size(
    public let width: Float64,
    public let height: Float64
)
```

**功能：** Size主构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|Float64|是|-|文本所占布局宽度。<br>初始值： 0.0。|
|height|Float64|是|-|文本所占布局高度。<br>初始值： 0.0。|

## 示例代码

### 示例1（计算文本单行布局下的宽度）

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    let textSize: Float64 = Measure.MeasureText(
        MeasureOptions(
            textContent: "Hello world1",
            fontWeight: FontWeight.Normal
        )
    )
    func build() {
        Row() {
            Column() {
                Text("The Size of 'Hello World1': ${this.textSize}")
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

![measure1](figures/measure_text.jpeg)

### 示例2（计算文本单行布局下的宽度和高度）

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import kit.UIKit.Size as MeasureSize
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    let context2: MeasureOptions = MeasureOptions(textContent: "Hello world2")
    let textSize: MeasureSize = Measure.MeasureTextSize(context2)
    func build() {
        Row() {
            Column() {
                Text("The Size of 'Hello World2': ${this.textSize.width}, ${this.textSize.height}")
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

![measure2](figures/measure_textsize.jpeg)