## 获取动态照片对象

- 应用可以通过Picker的方式获取用户媒体库里的动态照片对象，后续可用于在应用内播放动态照片，或是读取动态照片资源进行其他操作（如上传到应用共享给他人浏览等）。

- 应用也可以通过传入应用沙箱的[应用文件](../../file-management/cj-app-file-access.md)图片和视频fileUri的方式构造应用本地的动态照片对象。

### 获取媒体库动态照片对象

1. 通过Picker选择动态照片的[媒体文件](../../file-management/cj-user-file-uri-intro.md#媒体文件uri)uri。
2. 调用[getAssets](../../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#func-getassetsfetchoptions-1)和[getFirstObject](../../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#func-getfirstobject)接口获取uri对应的PhotoAsset资产。
3. 调用[requestMovingPhoto](../../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#static-func-requestmovingphotoabilitycontext-photoasset-requestoptions-mediaassetdatahandlermovingphoto)获取PhotoAsset对应的动态照片对象（MovingPhoto）。

```cangjie
import kit.MediaLibraryKit.*
import kit.ArkData.*
import std.collection.{ArrayList, HashMap}
import ohos.base.BusinessException

var ctx = None<UIAbilityContext>

func example() {
    try {
        let context = ctx.getOrThrow()
        let phAccessHelper = getPhotoAccessHelper(context)
        // picker选择动态照片uri。
        let photoSelectOptions = PhotoSelectOptions()
        photoSelectOptions.MIMEType = PhotoViewMIMETypes.MOVING_PHOTO_IMAGE_TYPE
        photoSelectOptions.maxSelectNumber = 9
        let photoViewPicker = PhotoViewPicker(context)
        photoViewPicker.select(
            {
                e, photoSelectResult => if (let Some(v) <- photoSelectResult) {
                    let uris = v.photoUris
                    for (i in 0..uris.size) {
                        // 获取uri对应的PhotoAsset资产。
                        let predicates: DataSharePredicates = DataSharePredicates()
                        predicates.equalTo(PhotoKeys.URI.toString(), Str(uris[i]))
                        let fetchOption: FetchOptions = FetchOptions(
                            fetchColumns: [],
                            predicates: predicates
                        )
                        let fetchResult: FetchResult<PhotoAsset> = phAccessHelper.getAssets(fetchOption)
                        let photoAsset: PhotoAsset = fetchResult.getFirstObject()
                        // 获取PhotoAsset对应的动态照片对象。
                        MediaAssetManager.requestMovingPhoto(context, photoAsset, RequestOptions(DeliveryMode.FAST_MODE),
                            MediaDataHandler())
                    }
                }
            },
            option: photoSelectOptions
        )
    } catch (e: BusinessException) {
        AppLog.error("request moving photo failed with error: ${e.code}, ${e.message}")
    }
}

class MediaDataHandler <: MediaAssetDataHandler<MovingPhoto> {
    public func onDataPrepared(movingPhoto: MovingPhoto, map: HashMap<String, String>) {
        // 应用可自定义对movingPhoto的处理逻辑。
        AppLog.info('request moving photo successfully, uri: ' + movingPhoto.getUri())
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