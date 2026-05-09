### func getAlbum()

```cangjie
public func getAlbum(): Album
```

**功能：** 获取当前相册变更请求中的相册。

**注意**：对于创建相册的变更请求，在调用[applyChanges](#func-applychangesmediachangerequest)提交生效之前，该接口返回异常。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[Album](./cj-apis-file-photo_access_helper.md#class-album)|返回当前相册变更请求中的相册。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](../CoreFileKit/cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 14000011 | System inner fail. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*
import kit.MediaLibraryKit.*
import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

@Component
class ChildItem {
    @Prop var item: String
    func build() {
        Text(this.item)
        .fontSize(50)
    }
}

func getPhotoAssetList(): Array<PhotoAsset> {
    try {
        // Global 的实现请参见本文"使用说明"小节
        let ctx = Global.abilityContext
        let phAccessHelper = getPhotoAccessHelper(ctx)
        let predicates = DataSharePredicates()
        let fetchOptions: FetchOptions = FetchOptions([], predicates)
        let albumList = phAccessHelper.getAlbums(AlbumType.User, AlbumSubtype.UserGeneric,
            options: fetchOptions)
        let album = albumList.getFirstObject()
        let albumChangeRequest = MediaAlbumChangeRequest(album)
        // 获取当前相册变更请求中的相册，后续可以调用接口获取相册相关信息
        let changeRequestAlbum = albumChangeRequest.getAlbum()
        let fetchResult = changeRequestAlbum.getAssets(fetchOptions)
        return fetchResult.getAllObjects()
    } catch (e: BusinessException) {
        Hilog.info(0, "test", "${e.message}")
        throw e
    }
}

@Entry
@Component
class EntryView {
    @State
    var albumList: Array<PhotoAsset> = getPhotoAssetList()

    func build() {
        Row {
            Column {
                ForEach(this.albumList, itemGeneratorFunc: {item: PhotoAsset,idx:Int64 =>
            ChildItem(item: item.displayName)}, keyGeneratorFunc: {item: PhotoAsset, idx: Int64 => return item.displayName})
            }.width(100.percent)
        }.height(100.percent)
    }
}
```