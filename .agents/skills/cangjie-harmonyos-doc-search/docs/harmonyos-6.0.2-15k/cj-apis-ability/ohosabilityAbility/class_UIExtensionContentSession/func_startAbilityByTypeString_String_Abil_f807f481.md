### func startAbilityByType(String, String, AbilityStartCallback)

```cangjie
public func startAbilityByType(abilityType: String, wantParam: String,
    abilityStartCallback: AbilityStartCallback): Unit
```

**功能：** 通过type隐式启动UIExtensionAbility。仅支持处于前台的应用调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|abilityType|String|是|-|显示拉起的UIExtensionAbility类型。|
|wantParam|String|是|-|表示扩展参数。|
|abilityStartCallback|[AbilityStartCallback](#class-abilitystartcallback)|是|-|回调函数，返回启动失败后的详细错误信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |16000050|Internal error.|

**示例：**

请确保下列两个示例文件在同一个包下面。

<!-- compile -->

```cangjie
// example_photo_extension_ability.cj

import ohos.base.*
import kit.AbilityKit.*

var globalSession: ?UIExtensionContentSession = None
let PHOTO_EDITOR_ABILITY_REGISTER_RESULT = PhotoEditorExtensionAbility.registerCreator("ExamplePhotoEditorAbility",
    {=> ExamplePhotoEditorAbility()})

class ExamplePhotoEditorAbility <: PhotoEditorExtensionAbility {
    public override func onStartContentEditing(uri: String, want: Want, session: UIExtensionContentSession): Unit {
        globalSession = session
        session.loadContent("EntryView")
    }
}
```

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

func getSession(): UIExtensionContentSession {
    return globalSession.getOrThrow()
}

let session = getSession()
let callBack = AbilityStartCallback(
    {
        code, name, message =>
        AppLog.info("AbilityStartCallback onError code ${code}")
        AppLog.info("AbilityStartCallback onError code ${name}")
        AppLog.info("AbilityStartCallback onError message ${message}")
    },
    onResult: {
        result =>
        AppLog.info("AbilityStartCallback onResult result ${result.resultCode}")
        AppLog.info("AbilityStartCallback onResult result ${result.want.abilityName}")
    }
)
session.startAbilityByType("finance", ##"{"wantParams.sceneType":1,"bankCardNo":1234567323}"##, callBack)
```