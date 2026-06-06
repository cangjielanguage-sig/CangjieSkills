## class PhotoEditorExtensionContext

```cangjie
public class PhotoEditorExtensionContext <: ExtensionContext {}
```

**功能：** PhotoEditorExtensionContext是[PhotoEditorExtensionAbility](#class-photoeditorextensionability)的上下文，继承自[ExtensionContext](#class-extensioncontext)，提供PhotoEditorExtensionAbility的相关配置信息以及保存图片接口。

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**起始版本：** 19

**父类型：**

- [ExtensionContext](#class-extensioncontext)

### func saveEditedContentWithImage(PixelMap, PackingOption)

```cangjie
public func saveEditedContentWithImage(pixelMap: PixelMap, option: PackingOption): AbilityResult
```

**功能：** 传入编辑过的图片的PixMap对象并保存。

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pixelMap|[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|是|-|编辑过的图片image.PixelMap。|
|option|[PackingOption](../ImageKit/cj-apis-image.md#class-packingoption)|是|-|设置打包参数。|

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
        let colors: Array<UInt8> = Array<UInt8>(96, repeat: 0)
        let pixelMap = createPixelMap(colors,
            InitializationOptions(editable: true, pixelFormat: RGBA_8888, size: Size(height: 4, width: 6)))
        let format = "image/jpeg"
        let packingOption = PackingOption(format, 98)
        try {
            let result = this.context.saveEditedContentWithImage(pixelMap, packingOption)
            AppLog.info("ExamplePhotoEditorAbility saveEditedContentWithImage: ${result.resultCode}.")
            AppLog.info("ExamplePhotoEditorAbility saveEditedContentWithImage: ${result.want.uri}.")
        } catch (e: BusinessException) {
            AppLog.error("ExamplePhotoEditorAbility saveEditedContentWithImage failed : ${e.code}, ${e.message}")
        }
    }
}
```