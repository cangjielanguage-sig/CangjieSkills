# 挂载卸载事件

挂载卸载事件指组件从组件树上挂载、卸载时触发的事件。

## func onAppear(() -> Unit)

```cangjie
public func onAppear(callback: ()->Unit): This
```

**功能：** 组件挂载显示时触发此回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|组件挂载显示回调函数，回调的调用时机有可能发生在组件布局渲染后。|

## func onDisAppear(() -> Unit)

```cangjie
public func onDisAppear(callback: ()->Unit): This
```

**功能：** 组件卸载消失时触发此回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|组件卸载消失回调函数，回调的调用时机有可能发生在组件布局渲染后。|

## 示例代码

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var isShow: Bool = true
    @State
    var changeAppear: String = "点我卸载挂载组件"
    var myText: String = "Text for onAppear"
    func build() {
        Column {
            Button(this.changeAppear).onClick({
                evt => this.isShow = !this.isShow
            }).margin(15.vp)
            if (this.isShow) {
                Text(this.myText).fontSize(26).fontWeight(FontWeight.Bold).onAppear(
                    {
                    => PromptAction.showToast(message: "The text is shown", bottom: "500vp")
                }).onDisAppear({
                    => PromptAction.showToast(message: "The text is hidden", bottom: "500vp")
                })
            }
        }.width(100.percent).height(100.percent)
    }
}
```

![appear](figures/appear.gif)
