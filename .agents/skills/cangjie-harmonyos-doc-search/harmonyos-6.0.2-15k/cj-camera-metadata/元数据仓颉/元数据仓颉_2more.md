# 元数据（仓颉）

在开发相机应用时，需要先参考开发准备[申请相关权限](./cj-camera-preparation.md)。

元数据（Metadata）是对相机返回的图像信息数据的描述和上下文，针对图像信息，提供的更详细的数据，如照片或视频中，识别人像的取景框坐标等信息。

Metadata主要是通过一个TAG（Key），去找对应的Data，用于传递参数和配置信息，减少内存拷贝操作。

## 开发步骤

详细的API说明请参见[Camera API参考](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md)。

1. 导入相关接口，导入方法如下。

    ```cangjie
    import kit.CameraKit.*
    import kit.BasicServicesKit.*
    ```

2. 调用[CameraOutputCapability](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#struct-cameraoutputcapability)类中的supportedMetadataObjectTypes属性，获取当前设备支持的元数据类型，并通过[createMetadataOutput](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-createmetadataoutputarraymetadataobjecttype)方法创建元数据输出流。

    ```cangjie
    func getMetadataOutput(cameraManager: CameraManager, cameraOutputCapability: CameraOutputCapability): MetadataOutput {
        let metadataObjectTypes: Array<MetadataObjectType> = cameraOutputCapability.supportedMetadataObjectTypes
        let metadataOutput = cameraManager.createMetadataOutput(metadataObjectTypes);
        return metadataOutput
    }
    ```

3. 调用[Session.start](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-start)方法开启metadata数据输出，再通过监听事件metadataObjectsAvailable回调拿到数据，接口调用失败时，会返回相应错误码，错误码类型参见[Camera错误码](../../../API_Reference/source_zh_cn/errorcodes/cj-errorcode-multimedia-camera.md)。

    previewOutput获取方式请参见[相机预览开发步骤](./cj-camera-preview.md#开发步骤)。

    ```cangjie
    func startMetadataOutput(previewOutput: PreviewOutput, metadataOutput: MetadataOutput, cameraManager: CameraManager): Unit {
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
        session.addOutput(metadataOutput)
        session.commitConfig()
        session.start()
    }
    ```

4. 调用[Session.stop](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-stop)方法停止输出metadata数据，接口调用失败会返回相应错误码，错误码类型参见[Camera错误码](../../../API_Reference/source_zh_cn/errorcodes/cj-errorcode-multimedia-camera.md)。

    ```cangjie
    func stopMetadataOutput(session: Session): Unit {
        session.stop()
    }
    ```