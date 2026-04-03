### 示例7（以当前行最高的GridItem的高度为其他GridItem的高度）

下面的Grid中包含两列，每列中的GridItem包括高度确定的两个Column和一个高度不确定的Text共三个子组件。

在默认情况下，左右两个GridItem的高度可能是不同的；在设置了Grid的[alignItems](#func-alignitemsgriditemalignment)属性为GridItemAlignment.STRETCH后，一行左右两个GridItem中原本高度较小的GridItem会以另一个高度较大的GridItem的高度作为自己的高度。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import ohos.state_macro_manage.Entry
import ohos.state_macro_manage.Component
import ohos.state_macro_manage.State
import ohos.state_macro_manage.r
import ohos.base.*
import ohos.component.*
import ohos.state_manage.*
import ohos.state_macro_manage.*
import std.collection.{ArrayList, HashMap}
import std.math.*
import std.random.*

@Entry
@Component
class EntryView {
    @State
    var data: ArrayList<Int64> = ArrayList<Int64>()
    @State
    var items: ArrayList<Int64> = ArrayList<Int64>()

    protected override func aboutToAppear() {
        for (i in 0..100) {
            this.data.add(i)
            this.items.add(this.getSize())
        }
    }

    func getSize(): Int64 {
        let ret = Int64(floor(Random().nextFloat64() * 5.0))
        return max(1, ret)
    }

    func build() {
        Column(10) {
            Text('Grid alignItems示例代码')

            Grid() {
                ForEach(
                    this.data,
                    itemGeneratorFunc: {
                        item: Int64, idx: Int64 =>
                        // GridItem和Column不设置高度，默认会自适应子组件大小，设置STRETCH的场景下，会变成与当前行最高节点同高。
                        // 若设置高度，则会保持已设置的高度，不会与当前行最高节点同高。
                        GridItem() {
                            Column() {
                                Column().height(100).backgroundColor(0xD5D5D5).width(100.percent)
                                // 中间的Text设置flexGrow(1)来自适应填满父组件的空缺
                                Text(String.fromUtf8("这是一段文字。".toArray().repeat(this.items[item]))).flexGrow(1).
                                    width(100.percent).align(Alignment.TopStart).backgroundColor(0xF7F7F7)
                                Column().height(50).backgroundColor(0x707070).width(100.percent)
                            }
                        }.border(color: Color.BLACK, width: 1.vp)
                    }
                )
            }.columnsGap(10).rowsGap(5).columnsTemplate("1fr 1fr").width(80.percent).height(100.percent)
                // Grid设置alignItems为STRETCH，以当前行最高的GridItem的高度为其他GridItem的高度。
                .alignItems(
                GridItemAlignment.STRETCH).scrollBar(BarState.Off)
        }.height(100.percent).width(100.percent)
    }
}
```

![griditem](figures/grid6_api.png)