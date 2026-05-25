# 悬浮态效果

设置组件的鼠标悬浮态显示效果。

## func hoverEffect(HoverEffect)

```cangjie
public open func hoverEffect(value: HoverEffect)
```

**功能：** 设置组件的鼠标悬浮态显示效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|参数类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[HoverEffect](./cj-common-types.md#enum-hovereffect)|是|-|当前组件悬停态下的悬浮效果。<br/>初始值：HoverEffect.Auto。|

## 示例代码

该示例通过hoverEffect设置组件的鼠标悬浮态显示效果。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.hilog.Hilog

@Entry
@Component
class EntryView {
    @State
    var isHoverVal: Bool = false
    func build() {
        Column(5) {
            Column(5) {
                Text('Scale').fontSize(20).fontColor(Color.GRAY).width(90.percent).position(x: 0, y: 80)
                Column().width(80.percent).height(200).backgroundColor(Color.GRAY).position(x: 40, y: 120).hoverEffect(
                    HoverEffect.Auto).onHover(
                    {
                        isHover: Bool =>
                        Hilog.info(0, "test", 'Scale isHover: ' + isHover.toString())
                        this.isHoverVal = isHover
                    }
                )
                Text('Board').fontSize(20).fontColor(Color.GRAY).width(90.percent).position(x: 0, y: 350)
                Column().width(80.percent).height(200).backgroundColor(Color.YELLOW).position(x: 40, y: 420).hoverEffect(
                    HoverEffect.Highlight).onHover(
                    {
                        isHover: Bool =>
                        Hilog.info(0, "test", 'Highlight  isHover: ' + isHover.toString())
                        this.isHoverVal = isHover
                    }
                )
            }.hoverEffect(HoverEffect.None).width(100.percent).height(100.percent).border(width: 1.vp).onHover(
                {
                    isHover: Bool =>
                    Hilog.info(0, "test", 'HoverEffect.None')
                    this.isHoverVal = isHover
                }
            )
        }
    }
}
```

![focus_control](figures/hovereffect.png)
