## DOWNLOAD模式保存文件

**模式特点**

- 自动创建在`Download/包名/`目录。
- 跳过文件选择界面直接保存。
- 返回的uri已具备持久化权限， 用户可在该uri下创建文件。

1. 模块导入。

    ```cangjie
    import kit.CoreFileKit.*
    import kit.BasicServicesKit.*
    import kit.AbilityKit.*
    import ohos.base.*
    ```

2. 配置下载模式。

    ```cangjie
    let documentSaveOptions = DocumentSaveOptions(
        // 配置保存的模式为DOWNLOAD，若配置了DOWNLOAD模式，此时配置的其他documentSaveOptions参数将不会生效。
        pickerMode: DocumentPickerMode.DOWNLOAD)
    ```

3. 保存到下载目录。

    ```cangjie
    // 见获取UIAbility的上下文信息章节
    let context = getContext()
    let documentViewPicker = DocumentViewPicker(context)
    documentViewPicker.save({ err, ret =>
        if (let Some(v) <- err) {
            AppLog.error("Invoke documentViewPicker.save failed, code is ${v.code}")
        }
        if (let Some(v) <- ret) {
            let testFilePath = v[0] + "/test.txt"
            let file = FileFs.open(testFilePath, mode: OpenMode.CREATE.mode | OpenMode.READ_WRITE.mode)
            FileFs.write(file.fd, "Hello World!")
            FileFs.close(file.fd)
        }
    }, option: documentSaveOptions)
    ```