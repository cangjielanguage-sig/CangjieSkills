## 使用if实现模态转场

上述模态转场接口需要绑定到其他组件上，通过监听状态变量改变调起模态界面。同时，也可以通过if范式，通过新增/删除组件实现模态转场效果。

完整示例和代码如下。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    private var listArr: Array<String> = ["WLAN", "蓝牙", "个人热点", "连接与共享"]
    private var shareArr: Array<String> = ["投屏", "打印", "VPN", "私人DNS", "NFC"]
    @State
    var isShowShare: Bool = false
    private func shareFunc(): Unit {
        animateTo(
            AnimateParam(duration: 500),
            {
                => this.isShowShare = !this.isShowShare
            }
        )
    }

    func build() {
        Stack {
            Column {
                Column {
                    Text("设置").fontSize(28.vp).fontColor(0x333333)
                }.width(90.percent).padding(top: 40.vp, bottom: 15.vp).alignItems(HorizontalAlign.Start)

                Search(placeholder: "输入关键字搜索").width(90.percent).height(40.vp).margin(bottom: 20.vp)

                List(initialIndex: 0) {
                    ForEach(
                        this.listArr,
                        itemGeneratorFunc: {
                            item: String, index: Int64 => ListItem {
                                Row {
                                    Row {
                                        Text((item.toRuneArray().get(0) ?? r'0').toString()).fontColor(Color.WHITE).
                                            fontSize(14.vp).fontWeight(FontWeight.Bold)
                                    }.width(30.vp).height(30.vp).backgroundColor(0xa8a8a8).margin(right: 12.vp).
                                        borderRadius(20.vp).justifyContent(FlexAlign.Center)

                                    Column {
                                        Text(item).fontSize(16.vp).fontWeight(FontWeight.Medium)
                                    }.alignItems(HorizontalAlign.Start)

                                    Blank()

                                    Row {
                                    }.width(12.vp).height(12.vp).margin(right: 15.vp).border(width: 2.vp,
                                        color: 0xcccccc).borderWidth(EdgeWidths(top: 2.vp, right: 2.vp)).rotate(45)
                                }.borderRadius(15.vp).shadow(radius: 100, color: 0xededed).width(90.percent).alignItems(
                                    VerticalAlign.Center).padding(top: 15.vp, bottom: 15.vp, left: 15.vp).
                                    backgroundColor(Color.WHITE)
                            }.width(100.percent).margin(top: 12.vp).onClick(
                                {
                                evt => if (item.endsWith("共享")) {
                                    this.shareFunc()
                                }
                            })
                        },
                        keyGeneratorFunc: {item: String, index: Int64 => item.toString()}
                    )
                }.width(100.percent).height(80.percent)
            }.width(100.percent).height(100.percent).backgroundColor(0xfefefe)

            if (this.isShowShare) {
                Column {
                    Column {
                        Row {
                            Row {
                                Row {
                                }.width(16.vp).height(16.vp).border(width: 2.vp, color: 0x333333).borderWidth(
                                    EdgeWidths(top: 2.vp, left: 2.vp)).rotate(-45)
                            }.padding(left: 15.vp, right: 10.vp).onClick({
                                evt => this.shareFunc()
                            })
                            Text("连接与共享").fontSize(28.vp).fontColor(0x333333)
                        }.padding(top: 30.vp)
                    }.width(90.percent).padding(bottom: 15.vp, top: 40.vp).alignItems(HorizontalAlign.Start)

                    List(initialIndex: 0) {
                        ForEach(
                            this.shareArr,
                            itemGeneratorFunc: {
                                item: String, Index: Int64 => ListItem {
                                    Row {
                                        Row {
                                            Text((item.toRuneArray().get(0) ?? r'0').toString()).fontColor(Color.WHITE).
                                                fontSize(14.vp).fontWeight(FontWeight.Bold)
                                        }.width(30.vp).height(30.vp).backgroundColor(0xa8a8a8).margin(right: 12.vp).
                                            borderRadius(20.vp).justifyContent(FlexAlign.Center)

                                        Column {
                                            Text(item).fontSize(16.vp).fontWeight(FontWeight.Medium)
                                        }.alignItems(HorizontalAlign.Start)

                                        Blank()