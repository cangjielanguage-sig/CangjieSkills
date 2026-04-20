### func terminateSelf()

```cangjie
public func terminateSelf(): Unit
```

**功能：** 停止UIExtensionContentSession对应的窗口界面对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

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
try {
    session.terminateSelf()
} catch (e: BusinessException) {
    AppLog.info("terminateSelf error ${e.message}")
}
```

### func terminateSelfWithResult(AbilityResult)

```cangjie
public func terminateSelfWithResult(parameter: AbilityResult): Unit
```

**功能：** 停止UIExtensionContentSession对应的窗口界面对象，并将结果返回给UIExtensionComponent控件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|parameter|[AbilityResult](#struct-abilityresult)|是|-|返回给UIExtensionComponent控件的信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

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
try {
    session.terminateSelfWithResult(AbilityResult(1234, Want(uri: "file://com.example.myapplication")))
} catch (e: BusinessException) {
    AppLog.info("terminateSelf error ${e.message}")
}
```