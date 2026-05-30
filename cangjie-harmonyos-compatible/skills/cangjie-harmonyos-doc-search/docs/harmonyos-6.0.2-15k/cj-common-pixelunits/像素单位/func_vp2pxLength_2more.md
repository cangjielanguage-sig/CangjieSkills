## func vp2px(Length)

```cangjie
public func vp2px(value: Length): Option<Length>
```

**功能：** 将vp单位的数值转换为以px为单位的数值。<br>说明：默认使用当前UI实例所在屏幕的虚拟像素比进行转换，UI实例未创建时，使用默认屏幕的虚拟像素比进行转换。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|需转换的vp单位的数值。|

**返回值：**

|类型|说明|
|:----|:----|
|Option\<[Length](./cj-common-types.md#interface-length)>|转换后以px为单位的数值。|

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
    var isShow: Bool = false
    func build() {
        Column() {
            Flex(FlexParams(wrap: FlexWrap.Wrap)) {
                Column() {
                    Text("width(180)").width(180).height(40).backgroundColor(0xF9CF93).textAlign(TextAlign.Center).
                        fontColor(Color.WHITE).fontSize(12.vp)
                }.margin(5)

                Column() {
                    Text("width('180px')").width(180.px).height(40).backgroundColor(0xF9CF93).textAlign(
                        TextAlign.Center).fontColor(Color.WHITE)
                }.margin(5)

                Column() {
                    Text("width('180vp')").width(180.vp).height(40).backgroundColor(0xF9CF93).textAlign(
                        TextAlign.Center).fontColor(Color.WHITE).fontSize(12.vp)
                }.margin(5)

                Column() {
                    Text("width('180lpx') designWidth:720").width(180.lpx).height(40).backgroundColor(0xF9CF93).
                        textAlign(TextAlign.Center).fontColor(Color.WHITE).fontSize(12.vp)
                }.margin(5)

                Column() {
                    Text("width(vp2px(180) + 'px')").width(vp2px(180.vp) ?? 180.vp).height(40).backgroundColor(0xF9CF93).
                        textAlign(TextAlign.Center).fontColor(Color.WHITE).fontSize(12.vp)
                }.margin(5)

                Column() {
                    Text("fontSize('12fp')").width(180).height(40).backgroundColor(0xF9CF93).textAlign(TextAlign.Center).
                        fontColor(Color.WHITE).fontSize(12.fp)
                }.margin(5)

                Column() {
                    Text("width(px2vp(180))").width(px2vp(180.px) ?? 180.px).height(40).backgroundColor(0xF9CF93).
                        textAlign(TextAlign.Center).fontColor(Color.WHITE).fontSize(12.fp)
                }.margin(5)
            }.width(100.percent)
        }
    }
}
```

![pixelUnits](./figures/pixelUnits.png)