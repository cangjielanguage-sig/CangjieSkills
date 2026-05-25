## 使用bindContentCover构建全屏模态转场效果

[bindContentCover](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-bindcontentcover.md)接口用于为组件绑定全屏模态页面，在组件出现和消失时可通过设置转场参数ModalTransition添加过渡动效。使用bindContentCover构建全屏模态转场效果步骤示例如下：

- 定义全屏模态转场效果[bindContentCover](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-bindcontentcover.md)。

- 定义模态展示界面。

   ```cangjie
   // 通过@Builder构建模态展示界面
   @Builder
   func MyBuilder() {
       Column {
           Text("my model view")
       }
           // 通过转场动画实现出现消失转场动画效果，transition需要加在builder下的第一个组件
           .transition(TransitionEffect.translate(TranslateOptions(y: 1000)).animation(AnimateParam(curve: Curve.Smooth)))
   }
   ```

- 通过模态接口调起模态展示界面，通过转场动画或者共享元素动画实现对应的动画效果。

   ```cangjie
   // 模态转场控制变量
   @State var isPresent: boolean = false

   Button("Click to present model view")
   // 通过选定的模态接口，绑定模态展示界面，ModalTransition是内置的ContentCover转场动画类型，这里选择None代表系统不加默认动画，通过onDisappear控制状态变量变换
   .bindContentCover(this.isPresent, this.MyBuilder, ContentCoverOptions(
               modalTransition: ModalTransition.DEFAULT,
               onDisappear: {
               => if (this.isPresent) {
                   this.isPresent = !this.isPresent
               }
               }
   ))
   .onClick({
       evt => this.isPresent = !this.isPresent
       // 改变状态变量，显示模态界面
   })
   ```

完整示例代码和效果如下。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

class PersonList {
    var name: String
    var cardnum: String
    public init(name: String, cardnum: String) {
        this.name = name
        this.cardnum = cardnum
    }
}

@Entry
@Component
class EntryView {
    private var personList: Array<PersonList> = [
        PersonList("王**", "1234***********789"),
        PersonList("宋*", "2345***********789"),
        PersonList("许**", "3456***********789"),
        PersonList("唐*", "4567***********789")
    ]

    @State
    var isPresent: Bool = false

    @Builder
    func MyBuilder() {
        Column {
            Row {
                Text("选择乘车人").fontSize(20.vp).fontColor(Color.WHITE).width(100.percent).textAlign(TextAlign.Center).
                    padding(top: 30.vp, bottom: 15.vp)
            }.backgroundColor(0x007dfe)

            Row {
                Text("+ 添加乘车人").fontSize(16.vp).fontColor(0x333333).margin(top: 10.vp).padding(top: 20.vp,
                    bottom: 20.vp).width(92.percent).borderRadius(10.vp).textAlign(TextAlign.Center).backgroundColor(
                    Color.WHITE)
            }

            Column {
                ForEach(
                    this.personList,
                    itemGeneratorFunc: {
                        item: PersonList, index: Int64 => Row {
                            Column {
                                if (index % 2 == 0) {
                                    Column {
                                    }.width(20.vp).height(20.vp).border(width: 1.vp, color: 0x007dfe).backgroundColor(
                                        0x007dfe)
                                } else {
                                    Column {
                                    }.width(20.vp).height(20.vp).border(width: 1.vp, color: 0x007dfe)
                                }
                            }.width(20.percent)

                            Column {
                                Text(item.name).fontColor(0x333333).fontSize(18.vp)
                                Text(item.cardnum).fontColor(0x666666).fontSize(14.vp)
                            }.width(60.percent).alignItems(HorizontalAlign.Start)

                            Column {
                                Text("编辑").fontColor(0x007dfe).fontSize(16.vp)
                            }.width(20.percent)
                        }.padding(top: 10.vp, bottom: 10.vp).border(width: 1.vp, color: 0xf1f1f1).width(92.percent).
                            backgroundColor(Color.WHITE)
                    }
                )
            }.padding(top: 20.vp, bottom: 20.vp)

            Text("确认").width(90.percent).height(40.vp).textAlign(TextAlign.Center).borderRadius(10.vp).fontColor(
                Color.WHITE).backgroundColor(0x007dfe).onClick({
                evt => this.isPresent = !this.isPresent
            })
        }.size(width: 100.percent, height: 100.percent).backgroundColor(0xf5f5f5).transition(
            TransitionEffect.translate(TranslateOptions(y: 1000)).animation(AnimateParam(curve: Curve.Smooth)))
    }