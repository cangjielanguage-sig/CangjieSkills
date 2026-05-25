## func radialGradient((Length,Length), Length, Array\<(Color,Float64)>, Bool)

```cangjie
public func radialGradient(
    center: (Length, Length),
    radius: Length,
    colors!: Array<(Color, Float64)> = [(Color.TRANSPARENT, 0.0)],
    repeating!: Bool = false
): This
```

**功能：** 设置径向渐变。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|参数类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|center|([Length](./cj-common-types.md#interface-length), Length)|是|-|为角度渐变的中心点，即相对于当前组件左上角的坐标。|
|radius|[Length](./cj-common-types.md#interface-length)|是|-|径向渐变的半径。<br>取值范围：\[0.0,+∞)。<br>说明：设置为小于的0.0值时，按值为0.0处理。初始值：0.0.vp。|
|colors|Array\<([Color](./cj-common-types.md#class-color), Float64)>|否|[(Color.TRANSPARENT, 0.0)]| **命名参数。** 指定渐变色颜色和其对应的百分比位置的数组，设置非法颜色直接跳过。|
|repeating|Bool|否|false| **命名参数。** 为渐变的颜色重复着色。|

> **说明：**
>
> - colors参数的约束：
> - Color表示填充的颜色，Float64表示指定颜色所处的位置，取值范围为[0,1.0]，0表示需要设置渐变色的容器的开始处，1.0表示容器的结尾处。想要实现多个颜色渐变效果时，多个数组中Float64参数建议递增设置，如后一个数组Float64参数比前一个数组Float64小的话，按照等于前一个数组Float64的值处理。