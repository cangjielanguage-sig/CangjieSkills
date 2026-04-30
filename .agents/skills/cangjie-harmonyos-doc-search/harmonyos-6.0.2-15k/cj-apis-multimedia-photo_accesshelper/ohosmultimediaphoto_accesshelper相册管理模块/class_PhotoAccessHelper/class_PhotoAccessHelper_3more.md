## class PhotoAccessHelper

```cangjie
public class PhotoAccessHelper {}
```

**功能：** 获取图片和视频资源。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

### func applyChanges(MediaChangeRequest)

```cangjie
public func applyChanges(mediaChangeRequest: MediaChangeRequest): Unit
```

**功能：** 提交媒体变更请求。

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mediaChangeRequest|[MediaChangeRequest](#interface-mediachangerequest)|是|-|媒体变更请求，支持资产变更请求和相册变更请求。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error. Possible causes: Parameter verification failed.|
  |14000011|System inner fail.|

### func getAlbums(AlbumType, AlbumSubtype, FetchOptions)

```cangjie
public func getAlbums(`type`: AlbumType, subtype: AlbumSubtype,
    options!: FetchOptions = FetchOptions()): FetchResult<Album>
```

**功能：** 根据检索选项和相册类型获取相册。获取相册前需先保证相册存在。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AlbumType](#enum-albumtype)|是|-|相册类型。|
|subtype|[AlbumSubtype](#enum-albumsubtype)|是|-|相册子类型。|
|options|[FetchOptions](#class-fetchoptions)|否|FetchOptions()| **命名参数。** 检索选项。|

**返回值：**

|类型|说明|
|:----|:----|
|[FetchResult](#class-fetchresult)\<[Album](#class-album)>|返回获取相册的结果集。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |13900012|Permission denied.|
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
predicates
    .equalTo('album_name', Str('test1'))
    .and()
    .equalTo('count', Integer(2))
let fetchOptions: FetchOptions = FetchOptions(fetchColumns: [], predicates: predicates)
let fetchResult: FetchResult<Album> = phAccessHelper.getAlbums(AlbumType.USER,
    AlbumSubtype.USER_GENERIC, options: fetchOptions)
```