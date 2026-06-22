# 使用Picker选择媒体库资源

用户有时需要分享图片、视频等用户文件，开发者可以通过特定接口拉起系统图库，用户自行选择待分享的资源，然后最终完成分享。此接口本身无需申请权限，目前适用于界面UIAbility，使用窗口组件触发。具体使用方式如下：

1. 导入选择器模块和文件管理模块。

    ```cangjie
    import kit.MediaLibraryKit.PhotoSelectOptions as MPhotoSelectOptions
    import kit.MediaLibraryKit.*
    import kit.CoreFileKit.*
    import kit.BasicServicesKit.*
    import std.collection.ArrayList
    ```

2. 创建图片-音频类型文件选择选项实例。

    ```cangjie
    var photoSelectOptions = MPhotoSelectOptions()
    ```

3. 配置可选的媒体文件类型和媒体文件的最大数目。
   以下示例以图片选择为例，媒体文件类型请参见[PhotoViewMIMETypes](../../cj-apis-multimedia-photo_accesshelper/.overview.md)。

    ```cangjie
    photoSelectOptions.MIMEType = IMAGE_TYPE // 过滤选择媒体文件类型为IMAGE。
    photoSelectOptions.maxSelectNumber = 5 // 选择媒体文件的最大数目。
    ```

4. 创建图库选择器实例。调用[select](../../cj-apis-multimedia-photo_accesshelper/.overview.md)接口拉起图库界面进行文件选择。文件选择成功后，返回[PhotoSelectResult](../../cj-apis-multimedia-photo_accesshelper/.overview.md)结果集。

    ```cangjie
    let photoViewPicker = MPhotoViewPicker(context)
    let uris: ArrayList<String> = ArrayList<String>()
    photoViewPicker.select(
        {
            e, photoSelectResult => uris.add(all: photoSelectResult.getOrThrow().photoUris)
        },
        option: photoSelectOptions
    )
    ```

   select返回的uri权限是只读权限，可以根据结果集中uri进行读取文件数据操作。注意不能在picker的回调里直接使用此uri进行打开文件操作，需要定义一个全局变量保存uri，类似使用一个按钮去触发打开文件。可参考[指定URI读取文件数据](#指定uri读取文件数据)。

   也可以通过返回的uri[获取图片或视频资源](#指定uri获取图片或视频资源)。

   如有获取元数据需求，可以通过[文件管理接口](../../cj-apis-file_fs/.overview.md)和[文件URI](../../cj-apis-file_fileuri/.overview.md)根据uri获取部分文件属性信息，比如文件大小、访问时间、修改时间、文件名、文件路径等。