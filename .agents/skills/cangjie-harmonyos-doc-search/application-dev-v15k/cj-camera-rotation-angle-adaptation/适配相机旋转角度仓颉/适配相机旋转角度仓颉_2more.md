# 适配相机旋转角度（仓颉）

屏幕处于不同的屏幕状态时，原始图像需旋转不同的角度，以确保图像在合适的方向显示，效果如图所示。

![Camera Angle](./figures/camera-angle.png)

本开发指导将指导开发者在预览、拍照、录像等不同场景下，如何适配相机的旋转角度。

- 在预览时，图像旋转角度与屏幕显示旋转角度（[Display.rotation](../../../API_Reference/source_zh_cn/arkui-cj/cj-apis-display.md#prop-rotation)）相关。具体开发指导：[创建会话](#创建会话) > [预览](#预览)
- 在拍照、录像时，图像旋转角度与设备重力方向（即[设备旋转角度](#计算设备旋转角度)）相关。

    录像开发指导：[创建会话](#创建会话) > [计算设备旋转角度](#计算设备旋转角度) > [录像](#录像)

详细的API参考说明，请参见[Camera API文档](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md)。

## 创建会话

1. 导入相机等相关模块。

    ```cangjie
    import kit.CameraKit.*
    import kit.BasicServicesKit.*
    ```

2. 创建Session会话。

    相机使用预览等功能前，均需创建相机会话，调用[CameraManager](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#class-cameramanager)类中的[createSession](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-createsessionscenemode)方法创建一个会话，创建会话时需指定创建[SceneMode](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#enum-scenemode)为NORMAL_PHOTO或NORMAL_VIDEO，创建的session处于拍照或者录像模式。

    ```cangjie
    func createPhotoSession(cameraManager: CameraManager): Session {
        return (cameraManager.createSession(SceneMode.NORMAL_PHOTO) as PhotoSession).getOrThrow()
    }

    func createVideoSession(cameraManager: CameraManager): Session {
        return (cameraManager.createSession(SceneMode.NORMAL_VIDEO) as PhotoSession).getOrThrow()
    }
    ```