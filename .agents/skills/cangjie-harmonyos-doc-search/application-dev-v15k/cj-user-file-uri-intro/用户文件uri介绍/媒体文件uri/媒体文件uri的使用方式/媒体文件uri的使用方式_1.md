### 媒体文件uri的使用方式

normal等级的应用使用此类uri可以通过[photoAccessHelper模块](../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md)进行进一步处理。示例代码参见媒体资源使用指导中的[指定URI获取图片或视频资源](../media/medialibrary/cj-photoAccessHelper-photoviewpicker.md#指定uri获取图片或视频资源)。此接口需要申请相册管理模块读权限'ohos.permission.READ_IMAGEVIDEO'，在使用中需要注意应用是否有此权限。

若normal等级的应用不想申请权限也可以通过临时授权的方式使用[PhotoAccessHelper的PhotoViewPicker](../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#class-photoviewpicker)得到的uri使用[photoAccessHelper.getAssets接口](../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#func-getassetsfetchoptions)获取对应uri的PhotoAsset对象。这种方式获取的对象可以调用[getThumbnail](../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#func-getthumbnailsize)获取缩略图和使用[get接口](../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#func-geturi)读取[PhotoKeys](../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#enum-photokeys)中的部分信息。

以下为PhotoKeys中支持临时授权方式可以读取的信息：

| 名称          | 值              | 说明                                                       |
| ------------- | ------------------- | ---------------------------------------------------------- |
| URI           | 'uri'                 | 文件uri。                                                   |
| PHOTO_TYPE    | 'media_type'           | 媒体文件类型。                                              |
| DISPLAY_NAME  | 'display_name'        | 显示名字。                                                   |
| SIZE          | 'size'                | 文件大小。                                                   |
| DATE_ADDED    | 'date_added'          | 文件创建时的Unix时间戳（单位：秒）。            |
| DATE_MODIFIED | 'date_modified'       | 文件修改时的Unix时间戳（单位：秒）。修改文件名不会改变此值，当文件内容发生修改时才会更新。 |
| DURATION      | 'duration'            | 持续时间（单位：毫秒）。                                    |
| WIDTH         | 'width'               | 图片宽度（单位：像素）。                                    |
| HEIGHT        | 'height'              | 图片高度（单位：像素）。                                      |
| DATE_TAKEN    | 'date_taken'          | 拍摄时的Unix时间戳（单位：秒）。                |
| ORIENTATION   | 'orientation'         | 图片文件的方向。                                             |
| TITLE         | 'title'               | 文件标题。                                                   |

下面为通过临时授权方式使用媒体文件uri进行获取缩略图和读取文件部分信息的示例代码。

```cangjie
import kit.MediaLibraryKit.*
import kit.BasicServicesKit.*
import kit.ArkData.*
import ohos.base.*

// 定义一个uri数组，用于接收PhotoViewPicker选择图片返回的uri
var uris = Box<Array<String>>([])
// 见获取UIAbility的上下文信息章节
let context = getContext()

// 调用PhotoViewPicker.select选择图片
func photoPickerGetUri() {
    let option = PhotoSelectOptions(
        MIMEType: PhotoViewMIMETypes.IMAGE_TYPE,
        maxSelectNumber: 1
    )
    let photoPicker = PhotoViewPicker(context)
    photoPicker.select(
        {
            err, result =>
            if (let Some(v) <- err) {
                AppLog.error("PhotoViewPicker.select failed with err: ${v}")
            }
            if (let Some(v) <- result) {
                uris.value = v.photoUris
            }
        },
        option
    )
}