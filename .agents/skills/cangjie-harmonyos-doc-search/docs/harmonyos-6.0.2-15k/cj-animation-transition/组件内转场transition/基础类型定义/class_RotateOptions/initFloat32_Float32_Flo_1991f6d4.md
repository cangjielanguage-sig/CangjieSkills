#### init(Float32, Float32, Float32, Float32, Length, Length, Length, Float32)

```cangjie
public init(
    angle: Float32,
    x!: Float32 = 0.0,
    y!: Float32 = 0.0,
    z!: Float32 = 0.0,
    centerX!: Length = 50.percent,
    centerY!: Length = 50.percent,
    centerZ!: Length = 0,
    perspective!: Float32 = 0.0
)
```

**功能：** RotateOptions构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|angle|Float32|是|-|旋转角度。取值为正时相对于旋转轴方向顺时针转动，取值为负时相对于旋转轴方向逆时针转动。|
|x|Float32|否|0.0| **命名参数。** 旋转轴向量x坐标。|
|y|Float32|否|0.0| **命名参数。** 旋转轴向量y坐标。|
|z|Float32|否|0.0| **命名参数。** 旋转轴向量z坐标。|
|centerX|[Length](./cj-common-types.md#interface-length)|否|50.percent| **命名参数。** 变换中心点x轴坐标。表示组件变换中心点（即锚点）的x方向坐标。|
|centerY|[Length](./cj-common-types.md#interface-length)|否|50.percent| **命名参数。** 变换中心点y轴坐标。表示组件变换中心点（即锚点）的y方向坐标。|
|centerZ|[Length](./cj-common-types.md#interface-length)|否|0| **命名参数。** z轴锚点，即3D旋转中心点的z轴分量。|
|perspective|Float32|否|0.0| **命名参数。** 视距，即视点到z=0平面的距离。<br>旋转轴和旋转中心点都基于坐标系设定，组件发生位移时，坐标系不会随之移动。|