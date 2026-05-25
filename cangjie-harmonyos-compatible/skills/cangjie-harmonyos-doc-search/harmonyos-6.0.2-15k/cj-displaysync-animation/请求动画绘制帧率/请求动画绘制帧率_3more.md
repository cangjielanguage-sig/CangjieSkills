# 请求动画绘制帧率

在应用开发中，[属性动画](../../API_Reference/source_zh_cn/arkui-cj/cj-animation-animation.md)和[显式动画](../../API_Reference/source_zh_cn/arkui-cj/cj-animation-animateto.md)能够使用可选参数[ExpectedFrameRateRange](../../API_Reference/source_zh_cn/arkui-cj/cj-animation-animateto.md#expectedframeraterangeint32-int32-int32)，为不同的动画配置不同的期望绘制帧率。

## 请求属性动画的绘制帧率

定义文本组件的属性动画，请求绘制帧率为60，范例如下：

```cangjie
import kit.UIKit.*

let animateOpt1 = AnimateParam(
    duration: 1200,
    iterations: 10,
    expectedFrameRateRange: ExpectedFrameRateRange( // 设置属性动画的帧率范围
        min: 0, // 设置帧率范围
        max: 120, // 设置帧率范围
        expected: 60 // 设置动画的期望帧率为60hz
    )
)

@Entry
@Component
class EntryView {
    @State
    var message: String = "Hello World"
    func build() {
        Row {
            Column {
                Text(this.message).animationStart(animateOpt1).fontSize(50).fontWeight(FontWeight.Bold).onClick {
                    evt => this.message = "Hello Cangjie"
                }
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

## 请求显式动画的绘制帧率

定义按钮组件的显式动画，请求绘制帧率为30，范例如下：

```cangjie
import kit.UIKit.*

@Entry
@Component
class EntryView {
    @State
    var rotateAngle: Float32 = 0.0
    @State
    var message: String = "Hello World"
    func build() {
        Row {
            Column {
                Text(this.message).fontSize(50).fontWeight(FontWeight.Bold).onClick {
                    evt => animateTo(
                        AnimateParam(
                            duration: 1200,
                            iterations: 10,
                            expectedFrameRateRange: ExpectedFrameRateRange( // 设置属性动画的帧率范围
                                min: 0, // 设置帧率范围
                                max: 120, // 设置帧率范围
                                expected: 30 // 设置动画的期望帧率为30hz
                            )
                        ),
                        {=> this.rotateAngle = 90.0}
                    )
                }
            }.width(100.percent)
        }.height(100.percent)
    }
}
```