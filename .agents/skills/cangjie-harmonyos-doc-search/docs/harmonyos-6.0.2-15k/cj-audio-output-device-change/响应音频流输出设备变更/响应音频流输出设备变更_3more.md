# 响应音频流输出设备变更

开发者可以了解音频流输出设备变更信息，并完成相应适配，确保应用在设备发生变更时的用户体验。

开发者可使用AudioRenderer的[on(AudioRendererCallbackType, Callback1Argument\<AudioStreamDeviceChangeInfo>)](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#func-onaudiorenderercallbacktype-callback1argumentaudiostreamdevicechangeinfo)接口，监听音频流输出设备变化及原因。当系统出现音频输出设备的上下线、用户强制选择、设备抢占或设备选择策略变更等情况，导致音频流输出设备变更时，系统将通过该接口通知应用当前音频流设备变更信息，包含当前音频流输出设备信息和设备变更原因。

## 音频流输出设备信息

在[on(AudioRendererCallbackType, Callback1Argument\<AudioStreamDeviceChangeInfo>)](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#func-onaudiorenderercallbacktype-callback1argumentaudiostreamdevicechangeinfo)返回的音频流设备变更信息中，包含当前音频流输出设备信息，以数组形式发送，一般该列表仅包含一个设备信息，具体请参见[AudioDeviceDescriptors](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#type-audiodevicedescriptors)（设备信息列表）。

## 音频流输出设备变更原因

> **说明：**
>
> 当发生下述四种情况（[AudioStreamDeviceChangeReason](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-audiostreamdevicechangereason)）时，系统将向应用发送设备变更回调。

- **REASON_NEW_DEVICE_AVAILABLE：** 新设备可用。

  **触发场景：**

  普通蓝牙设备（耳机、眼镜、音箱、车机等）连接、支持佩戴检测的蓝牙设备（耳机、眼镜等）佩戴、有线设备（3.5mm耳机、Type-C耳机、USB耳机、USB音箱等）插入、分布式设备上线等。

- **REASON_OLD_DEVICE_UNAVAILABLE：** 旧设备不可用。

    当报告此原因时，应用程序应考虑暂停音频播放。

    **触发场景：**

    普通蓝牙设备（耳机、眼镜、音箱、车机等）断开、支持佩戴检测的蓝牙耳机双耳摘下、支持佩戴检测的蓝牙眼镜摘下、有线设备（3.5mm耳机、Type-C耳机、USB耳机、音箱等）拔出、分布式设备下线等。

    针对此场景，常用业务场景的**处理建议**如下：

    - 游戏场景：不暂停
    - 听书场景：暂停
    - 音乐场景：暂停
    - 视频场景：暂停

- **REASON_OVERRODE：** 用户强制选择设备。

  **触发场景：**

  用户从界面选择切换音频流输出设备、从外设选择接听蜂窝或VoIP来电。

- **REASON_UNKNOWN：** 未知原因。