## 焦点样式

> **说明：**
>
> 最终绘制焦点态的组件的[zIndex](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-zorder.md#func-zindexint32)默认会被抬升至INT_MAX，如果该组件已经配置了zIndex，则不做zIndex调整。该组件不再绘制焦点态时，例如组件失焦或是退出走焦态，zIndex恢复为默认层级。

```cangjie
public func focusBox(style: FocusBoxStyle): This
```

设置当前组件系统焦点框样式。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Column(30) {
            Button("small black focus box").focusBox(
                FocusBoxStyle(
                    margin: 0.px,
                    strokeColor: ColorMetrics.rgba(0, 0, 0),
                )
            )
            Button("large red focus box").focusBox(
                FocusBoxStyle(
                    margin: 20.px,
                    strokeColor: ColorMetrics.rgba(255, 0, 0),
                    strokeWidth: 10.px
                )
            )
        }.alignItems(HorizontalAlign.Center).width(100.percent)
    }
}
```

![focusBox](figures/focusBox.gif)

上述示例包含以下2步：

- 进入页面，按下TAB触发走焦，第一个Button获焦，焦点框样式为紧贴边缘的蓝色细框。
- 按下TAB键，走焦到第二个Button，焦点框样式为远离边缘的红色粗框。

## 主动获焦/失焦

使用focusControl中的方法：

```cangjie
public static func requestFocus(keyValue: String): Bool
```

调用此接口可以主动让焦点转移至参数指定的组件上，焦点转移生效时间为下一个帧信号。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var btColor: UInt32 = 0x2787d9
    @State
    var btColor2: UInt32 = 0x2787d9

    func build() {
        Column(20) {
            Column(5) {
                Button("Button").width(200).height(70).fontColor(Color.WHITE).focusOnTouch(true).backgroundColor(
                    0x2787d9).onFocus({
                    => btColor = 0xd5d5d5
                }).onBlur({
                    => btColor = 0x2787d9
                }).id("testButton")

                Button("Button").width(200).height(70).fontColor(Color.WHITE).focusOnTouch(true).backgroundColor(
                    btColor2).onFocus({
                    => btColor2 = 0xd5d5d5
                }).onBlur({
                    => btColor2 = 0x2787d9
                }).id("testButton2")

                Divider().vertical(false).width(80.percent).backgroundColor(0x707070).height(10)
                //点击focusControl.requestFocus按钮，第二个Button获焦。
                Button("FocusControl.requestFocus").width(200).height(70).fontColor(Color.WHITE).onClick(
                    {
                    => FocusControl.requestFocus("testButton2")
                }).backgroundColor(0xff2787d9)
            }
        }.width(100.percent).height(100.percent)
    }
}
```

![focus-2](figures/focus-2.gif)