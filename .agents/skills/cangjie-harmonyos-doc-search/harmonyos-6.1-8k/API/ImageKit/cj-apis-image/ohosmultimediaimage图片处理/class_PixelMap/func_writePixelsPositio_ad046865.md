### func writePixels(PositionArea)

```cangjie
public func writePixels(area: PositionArea): Unit
```

**功能：** 固定按照BGRA_8888格式，读取[PositionArea](#class-positionarea).pixels缓冲区中的图像像素数据，并写入PixelMap指定区域内，该区域由[PositionArea](#class-positionarea).region指定。

可用公式计算PositionArea需要申请的内存大小。

YUV的区域计算公式：读取区域（region.size{width * height}）* 1.5 （1倍的Y分量+0.25倍U分量+0.25倍V分量）

RGBA的区域计算公式：读取区域（region.size{width * height}）* 4 （1倍的R分量+1倍G分量+1倍B分量+1倍A分量）

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|area|[PositionArea](#class-positionarea)|是|-|区域，根据区域写入。|

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980104 | Failed to initialize the internal object. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
    let sourceOptions: SourceOptions = SourceOptions(120)
    let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)  // 请替换为正确的图片源，参考本文使用说明。
    let pixelMap = imageSourceApi.createPixelMap()
    let area: PositionArea = PositionArea(
        Array<UInt8>(8, {i => UInt8(i)}),
        0,
        8,
        Region(Size(1, 2), 0, 0)
    )
    pixelMap.writePixels(area)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```