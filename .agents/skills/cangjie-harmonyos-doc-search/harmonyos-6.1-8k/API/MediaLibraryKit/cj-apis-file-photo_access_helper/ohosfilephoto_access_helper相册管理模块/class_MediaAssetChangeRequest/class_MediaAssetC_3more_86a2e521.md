## class MediaAssetChangeRequest

```cangjie
public class MediaAssetChangeRequest <: MediaChangeRequest {
    public init(asset: PhotoAsset)
}
```

**功能：** 资产变更请求。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**父类型：**

- [MediaChangeRequest](#interface-mediachangerequest)

### init(PhotoAsset)

```cangjie
public init(asset: PhotoAsset)
```

**功能：** 构造函数，用于初始化资产变更请求。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|asset|[PhotoAsset](./cj-apis-file-photo_access_helper.md#class-photoasset)|是|-|需要变更的资产。|

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
    let fetchOptions = FetchOptions([], predicates)
    let fetchResult = phAccessHelper.getAssets(fetchOptions)
    let photoAsset = fetchResult.getFirstObject()
    let assetChangeRequest = MediaAssetChangeRequest(photoAsset)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func createAssetRequest(UIAbilityContext, PhotoType, String, CreateOptions)

```cangjie
public static func createAssetRequest(context: UIAbilityContext, photoType: PhotoType, extension: String,
    options!: CreateOptions = CreateOptions(title: "", subtype: Default)): MediaAssetChangeRequest
```

**功能：** 指定文件类型和扩展名，创建资产变更请求。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiabilitycontext)|是|-|传入Ability实例的上下文。|
|photoType|[PhotoType](./cj-apis-file-photo_access_helper.md#enum-phototype)|是|-|待创建的文件类型，IMAGE或者VIDEO类型。|
|extension|String|是|-|文件扩展名，例如：'jpg'。|
|options|[CreateOptions](#class-createoptions)|否|CreateOptions(title: "", subtype: Default)|**命名参数。** 创建选项，例如：{title: 'testPhoto'}。<br>文件名中不允许出现非法英文字符，包括： . .. \ / : * ? " ' ` < > \| { } [ ]|

**返回值：**

|类型|说明|
|:----|:----|
|[MediaAssetChangeRequest](#class-mediaassetchangerequest)|返回创建资产的变更请求。|

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
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let photoType = PhotoType.Image
    let extension = "jpg"
    let options = CreateOptions(title: "testPhoto")
    let assetChangeRequest = MediaAssetChangeRequest.createAssetRequest(ctx, photoType,
        extension, options: options)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```