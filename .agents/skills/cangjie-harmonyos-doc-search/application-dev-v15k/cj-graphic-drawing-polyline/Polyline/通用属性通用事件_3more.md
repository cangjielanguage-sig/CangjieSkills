## 通用属性/通用事件

通用属性：除了支持通用属性外，还支持[图形绘制通用属性](./cj-graphic-drawing-common.md)。

通用事件：全部支持。

## 组件属性

### func points(Array\<(Int64, Int64)>)

```cangjie
public func points(pointList: Array<(Int64, Int64)>): This
```

**功能：** 设置折线的顶点坐标列表。异常值按照初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pointList|Array\<(Int64,Int64)>|是|-|折线的顶点坐标列表。<br>初始值：[]。<br>默认单位：vp。|

### func points(Array\<(Float64, Float64)>)

```cangjie
public func points(pointList: Array<(Float64, Float64)>): This
```

**功能：** 设置折线的顶点坐标列表。异常值按照初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pointList|Array\<(Float64,Float64)>|是|-|折线的顶点坐标列表。<br>初始值：[]。<br>默认单位：vp。|

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
            // 在 100 * 100 的矩形框中绘制一个折线，起点(0, 0)，经过(50, 100)，终点(100, 100)
            Polyline(width: 100, height: 100).points([(0, 0), (50, 100), (100, 100)]).fill(Color.GREEN)
            // 在 100 * 100 的矩形框中绘制一个折线，起点(0, 0)，经过(0, 100)和(100, 100)，终点(100, 200)
            Polyline().width(100).height(100).points([(0, 0), (0, 100), (100, 100), (100, 200)]).fillOpacity(0).
                strokeWidth(5).stroke(Color.BLUE)
        }.width(100.percent).margin(10)
    }
}
```

![polyline](./figures/polyline.png)