## class PhotoViewPicker

```cangjie
public class PhotoViewPicker {
    public init(gcontext: UIAbilityContext)
}
```

**功能：** 图库选择器对象，用来支撑选择图片/视频等用户场景。在使用前，需要先创建PhotoViewPicker实例。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

### init(UIAbilityContext)

```cangjie
public init(gcontext: UIAbilityContext)
```

**功能：** 构造PhotoViewPicker对象。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|gcontext|[UIAbilityContext](../AbilityKit/cj-apis-ability.md#class-uiabilitycontext)|是|-|传入Ability实例的Context。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaLibraryKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let photoPicker = PhotoViewPicker(ctx)
```

### func select(AsyncCallback\<PhotoSelectResult>, PhotoSelectOptions)

```cangjie
public func select(callback: AsyncCallback<PhotoSelectResult>,
    option!: PhotoSelectOptions = PhotoSelectOptions()): Unit
```

**功能：** 通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。传入可选参数PhotoSelectOptions对象，返回PhotoSelectResult对象。

**注意：** 此接口返回的PhotoSelectResult对象中的photoUris只能通过临时授权的方式调用[getAssets接口](#func-getassetsfetchoptions)去使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<[PhotoSelectResult](#struct-photoselectresult)>|是|-|回调函数。|
|option|[PhotoSelectOptions](#class-photoselectoptions)|否|PhotoSelectOptions()| **命名参数。** photoPicker选择选项，若无此参数，则默认选择媒体文件类型为图片和视频类型，默认选择媒体文件数量的最大值为50。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |13900042|Unknown error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaLibraryKit.*
import kit.ArkData.*
import ohos.base.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let photoPicker = PhotoViewPicker(ctx)
let callback4: AsyncCallback<PhotoSelectResult> = {
    errorCode: Option<AsyncError>, data: Option<PhotoSelectResult> => match (errorCode) {
        case Some(e) => AppLog.error("callback error: errcode is ${e.code}")
        case _ => match (data) {
            case Some(value) => AppLog.info(
                "callback: get data successfully. PhotoSelectResult: photoUris.size = ${value.photoUris.size}, isOriginalPhoto = ${value.isOriginalPhoto}"
            )
            case _ => AppLog.error("callback: data is null")
        }
    }
}

let textContextInfo = TextContextInfo(text: "上海野生动物园的大熊猫")
let recommendationOptions = RecommendationOptions(textContextInfo: textContextInfo)
let PhotoSelectOptions = PhotoSelectOptions(recommendationOptions: recommendationOptions)
PhotoSelectOptions.MIMEType = PhotoViewMIMETypes.IMAGE_TYPE
PhotoSelectOptions.maxSelectNumber = 5
photoPicker.select(callback4, option: PhotoSelectOptions)
```