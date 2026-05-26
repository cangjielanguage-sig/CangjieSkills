## class pageTransition

```cangjie
sealed abstract class pageTransition {}
```

**功能：** 页面转场通用动效基类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func scale(Float32, Float32, Float32, Length, Length)

```cangjie
public func scale(
    x!: Float32 = 1.0,
    y!: Float32 = 1.0,
    z!: Float32 = 1.0,
    centerX!: Length = 50.percent,
    centerY!: Length = 50.percent
): This
```

**功能：** 设置页面转场时的缩放效果。

> **说明：**
>
> 参数为为入场时起点和退场时终点的值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|否|1.0| **命名参数。** 横向放大倍数（或缩小比例）。|
|y|Float32|否|1.0| **命名参数。** 纵向放大倍数（或缩小比例）。|
|z|Float32|否|1.0| **命名参数。** 竖向放大倍数（或缩小比例）。|
|centerX|[Length](./cj-common-types.md#interface-length)|否|50.percent| **命名参数。** X轴缩放中心点。默认以页面的中心点为旋转中心点。<br>中心点为(0, 0)代表页面的左上角。|
|centerY|[Length](./cj-common-types.md#interface-length)|否|50.percent| **命名参数。** Y轴缩放中心点。默认以页面的中心点为旋转中心点。<br>中心点为(0, 0)代表页面的左上角。|

### func slide(SlideEffect)

```cangjie
public func slide(value: SlideEffect): This
```

**功能：** 设置页面转场时的滑入滑出效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[SlideEffect](#enum-slideeffect)|是|-|页面转场时的滑入滑出效果。|

### func translate(Length, Length, Length)

```cangjie
public func translate(x!: Length = 0.vp, y!: Length = 0.vp, z!: Length = 0.vp): This
```

**功能：** 设置页面转场时的平移效果。

> **说明：**
>
> 参数为为入场时起点和退场时终点的值，和slide同时设置时默认生效slide。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** x轴的平移距离。|
|y|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** y轴的平移距离。|
|z|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** z轴的平移距离。|

### func opacity(Float64)

```cangjie
public func opacity(value: Float64): This
```

**功能：** 设置入场的起点透明度值或者退场的终点透明度值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|入场的起点透明度值或者退场的终点透明度值。<br>取值范围：\[0.0, 1.0]。|

### func opacity(Int64)

```cangjie
public func opacity(value: Int64)
```

**功能：** 设置入场的起点透明度值或者退场的终点透明度值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int64|是|-|入场的起点透明度值或者退场的终点透明度值。<br>取值范围：\[0, 1]。|