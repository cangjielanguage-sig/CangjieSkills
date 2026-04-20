## Z序控制

Stack容器中兄弟组件显示层级关系可以通过[Z序控制](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-zorder.md)的zIndex属性改变。zIndex值越大，显示层级越高，即zIndex值大的组件会覆盖在zIndex值小的组件上方。

  在层叠布局中，如果后面子元素尺寸大于前面子元素尺寸，则前面子元素完全隐藏。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Stack(Alignment.BottomStart) {
            Column() {
                Text('Stack子元素1').textAlign(TextAlign.End).fontSize(20)
            }.width(100).height(100).backgroundColor(0xffd306)

            Column() {
                Text('Stack子元素2').fontSize(20)
            }.width(150).height(150).backgroundColor(Color.PINK)

            Column() {
                Text('Stack子元素3').fontSize(20)
            }.width(200).height(200).backgroundColor(Color.GREY)
        }.width(350).height(350).backgroundColor(0xe0e0e0)
    }
}
```

![z](figures/Z.png)

上图中，最后的子元素3的尺寸大于前面的所有子元素，所以，前面两个元素完全隐藏。改变子元素1，子元素2的zIndex属性后，可以将元素展示出来。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Stack(Alignment.BottomStart) {
            Column() {
                Text('Stack子元素1').fontSize(20)
            }.width(100).height(100).backgroundColor(0xffd306).zIndex(2)
            Column() {
                Text('Stack子元素2').fontSize(20)
            }.width(150).height(150).backgroundColor(Color.PINK).zIndex(1)
            Column() {
                Text('Stack子元素3').fontSize(20)
            }.width(200).height(200).backgroundColor(Color.GREY)
        }.width(350).height(350).backgroundColor(0xe0e0e0)
    }
}
```

![z2](figures/z2.png)

## 场景示例

使用层叠布局快速搭建页面。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    private var arr: Array<String> = ['APP1', 'APP2', 'APP3', 'APP4', 'APP5', 'APP6', 'APP7', 'APP8'];
    func build() {
        Stack(Alignment.Bottom) {
            Flex(FlexParams(wrap: FlexWrap.Wrap)) {
                ForEach(
                    this.arr,
                    itemGeneratorFunc: {
                        item: String, idx: Int64 => Text(item).width(100).height(100).fontSize(16).margin(10).textAlign(
                            TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
                    },
                    keyGeneratorFunc: {item: String, idx: Int64 => idx.toString()}
                )
            }.width(100.percent).height(100.percent)
            Flex(FlexParams(justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center)) {
                Text('联系人').fontSize(16)
                Text('设置').fontSize(16)
                Text('短信').fontSize(16)
            }.width(50.percent).height(50).backgroundColor(0x16302e2e).margin(bottom: 15).borderRadius(15)
        }.width(100.percent).height(100.percent).backgroundColor(0xCFD0CF)
    }
}
```

![z1](figures/z1.png)