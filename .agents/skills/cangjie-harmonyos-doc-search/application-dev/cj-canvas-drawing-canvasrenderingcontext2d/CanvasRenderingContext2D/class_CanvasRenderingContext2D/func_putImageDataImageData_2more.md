### func putImageData(ImageData, Length, Length)

```cangjie
public func putImageData(imageData: ImageData, dx: Length, dy: Length): Unit
```

**功能：** 使用[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)数据填充新的矩形区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|imageData|[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)|是|-| 包含像素值的ImageData对象。|
|dx|[Length](./cj-common-types.md#interface-length)|是|-|填充区域在x轴方向的偏移量。<br>默认单位：vp。|
|dy|[Length](./cj-common-types.md#interface-length)|是|-|填充区域在y轴方向的偏移量。<br>默认单位：vp。|

### func putImageData(ImageData, ?Length, ?Length, ?Length, ?Length, ?Length, ?Length)

```cangjie
public func putImageData(
    imageData: ImageData,
    dx: ?Length,
    dy: ?Length,
    dirtyX: ?Length,
    dirtyY: ?Length,
    dirtyWidth: ?Length,
    dirtyHeight: ?Length
): Unit
```

**功能：** 使用[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)数据填充新的矩形区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|imageData|[ImageData](./cj-canvas-drawing-imagedata.md#class-imagedata)|是|-| 包含像素值的ImageData对象。|
|dx|?[Length](./cj-common-types.md#interface-length)|是|-|填充区域在x轴方向的偏移量。<br>默认单位：vp。|
|dy|?[Length](./cj-common-types.md#interface-length)|是|-|填充区域在y轴方向的偏移量。<br>默认单位：vp。|
|dirtyX|?[Length](./cj-common-types.md#interface-length)|是|-|源图像数据矩形裁切范围左上角距离源图像左上角的x轴偏移量。<br>默认单位：vp。|
|dirtyY|?[Length](./cj-common-types.md#interface-length)|是|-|源图像数据矩形裁切范围左上角距离源图像左上角的y轴偏移量。<br>默认单位：vp。|
|dirtyWidth|?[Length](./cj-common-types.md#interface-length)|是|-|源图像数据矩形裁切范围的宽度。<br>默认单位：vp。|
|dirtyHeight|?[Length](./cj-common-types.md#interface-length)|是|-|源图像数据矩形裁切范围的高度。<br>默认单位：vp。|