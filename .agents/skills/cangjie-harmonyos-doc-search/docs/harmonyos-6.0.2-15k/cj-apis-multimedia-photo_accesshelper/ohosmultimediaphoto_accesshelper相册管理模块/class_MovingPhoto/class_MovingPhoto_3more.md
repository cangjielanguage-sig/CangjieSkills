## class MovingPhoto

```cangjie
public class MovingPhoto {}
```

**功能：** 动态照片对象。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

### func getUri()

```cangjie
public func getUri(): String
```

**功能：** 获取动态照片的uri。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|动态照片的uri。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.|
  |14000011|System inner fail.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaLibraryKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let imageFileUri = "file://com.example.xxx/data/storage/el2/base/haps/entry/files/test.jpg"
let videoFileUri = "file://com.example.xxx/data/storage/el2/base/haps/entry/files/test.mp4"
let photo = MediaAssetManager.loadMovingPhoto(ctx, imageFileUri, videoFileUri)
photo.getUri()
```

### func requestContent(String, String)

```cangjie
public func requestContent(imageFileUri: String, videoFileUri: String): Unit
```

**功能：** 请求指定资源类型的动态照片内容，以ArrayBuffer的形式返回。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

- 对于本应用保存到媒体库的动态照片资源，应用无需额外申请'ohos.permission.READ_IMAGEVIDEO'权限即可访问。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|imageFileUri|String|是|-|待写入动态照片图片内容的uri。|
|videoFileUri|String|是|-|待写入动态照片视频内容的uri。|

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

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let imageFileUri = "file://com.example.myapplication/data/storage/el2/base/haps/entry/files/test.jpg"
let videoFileUri = "file://com.example.myapplication/data/storage/el2/base/haps/entry/files/test.mp4"
let photo = MediaAssetManager.loadMovingPhoto(ctx, imageFileUri, videoFileUri)
let data = photo.requestContent(IMAGE_RESOURCE)
```