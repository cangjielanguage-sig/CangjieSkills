# Polygon

多边形绘制组件。

## 子组件

无

## 创建组件

### init(Length, Length)

```cangjie
public init(width!: Length, height!: Length)
```

**功能：** 绘制一个宽度为width，高度为height的多边形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 宽度，取值范围≥0。<br>初始值：0。<br>默认单位：vp。<br>异常值按照初始值处理。|
|height|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 高度，取值范围≥0。<br>初始值：0。<br>默认单位：vp。<br>异常值按照初始值处理。|

### init()

```cangjie
public init()
```

**功能：** 绘制一个宽度为0，高度为0的多边形。需要设置[width](./cj-universal-attribute-size.md#func-widthlength)或[height](./cj-universal-attribute-size.md#func-heightlength)属性参数不为0才能显示出来。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## 通用属性/通用事件

通用属性：除了支持通用属性外，还支持[图形绘制通用属性](./cj-graphic-drawing-common.md)。

通用事件：全部支持。

## 组件属性

### func points(Array\<(Int64, Int64)>)

```cangjie
public func points(value: Array<(Int64, Int64)>): This
```

**功能：** 设置多边形的顶点坐标列表。异常值按照初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Array\<(Int64,Int64)>|是|-|折线的顶点坐标列表。<br>初始值：[]。<br>默认单位：vp。|

### func points(Array\<(Float64, Float64)>)

```cangjie
public func points(value: Array<(Float64, Float64)>): This
```

**功能：** 设置多边形的顶点坐标列表。异常值按照初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Array\<(Float64,Float64)>|是|-|折线的顶点坐标列表。<br>初始值：[]。<br>默认单位：vp。|

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
        Column(10) {
            // 在 100 * 100 的矩形框中绘制一个三角形，起点(0, 0)，经过(50, 100)，终点(100, 0)
            Polygon(width: 100, height: 100).points([(0, 0), (50, 100), (100, 0)]).fill(Color.GREEN)
            // 在 100 * 100 的矩形框中绘制一个四边形，起点(0, 0)，经过(0, 100)和(100, 100)，终点(100, 0)
            Polygon().width(100).height(100).points([(0, 0), (0, 100), (100, 100), (100, 0)]).fillOpacity(0).strokeWidth(
                5).stroke(Color.BLUE)
            // 在 100 * 100 的矩形框中绘制一个五边形，起点(50, 0)，依次经过(0, 50)、(20, 100)和(80, 100)，终点(100, 50)
            Polygon().width(100).height(100).points([(50, 0), (0, 50), (20, 100), (80, 100), (100, 50)]).fill(Color.RED).
                fillOpacity(0.6)
        }.width(100.percent).margin(10)
    }
}
```

![polygon](./figures/polygon.png)
