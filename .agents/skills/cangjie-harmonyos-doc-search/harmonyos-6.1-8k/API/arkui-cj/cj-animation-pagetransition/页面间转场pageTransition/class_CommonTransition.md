## class CommonTransition

```cangjie
abstract sealed class CommonTransition {}
```

**功能：** 页面转场通用动效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func slide(SlideEffect)

```cangjie
public func slide(value: SlideEffect): This
```

**功能：** 设置页面转场时的滑入滑出效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[SlideEffect](#enum-slideeffect)|是|-|页面转场时的滑入滑出效果。|

### func translate(?Length, ?Length, ?Length)

```cangjie
public func translate(x!: ?Length = None, y!: ?Length = None, z!: ?Length = None): This
```

**功能：** 设置页面转场时的平移效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** x轴的平移距离。<br>取值范围为(-∞, +∞)。<br>初始值：0.0.vp。|
|y|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** y轴的平移距离。<br>取值范围为(-∞, +∞)。<br>初始值：0.0.vp。|
|z|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** z轴的平移距离。<br>取值范围为(-∞, +∞)。<br>初始值：0.0.vp。|

### func scale(?Float32, ?Float32, ?Float32, ?Length, ?Length)

```cangjie
public func scale(
    x!: ?Float32 = None,
    y!: ?Float32 = None,
    z!: ?Float32 = None,
    centerX!: ?Length = None,
    centerY!: ?Length = None
): This
```

**功能：** 设置页面转场时的缩放效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|?Float32|否|None|**命名参数。** x轴的缩放倍数。x>1时以x轴方向放大，0<x<1时以x轴方向缩小，x<0时沿x轴反向并缩放。<br>初始值：1.0。|
|y|?Float32|否|None|**命名参数。** y轴的缩放倍数。y>1时以y轴方向放大，0<y<1时以y轴方向缩小，y<0时沿y轴反向并缩放。<br>初始值：1.0。|
|z|?Float32|否|None|**命名参数。** z轴的缩放倍数。z>1时以z轴方向放大，0<z<1时以z轴方向缩小，z<0时沿z轴反向并缩放。<br>初始值：1.0。|
|centerX|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 变换中心点x轴坐标。<br>初始值：50.percent。|
|centerY|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 变换中心点y轴坐标。<br>初始值：50.percent。|

### func opacity(Float64)

```cangjie
public func opacity(value: Float64): This
```

**功能：** 设置入场的起点透明度值或者退场的终点透明度值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|设置入场的起点透明度值或者退场的终点透明度值。取值范围[0.0, 1.0]，0.0表示完全透明，1.0表示完全不透明。|