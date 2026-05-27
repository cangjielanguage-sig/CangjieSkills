# 组件区域变化事件

组件区域变化事件指组件显示的尺寸、位置等发生变化时触发的事件。

> **说明：**
>
> onAreaChange回调执行仅与本组件有关，对祖先或子孙组件上的onAreaChange的回调没有严格的执行顺序和限制保障。

## func onAreaChange((Area, Area) -> Unit)

```cangjie
public func onAreaChange(callback: (Area, Area)->Unit): This
```

**功能：** 组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。

由绘制变化所导致的渲染属性变化不会响应回调，如translate、offset。若组件自身位置由绘制变化决定也不会响应回调，如bindSheet。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([Area](./cj-common-types.md#class-area),[Area](./cj-common-types.md#class-area))->Unit|是|-|组件区域变化时触发该回调。<br/>参数一：变化前的组件区域信息。<br/>参数二：变化后的组件区域信息。|

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
    var value: String = "Text"
    @State
    var sizeValue: String = ""
    func build() {
        Column {
            Text(this.value).backgroundColor(Color.GREEN).margin(30).fontSize(30).onClick(
                {evt => this.value = this.value + "Text"}).onAreaChange(
                {old, new => this.sizeValue = "from " + old.width.toString() + " to " + new.width.toString()})
            Text("Area:\n" + this.sizeValue).margin(30)
        }
    }
}
```

![uni_area_change](figures/uni-area-change.gif)
