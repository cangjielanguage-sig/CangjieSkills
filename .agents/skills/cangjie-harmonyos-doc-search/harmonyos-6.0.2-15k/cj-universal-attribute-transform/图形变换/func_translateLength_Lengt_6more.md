## func translate(Length, Length, Length)

```cangjie
public func translate(x!: Length = 0.vp, y!: Length = 0.vp, z!: Length = 0.vp): This
```

**功能：** 设置组件平移距离。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

> **说明：**
>
> 可使组件在以组件左上角为坐标原点的坐标系中进行移动（坐标系如下图所示）。其中，x，y，z的值分别表示在对应轴移动的距离，值为正时表示向对应轴的正向移动，值为负时表示向对应轴的反向移动。<br/>默认值:<br/>{x:&nbsp;0,y:&nbsp;0,z:&nbsp;0}<br/>单位：vp。<br/>![coordinates](figures/coordinates.png) <br>**说明：** z轴方向移动时由于观察点位置不变，z的值接近观察点组件会有放大效果，远离则缩小。<br/>![coordinateNode](figures/coordinateNote.png)|

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|[Length](cj-common-types.md#interface-length)|否|0.vp| **命名参数。** X轴平移距离。|
|y|[Length](cj-common-types.md#interface-length)|否|0.vp| **命名参数。** Y轴平移距离。|
|z|[Length](cj-common-types.md#interface-length)|否|0.vp| **命名参数。** Z轴平移距离。|

## func translateX(Int64)

```cangjie
public func translateX(value: Int64): This
```

**功能：** 设置组件X轴平移距离,距离的正负控制平移的方向(单位为vp)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| value |Int64 |是|-|X轴平移距离。|

## func translateX(Length)

```cangjie
public func translateX(value: Length): This
```

**功能：** 设置组件X轴平移距离,距离的正负控制平移的方向(单位为vp)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| value |[Length](cj-common-types.md#interface-length)|是|-|X轴平移距离。|

## func translateY(Int64)

```cangjie
public func translateY(value: Int64): This
```

**功能：** 设置组件Y轴平移距离,距离的正负控制平移的方向(单位为vp)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| value |Int64|是|-|Y轴平移距离。|

## func translateY(Length)

```cangjie
public func translateY(value: Length): This
```

**功能：** 设置组件Y轴平移距离,距离的正负控制平移的方向(单位为vp)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| value |[Length](cj-common-types.md#interface-length)|是|-|Y轴平移距离。|

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
            Text("rotate").width(90.percent).fontColor(0xCCCCCC).padding(15).fontSize(14)
            Row().rotate(
                x: 1.0,
                y: 1.0,
                z: 1.0,
                angle: 300.0,
                centerX: 50.percent,
                centerY: 50.percent
            ) // 组件以矢量(1,1,1)为旋转轴，绕中心点顺时针旋转300度
                .width(100).height(100).backgroundColor(0xAFEEEE)

            Text("translate").width(90.percent).fontColor(0xCCCCCC).padding(10).fontSize(14)
            Row().translate(x: 100, y: 10) // x轴方向平移100，y轴方向平移10
                .width(100).height(100).backgroundColor(0xAFEEEE).margin(bottom: 10)

            Text("scale").width(90.percent).fontColor(0xCCCCCC).padding(15).fontSize(14)
            Row().scale(x: 2.0, y: 0.5) // 高度缩小一倍，宽度放大一倍，z轴在2D下无效果
                .width(100).height(100).backgroundColor(0xAFEEEE)
        }.width(100.percent).margin(top: 5)
    }
}
```

![uni_transform](figures/uni_transform.png)