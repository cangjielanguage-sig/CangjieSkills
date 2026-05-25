### 示例1（创建矩阵）

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import kit.LocalizationKit.*

@Entry
@Component
class EntryView {
    let matrix1: Matrix4Transit = Matrix4.initialize([1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0])
    let matrix2: Matrix4Transit = Matrix4.identity()
    func build() {
        Row {
            Column {
                // matrix1 和 matrix2 效果一致
                Image(@r(app.media.startIcon)).transform(matrix1).height(40)
                Image(@r(app.media.startIcon)).transform(matrix2).height(40)
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

![font](figures/matrix4_init.jpeg)

### 示例2（组合效果）

缩放及其逆矩阵的效果组合。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import kit.LocalizationKit.*

@Entry
@Component
class EntryView {
    let matrix1: Matrix4Transit = Matrix4.identity().scale(
        ScaleOption(x: 2.0, y: 3.0, z: 4.0, centerX: 50.0, centerY: 50.0))
    let matrix2: Matrix4Transit = matrix1.copy().invert()
    let matrix3: Matrix4Transit = matrix1.copy().combine(matrix2)
    func build() {
        Row {
            Column {
                Text("scale").fontSize(15).fontColor(0xCCCCCC).width(90.percent)
                Image(@r(app.media.startIcon)).transform(matrix1).height(40)

                Text("invert").fontSize(15).fontColor(0xCCCCCC).width(90.percent)
                Image(@r(app.media.startIcon)).transform(matrix2).height(40)

                Text("scale + invert + combine").fontSize(15).fontColor(0xCCCCCC).width(90.percent)
                Image(@r(app.media.startIcon)).transform(matrix3).height(40)
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

![font](figures/matrix4_combine.jpeg)

### 示例3（旋转效果）

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import kit.LocalizationKit.*

@Entry
@Component
class EntryView {
    let matrix: Matrix4Transit = Matrix4.identity().rotate(RotateOption(x: 1.0, y: 1.0, z: 2.0, angle: 30.0,
        centerY: 50.0))
    func build() {
        Row {
            Column {
                Image(@r(app.media.startIcon)).transform(matrix).height(40)
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

![font](figures/matrix4_rotate.jpeg)

### 示例4（倾斜效果）

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import kit.LocalizationKit.*

@Entry
@Component
class EntryView {
    let matrix: Matrix4Transit = Matrix4.identity().skew(2.0, 3.0)
    func build() {
        Row {
            Column {
                Image(@r(app.media.startIcon)).transform(matrix).height(40)
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

![font](figures/matrix4_skew.jpeg)

### 示例5（坐标点转换效果）

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import kit.LocalizationKit.*

@Entry
@Component
class EntryView {
    let matrix1: Matrix4Transit = Matrix4.identity().translate(TranslateOption(x: 150.0, y: -50.0))
    let transformP = matrix1.transformPoint([50.0, 50.0])
    let matrix2: Matrix4Transit = Matrix4.identity().translate(
        TranslateOption(x: Float32(transformP[0]), y: Float32(transformP[1])))
    func build() {
        Row {
            Column {
                Text("第一次变化，x平移150，y平移-50").textAlign(TextAlign.Center)
                Image(@r(app.media.startIcon)).transform(matrix1).height(40)

                Text(
                    "在第一次变化基础上TransformPoint([50,50])后，第二次变化，x平移：${transformP[0]}" +
                    "，y平移：${transformP[1]}").textAlign(TextAlign.Center)
                Image(@r(app.media.startIcon)).transform(matrix2).height(40)
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

![font](figures/matrix4_tp.jpeg)