## 使用bindMenu实现菜单弹出效果

[bindMenu](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-menu.md#func-bindmenuarraymenuelement-menuoptions)为组件绑定弹出式菜单，通过点击触发。完整示例和效果如下。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var items: Array<Action> = [Action(value: "菜单项1", action: {=> AppLog.info("handle Menu1 select")}),
        Action(value: "菜单项2", action: {=> AppLog.info("handle Menu2 select")})]

    func build() {
        Column {
            Button("click").backgroundColor(0x409eff).borderRadius(5.vp).bindMenu(this.items)
        }.justifyContent(FlexAlign.Center).width(100.percent).height(437.vp)
    }
}
```

![bindMenu](./figures/bindMenu.gif)

## 使用bindContextMenu实现菜单弹出效果

[bindContextMenu](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-menu.md#func-bindcontextmenu---unit-responsetype-contextmenuoptions)为组件绑定弹出式菜单，通过长按或右键点击触发。完整示例和效果如下。

完整示例和效果如下。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.*

@Entry
@Component
class EntryView {
    private var menu: Array<String> = ["保存图片", "收藏", "搜一搜"]
    private var pics: Array<AppResource> = [@r(app.media.startIcon)]

    @Builder
    func myMenu() {
        Column {
            ForEach(
                this.menu,
                itemGeneratorFunc: {
                    item: String, index: Int64 => Row {
                        Text(item).fontSize(18.vp).width(100.percent).textAlign(TextAlign.Center)
                    }.padding(15.vp).border(width: 1.vp, color: 0xcccccc)
                }
            )
        }.width(140.vp).borderRadius(15.vp).shadow(radius: 15, color: 0xf1f1f1).backgroundColor(0xf1f1f1)
    }

    func build() {
        Column {
            Row {
                Text("查看图片").fontSize(20.vp).fontColor(Color.WHITE).width(100.percent).textAlign(TextAlign.Center).
                    padding(top: 20.vp, bottom: 20.vp)
            }.backgroundColor(0x007dfe)

            Column {
                ForEach(
                    this.pics,
                    itemGeneratorFunc: {
                        item: AppResource, index: Int64 => Row {
                            Image(item).width(100.percent).draggable(false)
                        }.padding(top: 20.vp, bottom: 20.vp, left: 10.vp, right: 10.vp).bindContextMenu(
                            builder: this.myMenu, responseType: ResponseType.LongPress)
                    }
                )
            }
        }.width(100.percent).alignItems(HorizontalAlign.Center)
    }
}
```

![bindContextMenu1](figures/chakantupian.jpg)

## 使用bindPopUp实现气泡弹窗效果

[bindpopup](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-popup.md)属性可为组件绑定弹窗，并设置弹窗内容，交互逻辑和显示状态。

完整示例和代码如下。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var customPopup: Bool = false

    @Builder
    func popupBuilder() {
        Column(2.vp) {
            Row {
            }.width(64.vp).height(64.vp).backgroundColor(0x409eff)
            Text("Popup").fontSize(10.vp).fontColor(Color.WHITE)
        }.justifyContent(FlexAlign.SpaceAround).width(100.vp).height(100.vp).padding(5.vp).backgroundColor(Color.RED)
    }

    func build() {
        Column {
            Button("click").onClick({
                evt => this.customPopup = !this.customPopup
            }).backgroundColor(0xf56c6c).bindPopup(
                popup: CustomPopupOptions(
                    builder: bind(popupBuilder, this),
                    placement: Placement.Top,
                    maskColor: Color(0x33000000),
                    popupColor: Color(0xf56c6c),
                    enableArrow: true,
                    autoCancel: true,
                    onStateChange: {
                        e => if (!e.isVisible) {
                            this.customPopup = false
                        }
                    }
                ),
                show: this.customPopup
            )
        }.justifyContent(FlexAlign.Center).width(100.percent).height(437.vp)
    }
}
```

![bindPopUp](./figures/bindPopUp.gif)