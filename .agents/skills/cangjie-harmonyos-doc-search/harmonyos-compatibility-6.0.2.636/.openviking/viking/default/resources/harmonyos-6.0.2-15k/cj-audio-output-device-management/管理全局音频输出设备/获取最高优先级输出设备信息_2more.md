## 获取最高优先级输出设备信息

使用[getPreferredOutputDeviceForRendererInfo(AudioRendererInfo)](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#func-getpreferredoutputdeviceforrendererinfoaudiorendererinfo)方法, 可以获取当前最高优先级的输出设备。

> **说明：**
>
> 最高优先级输出设备表示声音将在此设备输出的设备。

```cangjie
import kit.AudioKit.*
import ohos.base.BusinessException

let rendererInfo = AudioRendererInfo(
    StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
    0 // 音频渲染器标志。
)

func getPreferOutputDeviceForRendererInfo() {
    try {
        let descriptors = audioRoutingManager.getPreferredOutputDeviceForRendererInfo(rendererInfo)
        AppLog.info("device descriptor size: ${descriptors.size}")
    } catch (e: BusinessException) {
        AppLog.error("Result ERROR: ${e.toString()}")
    }
}
```

## 监听最高优先级输出设备变化

```cangjie
import kit.AudioKit.*
import ohos.base.Callback1Argument

// 定义监听最高优先级输出设备变化回调函数
class PreferOutputDeviceChangeCallback <: Callback1Argument<AudioDeviceDescriptors> {
    public PreferOutputDeviceChangeCallback(let f: (AudioDeviceDescriptors) -> Unit) {}
    public func invoke(descriptions: AudioDeviceDescriptors): Unit {
        f(descriptions)
    }
}

let rendererInfo = AudioRendererInfo(
    StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
    0 // 音频渲染器标志。
)

func subscribe() {
    let callback: (AudioDeviceDescriptors) -> Unit = {
        descriptors: AudioDeviceDescriptors =>
        AppLog.info("device change descriptor : ${descriptors[0].deviceRole}") // 设备角色。
        AppLog.info("device change descriptor : ${descriptors[0].deviceType}") // 设备类型。
    }
    // 监听最高优先级输出设备变化。
    audioRoutingManager.on(
        AudioRoutingManagerCallbackType.PREFERR_OUTPUT_DEVICE_CHANGE_FOR_RENDERER_INFO,
        rendererInfo,
        PreferOutputDeviceChangeCallback(callback)
    )

    // 取消监听最高优先级输出设备变化。
    audioRoutingManager.off(AudioRoutingManagerCallbackType.PREFERR_OUTPUT_DEVICE_CHANGE_FOR_RENDERER_INFO)
}
```