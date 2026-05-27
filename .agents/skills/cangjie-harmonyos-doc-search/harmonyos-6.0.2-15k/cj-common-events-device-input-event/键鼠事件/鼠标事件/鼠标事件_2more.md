## 鼠标事件

支持的鼠标事件包含通过外设鼠标、触控板触发的事件。

鼠标可触发以下事件：

| 名称                                       | 描述                                       |
|:---------------------------------------- |:---------------------------------------- |
|  onHover(callback: (isHover: Bool)->Unit) | 鼠标进入或退出组件时，触发该事件。<br>isHover：表示鼠标是否悬浮在组件上，鼠标进入时为true，退出时为false。|
|  onMouse(callback: (event: MouseEvent)->Unit) | 当前组件被鼠标按键点击时或者鼠标在组件上悬浮移动时，触发该事件。<br>event返回值包含触发事件时的时间戳、鼠标按键、动作、鼠标位置在整个屏幕上的坐标和相对于当前组件的坐标。|

当组件绑定onHover事件时，可以通过[hoverEffect](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-hovereffect.md)属性设置该组件的鼠标悬浮态显示效果。

鼠标事件的原理如下图所示：

![Hover](./figures/Hover_mouse.png)

鼠标事件传递到ArkUI之后，会先判断鼠标事件是否是左键的按下/抬起/移动，然后做出不同响应：

- 是：鼠标事件先转换成相同位置的触摸事件，执行触摸事件的碰撞测试、手势判断和回调响应。接着去执行鼠标事件的碰撞测试和回调响应。

- 否：事件仅用于执行鼠标事件的碰撞测试和回调响应。

> **说明：**
>
> 所有单指可响应的触摸事件/手势事件，均可通过鼠标左键来操作和响应。例如当我们需要开发单击Button跳转页面的功能、且需要支持手指点击和鼠标左键点击，那么只绑定一个点击事件（onClick）就可以实现该效果。若需要针对手指和鼠标左键的点击实现不一样的效果，可以在onClick回调中，使用回调参数中的source字段即可判断出当前触发事件的来源是手指还是鼠标。

### onHover

```cangjie
public func onHover(callback: (Bool)->Unit): This
```

鼠标悬浮事件。参数类型为Bool，表示鼠标进入组件或离开组件。该事件不支持自定义冒泡设置，默认父子冒泡。

若组件绑定了该接口，当鼠标指针从组件外部进入到该组件的瞬间会触发事件，参数值为true；鼠标指针离开组件的瞬间也会触发该事件，参数值为false。

> **说明：**
>
> 事件冒泡：在一个树形结构中，当子节点处理完一个事件后，再将该事件交给它的父节点处理。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var hoverText: String = 'Not Hover'
    @State
    var color: Color = Color.GRAY

    func build() {
        Column() {
            Button(this.hoverText).width(200).height(100).backgroundColor(this.color).onHover(
                {
                isHover => // 使用onHover接口监听鼠标是否悬浮在Button组件上
                if (isHover) {
                    this.hoverText = 'Hovered!'
                    this.color = Color.GREEN
                } else {
                    this.hoverText = ' Hover'
                    this.color = Color.GRAY
                }
            })
        }.width(100.percent).height(100.percent).justifyContent(FlexAlign.Center)
    }
}
```

该示例创建了一个Button组件，初始背景色为灰色，内容为“Not Hover”，示例中的Button组件绑定了onHover回调。

当鼠标从Button外移动到Button内的瞬间，回调响应，参数值为true，将组件的背景色改成Color.Green，内容变为“Hovered!”。

当鼠标从Button内移动到Button外的瞬间，回调响应，参数值为false，又将组件变成了初始的样式。

![onHover](./figures/onHover.gif)