# 保存用户文件

在从网络下载文件到本地或将已有用户文件另存为新的文件路径等场景下，需要使用FilePicker提供的保存用户文件的能力。需关注以下关键点：

**权限说明**

- 通过Picker获取的uri默认只具备**临时读写权限**，临时授权在应用退出后台自动失效。
- 使用picker对音频、图片、视频、文档类文件的保存操作**无需申请权限**。

**系统隔离说明**

- 通过Picker保存的文件存储在用户指定的目录。此类文件与图库管理的资源隔离，无法在图库中看到。
- 若开发者需要保存图片、视频资源到图库，可使用用户无感的[安全控件进行保存](../media/medialibrary/cj-photoAccessHelper-savebutton.md)。

## 保存图片或视频类文件

[PhotoViewPicker](../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_picker.md#class-photoviewpicker)在后续版本不再演进，建议使用[Media Library Kit（媒体文件管理服务）中能力来保存媒体库资源](../media/medialibrary/cj-photoAccessHelper-savebutton.md)。

如果开发场景无法调用安全控件进行图片、视频保存，可使用相册管理模块[PhotoAccessHelper.showAssetsCreationDialog](../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#func-showassetscreationdialogarraystring-arrayphotocreationconfig-callback1argumentarraystring)接口进行保存操作。

## 保存文档类文件

1. 模块导入。

    ```cangjie
    import kit.CoreFileKit.*
    import kit.BasicServicesKit.*
    import kit.AbilityKit.*
    import ohos.base.*
    ```

2. 配置保存选项。

    ```cangjie
    // 创建文件管理器选项实例。
    let documentSaveOptions = DocumentSaveOptions(
        // 保存文件名（可选）。 默认为空。
        newFileNames: ["DocumentViewPicker01.txt"],
        // 保存文件类型['后缀类型描述|后缀类型'],选择所有文件：'所有文件(*.*)|.*'（可选） ，如果选择项存在多个后缀（最大限制100个过滤后缀），默认选择第一个。如果不传该参数，默认无过滤后缀。
        fileSuffixChoices: ["文档|.txt", ".pdf"]
    )
    ```

3. 创建[文件选择器DocumentViewPicker](../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_picker.md#documentviewpickerabilitycontext)实例。调用[save()](../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_picker.md#func-saveasynccallbackarraystring-documentsaveoptions)接口拉起FilePicker界面进行文件保存。

    ```cangjie
    let uris = Box<Array<String>>([])
    // 见获取UIAbility的上下文信息章节
    let context = getContext()
    let documentViewPicker = DocumentViewPicker(context)
    documentViewPicker.save({ err, ret =>
        if (let Some(v) <- err) {
            AppLog.error("Invoke documentViewPicker.save failed, code is ${v.code}")
        }
        if (let Some(v) <- ret) {
            uris.value = v
        }
    }, option: documentSaveOptions)
    ```

    > **注意：**
    >
    > 1、uri存储建议：
    >
    > 避免在Picker回调中直接操作uri。
    > 建议使用全局变量保存uri以供后续使用。
    >
    > 2、快捷保存:
    >
    > 可以通过[DOWNLOAD模式](#download模式保存文件)直达下载目录。

4. 待界面从FilePicker返回后，使用[基础文件API的file_fs.open](../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_fs.md#static-func-openstring-int64)接口，通过uri打开这个文件得到文件描述符(fd)。

    ```cangjie
    let uri = ''
    //这里需要注意接口权限参数是OpenMode.READ_WRITE。
    let file = FileFs.open(uri, mode: OpenMode.READ_WRITE.mode)
    AppLog.info('file fd: ${file.fd}')
    ```

5. 通过(fd)使用[基础文件API的file_fs.write](../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_fs.md#static-func-writeint32-string-writeoptions)接口对这个文件进行编辑修改，编辑修改完成后关闭(fd)。

    ```cangjie
    let writeLen = FileFs.write(file.fd, "hello, world")
    AppLog.info("write data to file succeed and size is: ${writeLen}")
    FileFs.close(file)
    ```