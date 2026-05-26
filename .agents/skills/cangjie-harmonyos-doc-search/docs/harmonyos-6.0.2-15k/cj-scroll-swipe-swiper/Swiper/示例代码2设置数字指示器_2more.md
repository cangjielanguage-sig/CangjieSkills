## 示例代码2（设置数字指示器）

该示例通过DigitIndicator接口，实现了数字指示器的效果和功能。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.ArrayList

class MyDataSource<T> <: IDataSource<T> {
    private var list: ArrayList<T> = ArrayList<T>([])

    MyDataSource(list: ArrayList<T>) {
        this.list = list
    }

    public func totalCount(): Int64 {
        return this.list.size
    }

    public func getData(index: Int64): T {
        return this.list[index]
    }

    public func onRegisterDataChangeListener(listener: DataChangeListener): Unit {
    }

    public func onUnregisterDataChangeListener(listener: DataChangeListener): Unit {
    }
}

@Entry
@Component
class EntryView {
    private var swiperController: SwiperController = SwiperController()
    private var data: MyDataSource<Int64> = MyDataSource<Int64>(ArrayList<Int64>([]))

    protected override func aboutToAppear() {
        var list: ArrayList<Int64> = ArrayList<Int64>([])
        for (i in 1..=10) {
            list.add(i)
        }
        this.data = MyDataSource<Int64>(list)
    }

    func build() {
        Column(5) {
            Swiper(this.swiperController) {
                LazyForEach(
                    this.data,
                    itemGeneratorFunc: {
                        item: Int64, idx: Int64 => Text(item.toString()).width(90.percent).height(160).backgroundColor(
                            0xAFEEEE).textAlign(TextAlign.Center).fontSize(30)
                    }
                )
            }.cachedCount(2).index(1).autoPlay(true).interval(4000).indicator( // 设置数字导航点样式
                Indicator.digit().top(200).fontColor(Color.GRAY).selectedFontColor(Color.GRAY).digitFont(
                FontOptions(size: 20, weight: FontWeight.Bold))).loop(true).duration(1000).itemSpace(0).displayArrow(
                true)

            Row(12) {
                Button("showNext").onClick({
                    _ => this.swiperController.showNext()
                })

                Button("showPrevious").onClick({
                    _ => this.swiperController.showPrevious()
                })
            }.margin(5)
        }.width(100.percent).margin(top: 5)
    }
}
```

![swiper2](./figures/swiper2.gif)

## 示例代码3（设置按组翻页）

该示例通过displayCount属性实现了按组翻页效果。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.ArrayList

class MyDataSource<T> <: IDataSource<T> {
    private var list: ArrayList<T> = ArrayList<T>([])

    MyDataSource(list: ArrayList<T>) {
        this.list = list
    }

    public func totalCount(): Int64 {
        return this.list.size
    }

    public func getData(index: Int64): T {
        return this.list[index]
    }

    public func onRegisterDataChangeListener(listener: DataChangeListener): Unit {
    }

    public func onUnregisterDataChangeListener(listener: DataChangeListener): Unit {
    }
}

@Entry
@Component
class EntryView {
    private var swiperController: SwiperController = SwiperController()
    private var data: MyDataSource<Int64> = MyDataSource<Int64>(ArrayList<Int64>([]))

    protected override func aboutToAppear() {
        var list: ArrayList<Int64> = ArrayList<Int64>([])
        for (i in 1..=10) {
            list.add(i)
        }
        this.data = MyDataSource<Int64>(list)
    }

    func build() {
        Column(5) {
            Swiper(this.swiperController) {
                LazyForEach(
                    this.data,
                    itemGeneratorFunc: {
                        item: Int64, idx: Int64 => Text(item.toString()).width(90.percent).height(160).backgroundColor(
                            0xAFEEEE).textAlign(TextAlign.Center).fontSize(30)
                    }
                )
            }.displayCount(3, true).autoPlay(true).interval(4000).indicator( // 设置圆点导航点样式
                DotIndicator().itemWidth(15).itemHeight(15).selectedItemWidth(15).selectedItemHeight(15).color(
                Color.GRAY).selectedColor(Color.BLUE)).loop(true).duration(1000)

            Row(12) {
                Button("showNext").onClick({
                    _ => this.swiperController.showNext()
                })

                Button("showPrevious").onClick({
                    _ => this.swiperController.showPrevious()
                })
            }.margin(5)
        }.width(100.percent).margin(top: 5)
    }
}
```

![swiper3](./figures/swiper3.gif)