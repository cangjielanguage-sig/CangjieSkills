## class AlbumResult

```cangjie
public class AlbumResult <: FetchResult {}
```

**功能：** 文件检索结果集。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**父类型：**

- [FetchResult](#class-fetchresult)

### func getAllObjects()

```cangjie
public func getAllObjects(): Array<Album>
```

**功能：** 获取文件检索结果中的所有文件资产。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[Album](#class-album)>|返回所有文件资产的数组。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](../CoreFileKit/cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900020 | Invalid argument. |
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

func getAlbumList(): Array<Album> {
    try {
        // Global 的实现请参见本文"使用说明"小节
        let ctx = Global.abilityContext
        let phAccessHelper = getPhotoAccessHelper(ctx)
        let predicates = DataSharePredicates()
        predicates.equalTo('album_name', StringValue('test1'))
        let fetchOptions: FetchOptions = FetchOptions([], predicates)
        let fetchResult = phAccessHelper.getAlbums(AlbumType.User,
            AlbumSubtype.UserGeneric, options: fetchOptions)
        // 获取文件检索结果中的所有相册资产，后续可以遍历相册数组获取每一个相册的信息
        let albums = fetchResult.getAllObjects()
        return albums
    } catch (e: BusinessException) {
        Hilog.info(0, "test", "${e.message}")
        throw e
    }
}

@Entry
@Component
class EntryView {
    @State
    var albumList: Array<Album> = getAlbumList()

    func build() {
        Row {
            Column {
                ForEach(this.albumList, itemGeneratorFunc: {item: Album,idx:Int64 =>
            ChildItem(item: item.albumUri)}, keyGeneratorFunc: {item: Album, idx: Int64 => return item.albumUri})
            }.width(100.percent)
        }.height(100.percent)
    }
}
```