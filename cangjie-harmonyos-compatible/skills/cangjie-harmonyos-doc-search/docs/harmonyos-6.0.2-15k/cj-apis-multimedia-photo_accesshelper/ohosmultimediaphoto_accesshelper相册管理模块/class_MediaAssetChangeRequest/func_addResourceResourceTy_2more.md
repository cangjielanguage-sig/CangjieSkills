### func addResource(ResourceType, String)

```cangjie
public func addResource(resourceType: ResourceType, fileUri: String): Unit
```

**功能：** 通过ArrayBuffer数据添加资源。

**注意：** 对于同一个资产变更请求，不支持在成功添加资源后，重复调用该接口。对于动态照片，可调用两次该接口分别添加图片和视频资源。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resourceType|[ResourceType](#enum-resourcetype)|是|-|待添加资源的类型。|
|fileUri|String|是|-|待添加资源的数据来源，在应用沙箱下的uri。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: Parameter verification failed.|
  |14000011|System inner fail.|
  |14000016|Operation Not Support.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaLibraryKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let phAccessHelper = getPhotoAccessHelper(ctx)
let photoType = PhotoType.IMAGE
let extension = "jpg"
let assetChangeRequest = MediaAssetChangeRequest.createAssetRequest(ctx, photoType,
    extension)
let buffer = Array<Byte>(2048, repeat: 0)
assetChangeRequest.addResource(IMAGE_RESOURCE, buffer)
phAccessHelper.applyChanges(assetChangeRequest)
```

### func addResource(ResourceType, Array\<Byte>)

```cangjie
public func addResource(resourceType: ResourceType, data: Array<Byte>): Unit
```

**功能：** 通过ArrayBuffer数据添加资源。

**注意：** 对于同一个资产变更请求，不支持在成功添加资源后，重复调用该接口。对于动态照片，可调用两次该接口分别添加图片和视频资源。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resourceType|[ResourceType](#enum-resourcetype)|是|-|待添加资源的类型。|
|data|Array\<Byte>|是|-|待添加资源的数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: Parameter verification failed.|
  |14000011|System inner fail.|
  |14000016|Operation Not Support.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaLibraryKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let phAccessHelper = getPhotoAccessHelper(ctx)
let photoType = PhotoType.IMAGE
let extension = "jpg"
let assetChangeRequest = MediaAssetChangeRequest.createAssetRequest(ctx, photoType,
    extension)
let buffer = Array<Byte>(2048, repeat: 0)
assetChangeRequest.addResource(IMAGE_RESOURCE, buffer)
phAccessHelper.applyChanges(assetChangeRequest)
```