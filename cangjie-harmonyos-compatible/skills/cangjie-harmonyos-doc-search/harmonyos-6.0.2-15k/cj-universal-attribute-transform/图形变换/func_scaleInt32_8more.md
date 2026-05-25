## func scale(Int32)

```cangjie
public func scale(scaleValue: Int32): This
```

**功能：** 设置组件缩放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scaleValue|Int32|是|-|缩放倍数。|

## func scale(Float32, Float32, Float32, Length, Length)

```cangjie
public func scale(
    x!: Float32 = 1.0,
    y!: Float32 = 1.0,
    z!: Float32 = 1.0,
    centerX!: Length = 50.percent,
    centerY!: Length = 50.percent
): This
```

**功能：** 设置组件缩放。

> **说明：**
>
> 可以分别设置X轴、Y轴、Z轴的缩放比例，默认值为1.0；同时可以通过centerX和centerY设置缩放的中心点。单独传Int32或者Float32时，同时在X轴、Y轴缩放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|否|1.0| **命名参数。** X轴缩放比例。|
|y|Float32|否|1.0| **命名参数。** Y轴缩放比例。|
|z|Float32|否|1.0| **命名参数。** Z轴缩放比例。|
|centerX|[Length](cj-common-types.md#interface-length)|否|50.percent| **命名参数。** 变换中心点x轴坐标。表示组件变换中心点（即锚点）的x方向坐标。|
|centerY|[Length](cj-common-types.md#interface-length)|否|50.percent| **命名参数。** 变换中心点y轴坐标。表示组件变换中心点（即锚点）的y方向坐标。|

## func scaleX(Float32)

```cangjie
public func scaleX(scale: Float32): This
```

**功能：** 设置X轴的缩放比例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scale|Float32|是|-|X轴的缩放比例。|

## func scaleX(Int32)

```cangjie
public func scaleX(scale: Int32): This
```

**功能：** 设置X轴的缩放比例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scale|Int32|是| - |X轴的缩放比例。|

## func scaleY(Float32)

```cangjie
public func scaleY(scale: Float32): This
```

**功能：** 设置Y轴的缩放比例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scale|Float32|是|-|Y轴的缩放比例。|

## func scaleY(Int32)

```cangjie
public func scaleY(scale: Int32): This
```

**功能：** 设置Y轴的缩放比例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scale|Int32|是|-|Y轴的缩放比例。|

## func transform(Matrix4Transit)

```cangjie
public func transform(matrix: Matrix4Transit): This
```

**功能：** 设置当前组件的变换矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|matrix|[Matrix4Transit](./cj-apis-matrix4.md#class-matrix4transit)|是|-|当前组件的变换矩阵。|

## func translate(Length)

```cangjie
public func translate(value: Length): This
```

**功能：** 设置组件平移距离。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|平移距离。|