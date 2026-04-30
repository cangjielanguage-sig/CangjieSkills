## 不推荐案例

开发者在使用ForEach的过程中，若对于键值生成规则的理解不够充分，可能会出现错误的使用方式。错误使用一方面会导致功能层面问题，例如[渲染结果非预期](#渲染结果非预期)，另一方面会导致性能层面问题，例如[渲染性能降低](#渲染性能降低)。

### 渲染结果非预期

在本示例中，通过设置ForEach的第三个参数keyGeneratorFunc函数，自定义键值生成规则为数据源的索引index的字符串类型值。当点击父组件EntryView中“在第1项后插入新项”文本组件后，界面会出现非预期的结果。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.ArrayList
import kit.LocalizationKit.*
import ohos.hilog.Hilog

@Component
class ChildItem {
    @Prop
    var item: String
    func build() {
        Text(this.item).fontSize(30)
    }
}

@Entry
@Component
class EntryView {
    @State
    var simpleList: ObservedArrayList<String> = ObservedArrayList(['one', 'two', 'three'])
    func build() {
        Column() {
            Button() {
                Text('在第1项后插入新项').fontSize(30)
            }.onClick({
                => this.simpleList.insert(1, 'new item')
            })
            ForEach(
                this.simpleList,
                itemGeneratorFunc: {
                    item: String, idx: Int64 => ChildItem(item: item)
                },
                keyGeneratorFunc: {item: String, index: Int64 => index.toString()}
            )
        }.justifyContent(FlexAlign.Center).width(100.percent).height(100.percent).backgroundColor(Color.WHITE)
    }
}
```

上述代码的初始渲染效果和点击“在第1项后插入新项”文本组件后的渲染效果如下图所示。

图6 渲染结果非预期运行效果图

![renderunexpect.gif](figures/renderunexpect.gif)

ForEach在首次渲染时，创建的键值依次为"0"、"1"、"2"。

插入新项后，数据源simpleList变为['one', 'new item', 'two', 'three']，框架监听到@State装饰的数据源长度变化触发ForEach重新渲染。

ForEach依次遍历新数据源，遍历数据项"one"时生成键值"0"，存在相同键值，因此不创建新组件。继续遍历数据项"new item"时生成键值"1"，存在相同键值，因此不创建新组件。继续遍历数据项"two"生成键值"2"，存在相同键值，因此不创建新组件。最后遍历数据项"three"时生成键值"3"，不存在相同键值，创建内容为"three"的新组件并渲染。

从以上可以看出，当最终键值生成规则包含index时，期望的界面渲染结果为['one', 'new item', 'two', 'three']，而实际的渲染结果为['one', 'two', 'three', 'three']，渲染结果不符合开发者预期。因此，开发者在使用ForEach时应尽量避免最终键值生成规则中包含index。