### func onForeground()

```cangjie
public open func onForeground(): Unit
```

**功能：** PhotoEditorExtensionAbility生命周期回调，当PhotoEditorExtensionAbility从后台转到前台时触发。

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**起始版本：** 19

**示例：**

详细使用说明请参见[拉起图片编辑类应用](../../../../Dev_Guide/application-models/cj-photoEditorExtensionAbility.md#拉起图片编辑类应用startabilitybytype)。

```cangjie
import ohos.base.*
import kit.AbilityKit.*

let PHOTO_EDITOR_ABILITY_REGISTER_RESULT = PhotoEditorExtensionAbility.registerCreator("ExamplePhotoEditorAbility",
    {=> ExamplePhotoEditorAbility()})

class ExamplePhotoEditorAbility <: PhotoEditorExtensionAbility {
    public override func onForeground(): Unit {
        AppLog.info("ExamplePhotoEditorAbility onForeground.")
    }
}
```

### func onStartContentEditing(String, Want, UIExtensionContentSession)

```cangjie
public open func onStartContentEditing(uri: String, want: Want, session: UIExtensionContentSession): Unit
```

**功能：** 当PhotoEditorExtensionAbility界面内容对象创建后调用，可以执行读取原始图片、加载页面等操作。

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uri|String|是|-|待编辑的原始图片uri，格式为file://\<bundleName>/\<sandboxPath>。|
|want|[Want](#class-want)|是|-|当前PhotoEditorExtensionAbility的Want类型信息，包括ability名称、bundle名称等。|
|session|[UIExtensionContentSession](#class-uiextensioncontentsession)|是|-|PhotoEditorExtensionAbility界面内容相关信息。|

**示例：**

详细使用说明请参见[拉起图片编辑类应用](../../../../Dev_Guide/application-models/cj-photoEditorExtensionAbility.md#拉起图片编辑类应用startabilitybytype)。

```cangjie
import ohos.base.*
import kit.AbilityKit.*

let PHOTO_EDITOR_ABILITY_REGISTER_RESULT = PhotoEditorExtensionAbility.registerCreator("ExamplePhotoEditorAbility",
    {=> ExamplePhotoEditorAbility()})

class ExamplePhotoEditorAbility <: PhotoEditorExtensionAbility {
    public override func onStartContentEditing(uri: String, want: Want, session: UIExtensionContentSession): Unit {
        AppLog.info("ExamplePhotoEditorAbility onStartContentEditing.")
    }
}
```