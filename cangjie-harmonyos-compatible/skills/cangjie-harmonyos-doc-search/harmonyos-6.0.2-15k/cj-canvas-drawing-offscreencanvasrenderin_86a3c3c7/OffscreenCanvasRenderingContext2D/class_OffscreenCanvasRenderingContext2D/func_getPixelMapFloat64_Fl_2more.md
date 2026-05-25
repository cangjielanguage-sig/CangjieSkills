### func getPixelMap(Float64, Float64, Float64, Float64)

```cangjie
public func getPixelMap(left: Float64, top: Float64, width: Float64, height: Float64): PixelMap
```

**功能：** 以当前canvas指定区域内的像素创建[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)对象，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|left|Float64|是|-|需要输出的区域的左上角x坐标。<br>默认单位：vp。|
|top |Float64|是|-|需要输出的区域的左上角y坐标。<br>默认单位：vp。|
|width |Float64|是|-|需要输出的区域的宽度。<br>默认单位：vp。|
|height|Float64|是|-|需要输出的区域的高度。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap) |新的PixelMap对象。|

### func getPixelMap(Int64, Int64, Int64, Int64)

```cangjie
public func getPixelMap(left: Int64, top: Int64, width: Int64, height: Int64): PixelMap
```

**功能：** 以当前canvas指定区域内的像素创建[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)对象，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|left|Int64|是|-|需要输出的区域的左上角x坐标。<br>默认单位：vp。|
|top |Int64|是|-|需要输出的区域的左上角y坐标。<br>默认单位：vp。|
|width |Int64|是|-|需要输出的区域的宽度。<br>默认单位：vp。|
|height|Int64|是|-|需要输出的区域的高度。<br>默认单位：vp。|

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap) |新的PixelMap对象。|