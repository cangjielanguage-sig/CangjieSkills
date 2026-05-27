# 预览（仓颉）

在开发相机应用时，需要先参考开发准备[申请相关权限](./cj-camera-preparation.md)。

预览是启动相机后看见的画面，通常在拍照和录像前执行。

## 开发步骤

详细的API说明请参见[Camera API参考](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md)。

1. 导入camera接口，接口中提供了相机相关的属性和方法，导入方法如下。

    ```cangjie
    import kit.CameraKit.*
    import kit.BasicServicesKit.*
    ```

2. 创建Surface。

    XComponent组件为预览流提供的Surface（获取surfaceId请参见[getXcomponentSurfaceId](../../../API_Reference/source_zh_cn/arkui-cj/cj-rendering-drawing-xcomponent.md#func-getxcomponentsurfaceid)方法），而XComponent的能力由UI提供，相关介绍请参见[XComponent组件参考](../../../Dev_Guide/arkui-cj/cj-common-components-xcomponent.md)。

    > **说明：**
    > 预览流与录像输出流的分辨率的宽高比要保持一致，如果设置XComponent组件中的Surface显示区域宽高比为1920:1080 = 16:9，则需要预览流中的分辨率的宽高比也为16:9，如分辨率选择640:360，或960:540，或1920:1080，以此类推。

3. 通过[CameraOutputCapability](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#struct-cameraoutputcapability)类中的previewProfiles属性获取当前设备支持的预览能力，返回previewProfilesArray数组 。通过[createPreviewOutput](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-createpreviewoutputprofile-string)方法创建预览输出流，其中，[createPreviewOutput](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-createpreviewoutputprofile-string)方法中的两个参数分别是previewProfilesArray数组中的第一项和步骤二中获取的surfaceId。

    ```cangjie
    func getPreviewOutput(cameraManager: CameraManager, cameraOutputCapability: CameraOutputCapability, surfaceId: String): PreviewOutput {
        let previewProfilesArray: Array<Profile> = cameraOutputCapability.previewProfiles
        let previewOutput: PreviewOutput = cameraManager.createPreviewOutput(previewProfilesArray[0], surfaceId)
        return previewOutput
    }
    ```

4. 使能。通过[Session.start](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-start)方法输出预览流，接口调用失败会返回相应错误码，错误码类型参见[Camera错误码](../../../API_Reference/source_zh_cn/errorcodes/cj-errorcode-multimedia-camera.md)。

    ```cangjie
    func startPreviewOutput(cameraManager: CameraManager, previewOutput: PreviewOutput): Unit {
        let cameraArray: Array<CameraDevice> = cameraManager.getSupportedCameras()
        if (cameraArray.size == 0) {
            AppLog.error('no camera.')
            return
        }
        // 获取支持的模式类型。
        let sceneModes: Array<SceneMode> = cameraManager.getSupportedSceneModes(cameraArray[0])
        let isSupportPhotoMode: Bool = sceneModes.indexOf(SceneMode.NORMAL_PHOTO).isSome()
        if (!isSupportPhotoMode) {
            AppLog.error('photo mode not support')
            return
        }
        let cameraInput: CameraInput = cameraManager.createCameraInput(cameraArray[0])
        // 打开相机。
        cameraInput.open()
        let session: PhotoSession = (cameraManager.createSession(SceneMode.NORMAL_PHOTO) as PhotoSession).getOrThrow()
        session.beginConfig()
        session.addInput(cameraInput)
        session.addOutput(previewOutput)
        session.commitConfig()
        session.start()
    }
    ```