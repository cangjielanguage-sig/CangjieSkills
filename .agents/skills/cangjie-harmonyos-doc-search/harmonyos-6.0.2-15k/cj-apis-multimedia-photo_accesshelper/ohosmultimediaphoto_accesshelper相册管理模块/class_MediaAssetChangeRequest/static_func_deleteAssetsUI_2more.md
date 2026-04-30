### static func deleteAssets(UIAbilityContext, Array\<PhotoAsset>)

```cangjie
public static func deleteAssets(context: UIAbilityContext, assets: Array<PhotoAsset>): Unit
```

**功能：** 删除媒体文件，删除的文件进入到回收站。

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-ability.md#class-uiabilitycontext)|是|-|传入Ability实例的Context。|
|assets|Array\<[PhotoAsset](#class-photoasset)>|是|-|待删除的媒体文件数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error. Possible causes: Parameter verification failed.|
  |14000002|Invalid asset uri.|
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
let asset = fetchResult.getFirstObject()
MediaAssetChangeRequest.deleteAssets(ctx, asset.uri)
```

### static func deleteAssets(UIAbilityContext, Array\<String>)

```cangjie
public static func deleteAssets(context: UIAbilityContext, assets: Array<String>): Unit
```

**功能：** 删除媒体文件，删除的文件进入到回收站。

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-ability.md#class-uiabilitycontext)|是|-|传入Ability实例的Context。|
|assets|Array\<String>|是|-|待删除的媒体文件uri数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error. Possible causes: Parameter verification failed.|
  |14000002|Invalid asset uri.|
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
let asset = fetchResult.getFirstObject()
MediaAssetChangeRequest.deleteAssets(ctx, asset.uri)
```