### 引用HAR的资源

通过`@r`引用HAR中的资源，例如在HAR模块的`src/main/resources`里添加字符串资源（在string.json中定义，name：hello_har）和图片资源（icon_har.png），然后在Entry模块中引用该字符串和图片资源的示例如下所示：

```cangjie
// entry/src/main/cangjie/index3.cj
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
import ohos.state_macro_manage.r
import ohos.resource_manager.__GenerateResource__
import ohos.component.Image
import ohos.component.List
import ohos.component.ListItem
import ohos.component.ListItemAlign

@Entry
@Component
class EntryView3 {
    @State
    var message: String = "Hello World"

    func build() {
        Row {
            Column {
                // 引用HAR的字符串资源
                Text(@r(app.string.hello_har)).fontSize(50).fontWeight(FontWeight.Bold).onClick {
                    evt => this.message = "Hello Cangjie"
                }
                List() {
                    ListItem() {
                        // 引用HAR的图片资源
                        Image(@r(app.media.icon_har)).id('iconHar').borderRadius(48.px)
                    }.margin(5.percent).width(312.px)
                }.alignListItem(ListItemAlign.Center)
            }.width(100.percent)
        }.height(100.percent)
    }
}
```