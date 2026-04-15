## class PhotoAsset

```cangjie
public class PhotoAsset {}
```

**功能：** 提供封装文件属性的方法。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### prop displayName

```cangjie
public prop displayName: String
```

**功能：** 显示文件名，包含后缀名。字符串长度为1~255。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### prop photoType

```cangjie
public prop photoType: PhotoType
```

**功能：** 媒体文件类型。

**类型：** [PhotoType](#enum-phototype)

**读写能力：** 只读

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### prop uri

```cangjie
public prop uri: String
```

**功能：** 媒体文件资源uri（如：file://media/Photo/1/IMG_datetime_0001/displayName.jpg）。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### func commitModify()

```cangjie
public func commitModify(): Unit
```

**功能：** 修改文件的元数据。

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[文件管理错误码](../CoreFileKit/cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 13900020 | Invalid argument. |
  | 14000001 | Invalid display name. |
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
    let fetchColumns = [PhotoKeys.Title.toString()]
    let fetchOptions: FetchOptions = FetchOptions(fetchColumns, predicates)
    let fetchResult = phAccessHelper.getAssets(fetchOptions)
    let firstPhotoAsset = fetchResult.getFirstObject()
    let photoAssetTitle = firstPhotoAsset.get('title')
    let newTitle = "NEW_TITLE" // 新标题，实际使用按需取名
    firstPhotoAsset.set('title', newTitle)
    firstPhotoAsset.commitModify()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```