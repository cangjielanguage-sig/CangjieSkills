### func setTransform(Float64, Float64, Float64, Float64, Float64, Float64)

```cangjie
public func setTransform(
    a: Float64,
    b: Float64,
    c: Float64,
    d: Float64,
    e: Float64,
    f: Float64
): Unit
```

**功能：** 对应一个变换矩阵，想对一个图形进行变化的时候，只要设置此变换矩阵相应的参数，对图形的各个定点的坐标分别乘以这个矩阵，就能得到新的定点的坐标。setTransform()方法会重置现有的变换矩阵并创建新的变换矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|a|Float64|是|-|指定水平缩放值。|
|b|Float64|是|-|指定水平倾斜值。|
|c|Float64|是|-|指定垂直倾斜值。|
|d|Float64|是|-|指定垂直缩放值。|
|e|Float64|是|-|指定水平移动值。<br>默认单位：vp。|
|f|Float64|是|-|指定垂直移动值。<br>默认单位：vp。|

### func setTransform(Option\<Matrix2D>)

```cangjie
public func setTransform(matrix: Option<Matrix2D>): Unit
```

**功能：** 以Matrix2D对象为模板重置现有的变换矩阵并创建新的变换矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|matrix|Option\<[Matrix2D](cj-canvas-drawing-matrix2d.md#class-matrix2d)>|是|-|变换矩阵。|

### func translate(Float64, Float64)

```cangjie
public func translate(x: Float64, y: Float64): Unit
```

**功能：** 移动当前坐标系的原点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|设置水平平移量。<br>默认单位：vp。|
|y|Float64|是|-|设置竖直平移量。<br>默认单位：vp。|

### func restore()

```cangjie
public func restore(): Unit
```

**功能：** 恢复保存的绘图上下文。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func save()

```cangjie
public func save(): Unit
```

**功能：** 将当前状态放入栈中，保存canvas的全部状态，通常在需要保存绘制状态时调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func createLinearGradient(Float64, Float64, Float64, Float64)

```cangjie
public func createLinearGradient(x0: Float64, y0: Float64, x1: Float64, y1: Float64): CanvasGradient
```

**功能：** 创建一个线性渐变色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x0|Float64|是|-|起点的x轴坐标。<br>默认单位：vp。|
|y0|Float64|是|-|起点的y轴坐标。<br>默认单位：vp。|
|x1|Float64|是|-|终点的x轴坐标。<br>默认单位：vp。|
|y1|Float64|是|-|终点的y轴坐标。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:---|:---|
|[CanvasGradient](cj-canvas-drawing-canvas.md#class-canvasgradient)|渐变对象。使用完毕后需要释放。|