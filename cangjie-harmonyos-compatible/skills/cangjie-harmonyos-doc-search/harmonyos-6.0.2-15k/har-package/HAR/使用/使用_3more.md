## 使用

介绍如何配置HAR依赖，并引用HAR的仓颉组件、接口、资源。

引用HAR前，需要先配置对HAR的依赖，详见[引用HAR文件和资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har-import)。

### 引用HAR的仓颉组件

HAR的依赖配置成功后，可以引用HAR的仓颉组件。通过`import`引入HAR导出的仓颉组件，示例如下所示：

```cangjie
// entry/src/main/cangjie/index.cj
package ohos_app_cangjie_entry

import ohos.base.LengthProp
import ohos.component.Column
import ohos.component.Row
import ohos.component.CustomView
import ohos.component.CJEntry
import ohos.component.loadNativeView
import ohos.state_manage.ObservedProperty
import ohos.state_manage.LocalStorage
import ohos.state_macro_manage.Entry
import ohos.state_macro_manage.Component
import ohos.state_manage.ViewStackProcessor
import ohos.state_manage.SubscriberManager
import ohos.component.LegalCallCheck
import ohos.component.ReuseParams
import ohos.component.ViewBuilder
import ohos.component.__Recycle__
import ohos.component.FakeComponent
import ohos_app_cangjie_library.MainPage

@Entry
@Component
class EntryView {
    func build() {
        Row {
            // 引用HAR的仓颉组件
            MainPage()
        }.height(100.percent)
    }
}
```

### 引用HAR的类和方法

通过`import`引用HAR导出的类和方法，示例如下所示：

```cangjie
// entry/src/main/cangjie/index2.cj
package ohos_app_cangjie_entry

import ohos.base.LengthProp
import ohos.component.Column
import ohos.component.Row
import ohos.component.Text
import ohos.component.CustomView
import ohos.component.CJEntry
import ohos.component.loadNativeView
import ohos.component.FontWeight
import ohos.state_manage.SubscriberManager
import ohos.state_manage.ObservedProperty
import ohos.state_manage.LocalStorage
import ohos.state_macro_manage.Entry
import ohos.state_macro_manage.Component
import ohos.state_macro_manage.State
import ohos_app_cangjie_library.Log
import ohos_app_cangjie_library.harFunc

@Entry
@Component
class EntryView2 {
    @State
    var message: String = "Hello World"

    func build() {
        Row {
            Column {
                Text(this.message).fontSize(50).fontWeight(FontWeight.Bold).onClick {
                    evt =>
                    // 引用HAR的类和方法
                    Log.info("har msg")
                    this.message = "func return: ${harFunc()}"
                }
            }.width(100.percent)
        }.height(100.percent)
    }
}
```