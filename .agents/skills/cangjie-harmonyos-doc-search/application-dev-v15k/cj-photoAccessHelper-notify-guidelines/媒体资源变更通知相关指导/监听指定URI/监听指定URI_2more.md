## 监听指定URI

通过调用[registerChange](../../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#func-registerchangestring-bool-callback1argumentchangedata)接口监听指定uri。当被监听对象发生变更时返回监听器回调函数的值。

### 对指定PhotoAsset注册监听

对指定PhotoAsset注册监听，当被监听的PhotoAsset发生变更时，返回监听回调。

**前提条件**

- 获取相册管理模块photoAccessHelper实例。
- [申请相册管理模块权限](./cj-photoAccessHelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ_IMAGEVIDEO'和'ohos.permission.WRITE_IMAGEVIDEO'。

下面以对一张图片注册监听，通过将这张图片删除触发监听回调为例。

**开发步骤**

1. [获取指定媒体资源](./cj-photoAccessHelper-resource-guidelines.md#获取指定媒体资源)。
2. 对指定PhotoAsset注册监听。
3. 将指定媒体资源删除。

```cangjie
import kit.MediaLibraryKit.*
import kit.ArkData.*
import ohos.base.BusinessException
import ohos.base.Callback1Argument

func example() {
    let context = ctx.getOrThrow()
    let phAccessHelper = getPhotoAccessHelper(context)
    let predicates: DataSharePredicates = DataSharePredicates()
    predicates.equalTo(PhotoKeys.DISPLAY_NAME.toString(), Str('test.jpg'))
    let fetchOptions: FetchOptions = FetchOptions(
        fetchColumns: [],
        predicates: predicates
    )

    try {
        let fetchResult: FetchResult<PhotoAsset> = phAccessHelper.getAssets(fetchOptions)
        let photoAsset: PhotoAsset = fetchResult.getFirstObject()
        AppLog.info('getAssets photoAsset.uri : ' + photoAsset.uri)
        phAccessHelper.registerChange(photoAsset.uri, false, Cb())
        MediaAssetChangeRequest.deleteAssets(Global.context, [photoAsset])
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