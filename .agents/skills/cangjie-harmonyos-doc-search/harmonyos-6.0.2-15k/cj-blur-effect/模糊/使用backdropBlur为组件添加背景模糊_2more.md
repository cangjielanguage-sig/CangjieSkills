## 使用backdropBlur为组件添加背景模糊

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.__GenerateResource__

@Entry
@Component
class EntryView {
    func build() {
        Column(10) {
            Text('backdropBlur').width(90.percent).height(90.percent).fontSize(20).fontColor(Color.WHITE).textAlign(
                TextAlign.Center).backdropBlur(10).backgroundImage(src: @r(app.media.share)).backgroundImageSize(
                width: 400, height: 300)
        }.width(100.percent).height(50.percent).margin(top: 30)
    }
}
```

![blur](./figures/blur.PNG)

## 使用blur为组件添加内容模糊

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.__GenerateResource__

@Entry
@Component
class EntryView {
    @State
    var radius: Float64 = 0.0
    @State
    var text: String = ''
    @State
    var y: String = '手指不在屏幕上'

    protected override func aboutToAppear() {
        this.text = "按住屏幕上下滑动\n" + "当前手指所在y轴位置 ： " + this.y + "\n" + "当前图片模糊程度为 : " +
            this.radius.toString()
    }

    func build() {
        Flex(
            FlexOptions(direction: FlexDirection.Column, justifyContent: FlexAlign.SpaceBetween,
            alignItems: ItemAlign.Center)) {
            Text(this.text).height(200).fontSize(20).fontWeight(FontWeight.Bold).fontFamily("cursive").fontStyle(
                FontStyle.Italic)
            Image(@r(app.media.share)).blur(this.radius).height(100.percent).width(100.percent).objectFit(
                ImageFit.Cover)
        }.height(100.percent).width(100.percent).onTouch(
            {
                event: TouchEvent =>
                if (event.eventType.getValue() == TouchType.Move.getValue()) {
                    this.y = event.touches[0].y.toString()
                    this.radius = event.touches[0].y / 10.0
                }
                if (event.eventType.getValue() == TouchType.Up.getValue()) {
                    this.radius = 0.0
                    this.y = '手指离开屏幕'
                }
                this.text = "按住屏幕上下滑动\n" + "当前手指所在y轴位置 ： " + this.y + "\n" +
                    "当前图片模糊程度为 : " + this.radius.toString()
            }
        )
    }
}
```

![blur2](./figures/blur2.gif)