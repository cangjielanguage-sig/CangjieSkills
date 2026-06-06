# 保存媒体库资源

当用户需要保存图片、视频等用户文件到图库时，需在应用中申请相册管理模块权限'ohos.permission.WRITE_IMAGEVIDEO'。

## 使用弹窗授权保存媒体库资源

下面以弹窗授权的方式保存一张图片资源为例。

**开发步骤**

1. 指定待保存到媒体库的位于应用沙箱的[应用文件](../../file-management/cj-user-file-uri-intro.md#媒体文件uri)图片uri。
2. 指定待保存照片的创建选项，包括文件后缀和照片类型，标题和照片子类型可选。
3. 调用[showAssetsCreationDialog](../../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#func-showassetscreationdialogarraystring-arrayphotocreationconfig-callback1argumentarraystring)，基于弹窗授权的方式获取的目标[媒体文件](../../file-management/cj-user-file-uri-intro.md#媒体文件uri)uri。
4. 将来源于应用沙箱的照片内容写入媒体库的目标uri。

```cangjie
import kit.MediaLibraryKit.*
import kit.CoreFileKit.*
import ohos.base.BusinessException
import std.collection.HashMap
import ohos.base.Callback1Argument

func example() {
    try {
        let context = ctx.getOrThrow()
        let phAccessHelper = getPhotoAccessHelper(context)
        // 指定待保存到媒体库的位于应用沙箱的图片uri。
        let srcFileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.jpg'
        let srcFileUris: Array<String> = [srcFileUri]
        // 指定待保存照片的创建选项，包括文件后缀和照片类型，标题和照片子类型可选。
        let photoCreationConfigs: Array<PhotoCreationConfig> = [
            PhotoCreationConfig(
                'jpg',
                PhotoType.IMAGE,
                title: 'test', // 可选。
                subtype: PhotoSubtype.DEFAULT, // 可选。
            )
        ]
        // 基于弹窗授权的方式获取媒体库的目标uri。
        phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs, Cb(srcFileUri))
    } catch (e: BusinessException) {
        AppLog.error("failed to create asset by dialog successfully errCode is: ${e.code}, ${e.message}")
    }
}

class Cb <: Callback1Argument<Array<String>> {
    Cb(let srcFileUri: String) {}
    public func invoke(desFileUris: Array<String>) {
        // 将来源于应用沙箱的照片内容写入媒体库的目标uri。
        let desFile: File = FileFs.open(desFileUris[0], mode: OpenMode.WRITE_ONLY.mode)
        let srcFile: File = FileFs.open(srcFileUri, mode: OpenMode.READ_ONLY.mode)
        FileFs.copyFile(srcFile.fd, desFile.fd)
        FileFs.close(srcFile)
        FileFs.close(desFile)
        AppLog.info('create asset by dialog successfully')
    }
}
```

```cangjie
// main_ability.cj
import kit.AbilityKit.{LaunchReason, LaunchParam, Want, UIAbility}
import kit.ArkUI.WindowStage
import kit.UIKit.AppLog

class MainAbility <: UIAbility {
    public init() {
        super()
        registerSelf()
    }

    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility OnCreated.${want.abilityName}")
        match (launchParam.launchReason) {
            case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
            case _ => ()
        }
    }

    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        AppLog.info("MainAbility onWindowStageCreate.")
        windowStage.loadContent("EntryView")
        // declared in index.cj
        ctx = this.context
    }
}
```
