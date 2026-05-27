### static func requestVideoFile(UIAbilityContext, PhotoAsset, RequestOptions, String, MediaAssetDataHandler\<Bool>)

```cangjie
public static func requestVideoFile(context: UIAbilityContext, asset: PhotoAsset, requestOptions: RequestOptions,
    fileUri: String, dataHandler: MediaAssetDataHandler<Bool>): String
```

**功能：** 根据不同的策略模式，请求视频资源数据到沙箱路径。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

- 对于本应用保存到媒体库的视频资源，应用无需额外申请'ohos.permission.READ_IMAGEVIDEO'权限即可访问。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-ability.md#class-uiabilitycontext)|是|-|传入Ability实例的Context。|
|asset|[PhotoAsset](#class-photoasset)|是|-|待请求的的媒体文件对象。|
|requestOptions|[RequestOptions](#class-requestoptions)|是|-|视频请求策略模式配置项。|
|fileUri|String|是|-|目标写入沙箱路径Uri。|
|dataHandler|[MediaAssetDataHandler](#class-mediaassetdatahandler)\<Bool>|是|-|媒体资源处理器，当所请求的视频资源写入完成时会触发回调。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回请求id，可用于[cancelRequest](#static-func-cancelrequestuiabilitycontext-string)取消请求。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error. Possible causes: Parameter verification failed.|
  |14000011|System inner fail.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaLibraryKit.*
import kit.ArkData.*
import kit.ImageKit.*
import ohos.base.*
import std.collection.HashMap

// 此处代码可添加在依赖项定义中
class MediaDataHandler <: MediaAssetDataHandler<Bool> {
    public func onDataPrepared(data: Bool, map: HashMap<String, String>): Unit {
        AppLog.info("on video request status prepared")
    }
}

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let phAccessHelper = getPhotoAccessHelper(ctx)
let predicates = DataSharePredicates()
let fetchOptions: FetchOptions = FetchOptions(fetchColumns: [], predicates: predicates)
let requestOptions = RequestOptions(HIGH_QUALITY_MODE)
let handler = MediaDataHandler()
let fileUri = "file://com.example.myapplication/data/storage/el2/base/haps/entry/files/VideoFile3.mp4"
let fetchResult = phAccessHelper.getAssets(fetchOptions)
let asset = fetchResult.getFirstObject()
let requestId = MediaAssetManager.requestVideoFile(ctx, asset, requestOptions,
    fileUri, handler)
MediaAssetManager.cancelRequest(ctx, requestId)
```