# 浮层

设置组件的遮罩文本。

## func overlay(String, Alignment, ContentOffset)

```cangjie
public func overlay(
    title!: String,
    align!: Alignment = Alignment.Center,
    offset!: ContentOffset = ContentOffset(x: 0.0, y: 0.0)
): This
```

**功能：** 在当前组件上，增加遮罩文本作为该组件的浮层。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| title   | String | 是   | - | **命名参数。**  遮罩文本内容。 |
| align   | [Alignment](./cj-common-types.md#enum-alignment) | 否   | Alignment.Center | **命名参数。**  浮层相对于组件的方位。 |
| offset   | [ContentOffset](#class-contentoffset) | 否   | ContentOffset(x: 0.0, y: 0.0) | **命名参数。**  浮层基于自身左上角的偏移量。浮层默认处于组件左上角。|

> **说明：**
>
> align和offset都设置时，效果重叠，浮层相对于组件方位定位后，再基于当前位置的左上角进行偏移。

## 基础类型定义

### class ContentOffset

```cangjie
public class ContentOffset {
    public var xOffset: Float64
    public var yOffset: Float64
    public init(x!: Float64, y!: Float64)
    public init(x!: Int64, y!: Int64)
}
```

**功能：** 表示浮层基于自身左上角的偏移量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var xOffset

```cangjie
public var xOffset: Float64
```

**功能：** 文本基于自身左上角沿X轴的偏移量，单位vp。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var yOffset

```cangjie
public var yOffset: Float64
```

**功能：** 文本基于自身左上角沿y轴的偏移量，单位vp。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(Float64, Float64)

```cangjie
public init(x!: Float64, y!: Float64)
```

**功能：** 构造浮层偏移量数据结构。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| x | Float64 | 是 | - | **命名参数。**  文本基于自身左上角沿X轴的偏移量。</br>单位:vp。 |
| y | Float64 | 是 | - | **命名参数。**  文本基于自身左上角沿Y轴的偏移量。</br>单位:vp。 |

#### init(Int64, Int64)

```cangjie
public init(x!: Int64, y!: Int64)
```

**功能：** 构造浮层偏移量数据结构。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| x | Int64 | 是 | - | **命名参数。**  文本基于自身左上角沿X轴的偏移量。</br>单位:vp。 |
| y | Int64 | 是 | - | **命名参数。**  文本基于自身左上角沿Y轴的偏移量。</br>单位:vp。 |

## 示例代码

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import kit.LocalizationKit.*

@Entry
@Component
class EntryView {
    func build() {
        Column(10) {
            Column() {
                Text("floating layer").fontSize(12).fontColor(0xCCCCCC).maxLines(1)
                Column() {
                    // 导入图片
                    Image(@r(app.media.icon)).width(240).height(240)
                        // 设置浮层
                        .overlay(
                        title: "Winter is a beautiful season, especially when it snows.",
                        align: Alignment.Bottom,
                        offset: ContentOffset(x: 0.0, y: -15.0)
                    )
                }.border(color: Color.BLACK, width: 2.px)
            }.width(100.percent)
        }
    }
}
```

![uni_overlay](figures/uni_overlay.png)
