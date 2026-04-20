## class ScaleOptions

```cangjie
public class ScaleOptions {
    public var x: ?Float32
    public var y: ?Float32
    public var z: ?Float32
    public var centerX: ?Length
    public var centerY: ?Length
    public init(x!: ?Float32 = None, y!: ?Float32 = None, z!: ?Float32 = None, centerX!: ?Length = None,
        centerY!: ?Length = None)
}
```

**功能：** 缩放参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var x

```cangjie
public var x: ?Float32
```

**功能：** x轴上的缩放比例。
x > 1: 组件沿x轴放大。
0 < x < 1: 组件沿x轴缩小。
x < 0: 组件沿x轴反方向缩放。

**类型：** ?Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var y

```cangjie
public var y: ?Float32
```

**功能：** y轴上的缩放比例。
y > 1: 组件沿y轴放大。
0 < y < 1: 组件沿y轴缩小。
y < 0: 组件沿y轴反方向缩放。

**类型：** ?Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var z

```cangjie
public var z: ?Float32
```

**功能：** z轴上的缩放比例。
z > 1: 组件沿z轴放大。
0 < z < 1: 组件沿z轴缩小。
z < 0: 组件沿z轴反方向缩放。

**类型：** ?Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var centerX

```cangjie
public var centerX: ?Length
```

**功能：** 变换中心点（锚点）的X坐标。对于数字类型，单位为vp。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var centerY

```cangjie
public var centerY: ?Length
```

**功能：** 变换中心点（锚点）的Y坐标。对于数字类型，单位为vp。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?Float32, ?Float32, ?Float32, ?Length, ?Length)

```cangjie
public init(x!: ?Float32 = None, y!: ?Float32 = None, z!: ?Float32 = None, centerX!: ?Length = None,
        centerY!: ?Length = None)
```

**功能：** ScaleOptions构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|?Float32|否|None|**命名参数。** x轴的缩放倍数。x>1时以x轴方向放大，0<x<1时以x轴方向缩小，x<0时沿x轴反向并缩放。<br>初始值：1.0|
|y|?Float32|否|None|**命名参数。** y轴的缩放倍数。y>1时以y轴方向放大，0<y<1时以y轴方向缩小，y<0时沿y轴反向并缩放。<br>初始值：1.0|
|z|?Float32|否|None|**命名参数。** 	z轴的缩放倍数。z>1时以z轴方向放大，0<z<1时以z轴方向缩小，z<0时沿z轴反向并缩放。<br>初始值：1.0|
|centerX|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 变换中心点x轴坐标。表示组件变换中心点（即锚点）的x方向坐标。对于数字类型，单位为vp。<br>初始值：50.percent|
|centerY|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 变换中心点y轴坐标。表示组件变换中心点（即锚点）的y方向坐标。对于数字类型，单位为vp。<br>初始值：50.percent|