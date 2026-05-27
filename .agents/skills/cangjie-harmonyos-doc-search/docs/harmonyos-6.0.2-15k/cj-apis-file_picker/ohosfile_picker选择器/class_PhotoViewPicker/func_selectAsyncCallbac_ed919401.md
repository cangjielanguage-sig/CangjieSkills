### func select(AsyncCallback\<PhotoSelectResult>, PhotoSelectOptions)

```cangjie
public func select(
    callback: AsyncCallback<PhotoSelectResult>,
    option!: PhotoSelectOptions = PhotoSelectOptions()
): Unit
```

**功能：** 通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用callback异步返回形式，传入参数PhotoSelectOptions对象，返回PhotoSelectResult对象。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<[PhotoSelectResult](#struct-photoselectresult)>|是|-|callback返回photoPicker选择后的结果集。|
|option|[PhotoSelectOptions](#struct-photoselectoptions)|否|PhotoSelectOptions()| **命名参数。** photoPicker选择选项。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*
import kit.CoreFileKit.*

let actualContext: UIAbilityContext =Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let picker = PhotoViewPicker(actualContext)
let option = PhotoSelectOptions(MIMEType: VIDEO_TYPE, maxSelectNumber: 20)
let photoResultCallback = {
    errorCode: Option<AsyncError>, data: Option<PhotoSelectResult> => match (errorCode) {
        case Some(e) =>
            AppLog.info("photo select error: errcode is ${e.code}")
        case _ =>
            match (data) {
                case Some(value) =>
                    AppLog.info("photoUris is ${value.photoUris}")
                    AppLog.info("isOriginalPhoto is ${value.isOriginalPhoto}")
                case _ => AppLog.info("photo select error: data is null")
            }
    }
}
picker.select(photoResultCallback, option: option)
```