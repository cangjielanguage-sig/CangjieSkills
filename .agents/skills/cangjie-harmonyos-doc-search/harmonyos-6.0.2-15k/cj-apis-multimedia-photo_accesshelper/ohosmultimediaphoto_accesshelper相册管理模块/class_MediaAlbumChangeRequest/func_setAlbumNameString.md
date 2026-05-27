### func setAlbumName(String)

```cangjie
public func setAlbumName(name: String): Unit
```

**功能：** 设置相册名称。

相册名的参数规格为

- 相册名字符串长度为1~255。
- 不允许出现非法字符，包括：. .. \ / : * ? " ' ` < > | { } [ ]
- 英文字符大小写不敏感。
- 相册名不允许重名。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|待设置的相册名称。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: Parameter verification failed.|
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
let fetchResult = phAccessHelper.getAlbums(AlbumType.USER, AlbumSubtype.USER_GENERIC,
    options: fetchOptions)
let album = fetchResult.getFirstObject()
let albumChangeRequest = MediaAlbumChangeRequest(album)
let newAlbumName = "newAAA"
albumChangeRequest.setAlbumName(newAlbumName)
```