# 用户相册资源使用指导

photoAccessHelper提供用户相册相关的接口，供开发者创建、删除用户相册，往用户相册中添加和删除图片和视频资源等。

> **说明：**
>
> 在进行功能开发前，请开发者查阅[开发准备](./cj-photoAccessHelper-preparation.md)，了解如何获取相册管理模块实例和如何申请相册管理模块功能开发相关权限。
>
> 文档中使用 `photoAccessHelper` 的地方，默认为使用开发准备中获取的对象。如未添加此段代码而出现 `photoAccessHelper` 未定义的错误，请自行添加。

如无特别说明，文档中涉及的待获取资源均视为已经预置且在数据库中存在相应数据。如按示例代码执行后获取的资源为空，请确认文件是否已预置，数据库中是否存在该文件的数据。

## 获取用户相册

通过[getAlbums](../../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#func-getalbumsalbumtype-albumsubtype-fetchoptions)接口获取用户相册。

**前提条件**

- 获取相册管理模块photoAccessHelper实例。
- [申请相册管理模块权限](./cj-photoAccessHelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ_IMAGEVIDEO'。

下面以获取一个相册名为'albumName'的用户相册为例。

**开发步骤**

1. 建立检索条件，用于获取用户相册。
2. 调用PhotoAccessHelper.getAlbums接口获取用户相册资源。
3. 调用[getFirstObject](../../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#func-getfirstobject)接口获取第一个用户相册。

```cangjie
import kit.MediaLibraryKit.*
import kit.ArkData.*
import ohos.base.BusinessException

func example() {
    let context = ctx.getOrThrow()
    let phAccessHelper = getPhotoAccessHelper(context)
    let predicates: DataSharePredicates = DataSharePredicates()
    let albumName = AlbumKeys.ALBUM_NAME
    predicates.equalTo(albumName.toString(), Str('albumName'))
    let fetchOptions: FetchOptions = FetchOptions(
        fetchColumns: [],
        predicates: predicates
    )
    try {
        let fetchResult: FetchResult<Album> = phAccessHelper.getAlbums(AlbumType.USER, AlbumSubtype.USER_GENERIC,
            options: fetchOptions)
        let album: Album = fetchResult.getFirstObject()
        AppLog.info('getAlbums successfully, albumName: ' + album.albumName)
        fetchResult.close()
    } catch (e: BusinessException) {
        AppLog.error('getAlbums failed with err: ' + e.toString())
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