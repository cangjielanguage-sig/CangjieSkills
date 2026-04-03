# 管理全局音频输出设备

有时设备同时连接多个音频输出设备，需要指定音频输出设备进行音频播放，此时需要使用[AudioRoutingManager接口](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#class-audioroutingmanager)进行输出设备的管理。

## 创建AudioRoutingManager实例

在使用AudioRoutingManager管理音频设备前，需要先导入模块并创建实例。

```cangjie
import kit.AudioKit.* // 导入audio模块。

let audioManager = getAudioManager() // 首先创建AudioManager实例。
let audioRoutingManager = audioManager.getRoutingManager() // 然后调用AudioManager的方法创建AudioRoutingManager实例。
```

## 支持的音频输出设备类型

目前支持的音频输出设备见下表：

| 名称 | 值 | 说明 |
| -------- | -------- | -------- |
| EARPIECE | 1 | 听筒。 |
| SPEAKER | 2 | 扬声器。 |
| WIRED_HEADSET | 3 | 有线耳机，带麦克风。 |
| WIRED_HEADPHONES | 4 | 有线耳机，无麦克风。 |
| BLUETOOTH_SCO | 7 | 蓝牙设备SCO（Synchronous&nbsp;Connection&nbsp;Oriented）连接。 |
| BLUETOOTH_A2DP | 8 | 蓝牙设备A2DP（Advanced&nbsp;Audio&nbsp;Distribution&nbsp;Profile）连接。 |
| USB_HEADSET | 22 | USB耳机，带麦克风。 |

## 获取输出设备信息

使用getDevices()方法可以获取当前所有输出设备的信息。

```cangjie
import kit.AudioKit.*

try {
    audioRoutingManager.getDevices(DeviceFlag.OUTPUT_DEVICES_FLAG)
} catch (e: BusinessException) {
    AppLog.info("Promise returned to indicate that the device list is obtained.")
}
```

## 监听设备连接状态变化

可以设置监听事件来监听设备连接状态的变化，当有设备连接或断开时触发回调：

> **说明：**
>
> 监听设备连接状态变化可以监听到全部的设备连接状态变化，不建议作为应用处理自动暂停的依据。应用如需处理自动暂停相关业务，请参见[音频流输出设备变更原因](./cj-audio-output-device-change.md#音频流输出设备变更原因)。

```cangjie
import kit.AudioKit.*
import ohos.base.Callback1Argument

// 定义监听音频设备状态变化回调函数
class DeviceChangeActionCallback <: Callback1Argument<DeviceChangeAction> {
    public DeviceChangeActionCallback(let f: (DeviceChangeAction) -> Unit) {}
    public func invoke(action: DeviceChangeAction): Unit {
        f(action)
    }
}

let callback: (DeviceChangeAction) -> Unit = {
    action: DeviceChangeAction =>
    AppLog.info("device change type : ${action.`type`}") // 设备连接状态变化，0为连接，1为断开连接。
    AppLog.info("device descriptor size : ${action.deviceDescriptors.size}")
    AppLog.info("device change descriptor : ${action.deviceDescriptors[0].deviceRole}") // 设备角色。
    AppLog.info("device change descriptor : ${action.deviceDescriptors[0].deviceType}") // 设备类型。
}

// 监听音频设备状态变化。
audioRoutingManager.on(
    AudioRoutingManagerCallbackType.DEVICE_CHANGE,
    DeviceFlag.OUTPUT_DEVICES_FLAG,
    DeviceChangeActionCallback(callback)
)

// 取消监听音频设备状态变化。
audioRoutingManager.off(AudioRoutingManagerCallbackType.DEVICE_CHANGE)
```