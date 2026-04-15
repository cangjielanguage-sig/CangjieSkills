## class PhotoAccessHelper

```cangjie
public class PhotoAccessHelper {}
```

**功能：** 获取图片和视频资源。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### func applyChanges(MediaChangeRequest)

```cangjie
public func applyChanges(mediaChangeRequest: MediaChangeRequest): Unit
```

**功能：** 提交媒体变更请求。

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mediaChangeRequest|[MediaChangeRequest](#interface-mediachangerequest)|是|-|媒体变更请求，支持资产变更请求和相册变更请求。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[文件管理错误码](../CoreFileKit/cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
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
    let fetchOptions = FetchOptions([], predicates)
    let fetchResult = phAccessHelper.getAssets(fetchOptions)
    let photoAsset = fetchResult.getFirstObject()
    let assetChangeRequest = MediaAssetChangeRequest(photoAsset)
    assetChangeRequest.setTitle("newTitle")
    phAccessHelper.applyChanges(assetChangeRequest)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```