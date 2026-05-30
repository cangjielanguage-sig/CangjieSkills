## class Album

```cangjie
public class Album {}
```

**功能：** 实体相册。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

### prop albumName

```cangjie
public mut prop albumName: String
```

**功能：** 获取相册名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### prop albumSubtype

```cangjie
public prop albumSubtype: AlbumSubtype
```

**功能：** 获取相册子类型。

**类型：** [AlbumSubtype](#enum-albumsubtype)

**读写能力：** 只读

**起始版本：** 19

### prop albumType

```cangjie
public prop albumType: AlbumType
```

**功能：** 获取相册类型。

**类型：** [AlbumType](#enum-albumtype)

**读写能力：** 只读

**起始版本：** 19

### prop albumUri

```cangjie
public prop albumUri: String
```

**功能：** 获取相册Uri。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop count

```cangjie
public prop count: Int32
```

**功能：** 相册中文件数量。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### prop coverUri

```cangjie
public prop coverUri: String
```

**功能：** 获取封面文件Uri。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop imageCount

```cangjie
public prop imageCount: Int32
```

**功能：** 获取相册中图片数量。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### prop videoCount

```cangjie
public prop videoCount: Int32
```

**功能：** 获取相册中图片数量。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### func commitModify()

```cangjie
public func commitModify(): Unit
```

**功能：** 更新相册属性修改到数据库中。

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

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
predicates.equalTo('album_name', Str('test1'))
let fetchOptions: FetchOptions = FetchOptions(fetchColumns: [], predicates: predicates)
let fetchResult: FetchResult<Album> = phAccessHelper.getAlbums(AlbumType.USER,
    AlbumSubtype.USER_GENERIC, options: fetchOptions)
let firstAlbum = fetchResult.getFirstObject()
firstAlbum.albumName = "test10086"
firstAlbum.commitModify()
```