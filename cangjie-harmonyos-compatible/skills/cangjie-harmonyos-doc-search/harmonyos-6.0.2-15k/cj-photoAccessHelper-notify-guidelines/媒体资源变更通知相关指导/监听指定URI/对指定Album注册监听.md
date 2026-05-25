### 对指定Album注册监听

对指定Album注册监听，当被监听的Album发生变更时，返回监听回调。

**前提条件**

- 获取相册管理模块photoAccessHelper实例。
- [申请相册管理模块权限](./cj-photoAccessHelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ_IMAGEVIDEO'和'ohos.permission.WRITE_IMAGEVIDEO'。

下面以对一个用户相册注册监听，通过重命名相册触发监听回调为例。

**开发步骤**

1. [获取用户相册](./cj-photoAccessHelper-userAlbum-guidelines.md#获取用户相册)。
2. 对指定Album注册监听。
3. 将指定用户相册重命名。

```cangjie
import kit.MediaLibraryKit.*
import kit.ArkData.*
import ohos.base.BusinessException
import ohos.base.Callback1Argument
import std.time.DateTime

func example() {
    let context = ctx.getOrThrow()
    let phAccessHelper = getPhotoAccessHelper(context)
    let predicates: DataSharePredicates = DataSharePredicates()
    let albumName: AlbumKeys = AlbumKeys.ALBUM_NAME
    predicates.equalTo(albumName.toString(), Str('albumName'))
    let fetchOptions: FetchOptions = FetchOptions(
        fetchColumns: [],
        predicates: predicates
    )

    try {
        let fetchResult: FetchResult<Album> = phAccessHelper.getAlbums(AlbumType.USER, AlbumSubtype.USER_GENERIC,
            options: fetchOptions)
        let album: Album = fetchResult.getFirstObject()
        AppLog.info('getAlbums successfully, albumUri: ' + album.albumUri)
        phAccessHelper.registerChange(album.albumUri, false, Cb())
        album.albumName = 'newAlbumName' + DateTime.now().toString()
        album.commitModify()
        fetchResult.close()
    } catch (e: BusinessException) {
        AppLog.error('onCallback failed with err: ' + e.toString())
    }
}

class Cb <: Callback1Argument<ChangeData> {
    public func invoke(changeData: ChangeData) {
        AppLog.info('onCallback successfully, changeData: ${changeData.`type`}')
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