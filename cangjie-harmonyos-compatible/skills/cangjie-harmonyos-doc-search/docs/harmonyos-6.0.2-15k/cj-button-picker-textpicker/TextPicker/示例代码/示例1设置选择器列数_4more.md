### 示例1（设置选择器列数）

该示例通过配置range实现单列或多列文本选择器。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    var select: UInt32 = 1
    @State
    var fruits: Array<String> = ["apple", "banana", "orange", "peach"]
    func build() {
        Column {
            TextPicker(this.fruits, selected: this.select).onChange(
                {
                result: TextPickerResData => nativeLog("Picker item changed, value: ${result.index}")
            })
        }.width(100.percent).height(100.percent).alignItems(HorizontalAlign.Center).justifyContent(FlexAlign.Center)
    }
}
```

![textpicker](figures/textpicker.png)

### 示例2（设置文本样式）

该示例通过配置textStyle、selectedTextStyle实现文本选择器中的文本样式。

<!-- run-->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    var select: UInt32 = 1
    @State
    var fruits: Array<String> = ["apple", "banana", "orange", "peach"]
    func build() {
        Column {
            TextPicker(this.fruits, selected: this.select).onChange(
                {
                result: TextPickerResData => nativeLog("Picker item changed, value: ${result.index}")
            }).textStyle(PickerTextStyle(Color.BLACK, MyFont(size: 20, weight: FontWeight.Normal))).selectedTextStyle(
                PickerTextStyle(Color.RED, MyFont(size: 30, weight: FontWeight.Bold)))
        }.width(100.percent).height(100.percent).alignItems(HorizontalAlign.Center).justifyContent(FlexAlign.Center)
    }
}
```

![textpicker5](figures/textpicker5.gif)

### 示例3（设置无分割线样式）

该示例通过配置divider实现无分割线样式的文本选择器。

<!-- run-->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    var select: UInt32 = 1
    @State
    var fruits: Array<String> = ["apple", "banana", "orange", "peach"]
    func build() {
        Column {
            TextPicker(this.fruits, selected: this.select).divider(
                value: DividerOptions(strokeWidth: 0, color: Color.RED, startMargin: 0, endMargin: 0)).onChange(
                {
                result: TextPickerResData => nativeLog("Picker item changed, value: ${result.index}")
            })
        }.width(100.percent).height(100.percent).alignItems(HorizontalAlign.Center).justifyContent(FlexAlign.Center)
    }
}
```

![textpicker2](figures/textpicker2.png)

### 示例4 (设置分割线样式)

该示例通过配置divider的DividerOptions类型实现分割线样式的文本选择器。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    var select: UInt32 = 1
    @State
    var fruits: Array<String> = ["apple", "banana", "orange", "peach"]
    func build() {
        Column {
            TextPicker(this.fruits, selected: this.select).divider(
                value: DividerOptions(strokeWidth: 10, color: Color.RED, startMargin: 10, endMargin: 20)).onChange(
                {
                result: TextPickerResData => nativeLog("Picker item changed, value: ${result.index}")
            })
        }.width(100.percent).height(100.percent).alignItems(HorizontalAlign.Center).justifyContent(FlexAlign.Center)
    }
}
```

![textpicker3](figures/textpicker3.gif)