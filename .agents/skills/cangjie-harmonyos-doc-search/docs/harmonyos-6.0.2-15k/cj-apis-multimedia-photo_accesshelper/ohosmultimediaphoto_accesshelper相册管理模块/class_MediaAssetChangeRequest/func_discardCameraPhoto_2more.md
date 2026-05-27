### func discardCameraPhoto()

```cangjie
public func discardCameraPhoto(): Unit
```

**功能：** 保存相机拍摄的照片。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |14000011|System inner fail.|
  |14000016|Operation Not Support.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaLibraryKit.*
import kit.ArkData.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let phAccessHelper = getPhotoAccessHelper(ctx)
let predicates = DataSharePredicates()
let fetchOptions = FetchOptions(fetchColumns: [], predicates: predicates)
let fetchResult = phAccessHelper.getAssets(fetchOptions)
let photoAsset = fetchResult.getFirstObject()
let assetChangeRequest = MediaAssetChangeRequest(photoAsset)
assetChangeRequest.discardCameraPhoto()
phAccessHelper.applyChanges(assetChangeRequest)
```

### func getAsset()

```cangjie
public func getAsset(): ?PhotoAsset
```

**功能：** 获取当前资产变更请求中的资产。

**注意：** 对于创建资产的变更请求，在调用[applyChanges](#func-applychangesmediachangerequest)提交生效之前，该接口返回None。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|?[PhotoAsset](#class-photoasset)|返回当前资产变更请求中的资产。|

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
import kit.ArkData.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let phAccessHelper = getPhotoAccessHelper(ctx)
let predicates = DataSharePredicates()
let fetchOptions: FetchOptions = FetchOptions(fetchColumns: [], predicates: predicates)
let fetchResult = phAccessHelper.getAssets(fetchOptions)
let photoAsset = fetchResult.getFirstObject()
let assetChangeRequest = MediaAssetChangeRequest(photoAsset)
let asset = assetChangeRequest.getAsset()
```