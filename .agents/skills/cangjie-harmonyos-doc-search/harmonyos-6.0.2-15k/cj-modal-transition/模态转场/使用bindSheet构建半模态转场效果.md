## 使用bindSheet构建半模态转场效果

[bindSheet](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-sheettransition.md#func-bindsheetbool----unit-sheetoptions)属性可为组件绑定半模态页面，在组件出现时可通过设置自定义或默认的内置高度确定半模态大小。构建半模态转场动效的步骤基本与使用[bindContentCover](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-bindcontentcover.md)构建全屏模态转场动效相同。

完整示例和效果如下。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var isShowSheet: Bool = false
    private let menusList: Array<String> = ["不要辣", "少放辣", "多放辣", "不要香菜", "不要香葱", "不要一次性餐具",
        "需要一次性餐具"]

    @Builder
    func mySheet() {
        Column {
            Flex(FlexOptions(direction: FlexDirection.Row, wrap: FlexWrap.Wrap)) {
                ForEach(
                    this.menusList,
                    itemGeneratorFunc: {
                        item: String, index: Int64 => Text(item).fontSize(16.vp).fontColor(0x333333).backgroundColor(
                            0xf1f1f1).borderRadius(8.vp).margin(10.vp).padding(10.vp)
                    }
                )
            }.padding(top: 18.vp)
        }.width(100.percent).height(100.percent).backgroundColor(Color.WHITE)
    }

    func build() {
        Column {
            Text("口味与餐具").fontSize(28.vp).padding(top: 30.vp, bottom: 30.vp)
            Column {
                Row {
                    Row {
                    }.width(10.vp).height(10.vp).backgroundColor(0xa8a8a8).margin(right: 12.vp).borderRadius(20.vp)
                    Column {
                        Text("选择点餐口味和餐具").fontSize(16.vp).fontWeight(FontWeight.Medium)
                    }.alignItems(HorizontalAlign.Start)

                    Blank()

                    Row {
                    }.width(12.vp).height(12.vp).margin(right: 15.vp).border(width: 2.vp, color: 0xcccccc).rotate(45)
                }.borderRadius(15.vp).shadow(radius: 100, color: 0xededed).width(90.percent).alignItems(
                    VerticalAlign.Center).padding(left: 15.vp, top: 15.vp, bottom: 15.vp).backgroundColor(Color.WHITE).
                    bindSheet(
                    this.isShowSheet,
                    this.mySheet,
                    options: SheetOptions(
                        height: SheetSize.FIT_CONTENT,
                        dragBar: false,
                        onDisappear: {
                            => this.isShowSheet = !this.isShowSheet
                        }
                    )
                ).onClick({evt => this.isShowSheet = !this.isShowSheet})
            }.width(100.percent)
        }.width(100.percent).height(100.percent).backgroundColor(0xf1f1f1)
    }
}
```

![bindSheet](./figures/bindSheet.gif)