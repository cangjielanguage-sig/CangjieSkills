## class Matrix4

```cangjie
public class Matrix4 {}
```

**功能：** 表示为列优先的四阶矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### static func initialize(Array\<Float64>)

```cangjie
public static func initialize(array: Array<Float64>): Matrix4Transit
```

**功能：** Matrix的构造函数，可以通过传入的参数创建一个四阶矩阵，矩阵为列优先。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|array|Array\<Float64>|是|-|长度为16（4*4）的数组，详见四阶矩阵说明。各数组元素取值范围： (-∞, +∞)<br>初始值：<br>[1, 0, 0, 0,<br>0, 1, 0, 0,<br>0, 0, 1, 0,<br>0, 0, 0, 1]|

**四阶矩阵说明：**

| 参数名 | 类型 | 必填  | 描述 |
| :--- | :--- | :--- | :--- |
| m00 | Float64  | 是 |x轴缩放值，单位矩阵默认为1。|
| m01 | Float64  | 是 |第2个值，xyz轴旋转或倾斜会影响这个值。|
| m02 | Float64  | 是 |第3个值，xyz轴旋转会影响这个值。|
| m03 | Float64  | 是 |第4个值，透视投影会影响这个值。|
| m10 | Float64  | 是 |第5个值，xyz轴旋转或倾斜会影响这个值。|
| m11 | Float64  | 是 |y轴缩放值，单位矩阵默认为1。|
| m12 | Float64  | 是 |第7个值，xyz轴旋转会影响这个值。|
| m13 | Float64  | 是 |第8个值，透视投影会影响这个值。|
| m20 | Float64  | 是 |第9个值，xyz轴旋转会影响这个值。|
| m21 | Float64  | 是 |第10个值，xyz轴旋转会影响这个值。|
| m22 | Float64  | 是 |z轴缩放值，单位矩阵默认为1。|
| m23 | Float64  | 是 |第12个值，透视投影会影响这个值。|
| m30 | Float64  | 是 |x轴平移值，单位px，单位矩阵默认为0。|
| m31 | Float64  | 是 |y轴平移值，单位px，单位矩阵默认为0。|
| m32 | Float64  | 是 |z轴平移值，单位px，单位矩阵默认为0。|
| m33 | Float64  | 是 |齐次坐标下生效，产生透视投影效果。|

**返回值：**

|类型|说明|
|:----|:----|
|[Matrix4Transit](#class-matrix4transit)|根据入参创建的四阶矩阵对象。|

### static func identity()

```cangjie
public static func identity(): Matrix4Transit
```

**功能：** Matrix的初始化函数，可以返回一个单位矩阵对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[Matrix4Transit](#class-matrix4transit)|单位矩阵对象。|