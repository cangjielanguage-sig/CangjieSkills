## 视频相册

视频相册属于系统相册，用户文件中属于视频类型的媒体文件会自动加入到视频相册中。

### 获取视频相册对象

通过[getAlbums](../../reference/MediaLibraryKit/cj-apis-file-photo_access_helper.md#func-getalbumsalbumtype-albumsubtype-fetchoptions)接口获取视频相册对象。

**前提条件**

- 获取相册管理模块photoAccessHelper实例。

**开发步骤**

1. 设置获取视频相册的参数为photoAccessHelper.AlbumType.SYSTEM和photoAccessHelper.AlbumSubtype.VIDEO。
2. 调用PhotoAccessHelper.getAlbums接口获取视频相册。

<!-- compile -->

```cangjie
import kit.MediaLibraryKit.*
import ohos.business_exception.*
import kit.AbilityKit.*
import kit.PerformanceAnalysisKit.Hilog

var ctx = Option<UIAbilityContext>.None

func example() {
  try {
    let context = ctx.getOrThrow()
    let phAccessHelper = getPhotoAccessHelper(context)
    let fetchResult: AlbumResult = phAccessHelper.getAlbums(AlbumType.System, AlbumSubtype.Video)
    let album: Album = fetchResult.getFirstObject()
    Hilog.info(1, "info", 'get video album successfully, albumUri: ' + album.albumUri)
    fetchResult.close()
  } catch (e: BusinessException) {
    Hilog.info(1, "info", 'get video album failed with err: ' + e.toString())
  }
}
```

<!-- compile -->

```cangjie
// main_ability.cj
import kit.AbilityKit.*
import kit.PerformanceAnalysisKit.Hilog
import kit.ArkUI.WindowStage

class MainAbility <: UIAbility {
    public init() {
        super()
        registerSelf()
    }

    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        Hilog.info(1, "info", "MainAbility OnCreated.${want.abilityName}")
        match (launchParam.launchReason) {
            case LaunchReason.StartAbility => Hilog.info(1, "info", "START_ABILITY")
            case _ => ()
        }
    }

    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        Hilog.info(1, "info", "MainAbility onWindowStageCreate.")
        windowStage.loadContent("EntryView")
        // declared in index.cj
        ctx = this.context
    }
}
```