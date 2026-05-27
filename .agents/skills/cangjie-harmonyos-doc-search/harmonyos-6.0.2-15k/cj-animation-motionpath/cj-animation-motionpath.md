# 路径动画 (motionPath)

设置组件进行位移动画时的运动路径。

## func motionPath(MotionPathOptions)

```cangjie
public func motionPath(options: MotionPathOptions): This
```

**功能：** 设置组件进行位移动画时的运动路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[MotionPathOptions](#class-motionpathoptions)|是|-|组件的运动路径。|

## 基础类型定义

### class MotionPathOptions

```cangjie
public class MotionPathOptions {
    public MotionPathOptions(
        public var path!: String = "",
        public var `from`!: Float64 = 0.0,
        public var to!: Float64 = 1.0,
        public var rotatable!: Bool = false
    )
}
```

**功能：** 组件的运动路径信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var \`from\`

```cangjie
public var `from`: Float64
```

**功能：** 设置运动路径的起点。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

#### var path

```cangjie
public var path: String
```

**功能：** 设置位移动画的运动路径。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

#### var rotatable

```cangjie
public var rotatable: Bool
```

**功能：** 设置是否跟随路径进行旋转。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 12

#### var to

```cangjie
public var to: Float64
```

**功能：** 设置运动路径的终点。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

#### MotionPathOptions(String,Float64,Float64,Bool)

```cangjie
public MotionPathOptions(
        public var path!: String = "",
        public var `from`!: Float64 = 0.0,
        public var to!: Float64 = 1.0,
        public var rotatable!: Bool = false
    )
```

**功能：** 构建一个MotionPathOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|否|""| **命名参数。** 位移动画的运动路径，使用svg路径字符串。path中支持使用start和end进行起点和终点的替代，如：'Mstart.x start.y L50 50 Lend.x end.y Z'。<br/>设置为空字符串时相当于不设置路径动画。|
|\`from\`|Float64|否|0.0|运动路径的起点。<br/>取值范围：[0.0, 1.0]。<br/>设置小于0或大于1的值时，按默认值0处理。|
|to| Float64|否|1.0| **命名参数。**  运动路径的终点。<br/>取值范围：[0.0, 1.0]。<br/>设置小于0或大于1的值时，按默认值1处理，且满足to值 >= 异常值处理后的from值。|
|rotatable|Bool|否|false| **命名参数。** 是否跟随路径进行旋转。true代表跟随路径进行旋转，false代表不跟随路径进行旋转。|

## 示例代码

该示例主要演示如何设置组件进行位移动画时的运动路径。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var toggle: Bool = true
    func build() {
        Column {
            Button('click me').margin(50.vp).motionPath(
                MotionPathOptions(path: "Mstart.x start.y L500 200 L200 700 Lend.x end.y", from: 0.0, to: 0.8,
                rotatable: true)).onClick {
                animateTo(AnimateParam(duration: 4000, curve: Curve.Linear), {=> this.toggle = !this.toggle})
            }
        }.width(100.percent).height(100.percent).alignItems(getAlign())
    }
    func getAlign() {
        if (this.toggle) {
            HorizontalAlign.Start
        } else {
            HorizontalAlign.End
        }
    }
}
```

![motionpath](figures/motionpath.gif)
