### func getAlbum()

```cangjie
public func getAlbum(): ?Album
```

**功能：** 获取当前相册变更请求中的相册。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|?[Album](#class-album)|返回当前相册变更请求中的相册。|

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
let fetchResult = phAccessHelper.getAlbums(AlbumType.USER, AlbumSubtype.USER_GENERIC, options: fetchOptions)
let album = fetchResult.getFirstObject()
let albumChangeRequest = MediaAlbumChangeRequest(album)
var changeRequestAlbum = albumChangeRequest.getAlbum()
```

### func removeAssets(Array\<PhotoAsset>)

```cangjie
public func removeAssets(assets: Array<PhotoAsset>): Unit
```

**功能：** 从相册中移除资产。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|assets|Array\<[PhotoAsset](#class-photoasset)>|是|-|待从相册中移除的资产数组。|

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
import kit.ArkData.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let phAccessHelper = getPhotoAccessHelper(ctx)
let predicates = DataSharePredicates()
let fetchOptions: FetchOptions = FetchOptions(fetchColumns: [], predicates: predicates)
let albumFetchResult = phAccessHelper.getAlbums(AlbumType.USER, AlbumSubtype.USER_GENERIC)
let album = albumFetchResult.getFirstObject()
let fetchResult = album.getAssets(fetchOptions)
let asset = fetchResult.getFirstObject()
let albumChangeRequest = MediaAlbumChangeRequest(album)
albumChangeRequest.removeAssets([asset])
phAccessHelper.applyChanges(albumChangeRequest)
```