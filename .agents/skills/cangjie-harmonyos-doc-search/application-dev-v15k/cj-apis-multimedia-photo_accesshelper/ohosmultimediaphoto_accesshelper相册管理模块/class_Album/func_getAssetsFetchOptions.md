### func getAssets(FetchOptions)

```cangjie
public func getAssets(options: FetchOptions): FetchResult<PhotoAsset>
```

**功能：** 获取相册中的文件。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[FetchOptions](#class-fetchoptions)|是|-|检索选项。|

**返回值：**

|类型|说明|
|:----|:----|
|[FetchResult](#class-fetchresult)\<[PhotoAsset](#class-photoasset)>|返回图片和视频数据结果集。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
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
predicates.equalTo('album_name', Str('test1'))
let fetchOptions: FetchOptions = FetchOptions(fetchColumns: [], predicates: predicates)
let fetchResult: FetchResult<Album> = phAccessHelper.getAlbums(AlbumType.USER,
    AlbumSubtype.USER_GENERIC, options: fetchOptions)
let firstAlbum = fetchResult.getFirstObject()
let photoCount = firstAlbum.count
let predicates1 = DataSharePredicates()
let fetchOptions1: FetchOptions = FetchOptions(fetchColumns: [], predicates: predicates1)
let fetchResult1: FetchResult<PhotoAsset> = firstAlbum.getAssets(fetchOptions1)
```