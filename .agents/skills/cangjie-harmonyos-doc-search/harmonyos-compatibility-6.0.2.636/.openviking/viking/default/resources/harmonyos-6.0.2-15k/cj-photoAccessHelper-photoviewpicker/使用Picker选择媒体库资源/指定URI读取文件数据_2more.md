## 指定URI读取文件数据

1. 待界面从图库返回后，再通过一个类似按钮的组件去调用其他函数，使用[open](../../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_fs.md#static-func-openstring-int64)接口，通过[媒体文件uri](../../file-management/cj-user-file-uri-intro.md#媒体文件uri)打开这个文件得到fd。这里需要注意接口权限参数是fileIo.OpenMode.READ_ONLY。

    ```cangjie
    let uri = ''
    let file = FileFs.open(uri, mode: OpenMode.READ_ONLY.mode)
    AppLog.info('file fd: ${file.fd}')
    ```

2. 通过fd使用[read](../../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_fs.md#func-readarraybyte-readoptions)接口读取这个文件内的数据，读取完成后关闭fd。

    ```cangjie
    let buffer = Array<UInt8>(4096, repeat: 0)
    let readLen = FileFs.read(file.fd, buffer)
    AppLog.info('read data to file succeed and buffer size is: ${readLen}')
    FileFs.close(file)
    ```

## 指定URI获取图片或视频资源

媒体库支持Picker选择[媒体文件](../../file-management/cj-user-file-uri-intro.md#媒体文件uri)URI后，根据指定URI获取图片或视频资源，下面以查询指定URI为'file://media/Photo/1/IMG_datetime_0001/displayName.jpg'为例。

```cangjie
import kit.MediaLibraryKit.*
import kit.ArkData.*
import std.collection.HashMap
import ohos.base.BusinessException

class MediaDataHandler <: MediaAssetDataHandler<Array<UInt8>> {
    public func onDataPrepared(data: Array<UInt8>, map: HashMap<String, String>) {
        if (data.isEmpty()) {
            AppLog.error('Error occurred when preparing data')
            return
        }
        AppLog.info('on image data prepared')
        // 应用自定义对资源数据的处理逻辑。
    }
}

func example() {
    let context = ctx.getOrThrow()
    let phAccessHelper = getPhotoAccessHelper(context)
    let predicates: DataSharePredicates = DataSharePredicates()
    let uri = 'file://media/Photo/1/IMG_datetime_0001/displayName.jpg' // 需保证此uri已存在。
    predicates.equalTo(PhotoKeys.URI.toString(), Str(uri))
    let fetchOptions: FetchOptions = FetchOptions(
        fetchColumns: [PhotoKeys.TITLE.toString()],
        predicates: predicates
    )

    try {
        let fetchResult: FetchResult<PhotoAsset> = phAccessHelper.getAssets(fetchOptions)
        let photoAsset: PhotoAsset = fetchResult.getFirstObject()
        AppLog.info('getAssets photoAsset.uri : ' + photoAsset.uri)
        // 获取属性值，以标题为例；对于非默认查询的属性，get前需要在fetchColumns中添加对应列名。
        AppLog.info('title : ' + photoAsset.get(PhotoKeys.TITLE.toString()).getString())
        // 请求图片资源数据。
        let requestOptions: RequestOptions = RequestOptions(DeliveryMode.HIGH_QUALITY_MODE)
        MediaAssetManager.requestImageData(Global.context, photoAsset, requestOptions, MediaDataHandler())
        AppLog.info('requestImageData successfully')
        fetchResult.close()
    } catch (e: BusinessException) {
        AppLog.error('getAssets failed with err: ' + e.toString())
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