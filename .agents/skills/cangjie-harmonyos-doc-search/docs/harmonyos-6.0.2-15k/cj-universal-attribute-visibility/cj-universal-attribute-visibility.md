# 显隐控制

控制组件是否可见。

## func visibility(Visibility)

```cangjie
public func visibility(value: Visibility): This
```

**功能：** 设置组件的可见性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Visibility](./cj-common-types.md#enum-visibility)|是| - | 控制当前组件显示或隐藏。根据具体场景需要，可使用条件渲染代替。初始值：Visibility.Visible。 |

## 示例代码

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build(): Unit {
        Column() {
            Column() {
                // 隐藏不参与占位
                Text("None").fontSize(9).width(90.percent).fontColor(0xCCCCCC)
                Row().visibility(Visibility.None).width(90.percent).height(80).backgroundColor(0xAFEEEE)

                // 隐藏参与占位
                Text("Hidden").fontSize(9).width(90.percent).fontColor(0xCCCCCC)
                Row().visibility(Visibility.Hidden).width(90.percent).height(80).backgroundColor(0xAFEEEE)

                // 正常显示，组件默认的显示模式
                Text("Visible").fontSize(9).width(90.percent).fontColor(0xCCCCCC)
                Row().visibility(Visibility.Visible).width(90.percent).height(80).backgroundColor(0xAFEEEE)
            }.width(90.percent).borderWidth(1)
        }.width(100.percent).margin(top: 5)
    }
}
```

![uni_visible](figures/uni_visible.png)
