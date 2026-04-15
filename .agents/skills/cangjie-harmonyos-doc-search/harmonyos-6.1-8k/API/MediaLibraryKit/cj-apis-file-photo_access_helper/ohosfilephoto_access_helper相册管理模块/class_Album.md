## class Album

```cangjie
public class Album <: AbsAlbum {}
```

**功能：** 实体相册。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**父类型：**

- [AbsAlbum](#class-absalbum)

### prop imageCount

```cangjie
public prop imageCount: Int32
```

**功能：** 相册中图片数量。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### prop videoCount

```cangjie
public prop videoCount: Int32
```

**功能：** 相册中视频数量。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### func commitModify()

```cangjie
public func commitModify(): Unit
```

**功能：** 更新相册属性修改到数据库中。

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[文件管理错误码](../CoreFileKit/cj-errorcode-filemanagement.md)。

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
    predicates.equalTo('album_name', StringValue('test1'))
    let fetchOptions: FetchOptions = FetchOptions([], predicates)
    let fetchResult = phAccessHelper.getAlbums(AlbumType.User,
        AlbumSubtype.UserGeneric, options: fetchOptions)
    let firstAlbum = fetchResult.getFirstObject()
    firstAlbum.albumName = "test10086"
    firstAlbum.commitModify()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```