## class AudioViewPicker

```cangjie
public class AudioViewPicker {
    public AudioViewPicker(let abilityContext: UIAbilityContext)
}
```

**功能：** 音频选择器对象，用来支撑选择和保存音频类文件等用户场景。在使用前，需要先创建AudioViewPicker实例。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

### AudioViewPicker(UIAbilityContext)

```cangjie
public AudioViewPicker(let abilityContext: UIAbilityContext)
```

**功能：** 创建AudioViewPicker实例。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|abilityContext|[UIAbilityContext](../AbilityKit/cj-apis-ability.md#class-uiabilitycontext)|是|-|提供允许访问特定Ability的资源的能力。|

### func save(AsyncCallback\<Array\<String>>, AudioSaveOptions)

```cangjie
public func save(callback: AsyncCallback<Array<String>>, option!: AudioSaveOptions = AudioSaveOptions()): Unit
```

**功能：** 通过保存模式拉起audioPicker界面（目前拉起的是documentPicker，audioPicker在规划中），用户可以保存一个或多个音频文件。接口采用callback异步返回形式，传入参数AudioSaveOptions对象，返回保存音频文件的URI数组。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<Array\<String>>|是|-|callback返回audioPicker保存音频文件后的结果集。|
|option|[AudioSaveOptions](#struct-audiosaveoptions)|否|AudioSaveOptions()| **命名参数。** audioPicker保存音频文件选项。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*
import kit.CoreFileKit.*

let actualContext: UIAbilityContext = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let picker = AudioViewPicker(actualContext)
let option = AudioSaveOptions(newFileNames: ["YourHairLikeSnow.mp3"])
let saveCallback = {
    errorCode: Option<AsyncError>, data: Option<Array<String>> => match (errorCode) {
        case Some(e) =>
            AppLog.info("audio save error: errcode is ${e.code}")
        case _ =>
            match (data) {
                case Some(value) =>
                    AppLog.info("audioUris is ${value}")
                case _ => AppLog.info("audio save error: data is null")
            }
    }
}
picker.save(saveCallback, option: option)
```