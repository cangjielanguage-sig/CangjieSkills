## 基础类型定义

### class SearchController

```cangjie
public class SearchController <: TextContentControllerBase {
    public init()
}
```

**功能：** Search组件的控制器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [TextContentControllerBase](./cj-common-types.md#interface-textcontentcontrollerbase)

#### init()

```cangjie
public init()
```

**功能：** 创建SearchController类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### func caretPosition(?Int32)

```cangjie
public func caretPosition(value: ?Int32): Unit
```

**功能：** 设置输入光标的位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Int32|是|-|从字符串开始到光标所在位置的字符长度。初始值：0。|

## 示例代码

<!--run-->

```cangjie
package ohos_app_cangjie_entry
import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State var changeValue: String = ""
    @State var submitValue: String = ""

    let controller = SearchController()
    func build() {
        Flex(direction: FlexDirection.Row, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center) {
          Text(submitValue)
          Text(changeValue)
          Search(value: "", placeholder: "Type to search", controller: controller)
            //设置搜索框末尾搜索按钮文本内容为"SearchBtn"
            .searchButton("SearchBtn")
            //宽300，高35
            .width(300)
            .height(35)
            //设置搜索组件背景色
            .backgroundColor(0xDDDDDD)
            //设置palaceholder文本颜色
            .placeholderColor(0x000000)
            //设置placeholder文本样式
            .placeholderFont(size: 26.px, weight: FontWeight.W100, family: "serif", style: FontStyle.Normal)
            .onSubmit({value =>
              submitValue = value
            })
            .onChange({value =>
              changeValue = value
            })
            //设置外边距，组件上部距父容器30vp
            .margin(top: 30)
            .id("searchComponent")
        }
    }
}
```

![search](figures/search.png)