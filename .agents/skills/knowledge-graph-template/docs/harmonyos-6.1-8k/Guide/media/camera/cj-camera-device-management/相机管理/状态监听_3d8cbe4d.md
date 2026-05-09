## 状态监听

在相机应用开发过程中，可以随时监听相机状态，包括新相机的出现、相机的移除、相机的可用状态。在回调函数中，通过相机ID、相机状态这两个参数进行监听，如当有新相机出现时，可以将新相机加入到应用的备用相机中。

通过注册cameraStatus事件，通过回调返回监听结果，callback返回CameraStatusInfo参数，参数的具体内容请参见相机管理器回调接口实例[CameraStatusInfo](../../reference/CameraKit/cj-apis-multimedia-camera.md#class-camerastatusinfo)。

<!-- compile -->

```cangjie
class CameraStatusCallBack <: Callback1Argument<CameraStatusInfo> {
    public open func invoke(error: ?BusinessException,cameraStatusInfo: CameraStatusInfo): Unit {
        // 如果当通过USB连接相机设备时，回调函数会返回新的相机出现状态。
        if (cameraStatusInfo.status == CameraStatus.CameraStatusAppear) {
            Hilog.info(0,"","New Camera device appear.")
        }
        // 如果当断开相机设备USB连接时，回调函数会返回相机被移除状态。
        if (cameraStatusInfo.status == CameraStatus.CameraStatusDisappear) {
            Hilog.info(0,"","Camera device has been removed.")
        }
        // 相机被关闭时，回调函数会返回相机可用状态。
        if (cameraStatusInfo.status == CameraStatus.CameraStatusAvailable) {
            Hilog.info(0,"","Current Camera is available.")
        }
        // 相机被打开/占用时，回调函数会返回相机不可用状态。
        if (cameraStatusInfo.status == CameraStatus.CameraStatusUnavailable) {
            Hilog.info(0,"","Current Camera has been occupied.")
        }
        Hilog.info(0,"","camera: ${cameraStatusInfo.camera.cameraId}")
        Hilog.info(0,"","status: ${cameraStatusInfo.status}")
    }
}

func onCameraStatusChange(cameraManager: CameraManager): Unit {
    cameraManager.on(CameraEvents.CameraStatus, CameraStatusCallBack())
}
```