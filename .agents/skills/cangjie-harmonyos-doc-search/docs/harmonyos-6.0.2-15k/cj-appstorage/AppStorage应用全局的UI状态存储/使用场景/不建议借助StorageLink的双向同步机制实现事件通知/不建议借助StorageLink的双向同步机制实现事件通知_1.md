### 不建议借助@StorageLink的双向同步机制实现事件通知

不建议开发者使用@StorageLink和AppStorage的双向同步的机制来实现事件通知，因为AppStorage中的变量可能绑定在多个不同页面的组件中，但事件通知则不一定需要通知到所有的这些组件。并且，当这些@StorageLink装饰的变量在UI中使用时，会触发UI刷新，带来不必要的性能影响。

示例代码中，TapImage中的单击事件，会触发AppStorage中tapIndex对应属性的改变。因为@StorageLink是双向同步，修改会同步回AppStorage中，所以，所有绑定AppStorage的tapIndex自定义组件里都能感知到tapIndex的变化。使用@Watch监听到tapIndex的变化后，修改状态变量tapColor从而触发UI刷新（此处tapIndex并未直接绑定在UI上，因此tapIndex的变化不会直接触发UI刷新）。

使用该机制来实现事件通知需要确保AppStorage中的变量尽量不要直接绑定在UI上，且需要控制@Watch函数的复杂度（如果@Watch函数执行时间长，会影响UI刷新效率）。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.AppResource
import ohos.resource_manager.__GenerateResource__
import ohos.request.agent.State
import ohos.hilog.Hilog

class ViewData {
    var title: String
    var uri: AppResource
    var color: Color = Color.BLACK

    init(title: String, uri: AppResource) {
        this.title = title
        this.uri = uri
    }
}

@Entry
@Component
class EntryView {
    // 此处"app.media.startIcon"仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
    let dataList: Array<ViewData> = [ViewData("flower", @r(app.media.startIcon)), ViewData("OMG", @r(app.media.image))]
    var gridScroller: Scroller = Scroller()

    func build() {
        Column() {
            Grid(this.gridScroller) {
                ForEach(
                    this.dataList,
                    itemGeneratorFunc: {
                        item: ViewData, idx: Int64 => GridItem() {
                            TapImage(index: idx, uri: item.uri)
                        }.aspectRatio(1)
                    }
                )
            }
        }
    }
}

@Component
class TapImage {
    @StorageLink["PropA"]
    @Watch[onTapIndexChange]
    var tapIndex: Int64 = -1
    @State
    var tapColor: Color = Color.BLACK
    var index: Int64
    var uri: AppResource

    func onTapIndexChange() {
        if (this.tapIndex >= 0 && this.index == this.tapIndex) {
            Hilog.info(0, "tapindex", "${this.tapIndex}, index: ${this.index},red")
            this.tapColor = Color.RED
        } else {
            Hilog.info(0, "tapindex", "${this.tapIndex}, index: ${this.index},black")
            this.tapColor = Color.BLACK
        }
    }
    func build() {
        Column() {
            Image(this.uri).objectFit(ImageFit.Cover).onClick({evt => this.tapIndex = this.index}).border(width: 5,
                color: this.tapColor)
        }
    }
}
```

相比借助@StorageLink的双向同步机制实现事件通知，开发者可以使用emit订阅某个事件并接收事件回调的方式来减少开销，增强代码的可读性。

> **说明：**
>
> emit接口不支持在Previewer预览器中使用。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.AppResource
import ohos.resource_manager.__GenerateResource__
import ohos.hilog.Hilog
import kit.BasicServicesKit.*
import std.collection.HashMap

class ViewData {
    var title: String
    var uri: AppResource
    var color: Color = Color.BLACK

    init(title: String, uri: AppResource) {
        this.title = title
        this.uri = uri
    }
}