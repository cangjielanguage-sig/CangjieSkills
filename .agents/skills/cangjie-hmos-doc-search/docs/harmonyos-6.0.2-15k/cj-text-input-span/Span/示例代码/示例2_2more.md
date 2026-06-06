### 示例2

font、lineHeight、baselineOffset属性接口使用示例。

<!--run-->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.*

@Entry
@Component
class EntryView {
    func build() {
        Column {
            Text("Basic Usage").fontSize(9).fontColor(0xCCCCCC)
            //文本样式展示
            Text() {
                Span("This is Span. ").font(size: 12.vp, weight: FontWeight.Bolder, family: "Arial",
                    style: FontStyle.Italic)
                        //设置文本行高为2.fp
                        .lineHeight(2.fp)
                        //设置Span基线的偏移量为10，即向上移动
                        .baselineOffset(10.fp)

                Span("This is Span.").font(size: 14.vp, weight: FontWeight.Lighter, family: "HarmonyOS Sans",
                    style: FontStyle.Normal).lineHeight(2.fp)

                Span("This is Span.").font(size: 12.vp, weight: FontWeight.Bolder, family: "Arial",
                    style: FontStyle.Italic).lineHeight(2.fp)
                        //设置Span基线的偏移量为-10，即向下移动
                        .baselineOffset(-10)
            }
        }
    }
}
```

![span](figures/span_font.PNG)

### 示例3

textBackgroundStyle、textShadow 属性接口使用示例。

<!--run-->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.*

@Entry
@Component
class EntryView {
    //设置背景样式属性，设置背景颜色为0xffff0000和四个圆角半径。
    let textBackGround1 = TextBackgroundStyle(color: 0xffff0000,
        radiusBorder: BorderRadiuses(topLeft: 0.vp, topRight: 12.vp, bottomLeft: 24.vp, bottomRight: 48.vp))
    let textBackGround2 = TextBackgroundStyle(color: Color.GRAY, radiusDimension: 3)
    let textShadows = ShadowOptions(radius: 10.0, shadowType: ShadowType.BLUR, offsetX: 10.0, offsetY: 0.0,
        color: Color.RED, fill: false)
    var textShadowsArray: Array<ShadowOptions> = [
        ShadowOptions(radius: 10.0, offsetX: 10.0, offsetY: 0.0, color: Color.RED),
        ShadowOptions(radius: 10.0, offsetX: 20.0, offsetY: 0.0, color: Color.BLACK),
        ShadowOptions(radius: 10.0, offsetX: 30.0, offsetY: 0.0, color: Color.BLUE),
        ShadowOptions(radius: 10.0, offsetX: 40.0, offsetY: 0.0, color: Color.GREEN),
        ShadowOptions(radius: 10.0, offsetX: 10.0, offsetY: 0.0, color: 0xFFFFFF),
        ShadowOptions(radius: 10.0, offsetX: 40.0, offsetY: 0.0, color: 0xFFFFFF)
    ]
    func build() {
        Column {
            Text("Basic Usage").fontSize(9).fontColor(0xCCCCCC)
            Text() {
                Span("This is Span. ")
                    //设置背景样式
                    .textBackgroundStyle(textBackGround1)
                    //设置阴影样式
                    .textShadow(textShadowsArray)
                Span("This is the Span component").textBackgroundStyle(textBackGround2).textShadow(textShadows)
            }
        }
    }
}
```

![span](figures/span_textBackgroundStyle.PNG)