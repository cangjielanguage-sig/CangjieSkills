# 动态调整预览帧率（仓颉）

动态调整帧率是直播、视频等场景下控制预览效果的重要能力之一。应用可通过此能力，显性地控制流输出帧率，以适应不同帧率下的业务目标。

某些场景下降低帧率可在相机设备启用时降低功耗。

## 约束与限制

支持的帧率范围及帧率的设置依赖于硬件能力的实现，不同的硬件平台可能拥有不同的默认帧率。

## 开发流程

相机使用预览功能前，均需要创建相机会话。完成会话配置后，应用提交和开启会话，才可以开始调用相机相关功能。

流程图如下所示：

![Camera Framerate](./figures/camera-framerate.png)

与普通的[预览](./cj-camera-preview.md)流程相比，动态调整预览帧率的注意点如图上标识：

1. 调用[createSession](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-createsessionscenemode)创建会话（Session）时，需要指定模式为NORMAL_PHOTO或NORMAL_VIDEO。仅当Session处于NORMAL_PHOTO或NORMAL_VIDEO模式时，支持调整预览流帧率。调整帧率的创建会话方式见[创建Session会话并指定模式](#创建session会话并指定模式)。
2. [动态调整帧率](#调整帧率)的操作，可在启动预览前后任意时刻调用。
3. [动态调整帧率](#调整帧率)在预览里属于可选操作，可以完成：
    - 查询当前支持调整的帧率范围
    - 设置当前帧率
    - 获取当前生效的帧率设置

如何配置会话（Session）、释放资源，请参见[会话管理](./cj-camera-session-management.md) > [预览](./cj-camera-preview.md)，或是[完整流程](#完整流程)示例。

## 创建Session会话并指定模式

相机使用预览等功能前，均需创建相机会话，调用[CameraManager](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#class-cameramanager)创建一个会话。

创建会话时需指定[SceneMode](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#enum-scenemode)为NORMAL_PHOTO或NORMAL_VIDEO，创建出的Session处于拍照或录像模式。

以创建Session会话并指定为NORMAL_PHOTO模式为例：

```cangjie
import kit.CameraKit.*

func createPhotoSession(cameraManager: CameraManager): Session {
    // 创建Session会话并指定为NORMAL_PHOTO模式
    return (cameraManager.createSession(SceneMode.NORMAL_PHOTO) as PhotoSession).getOrThrow()
}
```