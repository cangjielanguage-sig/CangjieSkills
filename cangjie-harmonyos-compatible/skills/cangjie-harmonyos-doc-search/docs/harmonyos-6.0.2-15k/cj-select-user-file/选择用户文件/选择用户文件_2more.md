# 选择用户文件

用户需要分享文件、保存图片、视频等用户文件时，开发者可以通过系统预置的[文件选择器（FilePicker）](../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_picker.md)，实现该能力。通过Picker访问相关文件，将拉起对应的应用，引导用户完成界面操作，接口本身无需申请权限。

根据用户文件的常见类型，选择器（FilePicker）分别提供以下选项：

- [PhotoViewPicker](../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_picker.md#class-photoviewpicker)：适用于图片或视频类型文件的选择与保存（该接口在后续版本不再演进）。请使用[PhotoAccessHelper的PhotoViewPicker](../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#class-photoviewpicker)来选择图片文件。请使用[安全控件保存媒体库资源](../media/medialibrary/cj-photoAccessHelper-savebutton.md)。

- [DocumentViewPicker](../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_picker.md#class-documentviewpicker)：适用于文件类型文件的选择与保存。DocumentViewPicker对接的选择资源来自于FilePicker，负责文件类型的资源管理，文件类型不区分后缀，比如浏览器下载的图片、文档等，都属于文件类型。

- [AudioViewPicker](../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_picker.md#class-audioviewpicker)：适用于音频类型文件的选择与保存。AudioViewPicker目前对接的选择资源来自于FilePicker。

## 选择图片或视频类文件

[PhotoViewPicker](../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_picker.md#class-photoviewpicker)在后续版本不再演进，请[PhotoAccessHelper的PhotoViewPicker](../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#class-photoviewpicker)来选择图片文件。