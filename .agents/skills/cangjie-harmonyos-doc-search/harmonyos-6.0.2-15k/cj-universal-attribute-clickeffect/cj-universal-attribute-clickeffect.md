# 点击回弹效果

设置组件点击时回弹效果。

## func clickEffect(ClickEffectLevel, Option\<Float32>)

```cangjie
public func clickEffect(level!: ClickEffectLevel = ClickEffectLevel.LIGHT, scale!: Option<Float32> = Option.None): This
```

**功能：** 设置当前组件点击回弹效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|level|[ClickEffectLevel](./cj-common-types.md#enum-clickeffectlevel)|否|ClickEffectLevel.LIGHT| **命名参数。** 当前组件点击回弹效果。|
|scale|Option\<Float32>|否|Option.None| **命名参数。** 回弹缩放比例，支持在设置ClickEffectLevel的基础上微调回弹缩放比例。<br>**说明：**<br>level等于ClickEffectLevel.LIGHT时，初始值：0.90。 <br>level等于ClickEffectLevel.MIDDLE或者ClickEffectLevel.HEAVY时，初始值：0.95。|

## 示例代码

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import kit.LocalizationKit.*

@Entry
@Component
class EntryView {
    @State
    var toggle: Bool = true
    func build() {
        Column {
            Radio(value: '20', group: '数字', indicatorType: RadioIndicatorType.TICK).clickEffect(
                level: ClickEffectLevel.LIGHT).height(50).width(50)

            Radio(value: '10', group: '数字', indicatorType: RadioIndicatorType.TICK).clickEffect(
                level: ClickEffectLevel.LIGHT, scale: 0.5).height(50).width(50)
        }.width(100.percent).padding(24.vp)
    }
}
```

![uni_click](figures/uni-click.jpg)
