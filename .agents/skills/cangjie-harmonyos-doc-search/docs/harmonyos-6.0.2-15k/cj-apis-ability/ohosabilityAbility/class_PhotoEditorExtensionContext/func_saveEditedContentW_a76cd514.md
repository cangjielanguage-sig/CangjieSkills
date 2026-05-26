### func saveEditedContentWithUri(String)

```cangjie
public func saveEditedContentWithUri(uri: String): AbilityResult
```

**功能：** 传入编辑过的图片的uri并保存。

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uri|String|是|-|编辑后图片的uri，格式为file://\<bundleName>/\<sandboxPath>。|

**返回值：**

|类型|说明|
|:----|:----|
|[AbilityResult](#struct-abilityresult)|AbilityResult对象，编辑过的图片uri存在want.uri中，uri格式为file://\<bundleName>/\<sandboxPath>。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |29600001|Internal error.|
  |29600002|Image input error.|
  |29600003|Image too big.|

**示例：**

详细使用说明请参见[拉起图片编辑类应用](../../../../Dev_Guide/application-models/cj-photoEditorExtensionAbility.md#拉起图片编辑类应用startabilitybytype)。

```cangjie
import ohos.base.*
import kit.AbilityKit.*
import kit.ImageKit.{createPixelMap, PixelMap, PackingOption, InitializationOptions, PixelMapFormat, Size}

let PHOTO_EDITOR_ABILITY_REGISTER_RESULT = PhotoEditorExtensionAbility.registerCreator("ExamplePhotoEditorAbility",
    {=> ExamplePhotoEditorAbility()})

class ExamplePhotoEditorAbility <: PhotoEditorExtensionAbility {
    public override func onStartContentEditing(uri: String, want: Want, session: UIExtensionContentSession): Unit {
        try {
            let result = context.saveEditedContentWithUri("file://xxx/xxx")
        } catch (e: BusinessException) {
            AppLog.error("ExamplePhotoEditorAbility saveEditedContentWithUri failed : ${e.code}, ${e.message}")
        }
    }
}
```