## func accessibilityVirtualNode(() -> Unit)

```cangjie
public func accessibilityVirtualNode(builder: () -> Unit): This
```

**功能：** 设置无障碍虚拟子节点。对自绘制组件传入一个自定义UI描述，该UI描述中的组件在后端仅做布局不做显示，辅助应用获取无障碍节点信息时会返回UI描述中的节点信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|()->Unit|是|-|无障碍虚拟子节点，使开发者可以对自绘制组件传入一个自定义UI描述，该UI描述中的组件在后端仅做布局不做显示，辅助应用获取无障碍节点信息时会返回UI描述中的节点信息。使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|

## 示例代码

<!--run-->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import kit.LocalizationKit.*

@Entry
@Component
class EntryView {
    func build() {
        Row {
            Column {
                Text("文本1").fontSize(50).fontWeight(FontWeight.Bold)
                Text("文本2").fontSize(50).fontWeight(FontWeight.Bold)
            }.width(100.percent).accessibilityGroup(true).accessibilityLevel("yes").accessibilityText("分组").
                accessibilityDescription("Column组件可以被选中，播报的内容是“分组”")
        }.height(100.percent)
    }
}
```