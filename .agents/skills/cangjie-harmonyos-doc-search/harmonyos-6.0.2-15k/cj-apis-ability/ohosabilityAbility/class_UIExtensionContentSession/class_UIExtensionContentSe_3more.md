## class UIExtensionContentSession

```cangjie
public class UIExtensionContentSession {}
```

**功能：** UIExtensionContentSession提供界面加载，结果通知等方法。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func loadContent(String)

```cangjie
public func loadContent(path: String): Unit
```

**功能：** 为当前UIExtensionComponent控件对应的窗口加载与LocalStorage相关联的具体页面内容。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|设置加载页面的内容。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |16000050|Internal error.|

**示例：**

详细使用说明请参见[拉起图片编辑类应用](../../../../Dev_Guide/application-models/cj-photoEditorExtensionAbility.md#拉起图片编辑类应用startabilitybytype)。

```cangjie
// example_photo_extension_ability.cj

import ohos.base.*
import kit.AbilityKit.*

let PHOTO_EDITOR_ABILITY_REGISTER_RESULT = PhotoEditorExtensionAbility.registerCreator("ExamplePhotoEditorAbility",
    {=> ExamplePhotoEditorAbility()})

class ExamplePhotoEditorAbility <: PhotoEditorExtensionAbility {
    public override func onStartContentEditing(uri: String, want: Want, session: UIExtensionContentSession): Unit {
        session.loadContent("EntryView")
    }
}
```

### func setWindowPrivacyMode(Bool)

```cangjie
public func setWindowPrivacyMode(isPrivacyMode: Bool): Unit
```

**功能：** 设置窗口是否为隐私模式。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。

**需要权限：** ohos.permission.PRIVACY_WINDOW

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isPrivacyMode|Bool|是|-|窗口是否为隐私模式。true表示模式开启；false表示模式关闭。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|The application does not have permission to call the interface.|
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
    session.setWindowPrivacyMode(true)
} catch (e: BusinessException) {
    AppLog.info("setWindowPrivacyMode error ${e.message}")
}
```