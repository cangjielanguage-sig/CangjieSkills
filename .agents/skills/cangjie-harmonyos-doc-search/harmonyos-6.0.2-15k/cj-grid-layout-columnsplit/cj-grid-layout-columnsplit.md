# ColumnSplit

将子组件纵向布局，并在每个子组件之间插入一根横向的分割线。

## 子组件

可以包含子组件。

ColumnSplit通过分割线限制子组件的高度。初始化时，分割线位置根据子组件的高度来计算。初始化后，后续动态修改子组件的高度则不生效，分割线位置保持不变，子组件高度可以通过拖动相邻分割线进行改变。

初始化后，动态修改[margin](./cj-universal-attribute-size.md#func-marginlength)、[border](./cj-universal-attribute-border.md#func-borderlength-resourcecolor-length-borderstyle)、[padding](./cj-universal-attribute-size.md#func-paddinglength)通用属性导致子组件尺寸大于相邻分割线间距的异常情况下，此时不支持拖动分割线改变子组件的高度。

## 创建组件

### init(() -> Unit)

```cangjie
public init(content: () -> Unit)
```

**功能：** 创建一个可以包含子组件的纵向布局。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|()->Unit|是|-|ColumnSplit组件的子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。

## 组件属性

### func divider(Length, Length)

```cangjie
public func divider(startMargin!: Length = 0.vp, endMargin!: Length = 0.vp): This
```

**功能：** 设置分割线的margin。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|startMargin|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 分割线与其上方子组件的距离。|
|endMargin|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 分割线与其下方子组件的距离。|

> **说明：**
>
> - 与[RowSplit](./cj-grid-layout-rowsplit.md)相同，ColumnSplit的分割线可以改变上下两边子组件的高度，子组件可改变高度的范围取决于子组件的最大最小高度。
> - 支持[clip](./cj-universal-attribute-shapclip.md)、[margin](./cj-universal-attribute-size.md#func-marginlength)等通用属性，clip不设置的时候默认值为true。

### func resizeable(Bool)

```cangjie
public func resizeable(value: Bool): This
```

**功能：** 设置分割线是否可拖拽。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|分割线是否可拖拽。<br>初始值：false。|

## 示例代码

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Column() {
            Text("The secant line can be dragged").fontSize(9).fontColor(0xCCCCCC).width(90.percent)
            ColumnSplit() {
                Text("1").width(100.percent).height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
                Text("2").width(100.percent).height(50).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
                Text("3").width(100.percent).height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
                Text("4").width(100.percent).height(50).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
                Text("5").width(100.percent).height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
            }.borderWidth(1).resizeable(true) // 可拖动
                .width(90.percent).height(60.percent)
        }.width(100.percent).padding(top: 5)
    }
}
```

![column_split](./figures/column_split.gif)
