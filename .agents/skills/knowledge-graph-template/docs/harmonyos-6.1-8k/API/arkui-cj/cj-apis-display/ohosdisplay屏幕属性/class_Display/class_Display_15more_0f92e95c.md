## class Display

```cangjie
public class Display {
}
```

**功能：** 定义显示屏的属性。它们不会自动更新。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### prop alive

```cangjie
public prop alive: Bool
```

**功能：** 显示屏是否处于活动状态。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### prop densityDpi

```cangjie
public prop densityDpi: Float64
```

**功能：** 显示屏密度，以像素为单位，是物理像素和逻辑像素之间的缩放系数。低分辨率显示屏的值为1.0。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### prop densityPixels

```cangjie
public prop densityPixels: Float64
```

**功能：** 显示分辨率，即每英寸的像素数。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### prop height

```cangjie
public prop height: Int64
```

**功能：** 显示屏高度，以像素为单位。

**类型：** Int64

**读写能力：** 只读

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### prop id

```cangjie
public prop id: Int64
```

**功能：** 显示屏ID。

**类型：** Int64

**读写能力：** 只读

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### prop name

```cangjie
public prop name: String
```

**功能：** 显示屏名称。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### prop orientation

```cangjie
public prop orientation: Orientation
```

**功能：** 显示屏方向。

**类型：** [Orientation](#enum-orientation)

**读写能力：** 只读

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### prop refreshRate

```cangjie
public prop refreshRate: UInt32
```

**功能：** 刷新率，以Hz为单位。

**类型：** UInt32

**读写能力：** 只读

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### prop rotation

```cangjie
public prop rotation: UInt32
```

**功能：** 显示屏旋转度数的枚举值。
值0表示显示屏顺时针旋转0°。
值1表示显示屏顺时针旋转90°。
值2表示显示屏顺时针旋转180°。
值3表示显示屏顺时针旋转270°。

**类型：** UInt32

**读写能力：** 只读

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### prop scaledDensity

```cangjie
public prop scaledDensity: Float64
```

**功能：** 显示屏文本缩放密度。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### prop state

```cangjie
public prop state: DisplayState
```

**功能：** 显示屏状态。

**类型：** [DisplayState](#enum-displaystate)

**读写能力：** 只读

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### prop width

```cangjie
public prop width: Int64
```

**功能：** 显示屏宽度，以像素为单位。

**类型：** Int64

**读写能力：** 只读

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### prop xDpi

```cangjie
public prop xDpi: Float64
```

**功能：** x轴上的DPI。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### prop yDpi

```cangjie
public prop yDpi: Float64
```

**功能：** y轴上的DPI。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22