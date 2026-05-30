## class PhotoEditorExtensionAbility

```cangjie
public open class PhotoEditorExtensionAbility <: ExtensionAbility {}
```

**功能：** PhotoEditorExtensionAbility继承自[ExtensionAbility](#class-extensionability)，开发者可通过PhotoEditorExtensionAbility实现图片编辑扩展页面。

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**起始版本：** 19

**父类型：**

- [ExtensionAbility](#class-extensionability)

### prop context

```cangjie
public prop context: PhotoEditorExtensionContext
```

**功能：** PhotoEditorExtensionAbility的上下文。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [PhotoEditorExtensionContext](#class-photoeditorextensioncontext)

**读写能力：** 只读

**起始版本：** 19

### func onBackground()

```cangjie
public open func onBackground(): Unit
```

**功能：** PhotoEditorExtensionAbility生命周期回调，当PhotoEditorExtensionAbility从前台转到后台时触发。

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
    public override func onBackground(): Unit {
        AppLog.info("ExamplePhotoEditorAbility onBackground.")
    }
}
```

### func onCreate()

```cangjie
public open func onCreate(): Unit
```

**功能：** PhotoEditorExtensionAbility创建时回调，执行初始化业务逻辑操作。

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
    public override func onCreate(): Unit {
        AppLog.info("ExamplePhotoEditorAbility OnCreated.")
    }
}
```

### func onDestroy()

```cangjie
public open func onDestroy(): Unit
```

**功能：** PhotoEditorExtensionAbility生命周期回调，在销毁时回调，执行资源清理等操作。

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
    public override func onDestroy(): Unit {
        AppLog.info("ExamplePhotoEditorAbility onDestroy.")
    }
}
```