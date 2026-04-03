# 触摸热区设置

适用于支持通用点击事件、通用触摸事件、通用手势处理的组件。

## func responseRegion(Rectangle)

```cangjie
public func responseRegion(rect: Rectangle): This
```

**功能：** 设置一个触摸热区。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| rect|  [Rectangle](./cj-common-types.md#class-rectangle) | 是  | - | 一个触摸热区，包括位置和大小。 |

## func responseRegionArray(Array\<Rectangle>)

```cangjie
public func responseRegionArray(array: Array<Rectangle>): This
```

**功能：** 设置多个触摸热区。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| array|  Array\<[Rectangle](./cj-common-types.md#class-rectangle)> | 是  |  \- | 多个触摸热区，包括位置和大小。 |

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
    var text: String = ""
    func build() {
        Column() {
            Text("x:0,y:0,width:50.percent,height:100.percent")
            // 热区宽度为按钮的一半，点击右侧无响应
            Button("button1").responseRegion(Rectangle(x: 0.vp, y: 0.vp, width: 50.percent, height: 100.percent)).
                onClick({
                => text = "button1 clicked"
            })
            // 热区宽度为按钮的一半，且右移一个按钮宽度，点击button2右侧左边，点击事件生效
            Text("x:100.percent,y:0,width:50.percent,height:100.percent")
            Button("button2").responseRegion(Rectangle(x: 100.percent, y: 0.vp, width: 50.percent, height: 100.percent)).
                onClick({
                => text = "button2 clicked"
            })
            // 热区大小为整个按钮，且下移一个按钮高度，点击button3下方按钮大小区域，点击事件生效
            Text("x:0,y:100.percent,width:100.percent,height:100.percent")
            Button("button3").responseRegion(Rectangle(x: 0.vp, y: 100.percent, width: 100.percent, height: 100.percent)
            ).onClick({
                => text = "button3 clicked"
            }).margin(bottom: 50)
            // 设置多个触摸热区
            Text(
                "[Rectangle(x: 0.vp, y: 100.percent, width: 100.percent, height: 100.percent)," +
                "\nRectangle(x: 100.percent, y: 0.vp, width: 50.percent, height: 100.percent)]")
            Button("button4").responseRegionArray(
                [Rectangle(x: 0.vp, y: 100.percent, width: 100.percent, height: 100.percent),
                Rectangle(x: 100.percent, y: 0.vp, width: 50.percent, height: 100.percent)]).onClick(
                {
                => text = "button4 clicked"
            })
            Text(text).margin(top: 50)
        }.width(100.percent).margin(top: 5)
    }
}
```

![uni_response_region](figures/uni_response_region.gif)
