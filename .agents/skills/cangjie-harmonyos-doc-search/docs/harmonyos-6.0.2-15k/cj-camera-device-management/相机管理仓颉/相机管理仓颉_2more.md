# 相机管理（仓颉）

在开发一个相机应用前，需要先通过调用相机接口来创建一个独立的相机设备。

## 开发步骤

详细的API说明请参见[Camera API参考](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md)。

1. 导入camera接口，接口中提供了相机相关的属性和方法，导入方法如下。

    ```cangjie
    import kit.CameraKit.*
    import ohos.base.*
    import kit.AbilityKit.*
    ```

2. 通过[getCameraManager](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-getcameramanagerabilitycontext)方法，获取cameraManager对象。

    Context获取方式请参见：[获取UIAbility的上下文信息](../../application-models/cj-uiability-usage.md#获取uiability的上下文信息)。

    ```cangjie
    func createCameraManager(context: UIAbilityContext): CameraManager {
        let cameraManager: CameraManager = getCameraManager(context)
        return cameraManager
    }
    ```

    > **说明：**
    >
    > 如果获取对象失败，说明相机可能被占用或无法使用。如果被占用，须等到相机被释放后才能重新获取。

3. 通过[CameraManager](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#class-cameramanager)类中的[getSupportedCameras](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-getsupportedcameras)方法，获取当前设备支持的相机列表，列表中存储了设备支持的所有相机ID。若列表不为空，则说明列表中的每个ID都支持独立创建相机对象；否则，说明当前设备无可用相机，不可继续后续操作。

    ```cangjie
    func getCameraDevices(cameraManager: CameraManager): Array<CameraDevice> {
        let cameraArray: Array<CameraDevice> = cameraManager.getSupportedCameras()
        if (cameraArray.size > 0) {
            for (index in 0..cameraArray.size) {
                AppLog.info("cameraId : ${cameraArray[index].cameraId}") // 获取相机ID。
                AppLog.info("cameraPosition : ${cameraArray[index].cameraPosition}") // 获取相机位置。
                AppLog.info("cameraType : ${cameraArray[index].cameraType}") // 获取相机类型。
                AppLog.info("connectionType : ${cameraArray[index].connectionType}") // 获取相机连接类型。
            }
            return cameraArray
        } else {
            AppLog.error("cameraManager.getSupportedCameras error")
            return []
        }
    }
    ```