# Ellipse

椭圆绘制组件。

## 子组件

无

## 创建组件

### init(Length, Length)

```cangjie
public init(width!: Length, height!: Length)
```

**功能：** 绘制一个宽度为width，高度为height的椭圆。异常值按照初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 宽度，取值范围≥0。<br>初始值：0。<br>默认单位：vp。|
|height|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 高度，取值范围≥0。<br>初始值：0。<br>默认单位：vp。|

### init()

```cangjie
public init()
```

**功能：** 绘制一个宽度为0，高度为0的椭圆。需要设置[width](./cj-universal-attribute-size.md#func-widthlength)或[height](./cj-universal-attribute-size.md#func-heightlength)属性参数不为0才能显示出来。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## 通用属性/通用事件

通用属性：除了支持通用属性外，还支持[图形绘制通用属性](./cj-graphic-drawing-common.md)。

通用事件：全部支持。

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
            // 绘制一个 150 * 80 的椭圆
            Ellipse(width: 150, height: 80)
            // 绘制一个 150 * 100 、线条为红色的椭圆环
            Ellipse().width(150).height(100).fillOpacity(0).stroke(Color.RED).strokeWidth(3).padding(top: 10)
        }.width(100.percent)
    }
}
```

![ellipse](./figures/ellipse.png)
