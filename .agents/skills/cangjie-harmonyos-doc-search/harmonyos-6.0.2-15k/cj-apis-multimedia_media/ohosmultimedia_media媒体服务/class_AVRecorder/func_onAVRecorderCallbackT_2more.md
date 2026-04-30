### func on(AVRecorderCallbackType, Callback1Argument\<PhotoAsset>)

```cangjie
public func on(`type`: AVRecorderCallbackType, callback: Callback1Argument<photo_accesshelper.PhotoAsset>): Unit
```

**功能：** 订阅媒体资源回调事件，当[FileGenerationMode](#enum-filegenerationmode)枚举设置为系统创建媒体文件时，会在[stop()](#func-stop)操作结束后把[PhotoAsset](../MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#class-photoasset)对象回调给应用。

当用户重复订阅时，以最后一次订阅的回调接口为准。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVRecorderCallbackType](#enum-avrecordercallbacktype)|是|-|录像资源的回调类型。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[photo_accesshelper](../MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md).[PhotoAsset](../MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#class-photoasset)>|是|-|系统创建的资源文件对应的PhotoAsset对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400103|IO error.|
  |5400105|Service died.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import kit.MediaLibraryKit.*
import ohos.base.*

// 此处代码可添加在依赖项定义中
class PhotoAssetAvailableCallback <: Callback1Argument<PhotoAsset> {
    public static var invoked = false

    public func invoke(asset: PhotoAsset) {
        AppLog.info("the uri is ${asset.uri}")
        invoked = true
    }
}

let avRecorder = createAVRecorder()
avRecorder.on(AVRECORDER_PHOTO_ASSET_AVAILABLE, PhotoAssetAvailableCallback())
```

### func pause()

```cangjie
public func pause(): Unit
```

**功能：** 暂停视频录制。

需要[start()](#func-start)事件成功触发后，才能调用pause方法，可以通过调用[resume()](#func-resume)接口来恢复录制。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operate not permit.|
  |5400103|IO error.|
  |5400105|Service died.|

**示例：**

完整示例参考[prepare](#func-prepareavrecorderconfig)的示例代码。

```cangjie
// index.cj

import ohos.base.*
import kit.MediaKit.*

try {
    let avRecorder = createAVRecorder()
    // 执行prepare、start之后，执行pause
    avRecorder.pause()
    AppLog.info("pause success")
} catch (e: BusinessException) {
    AppLog.info("pause exception: ${e}")
}
```