### func setPixelMap(?PixelMap)

```cangjie
public func setPixelMap(value: ?PixelMap): Unit
```

**功能：** 将PixelMap设置到当前上下文。绘制内容将同步到PixelMap。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|是|-|PixelMap对象。|

### func getLineDash()

```cangjie
public func getLineDash(): Array<Float64>
```

**功能：** 获得当前画布的虚线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:---|:---|
|Array\<Float64>|返回数组，该数组用来描述线段如何交替和间距长度。<br>默认单位：vp。|

### func toDataURL(?String, ?Float64)

```cangjie
public func toDataURL(imageType!: ?String = None, quality!: ?Float64 = None): String
```

**功能：** 生成一个包含图片展示的URL，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|imageType|?String|否|None|**命名参数。** 用于指定图像格式。|
|quality|?Float64|否|None|**命名参数。** 在指定图片格式为image/jpeg或image/webp的情况下，可以从0到1的区间内选择图片的质量。如果超出取值范围，将会使用默认值0.92。|

**返回值：**

|类型|说明|
|:---|:---|
|String|图像的URL地址。|

### func createImageData(?Float64, ?Float64)

```cangjie
public func createImageData(sw: ?Float64, sh: ?Float64): ImageData
```

**功能：** 创建新的、空白的、指定大小的ImageData 对象，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sw|?Float64|是|-|ImageData的宽度。<br>默认单位：vp。|
|sh|?Float64|是|-|ImageData的高度。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:---|:---|
|ImageData|ImageData对象。|

### func createImageData(?ImageData)

```cangjie
public func createImageData(imageData: ?ImageData): ImageData
```

**功能：** 根据一个现有的ImageData对象重新创建一个宽、高相同的ImageData对象（不会复制图像数据），请参考[ImageData](./cj-canvas-drawing-imagedata.md)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。createImageData示例同[putImageData](#func-putimagedataimagedata-length-length)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|imageData|?ImageData|是|-|现有的ImageData对象。|

**返回值：**

|类型|说明|
|:---|:---|
|ImageData|新的ImageData对象。|

### func getImageData(?Float64, ?Float64, ?Float64, ?Float64)

```cangjie
public func getImageData(sx: ?Float64, sy: ?Float64, sw: ?Float64, sh: ?Float64): ImageData
```

**功能：** 以当前canvas指定区域内的像素创建ImageData对象，该接口存在内存拷贝行为，高耗时，应避免频繁使用。
**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sx|?Float64|是|-|需要输出的区域的左上角x坐标。<br> 默认单位：vp。|
|sy|?Float64|是|-|需要输出的区域的左上角y坐标。<br> 默认单位：vp。|
|sw|?Float64|是|-|需要输出的区域的宽度。<br> 默认单位：vp。|
|sh|?Float64|是|-|需要输出的区域的高度。<br> 默认单位：vp。|

**返回值：**

|类型|说明|
|:---|:---|
|ImageData|新的ImageData对象。|