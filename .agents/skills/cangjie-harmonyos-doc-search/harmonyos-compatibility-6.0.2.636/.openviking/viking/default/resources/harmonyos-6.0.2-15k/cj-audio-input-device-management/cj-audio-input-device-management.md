# 管理全局音频输入设备

有时设备同时连接多个音频输入设备，需要指定音频输入设备进行音频录制，此时需要使用AudioRoutingManager接口进行输入设备的管理，API说明请参见[AudioRoutingManager API文档](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#class-audioroutingmanager)。

## 创建AudioRoutingManager实例

在使用AudioRoutingManager管理音频设备前，需要先导入模块并创建实例。

```cangjie
import kit.AudioKit.*
import ohos.base.*

let audioManager = getAudioManager() // 需要先创建AudioManager实例
let audioRoutingManager = audioManager.getRoutingManager() // 再调用AudioManager的方法创建AudioRoutingManager实例
```

## 支持的音频输入设备类型

目前支持的音频输入设备见下表：

| 名称 | 值 | 说明 |
| :-------- | :-------- | :-------- |
| WIRED_HEADSET | 3 | 有线耳机，带麦克风。 |
| BLUETOOTH_SCO | 7 | 蓝牙设备SCO（Synchronous Connection Oriented）连接。 |
| MIC | 15 | 麦克风。 |
| USB_HEADSET | 22 | USB耳机，带麦克风。 |

## 获取输入设备信息

使用getDevices()方法可以获取当前所有输入设备的信息。

```cangjie
let devices = audioRoutingManager.getDevices(DeviceFlag.INPUT_DEVICES_FLAG)
AppLog.info("getDevices success")
```

## 监听设备连接状态变化

可以设置监听事件来监听设备连接状态的变化，当有设备连接或断开时触发回调：

```cangjie
// 自定义回调
class DeviceChangeActionCallback <: Callback1Argument<DeviceChangeAction> {
    public func invoke(arg: DeviceChangeAction) {
        AppLog.info("device change type: ${arg.`type`}") // 设备连接状态变化，0为连接，1为断开连接
        AppLog.info("device descriptor size: ${arg.deviceDescriptors.size}")
        for (i in (0..arg.deviceDescriptors.size)) {
            AppLog.info("device change descriptor: ${arg.deviceDescriptors[i].deviceRole}") // 设备角色
            AppLog.info("device change descriptor: ${arg.deviceDescriptors[i].deviceType}") // 设备类型
        }
    }
}

audioRoutingManager.on(AudioRoutingManagerCallbackType.DEVICE_CHANGE, DeviceFlag.INPUT_DEVICES_FLAG, DeviceChangeActionCallback())
AppLog.info("on DEVICE_CHANGE success")
```

取消监听音频设备状态变化：

```cangjie
audioRoutingManager.off(AudioRoutingManagerCallbackType.DEVICE_CHANGE)
AppLog.info("off DEVICE_CHANGE success")
```
