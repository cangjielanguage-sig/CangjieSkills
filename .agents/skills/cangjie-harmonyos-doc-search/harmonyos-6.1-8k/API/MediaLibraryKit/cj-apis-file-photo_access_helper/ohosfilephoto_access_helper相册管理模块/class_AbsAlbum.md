## class AbsAlbum

```cangjie
public open class AbsAlbum {}
```

**功能：** AbsAlbum模块。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### prop albumName

```cangjie
public mut prop albumName: String
```

**功能：** 相册名称。预置相册不可写，用户相册可写。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### prop albumSubtype

```cangjie
public prop albumSubtype: AlbumSubtype
```

**功能：** 相册子类型。

**类型：** [AlbumSubtype](#enum-albumsubtype)

**读写能力：** 只读

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### prop albumType

```cangjie
public prop albumType: AlbumType
```

**功能：** 相册类型。

**类型：** [AlbumType](#enum-albumtype)

**读写能力：** 只读

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### prop albumUri

```cangjie
public prop albumUri: String
```

**功能：** 相册uri。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### prop count

```cangjie
public prop count: Int32
```

**功能：** 相册中文件数量。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### prop coverUri

```cangjie
public prop coverUri: String
```

**功能：** 封面文件uri。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### func getAssets(FetchOptions)

```cangjie
public func getAssets(options: FetchOptions): PhotoAssetResult
```

**功能：** 获取相册中的文件。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[FetchOptions](./cj-apis-file-photo_access_helper.md#class-fetchoptions)|是|-| 检索选项。|

**返回值：**

|类型|说明|
|:----|:----|
|[PhotoAssetResult](#class-photoassetresult)|返回图片和视频数据结果集。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](../CoreFileKit/cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 13900020 | Invalid argument. |
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
    let albumFetchResult = phAccessHelper.getAlbums(AlbumType.User, AlbumSubtype.UserGeneric)
    let album = albumFetchResult.getFirstObject()
    let fetchResult = album.getAssets(fetchOptions)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```