## class PhotoViewPicker

```cangjie
public class PhotoViewPicker {
    public PhotoViewPicker(let abilityContext: UIAbilityContext)
}
```

**功能：** 图库选择器对象，用来支撑选择图片/视频和保存图片/视频等用户场景。在使用前，需要先通过AbilityContext创建PhotoViewPicker实例。

**系统能力：** SystemCapability.FileManagement.UserFileService

### PhotoViewPicker(UIAbilityContext)

```cangjie
public PhotoViewPicker(let abilityContext: UIAbilityContext)
```

**功能：** 创建PhotoViewPicker实例。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|abilityContext|[UIAbilityContext](../AbilityKit/cj-apis-ability.md#class-uiabilitycontext)|是|-|提供允许访问特定Ability的资源的能力。|

### func save(AsyncCallback\<Array\<String>>, PhotoSaveOptions)

```cangjie
public func save(callback: AsyncCallback<Array<String>>, option!: PhotoSaveOptions = PhotoSaveOptions()): Unit
```

**功能：** 通过保存模式拉起photoPicker界面，用户可以保存一个或多个图片/视频。接口采用callback异步返回形式，传入参数PhotoSaveOptions对象，返回保存文件的URI数组。

> **注意：**
>
> 此接口会将文件保存在文件管理器，而不是图库。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<Array\<String>>|是|-|callback返回photoPicker保存图片或视频文件后的结果集。|
|option|[PhotoSaveOptions](#struct-photosaveoptions)|否|PhotoSaveOptions()| **命名参数。** photoPicker保存图片或视频文件选项。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*
import kit.CoreFileKit.*

let actualContext: UIAbilityContext =Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let picker = PhotoViewPicker(actualContext)
let option = PhotoSaveOptions(newFileNames: ["PhotoViewPicker.jpg", "PhotoViewPicker.mp4"])
let saveCallback = {
    errorCode: Option<AsyncError>, data: Option<Array<String>> => match (errorCode) {
        case Some(e) =>
            AppLog.info("photo save error: errcode is ${e.code}")
        case _ =>
            match (data) {
                case Some(value) =>
                    AppLog.info("photoUris is ${value}")
                case _ => AppLog.info("photo save error: data is null")
            }
    }
}
picker.save(saveCallback, option: option)
```