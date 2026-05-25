# ohos.screenshot（屏幕截图）

本模块提供屏幕截图的能力。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## func capture(CaptureOption)

```cangjie
public func capture(options!: CaptureOption = CaptureOption()): PixelMap
```

**功能：** 获取屏幕全屏截图，此接口仅支持在平板和2in1设备上使用。与[pick](#func-pick)接口不同之处是可以通过设置不同的displayId截取不同屏幕的截图。

**需要权限：** ohos.permission.CUSTOM_SCREEN_CAPTURE

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[CaptureOption](#class-captureoption)|否|CaptureOption()| **命名参数。** 截取图像的相关信息。可包含设备ID，即displayId。 此参数不填时，默认截取displayId为0的屏幕截图。|

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)|返回一个PixelMap对象。|

**异常：**

- BusinessException：对应错误码如下表。

  |错误码ID|错误信息|
  |:---|:---|
  |201|ERROR: Failed to get default PixelMap.|
  |401|ERROR: Failed to get default PixelMap.|
  |801|ERROR: Failed to get default PixelMap.|
  |1400003|ERROR: Failed to get default PixelMap.|

## func pick()

```cangjie
public func pick(): PickInfo
```

**功能：** 获取屏幕截图。此接口仅可在2in1设备上使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[PickInfo](#class-pickinfo)|返回一个PickInfo对象。|

**异常：**

- BusinessException：对应错误码如下表。

|错误码ID|错误信息|
|:---|:---|
|201|ERROR: Failed to get default PickInfo.|
|401|ERROR: Failed to get default PickInfo.|
|801|ERROR: Failed to get default PickInfo.|
|1400003|ERROR: Failed to get default PickInfo.|

## class CaptureOption

```cangjie
public class CaptureOption {
    public CaptureOption(
        public var displayId!: Int32 = 0
    )
}
```

**功能：** 设置截取图像的信息。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### var displayId

```cangjie
public var displayId: Int32 = 0
```

**功能：** 表示截取图像的显示设备[Display](./cj-apis-display.md#class-display)的ID号，默认为0，该参数应为大于或等于0的整数，非整数会报参数错误。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### CaptureOption(Int32)

```cangjie
public CaptureOption(
    public var displayId!: Int32 = 0
)
```

**功能：** 创建一个CaptureOption类型的对象。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|displayId|Int32|否|0| **命名参数。** 表示截取图像的显示设备Display的ID号，该参数应为大于或等于0的整数，非整数会报参数错误。|