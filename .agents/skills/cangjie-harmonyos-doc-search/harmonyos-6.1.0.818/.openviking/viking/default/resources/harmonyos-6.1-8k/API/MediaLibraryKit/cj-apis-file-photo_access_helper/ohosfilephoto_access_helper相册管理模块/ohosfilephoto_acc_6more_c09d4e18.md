# ohos.file.photo_access_helper（相册管理模块）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

photo_access_helper模块提供相册管理模块能力，包括创建相册以及访问、修改相册中的媒体数据信息等。

## 导入模块

```cangjie
import kit.MediaLibraryKit.*
```

## 权限列表

ohos.permission.READ_IMAGEVIDEO

ohos.permission.WRITE_IMAGEVIDEO

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。

## func getPhotoAccessHelper(UIAbilityContext)

```cangjie
public func getPhotoAccessHelper(context: UIAbilityContext): PhotoAccessHelper
```

**功能：** 获取相册管理模块的实例，用于访问和修改相册中的媒体文件。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiabilitycontext)|是|-|传入Ability实例的上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[PhotoAccessHelper](./cj-apis-file-photo_access_helper.md#class-photoaccesshelper)|相册管理模块的实例。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](../CoreFileKit/cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900020 | Invalid argument. |

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
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## interface MediaChangeRequest

```cangjie
public interface MediaChangeRequest {}
```

**功能：** 媒体变更请求，资产变更请求和相册变更请求的父类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22