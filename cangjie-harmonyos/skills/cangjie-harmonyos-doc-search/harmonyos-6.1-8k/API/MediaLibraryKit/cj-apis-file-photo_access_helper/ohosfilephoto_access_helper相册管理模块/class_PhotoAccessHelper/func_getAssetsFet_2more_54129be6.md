### func getAssets(FetchOptions)

```cangjie
public func getAssets(options: FetchOptions): PhotoAssetResult
```

**功能：** 获取图片和视频资源。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[FetchOptions](#class-fetchoptions)|是|-|图片和视频检索选项。|

**返回值：**

|类型|说明|
|:----|:----|
|PhotoAssetResult|返回图片和视频数据结果集。|

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
    let fetchResult: PhotoAssetResult = phAccessHelper.getAssets(fetchOptions)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getBurstAssets(String, FetchOptions)

```cangjie
public func getBurstAssets(burstKey: String, options: FetchOptions): PhotoAssetResult
```

**功能：** 获取连拍照片资源。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|burstKey|String|是|-|一组连拍照片的唯一标识：uuid(可传入[PhotoKeys](#enum-photokeys)的BURST_KEY)。字符串长度为36。|
|options|[FetchOptions](#class-fetchoptions)|是|-|连拍照片检索选项。|

**返回值：**

|类型|说明|
|:----|:----|
|PhotoAssetResult|返回获取连拍照片的结果集。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[文件管理错误码](../CoreFileKit/cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 14000011 | Internal system error. |

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
    let burstKey = "YOUR_UUID" // 请输入uuid
    let fetchResult: PhotoAssetResult = phAccessHelper.getBurstAssets(burstKey, fetchOptions)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```