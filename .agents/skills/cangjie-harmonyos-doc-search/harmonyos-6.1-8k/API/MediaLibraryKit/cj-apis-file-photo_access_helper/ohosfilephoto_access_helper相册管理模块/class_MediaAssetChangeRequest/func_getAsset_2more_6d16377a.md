### func getAsset()

```cangjie
public func getAsset(): PhotoAsset
```

**功能：** 获取当前资产变更请求中的资产。

**注意**：对于创建资产的变更请求，在调用[applyChanges](#func-applychangesmediachangerequest)提交生效之前，该接口返回异常。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[PhotoAsset](./cj-apis-file-photo_access_helper.md#class-photoasset)|返回当前资产变更请求中的资产。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](../CoreFileKit/cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
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
    let fetchResult = phAccessHelper.getAssets(fetchOptions)
    let photoAsset = fetchResult.getFirstObject()
    let assetChangeRequest = MediaAssetChangeRequest(photoAsset)
    let asset = assetChangeRequest.getAsset()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getWriteCacheHandler()

```cangjie
public func getWriteCacheHandler(): Int32
```

**功能：** 获取临时文件写句柄。

**注意**：对于同一个资产变更请求，不支持在成功获取临时文件写句柄后，重复调用该接口。

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回临时文件写句柄。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[文件管理错误码](../CoreFileKit/cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 14000011 | System inner fail. |
  | 14000016 | Operation Not Support. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*
import kit.MediaLibraryKit.*
import kit.CoreFileKit.*
import kit.ImageKit.{createImageSource, PixelMap}
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

func getPixelMap(): PixelMap {
    try {
        // Global 的实现请参见本文"使用说明"小节
        let ctx = Global.abilityContext
        let phAccessHelper = getPhotoAccessHelper(ctx)
        let assetChangeRequest = MediaAssetChangeRequest.createAssetRequest(ctx,
            PhotoType.Image, "jpg")
        // 获取临时文件写句柄，后续可以通过该句柄写入数据
        let fd = assetChangeRequest.getWriteCacheHandler()
        // write data into fd..
        FileIo.write(fd, Array<UInt8>(96, repeat: 0))
        let imageSource = createImageSource(fd)
        let pixelMap = imageSource.createPixelMap()
        FileIo.close(fd)
        phAccessHelper.applyChanges(assetChangeRequest)
        return pixelMap
    } catch (e: BusinessException) {
        Hilog.info(0, "test", "${e.message}")
        throw e
    }
}

@Entry
@Component
class EntryView {

    func build() {
        Row {
            Column {
                Image(getPixelMap())
            }.width(100.percent)
        }.height(100.percent)
    }
}
```