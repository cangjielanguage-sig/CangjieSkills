## class Matrix4Transit

```cangjie
public class Matrix4Transit {
    public var id: Int64
    public init(id: Int64)
}
```

**功能：** 矩阵对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var id

```cangjie
public var id: Int64
```

**功能：** 表示矩阵的标识id。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### init(Int64)

```cangjie
public init(id: Int64)
```

**功能：** 矩阵对象构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int64|是|-|矩阵的标识id。|

### func combine(Matrix4Transit)

```cangjie
public func combine(target: Matrix4Transit): This
```

**功能：** Matrix的叠加函数，可以将两个矩阵的效果叠加起来生成一个新的矩阵对象。会改变调用该函数的原始矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Matrix4Transit](#class-matrix4transit)|是|-|待叠加的矩阵对象。|

### func copy()

```cangjie
public func copy(): Matrix4Transit
```

**功能：** Matrix的拷贝函数，可以拷贝一份当前的矩阵对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[Matrix4Transit](#class-matrix4transit)|当前矩阵的拷贝对象。|

### func invert()

```cangjie
public func invert(): This
```

**功能：** Matrix的逆函数，可以返回一个当前矩阵对象的逆矩阵，即效果正好相反。会改变调用该函数的原始矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### func rotate(RotateOption)

```cangjie
public func rotate(params: RotateOption): This
```

**功能：** Matrix的旋转函数，可以为当前矩阵增加x轴/y轴/z轴旋转效果。会改变调用该函数的原始矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|params|[RotateOption](#class-rotateoption)|是|-|设置旋转参数。|

### func scale(ScaleOption)

```cangjie
public func scale(params: ScaleOption): This
```

**功能：** Matrix的缩放函数，可以为当前矩阵增加x轴/y轴/z轴缩放效果。会改变调用该函数的原始矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|params|[ScaleOption](#class-scaleoption)|是|-|设置缩放参数。|

### func setPolyToPoly(PolyToPolyOptions)

```cangjie
public func setPolyToPoly(options: PolyToPolyOptions): This
```

**功能：** 将一个多边形的顶点坐标映射到另外一个多边形的顶点坐标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[PolyToPolyOptions](#class-polytopolyoptions)|是|-|映射相关的参数。|

### func skew(Float32, Float32)

```cangjie
public func skew(x: Float32, y: Float32): This
```

**功能：** Matrix的倾斜函数，可以为当前矩阵增加x轴/y轴倾斜效果。会改变调用该函数的原始矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|设置x轴倾斜参数。|
|y|Float32|是|-|设置y轴倾斜参数。|