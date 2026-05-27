### func getThumbnail(?Size)

```cangjie
public func getThumbnail(size!: ?Size = None): PixelMap
```

**功能：** 获取文件的缩略图，传入缩略图尺寸。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|?[Size](../ImageKit/cj-apis-image.md#struct-size)|否|None| **命名参数。** 缩略图尺寸。|

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|返回缩略图的PixelMap。|

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
import ohos.base.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let phAccessHelper = getPhotoAccessHelper(ctx)
let predicates = DataSharePredicates()
let fetchColumns = [PhotoKeys.TITLE.toString()]
let fetchOptions: FetchOptions = FetchOptions(fetchColumns: fetchColumns, predicates: predicates)
let fetchResult: FetchResult<PhotoAsset> = phAccessHelper.getAssets(fetchOptions)
let firstPhotoAsset = fetchResult.getFirstObject()
let pixm = firstPhotoAsset.getThumbnail()
```

### func set(String, String)

```cangjie
public func set(member: String, data: String): Unit
```

**功能：** 设置PhotoAsset成员参数。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|member|String|是|-|成员参数名称例如：[PhotoKeys](#enum-photokeys).TITLE。|
|data|String|是|-|设置成员参数名称，只能修改[PhotoKeys](#enum-photokeys).TITLE的值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |13900020|Invalid argument.|
  |14000014|Member is not a valid PhotoKey.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaLibraryKit.*
import kit.ArkData.*
import ohos.base.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let phAccessHelper = getPhotoAccessHelper(ctx)
let predicates = DataSharePredicates()
let fetchColumns = [PhotoKeys
    .TITLE
    .toString()]
let fetchOptions: FetchOptions = FetchOptions(fetchColumns: fetchColumns, predicates: predicates
)
let fetchResult: FetchResult<PhotoAsset> = phAccessHelper.getAssets(fetchOptions)
let firstPhotoAsset = fetchResult.getFirstObject()
let photoAssetTitle = firstPhotoAsset
    .get('title')
    .getString()
let newTitle = "123456789"
firstPhotoAsset.set('title', newTitle)
```