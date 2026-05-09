## class MediaAlbumChangeRequest

```cangjie
public class MediaAlbumChangeRequest <: MediaChangeRequest {
    public init(album: Album)
}
```

**功能：** 相册变更请求。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**父类型：**

- [MediaChangeRequest](#interface-mediachangerequest)

### init(Album)

```cangjie
public init(album: Album)
```

**功能：** 构造函数用于初始化新创建的对象。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|album|[Album](./cj-apis-file-photo_access_helper.md#class-album)|是|-|需要变更的相册。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](../CoreFileKit/cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 14000011 | System inner fail. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaLibraryKit.*
import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let phAccessHelper = getPhotoAccessHelper(ctx)
    let predicates = DataSharePredicates()
    let fetchOptions: FetchOptions = FetchOptions([], predicates)
    let fetchResult = phAccessHelper.getAlbums(AlbumType.User, AlbumSubtype.UserGeneric,
        options: fetchOptions)
    let album = fetchResult.getFirstObject()
    let albumChangeRequest = MediaAlbumChangeRequest(album)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func addAssets(Array\<PhotoAsset>)

```cangjie
public func addAssets(assets: Array<PhotoAsset>): Unit
```

**功能：** 向相册中添加资产。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|assets|Array\<[PhotoAsset](./cj-apis-file-photo_access_helper.md#class-photoasset)>|是|-|待添加到相册中的资产数组。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](../CoreFileKit/cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 14000011 | System inner fail. |
  | 14000016 | Operation Not Support. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaLibraryKit.*
import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let phAccessHelper = getPhotoAccessHelper(ctx)
    let predicates = DataSharePredicates()
    let fetchOptions: FetchOptions = FetchOptions([], predicates)
    let fetchResult = phAccessHelper.getAssets(fetchOptions)
    let asset = fetchResult.getFirstObject()
    let albumFetchResult = phAccessHelper.getAlbums(AlbumType.User, AlbumSubtype.UserGeneric)
    let album = albumFetchResult.getFirstObject()
    let albumChangeRequest = MediaAlbumChangeRequest(album)
    albumChangeRequest.addAssets([asset, asset])
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```