## 通用属性/通用事件

**通用属性：** 全部支持

**通用事件：** 全部支持

## 组件属性

### func color(ResourceColor)

```cangjie
public func color(value: ResourceColor): This
```

**功能：** 设置超链接文本的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|超链接文本的颜色。<br/>phone初始值：0xff0a59f7。|

## 示例代码

该示例展示了超链接图片和文本跳转的效果。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.*
import ohos.resource_manager.__GenerateResource__

@Entry
@Component
class EntryView {
    func build() {
        Column() {
            Column() {
                Hyperlink(address: "https://www.huawei.com/", content: "jumper to huawei").color(Color.BLUE)
            }
            Column() {
                Hyperlink("https://www.huawei.com/") {
                    Image(@r(app.media.startIcon)).width(100).height(100)
                }
            }
        }
    }
}
```

![hyperlink](figures/hyperlink.png)