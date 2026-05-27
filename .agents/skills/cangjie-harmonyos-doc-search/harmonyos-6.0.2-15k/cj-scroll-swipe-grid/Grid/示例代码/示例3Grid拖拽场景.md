### 示例3（Grid拖拽场景）

1. 设置属性editMode(true)设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部GridItem。
2. 在[onItemDragStart](#func-onitemdragstartitemdraginfoint32------unit)回调中设置拖拽过程中显示的图片。
3. 在[onItemDrop](#func-onitemdropitemdraginfoint32int32bool---unit)中获取拖拽起始位置，和拖拽插入位置，并在[onItemDrop](#func-onitemdropitemdraginfoint32int32bool---unit)中完成交换数组位置逻辑。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import std.collection.*
import ohos.state_macro_manage.*

@Entry
@Component
class grid5 {
    @State
    var numbers: ObservedArrayList<String> = ObservedArrayList<String>()
    var scroller: Scroller = Scroller()
    @State
    var text: String = 'drag'

    protected override func aboutToAppear() {
        for (i in 1..=15 : 1) {
            numbers.append("${i}")
        }
    }

    @Builder
    func pixelMapBuilder() {
        Column() {
            Text(this.text).fontSize(16).backgroundColor(0xF9CF93).width(80).height(80).textAlign(TextAlign.Center)
        }
    }

    func changeIndex(index1: Int64, index2: Int64) {
        let temp: String
        temp = this.numbers[index1]
        this.numbers[index1] = this.numbers[index2]
        this.numbers[index2] = temp
    }

    func build() {
        Column(5) {
            Grid(this.scroller) {
                ForEach(
                    this.numbers,
                    {
                        day: String, _: Int64 => GridItem() {
                            Text(day).fontSize(16).backgroundColor(0xF9CF93).width(80).height(80).textAlign(
                                TextAlign.Center)
                        }
                    }
                )
            }.columnsTemplate('1fr 1fr 1fr').columnsGap(10).rowsGap(10).width(90.percent).backgroundColor(0xFAEEE0).
                height(300).editMode(true).onItemDragStart(
                {
                    event: ItemDragInfo, itemIndex: Int32 =>
                    this.text = this.numbers[Int64(itemIndex)]
                    bind(this.pixelMapBuilder, this)()
                }
            ).onItemDrop(
                {
                    event: ItemDragInfo, itemIndex: Int32, insertIndex: Int32, isSuccess: Bool =>
                    if (!isSuccess || Int64(insertIndex) >= this.numbers.size) {
                        return
                    }
                    this.changeIndex(Int64(itemIndex), Int64(insertIndex))
                }
            )
        }.width(100.percent).margin(top: 5)
    }
}
```

示例图：

网格子组件开始拖拽：

![griditem](figures/grid51.png)

网格子组件拖拽过程中：

![griditem](figures/grid52.png)

网格子组件1与子组件6拖拽交换位置后：

![griditem](figures/grid53.png)