## class MediaAssetManager

```cangjie
public class MediaAssetManager {}
```

**功能：** 根据不同的策略模式，请求图片资源。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

### static func cancelRequest(UIAbilityContext, String)

```cangjie
public static func cancelRequest(context: UIAbilityContext, requestId: String): Unit
```

**功能：** 取消尚未触发回调的资产内容请求。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-ability.md#class-uiabilitycontext) |是|-|传入Ability实例的Context。|
|requestId|String|是|-|需要取消的请求id。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error. Possible causes: Parameter verification failed.|
  |14000011|System inner fail.|

### static func loadMovingPhoto(UIAbilityContext, String, String)

```cangjie
public static func loadMovingPhoto(context: UIAbilityContext, imageFileUri: String, videoFileUri: String): MovingPhoto
```

**功能：** 加载应用沙箱的动态照片。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-ability.md#class-uiabilitycontext)|是|-|传入AbilityContext或者UIExtensionContext的实例。|
|imageFileUri|String|是|-|应用沙箱动态照片的图片uri。|
|videoFileUri|String|是|-|应用沙箱动态照片的视频uri。|

**返回值：**

|类型|说明|
|:----|:----|
|[MovingPhoto](#class-movingphoto)|返回[MovingPhoto](#class-movingphoto)实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: Parameter verification failed.|
  |14000011|Internal system error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaLibraryKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let phAccessHelper = getPhotoAccessHelper(ctx)
let imageFileUri = "file://com.example.myapplication/data/storage/el2/base/haps/entry/files/test.jpg"
let videoFileUri = "file://com.example.myapplication/data/storage/el2/base/haps/entry/files/test.mp4"
let photo = MediaAssetManager.loadMovingPhoto(ctx, imageFileUri, videoFileUri)
let srcUri = "file://com.example.myapplication/data/storage/el2/base/haps/entry/files/ImageFile2.jpg"
photo.requestContent(IMAGE_RESOURCE, srcUri)
photo.requestContent(IMAGE_RESOURCE)
```