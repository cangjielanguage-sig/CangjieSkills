## 页面切换方式

Swiper支持手指滑动、点击导航点和通过控制器三种方式切换页面，以下示例展示通过控制器切换页面的方法。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    private var swiperBackgroundColors: Array<Color> = [Color.BLUE, Color.BROWN, Color.GRAY, Color.GREEN, Color.ORANGE,
        Color.PINK, Color.RED, Color.YELLOW]
    private var swiperController: SwiperController = SwiperController();
    @State
    var animationModeStr: Bool = false
    @State
    var targetIndex: Int64 = 0
    func build() {
        Column(5) {
            Swiper(this.swiperController) {
                ForEach(
                    this.swiperBackgroundColors,
                    itemGeneratorFunc: {
                        item: Color, index: Int64 => Text(index.toString()).width(250).height(250).backgroundColor(item).
                            textAlign(TextAlign.Center).fontSize(30)
                    }
                )
            }.indicator(true)

            Row(12) {
                Button('showNext').onClick({
                    => this.swiperController.showNext(); // 通过controller切换到后一页
                })
                Button('showPrevious').onClick({
                    => this.swiperController.showPrevious(); // 通过controller切换到前一页
                })
            }.margin(5)
            Row(12) {
                Text('Index:')
                Button(this.targetIndex.toString()).onClick(
                    {
                    => this.targetIndex = (this.targetIndex + 1) % this.swiperBackgroundColors.toArray().size
                })
            }.margin(5)
            Row(12) {
                Text('AnimationMode:')
                Button(this.animationModeStr.toString()).onClick(
                    {
                    => if (this.animationModeStr == false) {
                        this.animationModeStr = true
                    } else {
                        this.animationModeStr = false
                    }
                })
            }.margin(5)
            Row(12) {
                Button("changeIndex(${this.targetIndex},${this.animationModeStr})").onClick(
                    {
                    => this.swiperController.changeIndex(Int32(this.targetIndex), this.animationModeStr)
                })
            }.margin(5)
        }.width(100.percent).margin(top: 5)
    }
}
```

![controll](figures/controll.gif)

## 轮播方向

Swiper支持水平和垂直方向上进行轮播，主要通过vertical属性控制。

当vertical为true时，表示在垂直方向上进行轮播；为false时，表示在水平方向上进行轮播。vertical默认值为false。

- 设置水平方向上轮播。

  ```cangjie
  Swiper() {
    // ...
  }
  .indicator(true)
  .vertical(false)
  ```

  ![verticalFalse](figures/verticalFalse.PNG)

- 设置垂直方向轮播。

  ```cangjie
  Swiper() {
    // ...
  }
  .indicator(true)
  .vertical(true)
  ```

  ![verticalTrue](figures/verticalTrue.PNG)

## 每页显示多个子页面

Swiper支持在一个页面内同时显示多个子组件，通过[displayCount](../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-swiper.md#func-displaycountint32)属性设置。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Column(5) {
            Swiper() {
                Text('0').width(250).height(250).backgroundColor(Color.GRAY).textAlign(TextAlign.Center).fontSize(30)
                Text('1').width(250).height(250).backgroundColor(Color.GREEN).textAlign(TextAlign.Center).fontSize(30)
                Text('2').width(250).height(250).backgroundColor(Color.PINK).textAlign(TextAlign.Center).fontSize(30)
                Text('3').width(250).height(250).backgroundColor(Color.BLUE).textAlign(TextAlign.Center).fontSize(30)
            }.indicator(true).displayCount(2)
        }.width(100.percent)
    }
}
```

![two](figures/two.PNG)