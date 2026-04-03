### func release()

```cangjie
public func release(): Unit
```

**功能：** 释放PhotoAccessHelper实例。当后续不需要使用PhotoAccessHelper 实例中的方法时调用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |13900020|Invalid argument.|
  |14000011|System inner fail.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaLibraryKit.*
import kit.ArkData.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let phAccessHelper = getPhotoAccessHelper(ctx)
let predicates = DataSharePredicates()
let fetchOptions: FetchOptions = FetchOptions(fetchColumns: [], predicates: predicates)
let fetchResult: FetchResult<PhotoAsset> = phAccessHelper.getAssets(fetchOptions)
fetchResult.close()
phAccessHelper.release()
```

### func showAssetsCreationDialog(Array\<String>, Array\<PhotoCreationConfig>, Callback1Argument\<Array\<String>>)

```cangjie
public func showAssetsCreationDialog(srcFileUris: Array<String>, photoCreationConfigs: Array<PhotoCreationConfig>,
    callback: Callback1Argument<Array<String>>): Unit
```

**功能：** 调用接口拉起保存确认弹窗。用户同意保存后，在callback中返回已创建并授予保存权限的uri列表，该列表永久生效，应用可使用该uri写入图片/视频。如果用户拒绝保存，将返回空列表。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|srcFileUris|Array\<String>|是|-|需保存到媒体库中的图片/视频文件对应的[媒体库uri](../../../../Dev_Guide/file-management/cj-user-file-uri-intro.md#媒体文件uri)。<br>**注意：**  仅支持处理图片、视频uri。|
|photoCreationConfigs|Array\<[PhotoCreationConfig](#struct-photocreationconfig)>|是|-|保存图片/视频到媒体库的配置，包括保存的文件名等，与srcFileUris保持一一对应。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Array\<String>>|是|-|回调函数，获取返回给应用的媒体库文件uri列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |13900020|Invalid argument.|
  |14000011|System inner fail.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaLibraryKit.*
import kit.ArkData.*
import ohos.base.*

// 此处代码可添加在依赖项定义中
class MyCallback<T> <: Callback1Argument<T> {
    public let callabck_: (T) -> Unit
    public init(callabck: (T) -> Unit) {
        callabck_ = callabck
    }
    public open func invoke(arg: T): Unit {
        callabck_(arg)
    }
}

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let phAccessHelper = getPhotoAccessHelper(ctx)
let callback3 = MyCallback<Array<String>>(
    {
        arg: Array<String> =>
        AppLog.info("oncallback3: Array.size: ${arg.size}")
        for (str in arg) {
            AppLog.info("oncallback3: uri: ${str}")
        }
    }
)
// 获取需要保存到媒体库的位于应用沙箱的图片/视频uri
// 实际场景请使用真实的uri
let srcFileUris: Array<String> = ["file://media/Photo/37/IMG_1731463495_028/IMG_20241113_100315.jpg"]
let photoCreationConfigs: Array<PhotoCreationConfig> = [
    PhotoCreationConfig(
        'jpg',
        PhotoType.IMAGE,
        title: "test4",
        subtype: PhotoSubtype.DEFAULT
    )
]
phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs, callback3)
```