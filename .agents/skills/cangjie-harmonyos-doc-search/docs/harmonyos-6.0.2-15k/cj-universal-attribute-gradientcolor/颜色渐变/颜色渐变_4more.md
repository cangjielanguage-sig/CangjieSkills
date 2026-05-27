# 颜色渐变

设置组件的颜色渐变效果。

> **说明：**
>
> - 颜色渐变属于组件内容，绘制在背景上方。
> - 颜色渐变不支持宽高显式动画，执行宽高动画时颜色渐变会直接过渡到终点。

## func linearGradient(Option\<Float64>, GradientDirection, Array\<(Color,Float64)>, Bool)

```cangjie
public func linearGradient(
    angle!: Option<Float64> = None,
    direction!: GradientDirection = Bottom,
    colors!: Array<(Color, Float64)> = [(Color.TRANSPARENT, 0.0)],
    repeating!: Bool = false
): This
```

**功能：** 设置线性渐变。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|angle|Option\<Float64>|否|None| **命名参数。** 线性渐变的起始角度。0点方向顺时针旋转为正向角度。|
|direction|[GradientDirection](./cj-common-types.md#enum-gradientdirection)|否|GradientDirection.Bottom| **命名参数。**  线性渐变的方向，设置angle后不生效。|
|colors|Array\<([Color](./cj-common-types.md#class-color),Float64)>|否|[(Color.TRANSPARENT, 0.0)]| **命名参数。** 指定渐变色颜色和其对应的百分比位置的数组，设置非法颜色直接跳过。|
|repeating|Bool|否|false| **命名参数。** 为渐变的颜色重复着色。 |

## func sweepGradient((Length,Length), Float64, Float64, Float64, Array\<(Color,Float64)>, Bool)

```cangjie
public func sweepGradient(
    center: (Length, Length),
    start!: Float64 = 0.0,
    end!: Float64 = 0.0,
    rotation!: Float64 = 0.0,
    colors!: Array<(Color, Float64)> = [(Color.TRANSPARENT, 0.0)],
    repeating!: Bool = false
): This
```

**功能：** 设置角度渐变。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|center|([Length](./cj-common-types.md#interface-length),[Length](./cj-common-types.md#interface-length))|是|-|为角度渐变的中心点，即相对于当前组件左上角的坐标。|
|start|Float64|否|0.0| **命名参数。** 角度渐变的起点。|
|end|Float64|否|0.0| **命名参数。** 角度渐变的终点。|
|rotation|Float64|否|0.0| **命名参数。** 角度渐变的旋转角度。|
|colors|Array\<([Color](./cj-common-types.md#class-color),Float64)>|否|[(Color.TRANSPARENT, 0.0)]| **命名参数。** 指定渐变色颜色和其对应的百分比位置的数组，设置非法颜色直接跳过。|
|repeating|Bool|否|false| **命名参数。** 为渐变的颜色重复着色。|

> **说明：**
>
> start、end、rotation设置为小于0的值时，按值为0处理；设置为大于360的值时，按值为360处理。

## func radialGradient((Length,Length), Float64, Array\<(Color,Float64)>, Bool)

```cangjie
public func radialGradient(
    center: (Length, Length),
    radius: Float64,
    colors!: Array<(Color, Float64)> = [(Color.TRANSPARENT, 0.0)],
    repeating!: Bool = false
): This
```

**功能：** 设置径向渐变。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|center|([Length](./cj-common-types.md#interface-length),[Length](./cj-common-types.md#interface-length))|是|-|为角度渐变的中心点，即相对于当前组件左上角的坐标。|
|radius|Float64|是|-|径向渐变的半径。<br>取值范围：\[0.0,+∞)。<br> **说明：** <br> 设置为小于的0值时，按值为0处理。初始值：0.0。|
|colors|Array\<([Color](./cj-common-types.md#class-color), Float64)>|否|[(Color.TRANSPARENT, 0.0)]| **命名参数。** 指定渐变色颜色和其对应的百分比位置的数组，设置非法颜色直接跳过。|
|repeating|Bool|否|false| **命名参数。** 为渐变的颜色重复着色。|