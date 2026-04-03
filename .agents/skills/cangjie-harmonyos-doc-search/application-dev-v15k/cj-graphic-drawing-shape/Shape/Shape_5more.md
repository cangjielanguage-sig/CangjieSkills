# Shape

绘制组件的父组件，父组件中会描述所有绘制组件均支持的通用属性。

1、绘制组件使用Shape作为父组件，实现类似SVG的效果。

2、绘制组件单独使用，用于在页面上绘制指定的图形。

## 子组件

包含 [Rect](./cj-graphic-drawing-rect.md)、[Circle](./cj-graphic-drawing-circle.md)、[Ellipse](./cj-graphic-drawing-ellipse.md)、[Image](./cj-image-video-image.md)、[Text](./cj-text-input-text.md)、[Column](./cj-row-column-stack-column.md)、[Row](./cj-row-column-stack-row.md)、Shape子组件。

## 创建组件

### init()

```cangjie
public init()
```

**功能：** Shape组件构造器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(() -> Unit)

```cangjie
public init(content!: () -> Unit)
```

**功能：** Shape组件构造器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|()->Unit|是|-| **命名参数。** 声明Shape容器内支持的子组件。|

### init(PixelMap)

```cangjie
public init(target!: PixelMap)
```

**功能：** Shape组件构造器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|PixelMap|是|-| **命名参数。** 绘制目标，可将图形绘制在指定的PixelMap对象中，若未设置，则在当前绘制目标中进行绘制。|

## 通用属性/通用事件

通用属性：除了支持通用属性外，还支持[图形绘制通用属性](./cj-graphic-drawing-common.md)。

通用事件：全部支持。

## 组件属性

### func mesh(Array\<Float64>, UInt32, UInt32)

```cangjie
public func mesh(array: Array<Float64>, column: UInt32, row: UInt32): This
```

**功能：** 设置mesh效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|array|Array\<Float64>|是|-|长度（column + 1）\*（row + 1）\* 2的数组，它记录了扭曲后的位图各个顶点位置。|
|column|UInt32|是|-|mesh矩阵列数。|
|row|UInt32|是|-|mesh矩阵行数。|

### func mesh(Array\<Int64>, UInt32, UInt32)

```cangjie
public func mesh(array: Array<Int64>, column: UInt32, row: UInt32): This
```

**功能：** 设置mesh效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|array|Array\<Int64>|是|-|长度（column + 1）\*（row + 1）\* 2的数组，它记录了扭曲后的位图各个顶点位置。|
|column|UInt32|是|-|mesh矩阵列数。|
|row|UInt32|是|-|mesh矩阵行数。|

### func viewPort(Length, Length, Length, Length)

```cangjie
public func viewPort(
    x!: Length = 0.vp,
    y!: Length = 0.vp,
    width!: Length = 0.vp,
    height!: Length = 0.vp
): This
```

**功能：** 设置Shape的视口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 视口起始点x坐标。|
|y|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 视口起始点y坐标。|
|width|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 视口宽度。|
|height|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 视口高度。|