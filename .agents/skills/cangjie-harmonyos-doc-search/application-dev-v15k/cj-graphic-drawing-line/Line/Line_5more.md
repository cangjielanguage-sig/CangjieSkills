# Line

直线绘制组件。

## 子组件

无

## 创建组件

### init(Length, Length)

```cangjie
public init(width!: Length, height!: Length)
```

**功能：** 在宽度为width、高度为height的填充区域内绘制一条直线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 填充区域宽度，取值范围≥0。<br>默认单位：vp。<br>值为异常值或缺省时按照自身内容需要的宽度处理。|
|height|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 填充区域高度，取值范围≥0。<br>默认单位：vp。<br>值为异常值或缺省时按照自身内容需要的高度处理。|

### init()

```cangjie
public init()
```

**功能：** 在宽度为0、高度为0的填充区域内绘制一条直线。需要设置[width](./cj-universal-attribute-size.md#func-widthlength)或[height](./cj-universal-attribute-size.md#func-heightlength)属性参数不为0才能显示出来。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## 通用属性/通用事件

通用属性：除了支持通用属性外，还支持[图形绘制通用属性](./cj-graphic-drawing-common.md)。

通用事件：全部支持。

## 组件属性

### func endPoint((Float64, Float64))

```cangjie
public func endPoint(value: (Float64, Float64)): This
```

**功能：** 设置直线终点坐标点（相对坐标），异常值按照初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|(Float64,Float64)|是|-|直线终点坐标点（相对坐标）。<br>初始值：[0.0, 0.0]。<br>单位：vp。|

### func endPoint((Int64, Int64))

```cangjie
public func endPoint(value: (Int64, Int64)): This
```

**功能：** 设置直线终点坐标点（相对坐标），异常值按照初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|(Int64,Int64)|是|-|直线终点坐标点（相对坐标）。<br>初始值：[0, 0]。<br>单位：vp。|

### func startPoint((Float64, Float64))

```cangjie
public func startPoint(value: (Float64, Float64)): This
```

**功能：** 设置直线起点坐标点（相对坐标），异常值按照初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|(Float64,Float64)|是|-|直线起点坐标点（相对坐标）。<br>初始值：[0.0, 0.0]。<br>单位：vp。|

### func startPoint((Int64, Int64))

```cangjie
public func startPoint(value: (Int64, Int64)): This
```

**功能：** 设置直线起点坐标点（相对坐标），异常值按照初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|(Int64,Int64)|是|-|直线起点坐标点（相对坐标）。<br>初始值：[0, 0]。<br>单位：vp。|