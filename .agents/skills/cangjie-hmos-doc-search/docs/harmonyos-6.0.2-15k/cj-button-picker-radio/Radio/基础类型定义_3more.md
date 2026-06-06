## 基础类型定义

### enum RadioIndicatorType

```cangjie
public enum RadioIndicatorType {
    | TICK
    | DOT
    | CUSTOM
}
```

**功能：** 单选框的选中样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### CUSTOM

```cangjie
CUSTOM
```

**功能：** 选中样式为indicatorBuilder中的内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### DOT

```cangjie
DOT
```

**功能：** 选中样式为系统默认DOT图标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### TICK

```cangjie
TICK
```

**功能：** 选中样式为系统默认TICK图标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## 示例1 （设置底板颜色）

该示例通过配置checkedBackgroundColor实现自定义单选框的底板颜色。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var radioName: String = "Null"

    func build() {
        Flex(FlexParams(direction: FlexDirection.Row, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center)) {
            Column() {
                Text("Radio1")
                Radio(group: "radioGroup", value: "Radio1").checked(true).height(50).width(50)
            }
            Column() {
                Text("Radio2")
                Radio(group: "radioGroup", value: "Radio2").checked(true).height(50).width(50)
            }
            Column() {
                Text("Radio3")
                Radio(group: "radioGroup", value: "Radio3").checked(true).height(50).width(50)
            }
        }
    }
}
```

![radio](figures/radio.gif)

## 示例2 （设置选中样式）

该示例通过配置indicatorType、indicatorBuilder实现自定义选中样式。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
internal import kit.LocalizationKit.{AppResource, __GenerateResource__}

@Entry
@Component
class EntryView {
    @State
    var message: String = "Hello Cangjie"
    @State
    var select_onselect: String = ""

    func build() {
        Column {
            Flex(FlexParams(direction: FlexDirection.Row, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center
            )) {
                Column {
                    Text('Radio1')
                    Radio(value: '10', group: '数字', indicatorType: RadioIndicatorType.TICK).checked(true).radioStyle(
                        checkedBackgroundColor: Color.RED, uncheckedBorderColor: Color.BLUE, indicatorColor: Color.GRAY).
                        height(50).width(50)
                }
                Column {
                    Text('Radio2')
                    Radio(value: '20', group: '数字', indicatorType: RadioIndicatorType.DOT).checked(false).radioStyle(
                        checkedBackgroundColor: Color.BLUE, uncheckedBorderColor: Color.RED, indicatorColor: Color.GRAY).
                        height(50).width(50)
                }
                Column {
                    Text('Radio3')
                    Radio(value: '30', group: '数字', indicatorType: RadioIndicatorType.CUSTOM,
                        indicatorBuilder: {=> Image(@r(app.media.layered_image))}).checked(false).height(50).width(50).
                        onClick({click => this.select_onselect = 'click radio 30'})
                }
            }
            Text(this.select_onselect).id("select_onchange")
        }
    }
}
```

![radioSample2](figures/radioSample2.gif)