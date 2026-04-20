# 相机管理

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

在开发一个相机应用前，需要先通过调用相机接口来创建一个独立的相机设备。

## 开发步骤

详细的API说明请参见[Camera API参考](../../reference/CameraKit/cj-apis-multimedia-camera.md)。

1. 导入camera接口，接口中提供了相机相关的属性和方法，导入方法如下。

    <!-- compile -->

    ```cangjie
    import kit.CameraKit.*
    import kit.AbilityKit.*
    import kit.PerformanceAnalysisKit.Hilog
    import ohos.callback_invoke.Callback1Argument
    import ohos.business_exception.BusinessException
    ```

2. 通过[getCameraManager](../../reference/CameraKit/cj-apis-multimedia-camera.md#func-getcameramanageruiabilitycontext)方法，获取cameraManager对象。

    Context获取方式请参见：[获取UIAbility的上下文信息](../../application-models/cj-uiability-usage.md#获取uiability的上下文信息)。

    <!-- compile -->

    ```cangjie
    func createCameraManager(context: UIAbilityContext): CameraManager {
        let cameraManager: CameraManager = getCameraManager(context)
        return cameraManager
    }
    ```

    > **说明：**
    >
    > 如果获取对象失败，说明相机可能被占用或无法使用。如果被占用，须等到相机被释放后才能重新获取。

3. 通过[CameraManager](../../reference/CameraKit/cj-apis-multimedia-camera.md#class-cameramanager)类中的[getSupportedCameras](../../reference/CameraKit/cj-apis-multimedia-camera.md#func-getsupportedcameras)方法，获取当前设备支持的相机列表，列表中存储了设备支持的所有相机ID。若列表不为空，则说明列表中的每个ID都支持独立创建相机对象；否则，说明当前设备无可用相机，不可继续后续操作。

    <!-- compile -->

    ```cangjie
    func getCameraDevices(cameraManager: CameraManager): Array<CameraDevice> {
        let cameraArray: Array<CameraDevice> = cameraManager.getSupportedCameras()
        if (cameraArray.size > 0) {
            for (index in 0..cameraArray.size) {
                Hilog.info(0,"","cameraId : ${cameraArray[index].cameraId}")  // 获取相机ID。
                Hilog.info(0,"","cameraPosition : ${cameraArray[index].cameraPosition}")  // 获取相机位置。
                Hilog.info(0,"","cameraType : ${cameraArray[index].cameraType}")  // 获取相机类型。
                Hilog.info(0,"","connectionType : ${cameraArray[index].connectionType}")  // 获取相机连接类型。
            }
            return cameraArray
        } else {
            Hilog.error(0,"","cameraManager.getSupportedCameras error")
            return []
        }
    }
    ```