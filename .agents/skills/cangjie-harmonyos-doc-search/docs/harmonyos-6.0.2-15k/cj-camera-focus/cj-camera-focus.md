# 对焦（仓颉）

相机框架提供对设备对焦的能力，业务应用可以根据使用场景进行对焦模式和对焦点的设置。

## 开发步骤

详细的API说明请参见[Camera API参考](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md)。

1. 导入相关接口，导入方法如下。

    ```cangjie
    import kit.CameraKit.*
    import kit.BasicServicesKit.*
    ```

2. 在设置对焦模式前，需要先调用[isFocusModeSupported](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-isfocusmodesupportedfocusmode)检查设备是否支持指定的焦距模式。

    > **说明：**
    >
    > 需要在Session调用[commitConfig](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-commitconfig)完成配流之后调用。

    ```cangjie
    func isFocusModeSupported(photoSession: PhotoSession): Bool {
        // 以检查是否支持连续自动对焦模式为例
        return photoSession.isFocusModeSupported(FocusMode.FOCOS_MODE_CONTINUOUS_AUTO)
    }
    ```

3. 调用[setFocusMode](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-setfocusmodefocusmode)设置对焦模式。

    若设置为自动对焦模式，支持调用[setFocusPoint](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-setfocuspointpoint)设置对焦点，根据对焦点执行一次自动对焦。

    > **说明：**
    >
    > 需要在Session调用[commitConfig](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-commitconfig)完成配流之后调用。

    ```cangjie
    func setFocusMode(photoSession: PhotoSession): Unit {
        let focusPoint: Point = Point(1.0, 1.0)
        try {
            // 设置自动对焦模式
            photoSession.setFocusMode(FocusMode.FOCOS_MODE_AUTO)
            // 设置对焦点
            photoSession.setFocusPoint(focusPoint)
        } catch (error: BusinessException) {
            // 失败返回错误码error.code并处理
            AppLog.error("The setFocusMode and setFocusPoint call failederror code: ${error.code}")
        }
    }
    ```

## 状态监听

在相机应用开发过程中，可以随时监听相机聚焦的状态变化。

通过注册[focusStateChange](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera.md#func-offcameracallbacktype-callback1argumentfocusstate)的回调函数获取监听结果，仅当自动对焦模式时，且相机对焦状态发生改变时触发该事件。

```cangjie
class FocusStateChangeCallBack <: Callback1Argument<FocusState> {
    var cb: (FocusState) -> Unit
    init(cb: (FocusState) -> Unit) {
        this.cb = cb
    }
    public open func invoke(focusState: FocusState): Unit {
        cb(focusState)
    }
}

func onFocusStateChange(photoSession: PhotoSession): Unit {
    let cb = {
        focusState: FocusState =>
        AppLog.info("focusStateChange focusState: ${focusState}")
        // 为保证对焦功能的用户体验，在自动对焦成功后，可将对焦模式设置为连续自动对焦
        if (focusState == FocusState.FOCUS_STATE_FOCUSED) {
            photoSession.setFocusMode(FocusMode.FOCOS_MODE_CONTINUOUS_AUTO)
        }
    }
    photoSession.on(CameraCallbackType.FocusStateChange, FocusStateChangeCallBack(cb))
}
```
