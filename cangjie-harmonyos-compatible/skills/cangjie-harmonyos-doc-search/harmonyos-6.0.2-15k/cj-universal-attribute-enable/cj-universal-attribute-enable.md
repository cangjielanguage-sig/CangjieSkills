# 禁用控制

组件是否可交互，可交互状态下响应[点击事件](./cj-universal-event-click.md#)、[触摸事件](./cj-universal-event-touch.md)、[拖拽事件](./cj-universal-event-drag.md)、[按键事件](./cj-universal-event-key.md)、[焦点事件](./cj-universal-event-focus.md)、[鼠标事件](./cj-universal-event-mouse.md)、[悬浮事件](./cj-universal-event-hover.md)和[手势事件](./cj-universal-gesture-bind.md)。

> **说明：**
>
> 禁用控制属性只能在按下时生效，已经在交互过程中，更改enabled属性不生效。

## func enabled(Bool)

```cangjie
public func enabled(value: Bool): This
```

**功能：** 设置组件是否可交互。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :--- | :--- | :--- | :--- | :--- |
| value  | Bool | 是   | - | 值为true表示组件可交互，响应点击等操作。<br>值为false表示组件不可交互，不响应点击等操作。<br>初始值：true。|

## 示例代码

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Flex(FlexParams(justifyContent: FlexAlign.SpaceAround)) {
            // 点击没有反应
            Button("disable").enabled(false).backgroundColor(0x317aff).opacity(0.4)
            Button("enable").backgroundColor(0x317aff)
        }.width(100.percent).padding(top: 5)
    }
}
```

![uni_enabled](figures/uni_enabled.gif)
