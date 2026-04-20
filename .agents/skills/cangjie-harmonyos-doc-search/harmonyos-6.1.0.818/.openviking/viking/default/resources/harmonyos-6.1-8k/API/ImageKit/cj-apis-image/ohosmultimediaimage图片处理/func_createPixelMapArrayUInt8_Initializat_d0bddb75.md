## func createPixelMap(Array\<UInt8>, InitializationOptions)

```cangjie
public func createPixelMap(colors: Array<UInt8>, options: InitializationOptions): PixelMap
```

**功能：** 通过属性创建PixelMap，默认采用Bgra8888格式处理数据。

> **说明：**
>
> 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](#func-release-4)方法及时释放内存。释放时应确保后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|colors|Array\<UInt8>|是|-|图像像素数据的缓冲区，用于初始化PixelMap的像素。初始化前，缓冲区中的像素格式需要由[InitializationOptions](#class-initializationoptions).srcPixelFormat指定。<br>**说明：** 图像像素数据的缓冲区长度：length = width * height * 单位像素字节数。|
|options|[InitializationOptions](#class-initializationoptions)|是|-|创建像素的属性，包括透明度，尺寸，缩略值，像素格式和是否可编辑。|

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](#class-pixelmap)|返回PixelMap。<br>当创建的pixelMap大小超过原图大小时，返回原图pixelMap大小。|

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980104 | Failed to initialize the internal object. |
  | 62980115 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkUI.Row
import kit.ArkUI.Column
import kit.ArkUI.loadNativeView
import kit.ArkUI.CustomView
import kit.ArkUI.CJEntry
import kit.ArkUI.Image
import kit.ArkUI.LengthProp
import kit.ArkUI.SubscriberManager
import kit.ArkUI.LocalStorage
import ohos.arkui.state_macro_manage.*
import kit.ImageKit.{InitializationOptions, createPixelMap, Size, PixelMap}
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

func getPixelMap(): PixelMap {
    try {
        // 96 为需要创建的像素 buffer 大小，取值为：height * width * 4
        let color: Array<UInt8> = Array<UInt8>(96, repeat: 0)
        let opts: InitializationOptions = InitializationOptions(Size(4, 6))
        // 通过属性创建的PixelMap实例，后续可以调用该实例的方法读取或写入图像数据
        let pixelMap = createPixelMap(color, opts)
        return pixelMap
    } catch (e: BusinessException) {
        Hilog.info(0, "test", "${e.message}")
        throw e
    }
}

@Entry
@Component
class EntryView {

    func build() {
        Row {
            Column {
                Image(getPixelMap())
            }.width(100.percent)
        }.height(100.percent)
    }
}
```