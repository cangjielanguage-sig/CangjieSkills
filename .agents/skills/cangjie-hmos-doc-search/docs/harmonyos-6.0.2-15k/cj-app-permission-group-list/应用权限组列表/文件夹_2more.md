## 文件夹

> **说明：**
>
> 仅2in1设备可申请。

- [ohos.permission.READ_WRITE_DOWNLOAD_DIRECTORY](./cj-permissions-for-all-user.md#ohospermissionread_write_download_directory)
- [ohos.permission.READ_WRITE_DOCUMENTS_DIRECTORY](./cj-permissions-for-all-user.md#ohospermissionread_write_documents_directory)

## 文件

- 读写媒体库图片或视频：[](../../media/medialibrary/cj-photoAccessHelper-photoviewpicker.md)

    - 推荐方案（无需申请权限）：使用[Picker](../../media/medialibrary/cj-photoAccessHelper-photoviewpicker.md)读取媒体库的图片与视频。
    - 受限使用方案：申请受限权限[ohos.permission.READ_IMAGEVIDEO](./cj-permissions-for-acl.md#ohospermissionread_imagevideo)或[ohos.permission.WRITE_IMAGEVIDEO](./cj-permissions-for-acl.md#ohospermissionwrite_imagevideo)读取媒体库的图片与视频。

- 读取媒体库音频文件：

  申请受限权限[ohos.permission.READ_AUDIO](./cj-permissions-for-acl.md#ohospermissionread_audio)或[ohos.permission.WRITE_AUDIO](./cj-permissions-for-acl.md#ohospermissionwrite_audio)读写媒体库的音频文件。

- 读取文件管理器中的文件：

  无需申请权限，通过文件Picker读写文件管理器中的文件。请参见：[选择用户文件](../../file-management/cj-select-user-file.md#选择文档类文件)、[保存用户文件](../../file-management/cj-save-user-file.md#保存文档类文件)。