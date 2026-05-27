# Rect

矩形绘制组件。

## 子组件

无

## 创建组件

### init(Length, Length)

```cangjie
public init(width!: Length, height!: Length)
```

**功能：** 绘制一个宽度为width，高度为height的矩形。异常值按照初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 矩形宽度，取值范围≥0。<br>初始值：0。<br>默认单位：vp。|
|height|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 矩形高度，取值范围≥0。<br>初始值：0。<br>默认单位：vp。|

### init()

```cangjie
public init()
```

**功能：** 绘制一个宽度为0，高度为0的矩形。需要设置[width](./cj-universal-attribute-size.md#func-widthlength)或[height](./cj-universal-attribute-size.md#func-heightlength)属性参数不为0才能显示出来。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## 通用属性/通用事件

通用属性：除了支持通用属性外，还支持[图形绘制通用属性](./cj-graphic-drawing-common.md)。

通用事件：全部支持。