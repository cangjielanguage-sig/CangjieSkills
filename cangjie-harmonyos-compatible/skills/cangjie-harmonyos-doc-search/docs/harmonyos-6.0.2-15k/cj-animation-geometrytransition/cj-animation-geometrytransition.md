# 组件内隐式共享元素转场（geometryTransition）

在视图切换过程中提供丝滑的上下文传承过渡。通用transition机制提供了opacity、scale等转场效果，geometryTransition通过安排绑定的in/out组件(in指新视图、out指旧视图)的frame、position使得原本独立的transition动画在空间位置上发生联系，将视觉焦点由旧视图位置引导到新视图位置。

## func geometryTransition(String, Bool)

```cangjie
public func geometryTransition(id: String, followWithoutTransition!: Bool = false): This
```

**功能：** 设置组件内隐式共享元素转场。

> **说明：**
>
> geometryTransition必须配合[animateTo](cj-animation-animateto.md)使用才有动画效果，动效时长、曲线跟随[animateTo](cj-animation-animateto.md)中的配置，不支持[animation](cj-animation-animation.md)隐式动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|String|是|-|用于设置绑定关系，id置空字符串清除绑定关系避免参与共享行为，id可更换重新建立绑定关系。同一个id只能有两个组件绑定且是in/out不同类型角色，不能多个组件绑定同一个id。|
|followWithoutTransition|Bool|否|false| **命名参数。** 仅用于if范式下标记始终在组件树上的组件是否跟随做共享动画。|

## 示例代码

<!-- run -->

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
                Image(@r(app.media.startIcon)).autoResize(false).clip(true).width(300).height(400).offset(x: 0, y: 100).
                    geometryTransition("picture").transition(TransitionEffect.OPACITY)
            } else {
                Column() {
                    Column() {
                        Image(@r(app.media.startIcon)).width(100.percent).height(100.percent)
                    }.width(100.percent).height(100.percent)
                }.width(80).height(80).borderRadius(20).clip(true).geometryTransition("picture").transition(
                    TransitionEffect.OPACITY)
            }
        }.onClick({
            event => animateTo(AnimateParam(duration: 1000), ({=> this.isShow = !this.isShow}))
        })
    }
}
```

![geometrytransition](figures/geometrytransition.gif)
