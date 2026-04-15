### func addResource(ResourceType, Array\<Byte>)

```cangjie
public func addResource(resourceType: ResourceType, data: Array<Byte>): Unit
```

**功能：** 通过ArrayBuffer数据添加资源。

**注意**：对于同一个资产变更请求，成功添加资源后不支持重复调用该接口。对于动态照片，可调用两次该接口分别添加图片和视频资源。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resourceType|[ResourceType](#enum-resourcetype)|是|-|待添加资源的类型。|
|data|Array\<Byte>|是|-|待添加资源的数据。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[文件管理错误码](../CoreFileKit/cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 14000011 | System inner fail. |
  | 14000016 | Operation Not Support. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaLibraryKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let phAccessHelper = getPhotoAccessHelper(ctx)
    let photoType = PhotoType.Image
    let extension = "jpg"
    let assetChangeRequest = MediaAssetChangeRequest.createAssetRequest(ctx, photoType,
        extension)
    let buffer = Array<Byte>(2048, repeat: 0)
    assetChangeRequest.addResource(ResourceType.ImageResource, buffer)
    phAccessHelper.applyChanges(assetChangeRequest)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func discardCameraPhoto()

```cangjie
public func discardCameraPhoto(): Unit
```

**功能：** 删除相机拍摄的照片。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](../CoreFileKit/cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 14000011 | Internal system error. |
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
    let fetchOptions = FetchOptions([], predicates)
    let fetchResult = phAccessHelper.getAssets(fetchOptions)
    let photoAsset = fetchResult.getFirstObject()
    let assetChangeRequest = MediaAssetChangeRequest(photoAsset)
    assetChangeRequest.discardCameraPhoto()
    phAccessHelper.applyChanges(assetChangeRequest)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```