### func getAlbums(AlbumType, AlbumSubtype, FetchOptions)

```cangjie
public func getAlbums(albumType: AlbumType, subtype: AlbumSubtype,
    options!: FetchOptions = FetchOptions(["uri", "album_name"], DataSharePredicates())): AlbumResult
```

**功能：** 根据检索选项和相册类型获取相册。

在获取相册之前，确保相册已存在。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|albumType|[AlbumType](#enum-albumtype)|是|-|相册类型。|
|subtype|[AlbumSubtype](#enum-albumsubtype)|是|-|相册子类型。|
|options|[FetchOptions](#class-fetchoptions)|否|FetchOptions(["uri", "album_name"], DataSharePredicates())|**命名参数。** 检索选项，不填时默认根据相册类型检索。|

**返回值：**

|类型|说明|
|:----|:----|
|AlbumResult|返回获取相册的结果集。|

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
    let fetchOptions: FetchOptions = FetchOptions([], predicates)
    let fetchResult: AlbumResult = phAccessHelper.getAlbums(AlbumType.User,
        AlbumSubtype.UserGeneric, options: fetchOptions)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```