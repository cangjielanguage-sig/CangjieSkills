# 透明度设置

设置组件的透明度。

## func opacity(Float64)

```cangjie
public func opacity(opacityValue: Float64): This
```

**功能：** 设置组件的透明度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|opacityValue|Float64|是|-|元素的不透明度，取值范围为0到1，1表示不透明，0表示完全透明, 达到隐藏组件效果，但是在布局中占位。<br> 初始值：1.0。 <br> **说明：**<br> 子组件会继承父组件的透明度，并与自身的透明度属性叠加。如：父组件透明度为0.1，子组件设置透明度为0.8，则子组件实际透明度为0.1*0.8=0.08。|

## func opacity(Int64)

```cangjie
public func opacity(opacityValue: Int64): This
```

**功能：** 设置组件的透明度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|opacityValue|Int64|是|-|元素的不透明度，取值范围为0和1，1表示不透明，0表示完全透明, 达到隐藏组件效果，但是在布局中占位。<br> 初始值：1。 <br> **说明：** <br> 子组件会继承父组件的透明度，并与自身的透明度属性叠加。|

## 示例代码

该示例主要显示通过opacity设置组件的不透明度。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Column(5) {
            Text("opacity(1)").fontSize(9).width(90.percent).fontColor(0xCCCCCC)
            Text("").width(90.percent).height(50).opacity(1).backgroundColor(0xAFEEEE)
            Text("opacity(0.7)").fontSize(9).width(90.percent).fontColor(0xCCCCCC)
            Text("").width(90.percent).height(50).opacity(0.7).backgroundColor(0xAFEEEE)
            Text("opacity(0.4)").fontSize(9).width(90.percent).fontColor(0xCCCCCC)
            Text("").width(90.percent).height(50).opacity(0.4).backgroundColor(0xAFEEEE)
            Text("opacity(0.1)").fontSize(9).width(90.percent).fontColor(0xCCCCCC)
            Text("").width(90.percent).height(50).opacity(0.1).backgroundColor(0xAFEEEE)
            Text("opacity(0)").fontSize(9).width(90.percent).fontColor(0xCCCCCC)
            Text("").width(90.percent).height(50).opacity(0).backgroundColor(0xAFEEEE)
        }.width(100.percent).padding(top: 5)
    }
}
```

![uni_opacity](figures/uni_opacity.png)
