# 动态手势设置

动态设置组件绑定的手势，支持开发者在属性设置时使用if/else语法。

## func gestureModifier(GestureModifier)

```cangjie
public func gestureModifier(modifier: GestureModifier): This
```

**功能：** 动态设置组件绑定的手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|modifier|[GestureModifier](#interface-gesturemodifier)|是|-|手势修改器，开发者需要自定义class实现GestureModifier接口。|

## interface GestureModifier

```cangjie
public interface GestureModifier {
    func applyGesture(event: UIGestureEvent): Unit
}
```

**功能：** 动态设置组件绑定的手势。开发者需要自定义class实现GestureModifier接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### func applyGesture(UIGestureEvent)

```cangjie
func applyGesture(event: UIGestureEvent): Unit
```

**功能：** 组件需要绑定的手势，开发者可根据需要自定义实现这个方法，对组件设置需要绑定的手势，支持使用if/else语法进行动态设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[UIGestureEvent](./cj-universal-gesture-handle.md#class-uigestureevent)|是|-|UIGestureEvent对象，用于设置组件需要绑定的手势。|

## 示例代码

该示例通过GestureModifier动态设置组件绑定的手势。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

class MyButtonModifier <: GestureModifier {
    public func applyGesture(event: UIGestureEvent): Unit {
        event.addGesture(TapGestureHandler().onAction({
            evt => AppLog.info("TapGestureHandler onAction")
        }))
    }
}

@Entry
@Component
class EntryView {
    @State
    var modifier: MyButtonModifier = MyButtonModifier()

    func build() {
        Scroll() {
            Column() {
                Row() {
                    Text("Tap")
                }.height(100).width(200).borderWidth(1).gestureModifier(this.modifier)
            }.width(100.percent)
        }.width(100.percent).width(100.percent)
    }
}
```

![dynamic_gestures](./figures/Dynamic_gestures.png)
