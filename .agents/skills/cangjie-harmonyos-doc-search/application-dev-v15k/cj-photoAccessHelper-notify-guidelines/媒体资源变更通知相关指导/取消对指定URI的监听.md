## 取消对指定URI的监听

取消对指定uri的监听，通过调用[unRegisterChange](../../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#func-unregisterchangestring-callback1argumentchangedata)接口取消对指定uri的监听。一个uri可以注册多个监听，存在多个callback监听时，可以取消指定注册的callback的监听；不指定callback时取消该uri的所有监听。

**前提条件**

- 获取相册管理模块photoAccessHelper实例。
- [申请相册管理模块权限](./cj-photoAccessHelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ_IMAGEVIDEO'和'ohos.permission.WRITE_IMAGEVIDEO'。

下面以取消对一张图片指定的监听为例，取消监听后，删除图片不再触发对应的监听回调。

**开发步骤**

1. [获取指定媒体资源](./cj-photoAccessHelper-resource-guidelines.md#获取指定媒体资源)。
2. 取消对指定媒体资源uri的监听。
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
        phAccessHelper.registerChange(photoAsset.uri, false, Cb1())
        phAccessHelper.registerChange(photoAsset.uri, false, Cb2())
        phAccessHelper.unRegisterChange(photoAsset.uri, callback: Cb1())
        MediaAssetChangeRequest.deleteAssets(Global.context, [photoAsset])
        fetchResult.close()
    } catch (e: BusinessException) {
        AppLog.error('onCallback failed with err: ' + e.toString())
    }
}

class Cb1 <: Callback1Argument<ChangeData> {
    public func invoke(changeData: ChangeData) {
        AppLog.info('onCallback1 successfully, changeData: ${changeData.`type`}')
    }
}

class Cb2 <: Callback1Argument<ChangeData> {
    public func invoke(changeData: ChangeData) {
        AppLog.info('onCallback2 successfully, changeData: ${changeData.`type`}')
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