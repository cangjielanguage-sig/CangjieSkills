## 合理控制对象类型状态变量关联的组件数量

如果将一个复杂对象定义为状态变量，需要合理控制其关联的组件数。当对象中某一个成员属性发生变化时，会导致该对象关联的所有组件刷新，尽管这些组件可能并没有直接使用到该改变的属性。为了避免这种“冗余刷新”对性能产生影响，建议合理拆分该复杂对象，控制对象关联的组件数量。具体请参见[状态管理合理使用开发指导](cj-properly-use-state-management-to-develope.md)。

## 避免在for、while等循环逻辑中频繁读取状态变量

在应用开发中，应避免在循环逻辑中频繁读取状态变量，而是应该放在循环外面读取。

【反例】

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.hilog.Hilog

@Entry
@Component
class EntryView {
    @State
    var message: String = "message"

    func build() {
        Column() {
            Button("点击打印日志").onClick({
                event => for (i in 0..10 : 1) {
                    Hilog.info(0, "test", this.message)
                }
            }).width(90.percent).backgroundColor(Color.BLUE).fontColor(Color.WHITE).margin(top: 10)
        }.justifyContent(FlexAlign.Start).alignItems(HorizontalAlign.Center).margin(top: 15)
    }
}
```

【正例】

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.hilog.Hilog

@Entry
@Component
class EntryView {
    @State
    var message: String = "message"

    func build() {
        Column() {
            Button("点击打印日志").onClick(
                {
                    event =>
                    let logMessage: String = this.message
                    for (i in 0..10 : 1) {
                        Hilog.info(0, "test", logMessage)
                    }
                }
            ).width(90.percent).backgroundColor(Color.BLUE).fontColor(Color.WHITE).margin(top: 10)
        }.justifyContent(FlexAlign.Start).alignItems(HorizontalAlign.Center).margin(top: 15)
    }
}
```