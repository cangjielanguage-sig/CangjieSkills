# 图形变换

用于对组件进行旋转、平移、缩放、矩阵变换等操作。

## func rotate(Float32, Float32, Float32, Float64, Length, Length)

```cangjie
public func rotate(
    x!: Float32 = 0.0,
    y!: Float32 = 0.0,
    z!: Float32 = 0.0,
    angle!: Float32 = 0.0,
    centerX!: Length = 50.percent,
    centerY!: Length = 50.percent
): This
```

**功能：** 设置组件旋转。

> **说明：**
>
> - 可使组件在以组件左上角为坐标原点的坐标系中进行旋转（坐标系如下图所示）。其中，(x, y, z)指定一个矢量，作为旋转轴。
> - 旋转轴和旋转中心点都基于坐标系设定，组件发生位移时，坐标系不会随之移动。
> - 默认值: 在x、y、z都不指定时，x、y、z的默认值分别为0.0、0.0、0.0。指定了x、y、z任何一个值时，x、y、z中未指定的值默认为0。
> ![coordinates](figures/coordinates.png)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|否|0.0| **命名参数。** 旋转轴向量x坐标。|
|y|Float32|否|0.0| **命名参数。** 旋转轴向量y坐标。|
|z|Float32|否|0.0| **命名参数。** 旋转轴向量z坐标。|
|angel|Float32|否|0.0|**命名参数。** 旋转角度。取值为正时相对于旋转轴方向顺时针转动，取值为负时相对于旋转轴方向逆时针转动。|
|centerX|[Length](cj-common-types.md#interface-length)|否|50.percent| **命名参数。** 变换中心点x轴坐标。表示组件变换中心点（即锚点）的x方向坐标。|
|centerY|[Length](cj-common-types.md#interface-length)|否|50.percent| **命名参数。** 变换中心点y轴坐标。表示组件变换中心点（即锚点）的y方向坐标。|

## func rotateX(Float32)

```cangjie
public func rotateX(rotateVal: Float32): This
```

**功能：** 以X轴旋转指定角度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rotateVal|Float32|是|-|旋转轴向量x坐标。|

## func rotateX(Int32)

```cangjie
public func rotateX(rotateVal: Int32): This
```

**功能：** 以X轴旋转指定角度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rotateVal|Int32|是|-|旋转轴向量x坐标。|

## func rotateY(Float32)

```cangjie
public func rotateY(rotateVal: Float32): This
```

**功能：** 以Y轴旋转指定角度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rotateVal|Float32|是|-|旋转轴向量y坐标。|

## func rotateY(Int32)

```cangjie
public func rotateY(rotateVal: Int32): This
```

**功能：** 以Y轴旋转指定角度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rotateVal|Int32|是|-|旋转轴向量y坐标。|

## func rotate(Float32)

```cangjie
public func rotate(rotateZ: Float32): This
```

**功能：** 设置组件旋转。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rotateZ|Float32|是|-|z轴锚点，即3D旋转中心点的z轴分量。|

## func rotate(Int32)

```cangjie
public func rotate(rotateZ: Int32): This
```

**功能：** 设置组件旋转。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rotateZ|Int32|是|-|z轴锚点，即3D旋转中心点的z轴分量。|

## func scale(Float32)

```cangjie
public func scale(scaleValue: Float32): This
```

**功能：** 设置组件缩放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scaleValue|Float32|是|-|缩放倍数。|