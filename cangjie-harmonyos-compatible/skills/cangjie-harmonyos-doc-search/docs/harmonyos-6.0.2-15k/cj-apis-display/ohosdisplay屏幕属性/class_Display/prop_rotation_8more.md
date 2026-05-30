### prop rotation

```cangjie
public prop rotation: UInt32
```

**功能：** 设置显示设备的屏幕顺时针旋转角度。

> **说明：**
>
> 值为0时，表示显示设备屏幕顺时针旋转为0°；值为1时，表示显示设备屏幕顺时针旋转为90°；值为2时，表示显示设备屏幕顺时针旋转为180°；值为3时，表示显示设备屏幕顺时针旋转为270°。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### prop scaledDensity

```cangjie
public prop scaledDensity: Float32
```

**功能：** 显示设备的显示字体的缩放因子。该参数为浮点数，通常与densityPixels相同。

> **说明：**
>
> 该参数为浮点数，通常与densityPixels相同。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 12

### prop state

```cangjie
public prop state: DisplayState
```

**功能：** 设置显示设备的状态。

**类型：** [DisplayState](#enum-displaystate)

**读写能力：** 只读

**起始版本：** 12

### prop width

```cangjie
public prop width: Int32
```

**功能：** 设置显示设备的屏幕宽度。

> **说明：**
>
> 单位为px，该参数应为整数。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### prop xDPI

```cangjie
public prop xDPI: Float32
```

**功能：** 设置x方向中每英寸屏幕的确切物理像素值。

> **说明：**
>
> 该参数为浮点数。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 12

### prop yDPI

```cangjie
public prop yDPI: Float32
```

**功能：** 设置y方向中每英寸屏幕的确切物理像素值。

> **说明：**
>
> 该参数为浮点数。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 12

### func getAvailableArea()

```cangjie
public func getAvailableArea(): Rect
```

**功能：** 获取当前2in1设备屏幕的可用区域。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[Rect](#class-rect)|返回当前屏幕可用矩形区域。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[屏幕错误码](../errorcodes/cj-errorcode-display.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1400003|ERROR: Failed to get available area.|

**示例:**

```cangjie
import ohos.display.*

func getAvailableAreaExample() {
    try {
        let displayClass = getDefaultDisplaySync()
        let rect = displayClass.getAvailableArea()
        AppLog.info("getAvailableArea left: ${rect.left} top: ${rect.top} width: ${rect.width} heigth: ${rect.height}")
    } catch (exception: Exception) {
        AppLog.error(exception.toString())
    }
}
```

### func getCutoutInfo()

```cangjie
public func getCutoutInfo(): CutoutInfo
```

**功能：** 获取挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。建议应用布局规避该区域。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[CutoutInfo](#class-cutoutinfo)|返回描述不可用屏幕区域的CutoutInfo对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[屏幕错误码](../errorcodes/cj-errorcode-display.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1400001|ERROR: Failed to get cutout info.|
  |1400003|ERROR: Failed to get cutout info.|

**示例:**

```cangjie
import ohos.display.*

func getCutoutInfoExample() {
    try {
        let displayClass = getDefaultDisplaySync()
        let cutout = displayClass.getCutoutInfo()
        println(cutout.boundingRects.size)
    } catch (exception: Exception) {
        AppLog.error(exception.toString())
    }
}
```