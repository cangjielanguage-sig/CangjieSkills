## 收藏夹

收藏夹属于系统相册，对图片或视频设置收藏时会自动将其加入到收藏夹中，取消收藏则会将其从收藏夹中移除。

### 获取收藏夹对象

通过[getAlbums](../../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#func-getalbumsalbumtype-albumsubtype-fetchoptions)接口获取收藏夹对象。

**前提条件**

- 获取相册管理模块photoAccessHelper实例。
- [申请相册管理模块权限](./cj-photoAccessHelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ_IMAGEVIDEO'。

**开发步骤**

1. 设置获取收藏夹的参数为photoAccessHelper.AlbumType.SYSTEM和photoAccessHelper.AlbumSubtype.FAVORITE。
2. 调用PhotoAccessHelper.getAlbums接口获取收藏夹对象。

```cangjie
import kit.MediaLibraryKit.*
import kit.ArkData.*
import ohos.base.BusinessException

func example() {
    try {
        let context = ctx.getOrThrow()
        let phAccessHelper = getPhotoAccessHelper(context)
        let fetchResult: FetchResult<Album> = phAccessHelper.getAlbums(AlbumType.SYSTEM, AlbumSubtype.FAVORITE)
        let album: Album = fetchResult.getFirstObject()
        AppLog.info('get favorite album successfully, albumUri: ' + album.albumUri)
        fetchResult.close()
    } catch (e: BusinessException) {
        AppLog.error('get favorite album failed with err: ' + e.toString())
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