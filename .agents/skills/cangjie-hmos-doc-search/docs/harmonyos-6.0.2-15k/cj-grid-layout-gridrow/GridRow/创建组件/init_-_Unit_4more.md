### init(() -> Unit)

```cangjie
public init(child: () -> Unit)
```

**功能：** 创建一个可包含子组件的GridRow容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|child|()->Unit|是|-|GridRow容器的子组件。|

### init(Int32, BreakPoints, GridRowDirection, () -> Unit)

```cangjie
public init(
    columns!: Int32,
    breakpoints!: BreakPoints = BreakPoints(),
    direction!: GridRowDirection = GridRowDirection.GridRowRow,
    child!: () -> Unit
)
```

**功能：** 创建一个可包含子组件的GridRow容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|columns|Int32|是|-| **命名参数。** 布局列数设置。<br>取值为大于0的整数，初始值：12。|
|breakpoints|[BreakPoints](#class-breakpoints)|否|BreakPoints()| **命名参数。** 断点值的断点数列以及基于窗口或容器尺寸的相应参照。<br>初始值：<br>{<br>value: ["320vp", "600vp", "840vp"],reference: BreakpointsReference.WindowSize<br>}|
|direction|[GridRowDirection](#enum-gridrowdirection)|否|GridRowDirection.GridRowRow| **命名参数。** 栅格布局排列方向。|
|child|()->Unit|是|-| **命名参数。** GridRow 容器的子组件。|

### init(GridRowColumnOption, BreakPoints, GridRowDirection, () -> Unit)

```cangjie
public init(
    columns!: GridRowColumnOption,
    breakpoints!: BreakPoints = BreakPoints(),
    direction!: GridRowDirection = GridRowDirection.GridRowRow,
    child!: () -> Unit
)
```

**功能：** 创建一个可包含子组件的GridRow容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|columns|[GridRowColumnOption](#struct-gridrowcolumnoption)|是|-| **命名参数。** 布局列数设置。|
|breakpoints|[BreakPoints](#class-breakpoints)|否|BreakPoints()| **命名参数。** 断点值的断点数列以及基于窗口或容器尺寸的相应参照。<br>初始值：<br>{<br>value: ["320vp", "600vp", "840vp"],reference: BreakpointsReference.WindowSize<br>}|
|direction|[GridRowDirection](#enum-gridrowdirection)|否|GridRowDirection.GridRowRow| **命名参数。** 栅格布局排列方向。|
|child|()->Unit|是|-| **命名参数。** GridRow 容器的子组件。|

### init(Length, BreakPoints, GridRowDirection, () -> Unit)

```cangjie
public init(
    gutter!: Length,
    breakpoints!: BreakPoints = BreakPoints(),
    direction!: GridRowDirection = GridRowDirection.GridRowRow,
    child!: () -> Unit
)
```

**功能：** 创建一个可包含子组件的GridRow容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|gutter|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 栅格布局间距，x代表水平方向。<br>初始值：0。|
|breakpoints|[BreakPoints](#class-breakpoints)|否|BreakPoints()| **命名参数。** 断点值的断点数列以及基于窗口或容器尺寸的相应参照。<br>初始值：<br>{<br>value: ["320vp", "600vp", "840vp"],reference: BreakpointsReference.WindowSize<br>}|
|direction|[GridRowDirection](#enum-gridrowdirection)|否|GridRowDirection.GridRowRow| **命名参数。** 栅格布局排列方向。|
|child|()->Unit|是|-| **命名参数。** GridRow容器的子组件。|