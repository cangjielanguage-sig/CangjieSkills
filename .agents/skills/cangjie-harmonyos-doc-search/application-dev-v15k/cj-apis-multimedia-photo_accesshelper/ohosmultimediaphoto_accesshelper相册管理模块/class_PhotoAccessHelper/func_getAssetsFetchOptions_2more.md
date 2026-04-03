### func getAssets(FetchOptions)

```cangjie
public func getAssets(options: FetchOptions): FetchResult<PhotoAsset>
```

**功能：** 获取图片和视频资源。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[FetchOptions](#class-fetchoptions)|是|-|图片和视频检索选项。|

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
let fetchOptions: FetchOptions = FetchOptions(fetchColumns: [], predicates: predicates)
let fetchResult: FetchResult<PhotoAsset> = phAccessHelper.getAssets(fetchOptions)
```

### func getBurstAssets(String, FetchOptions)

```cangjie
public func getBurstAssets(burstKey: String, options: FetchOptions): FetchResult<PhotoAsset>
```

**功能：** 获取连拍照片资源。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|burstKey|String|是|-|一组连拍照片的唯一标识：uuid(可传入[PhotoKeys](#enum-photokeys)的BURST_KEY)。|
|options|[FetchOptions](#class-fetchoptions)|是|-|连拍照片检索选项。|

**返回值：**

|类型|说明|
|:----|:----|
|[FetchResult](#class-fetchresult)\<[PhotoAsset](#class-photoasset)>|返回连拍照片数据结果集。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error.|
  |13900020|Invalid argument.|
  |14000011|Internal system error.|

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
let burstKey = "a042847b-2f1a-492a-897e-028b7d6dc475"
let fetchResult: FetchResult<PhotoAsset> = phAccessHelper.getBurstAssets(burstKey, fetchOptions)
```