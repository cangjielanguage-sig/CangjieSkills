## 使用geometryTransition共享元素转场

[geometryTransition](../../API_Reference/source_zh_cn/arkui-cj/cj-animation-geometrytransition.md)用于组件内隐式共享元素转场，在视图状态切换过程中提供丝滑的上下文继承过渡体验。

geometryTransition的使用方式为对需要添加一镜到底动效的两个组件使用geometryTransition接口绑定同一id，这样在其中一个组件消失同时另一个组件创建出现的时候，系统会对二者添加一镜到底动效。

geometryTransition绑定两个对象的实现方式使得geometryTransition区别于其他方法，最适合用于两个不同对象之间完成一镜到底。

### geometryTransition的简单使用

对于同一个页面中的两个元素的一镜到底效果，geometryTransition接口的简单使用示例如下：

<!-- run-->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import kit.LocalizationKit.*

@Entry
@Component
class EntryView {
    @State
    var isShow: Bool = false
    func build() {
        Stack(Alignment.Center) {
            if (this.isShow) {
                Image(@r(app.media.spring)).autoResize(false).clip(true).width(200).height(200).borderRadius(100).
                    geometryTransition("picture").transition(TransitionEffect.OPACITY).id("item1")
            } else {
                Column() {
                    Column() {
                        Image(@r(app.media.sky)).width(100.percent).height(100.percent)
                    }.width(100.percent).height(100.percent)
                }.width(100).height(100)
                    // geometryTransition会同步圆角，但仅限于geometryTransition绑定处，此处绑定的是容器
                    // 则对容器本身有圆角同步而不会操作容器内部子组件的borderRadius
                    .borderRadius(20).clip(true).position(x: 40, y: 40).geometryTransition(
                    "picture")
                        // transition保证节点离场不被立即析构，设置通用转场效果
                        .transition(TransitionEffect.OPACITY).id("item2")
            }
        }.onClick(
            {
            event => animateTo(AnimateParam(duration: 1000, curve: Curve.Linear), ({=> this.isShow = !this.isShow}))
        }).size(width: 100.percent, height: 100.percent)
    }
}
```

![shared-element-transition1](./figures/shared-element-transition1.gif)