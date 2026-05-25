### func getObjectByPosition(Int32)

```cangjie
public func getObjectByPosition(index: Int32): PhotoAsset
```

**功能：** 获取文件检索结果中具有指定索引的文件资产。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|要获取的文件的索引，从0开始。|

**返回值：**

|类型|说明|
|:----|:----|
|[PhotoAsset](#class-photoasset)|返回结果集中指定索引的一个对象。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](../CoreFileKit/cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
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
    let photoAsset = fetchResult.getObjectByPosition(0)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```