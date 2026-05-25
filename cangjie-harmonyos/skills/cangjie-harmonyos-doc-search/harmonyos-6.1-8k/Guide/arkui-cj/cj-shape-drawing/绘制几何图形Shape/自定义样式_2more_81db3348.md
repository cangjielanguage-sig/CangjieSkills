## 自定义样式

绘制组件支持通过各种属性对组件样式进行更改。

- 通过[fill](../reference/arkui-cj/cj-graphic-drawing-common.md#func-fillresourcecolor)可以设置组件填充区域颜色。

  <!-- code_check_manual -->

  ```cangjie
  Path()
      .width(100)
      .height(100)
      .commands('M150 0 L300 300 L0 300 Z')
      .fill(0xE87361)
      .strokeWidth(0)
  ```

  ![drawing3](figures/drawing3.jpg)

- 通过[stroke](../reference/arkui-cj/cj-graphic-drawing-common.md#func-strokeresourcecolor)可以设置组件边框颜色。

  <!-- code_check_manual -->

  ```cangjie
  Path()
      .width(100)
      .height(100)
      .fillOpacity(0.0)
      .commands('M150 0 L300 300 L0 300 Z')
      .stroke(Color.Red)
  ```

  ![stroke](figures/stroke.png)

- 通过[strokeOpacity](../reference/arkui-cj/cj-graphic-drawing-common.md#func-strokeopacityappresource)可以设置边框透明度。

  <!-- code_check_manual -->

  ```cangjie
  Path()
      .width(100)
      .height(100)
      .fillOpacity(0.0)
      .commands('M150 0 L300 300 L0 300 Z')
      .stroke(Color.Red)
      .strokeWidth(10)
      .strokeOpacity(0.2)
  ```

  ![strokeopacity](figures/strokeopacity.jpg)

- 通过[antiAlias](../reference/arkui-cj/cj-graphic-drawing-common.md#func-antialiasbool)设置是否开启抗锯齿，默认值为true（开启抗锯齿）。

  <!-- code_check_manual -->

  ```cangjie
  // 开启抗锯齿
  Circle()
      .width(150)
      .height(200)
      .fillOpacity(0.0)
      .strokeWidth(5)
      .stroke(Color.Black)
  ```

  ![antiAliasTrue](figures/antiAliasTrue.png)

  <!-- code_check_manual -->

  ```cangjie
  // 关闭抗锯齿
  Circle()
      .width(150)
      .height(200)
      .fillOpacity(0.0)
      .strokeWidth(5)
      .stroke(Color.Black)
      .antiAlias(false)
  ```

  ![antiAliasFalse](figures/antiAliasFalse.jpg)

## 场景示例

### 绘制封闭路径

在Shape的(-80, -5)点绘制一个封闭路径，填充颜色0x317AF7，线条宽度3，边框颜色红色，拐角样式锐角（默认值）。

 <!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Column(space: 10) {
            Shape() {
                Path().width(200).height(60).commands('M0 0 L400 0 L400 150 Z')
            }
            .viewPort( x: -80, y: -5, width: 500, height: 300 )
            .fill(0x317AF7)
            .stroke(Color.Red)
            .strokeWidth(3)
            .strokeLineJoin(LineJoinStyle.Miter)
            .strokeMiterLimit(5.0)
        }.width(100.percent).margin( top: 15 )
    }
}
```

![scene1](figures/scene1.jpg)

### 绘制圆和圆环

绘制一个直径为150的圆，和一个直径为150、线条为红色虚线的圆环（宽高设置不一致时以短边为直径）。

 <!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Column(space: 10) {
            //绘制一个直径为150的圆
            Circle( width: 150, height: 150 )
            //绘制一个直径为150、线条为红色虚线的圆环
            Circle()
                .width(150)
                .height(200)
                .fillOpacity(0.0)
                .strokeWidth(3)
                .stroke(Color.Red)
                .strokeDashArray([1, 2])
        }.width(100.percent).margin( top: 15 )
    }
}
```

![场景2](figures/scene2.png)