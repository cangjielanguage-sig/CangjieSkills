## 组件事件

### func onChange((Float64,Float64,PanelMode) -> Unit)

```cangjie
public func onChange(callback: (Float64, Float64, PanelMode) -> Unit): This
```

**功能：** 当可滑动面板发生状态变化时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Float64,Float64,PanelMode)->Unit|是|-|回调函数，当可滑动面板发生状态变化时触发。<br/>第一个参数：内容区的宽度值；<br/>第二个参数：内容区的高度值；当dragbar属性为true时，panel本身的高度值为dragbar高度加上内容区高度。<br/>第三个参数：面板的状态。|

### func onHeightChange((Float64) -> Unit)

```cangjie
public func onHeightChange(callback: (Float64) -> Unit): This
```

**功能：** 当可滑动面板发生高度变化时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Float64)->Unit|是|-|回调函数，当可滑动面板发生高度变化时触发。<br/>当dragbar属性为true时，panel本身的高度值为dragbar高度加上内容区高度。<br/>因用户体验设计原因，panel最高只能滑到 fullHeight-8.vp。|

## 基础类型定义



## enum PanelType

```cangjie
public enum PanelType {
    | Minibar
    | Foldable
    | Foldable
}
```

**功能：** 可滑动面板的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Minibar

```cangjie
Minibar
```

**功能：** 提供minibar和类全屏展示切换效果。PanelType为minibar时，PanelMode默认值是Mini。

**起始版本：** 12

### Foldable

```cangjie
Foldable
```

**功能：** 内容永久展示类，提供大（类全屏）、中（类半屏）、小三种尺寸展示切换效果。

**起始版本：** 12

### Temporary

```cangjie
Temporary
```

**功能：** 内容临时展示区，提供大（类全屏）、中（类半屏）两种尺寸展示切换效果。

**起始版本：** 12

## enum PanelMode

```cangjie
public enum PanelMode {
    | Mini
    | Half
    | Full
}
```

**功能：** 可滑动面板的状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Mini

```cangjie
Mini
```

**功能：** 类型为minibar和foldable时，为最小状态；类型为temporary，则不生效。

**起始版本：** 12

### Half

```cangjie
Half
```

**功能：** 类型为foldable和temporary时，为类半屏状态；类型为minibar，则不生效。

**起始版本：** 12

### Full

```cangjie
Full
```

**功能：** 类全屏状态。

**起始版本：** 12

## 示例代码

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var width: Float64 = 0.0
    @State
    var height: Float64 = 0.0
    @State
    var height2: Float64 = 0.0
    @State
    var mode: Int32 = 0
    func build() {
        Column(10) {
            Panel(true) {
                Text("${width}").fontSize(20)
                Text("${height}").fontSize(20)
                Text("${height2}").fontSize(20)
                Text("${mode}").fontSize(20)
            }.fullHeight(600).halfHeight(300).miniHeight(100).backgroundMask(Color.RED).dragBar(true).onChange(
                {
                    w, h, m =>
                    width = w
                    height = h
                    mode = m.getValue()
                }
            ).onHeightChange({
                h => height2 = h
            })
        }
    }
}
```

![panel](figures/panel.png)