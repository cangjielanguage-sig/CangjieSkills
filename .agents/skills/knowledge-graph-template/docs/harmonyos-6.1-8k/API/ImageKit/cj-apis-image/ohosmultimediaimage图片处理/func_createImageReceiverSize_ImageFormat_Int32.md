## func createImageReceiver(Size, ImageFormat, Int32)

```cangjie
public func createImageReceiver(size: Size, format: ImageFormat, capacity: Int32): ImageReceiver
```

**功能：** 通过图片大小、图片格式、容量创建ImageReceiver实例。

> **说明：**
>
> - ImageReceiver做为图片的接收方、消费者，它的参数属性实际上不会对接收到的图片产生影响。图片属性的配置应在发送方、生产者进行，如相机预览流[createPreviewOutput](../CameraKit/cj-apis-multimedia-camera.md#func-createpreviewoutputprofile-string)。
>
> - 由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](#func-release-2)方法及时释放内存。释放时应确保后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Size](#class-size)|是|-|图像的默认大小。该参数不会影响接收到的图片大小，实际返回大小由生产者决定，如相机。|
|format|[ImageFormat](#enum-imageformat)|是|-|图像格式，取值为[ImageFormat](#enum-imageformat)常量（目前仅支持 ImageFormat:Jpeg，实际返回格式由生产者决定，如相机）。|
|capacity|Int32|是|-|同时访问的最大图像数。该参数仅作为期望值，实际capacity由设备硬件决定。|

**返回值：**

|类型|说明|
|:----|:----|
|[ImageReceiver](#class-imagereceiver)|如果操作成功，则返回ImageReceiver实例。|

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980104 | Failed to initialize the internal object. |
  | 62980115 | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let size = Size(8, 8192)
    let receiver:ImageReceiver = createImageReceiver(size, ImageFormat.Jpeg, 8)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```