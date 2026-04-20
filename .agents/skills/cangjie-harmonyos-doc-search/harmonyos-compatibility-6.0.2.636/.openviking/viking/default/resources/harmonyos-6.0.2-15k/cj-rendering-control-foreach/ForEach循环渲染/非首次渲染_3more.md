## 非首次渲染

在ForEach组件进行非首次渲染时，它会检查新生成的键值是否在上次渲染中已经存在。如果键值不存在，则会创建一个新的组件；如果键值存在，则不会创建新的组件，而是直接渲染该键值所对应的组件。例如，在以下的代码示例中，通过点击事件修改了数组的第三项值为"new three"，这将触发ForEach组件进行非首次渲染。
<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Component
class ChildItem {
    @Prop
    var item: String
    func build() {
        Text(this.item).fontSize(50)
    }
}

@Entry
@Component
class EntryView {
    @State
    var simpleList: ObservedArrayList<String> = ObservedArrayList<String>(['one', 'two', 'three'])
    func build() {
        Row() {
            Column() {
                Text("点击修改第3个数组项的值").fontSize(24).fontColor(Color.RED).onClick(
                    {
                    evt => this.simpleList[2] = 'new three'
                })
                ForEach(
                    this.simpleList,
                    itemGeneratorFunc: {
                        item: String, idx: Int64 => ChildItem(item: item)
                    },
                    keyGeneratorFunc: {item: String, idx: Int64 => return item}
                )
            }.justifyContent(FlexAlign.Center).width(100.percent).height(100.percent)
        }.height(100.percent).backgroundColor(Color.WHITE)
    }
}
```

运行效果如下图所示。

图3 ForEach非首次渲染案例运行效果图

![changenumthree.gif](figures/changenumthree.gif)

从本例可以看出@State 能够监听到简单数据类型数组数据源 simpleList 数组项的变化。

1. 当 simpleList 数组项发生变化时，会触发 ForEach 进行重新渲染。
2. ForEach 遍历新的数据源 ['one', 'two', 'new three']，并生成对应的键值one、two和new three。
3. 其中，键值one和two在上次渲染中已经存在，所以 ForEach 复用了对应的组件并进行了渲染。对于第三个数组项 "new three"，由于其通过键值生成规则 item 生成的键值new three在上次渲染中不存在，因此 ForEach 为该数组项创建了一个新的组件。

## 使用场景

ForEach组件在开发过程中的主要应用场景包括：[数据源不变](#数据源不变)、[数据源数组项发生变化](#数据源数组项发生变化)（如插入、删除操作）。

## 数据源不变

在数据源保持不变的场景中，数据源可以直接采用基本数据类型。例如，在页面加载状态时，可以使用骨架屏列表进行渲染展示。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Builder
func textArea(width: Int64, height: Int64) {
    Row().width(width).height(height).backgroundColor(Color.WHITE)
}

@Component
class ArticleSkeletonView {
    func build() {
        Row() {
            Column() {
                textArea(80, 80)
            }.margin(right: 20)
            Column() {
                textArea(60, 20)
                textArea(50, 20)
            }.alignItems(HorizontalAlign.Start).justifyContent(FlexAlign.SpaceAround).height(100)
        }.padding(20).borderRadius(12).backgroundColor(Color.GRAY).height(120).width(100.percent).justifyContent(
            FlexAlign.SpaceBetween).margin(top: 20)
    }
}

@Entry
@Component
class EntryView {
    @State
    var simpleList: Array<Int64> = [1, 2, 3, 4, 5]
    func build() {
        Column() {
            ForEach(this.simpleList, itemGeneratorFunc: {item: Int64, idx: Int64 => ArticleSkeletonView()})
        }.padding(20).width(100.percent).height(100.percent)
    }
}
```

运行效果如下图所示。

图4 骨架屏运行效果图

![skscreem.png](figures/skscreem.png)