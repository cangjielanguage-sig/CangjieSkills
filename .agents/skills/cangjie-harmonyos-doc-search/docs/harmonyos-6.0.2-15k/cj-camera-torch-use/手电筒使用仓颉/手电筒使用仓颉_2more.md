# 手电筒使用（仓颉）

手电筒模式的使用是通过操作手机启用手电筒功能，使设备的手电筒功能持续保持常亮状态。

在使用相机应用并操作手电筒功能时，存在以下几种情况说明：

- 当使用后置摄像头并设置闪光灯模式[FlashMode](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#enum-flashmode)关闭时，手电筒功能无法启用。
- 当使用前置摄像头时，手电筒可以正常启用并保持常亮状态。
- 从前置摄像头切换至后置摄像头时，如果手电筒原本处于开启状态，它将会被自动关闭。

## 开发步骤

详细的API说明请参见[Camera API参考](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md)。

1. 导入camera接口，接口中提供了相机相关的属性和方法，导入方法如下。

    ```cangjie
    import kit.CameraKit.*
    import kit.BasicServicesKit.*
    ```

2. 通过[CameraManager](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#class-cameramanager)类中的[isTorchSupported](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-istorchsupported)方法，检测当前设备是否支持手电筒功能。

    ```cangjie
    func isTorchSupported(cameraManager: CameraManager): Bool {
        let torchSupport: Bool = cameraManager.isTorchSupported()
        AppLog.info("Returned with the torch support status: ${torchSupport}")
        return torchSupport
    }
    ```

3. 通过[CameraManager](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#class-cameramanager)类中的[isTorchModeSupported](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-istorchmodesupportedtorchmode)方法，检测是否支持指定的手电筒模式[TorchMode](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#enum-torchmode)。

    ```cangjie
    func isTorchModeSupported(cameraManager: CameraManager, torchMode: TorchMode): Bool {
        return cameraManager.isTorchModeSupported(torchMode)
    }
    ```

4. 通过[CameraManager](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#class-cameramanager)类中的[setTorchMode](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-settorchmodetorchmode)方法，设置当前设备的手电筒模式。以及通过[CameraManager](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#class-cameramanager)类中的[getTorchMode](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-gettorchmode)方法，获取当前设备的手电筒模式。

    > **说明：**
    >
    > 在使用[getTorchMode](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-gettorchmode)方法前，需要先注册监听手电筒的状态变化，请参见[状态监听](#状态监听)。

    ```cangjie
    func setTorchModeSupported(cameraManager: CameraManager, torchMode: TorchMode): Unit {
        cameraManager.setTorchMode(torchMode)
        let isTorchMode = cameraManager.getTorchMode()
        AppLog.info("Returned with the torch mode supportd mode: ${isTorchMode}")
    }
    ```