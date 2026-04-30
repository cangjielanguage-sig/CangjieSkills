## class Display

```cangjie
public class Display {}
```

**功能：** 设置屏幕实例。描述Display对象的属性和方法。

> **说明:**
>
> 下列API示例中都需先使用[getAllDisplays()](#func-getalldisplays)、[getDefaultDisplaySync()](#func-getdefaultdisplaysync)中的任一方法获取到Display对象，再通过此实例调用对应方法。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### prop alive

```cangjie
public prop alive: Bool
```

**功能：** 设置显示设备是否启用。true表示设备启用，false表示设备未启用。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### prop availableHeight

```cangjie
public prop availableHeight: UInt32
```

**功能：** 2in1设备上屏幕的可用区域高度。

> **说明：**
>
> 单位为px，该参数为大于0的整数。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### prop availableWidth

```cangjie
public prop availableWidth: UInt32
```

**功能：** 设置2in1设备上屏幕的可用区域宽度。

> **说明：**
>
> 单位为px，该参数为大于0的整数。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### prop colorSpaces

```cangjie
public prop colorSpaces: Array<ColorSpace>
```

**功能：** 设置显示设备支持的所有色域类型。

**类型：** Array\<[color_manager.ColorSpace](../apis/ArkGraphics2D/cj-apis-color_manager.md#enum-colorspace)>

**读写能力：** 只读

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[屏幕错误码](../errorcodes/cj-errorcode-display.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1400003|ERROR: Failed to get cutout info.|

### prop densityDPI

```cangjie
public prop densityDPI: Float32
```

**功能：** 设置显示设备屏幕的物理像素密度，表示每英寸上的像素点数。

> **说明：**
>
> 该参数为浮点数，单位为px。一般取值160.0、480.0等，实际能取到的值取决于不同设备设置里提供的可选值。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 12

### prop densityPixels

```cangjie
public prop densityPixels: Float32
```

**功能：** 设置显示设备的逻辑密度，是像素单位无关的缩放系数。

> **说明：**
>
> 该参数为浮点数，受densityDPI范围限制，取值范围在[0.5，4.0]。一般取值1.0、3.0等，实际取值取决于不同设备提供的densityDPI。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 12

### prop hdrFormats

```cangjie
public prop hdrFormats: Array<HDRFormat>
```

**功能：** 设置显示设备支持的所有HDR格式。

**类型：**  Array\<[HDRFormat](#enum-hdrformat)>

**读写能力：** 只读

**起始版本：** 12

### prop height

```cangjie
public prop height: Int32
```

**功能：** 显示设备的屏幕高度。

> **说明：**
>
> 单位为px，该参数应为整数。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### prop id

```cangjie
public prop id: UInt32
```

**功能：** 设置显示设备的id号，该参数应为大于等于0的整数。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### prop name

```cangjie
public prop name: String
```

**功能：** 设置显示设备的名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### prop orientation

```cangjie
public prop orientation: Orientation
```

**功能：** 设置屏幕当前显示的方向。

**类型：** [Orientation](#enum-orientation)

**读写能力：** 只读

**起始版本：** 12

### prop refreshRate

```cangjie
public prop refreshRate: UInt32
```

**功能：** 设置显示设备的刷新率。

> **说明：**
>
>该参数应为整数，单位为hz。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12