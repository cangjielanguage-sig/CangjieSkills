## 音频焦点

系统预设了默认的[音频焦点策略](#音频焦点策略)，根据音频流的类型及启动的先后顺序，对所有播放和录制音频流进行统一管理。

在启动播放或录制功能前，应用需要先[申请音频焦点](#申请音频焦点)；而在播放或录制结束后，应适时[释放音频焦点](#释放音频焦点)。在播放或录制的过程中，可能会因其他音频流的介入而失去焦点，此时，应用需依据焦点变化采取[相应措施](#处理音频焦点变化)。

对于应用而言，为了确保为用户提供优质的音频焦点体验，应当注意以下几点：

- 在启动播放或录制操作前，应根据音频的具体用途，选择并[使用合适的音频流类型](./cj-using-right-streamusage-and-sourcetype.md)，即准确设置[StreamUsage](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-streamusage)或[SourceType](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-sourcetype)。

- 在播放或录制的过程中，需[监听音频焦点事件](#处理音频焦点变化)，并在接收到音频焦点中断事件（[InterruptEvent](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#class-interruptevent)）时，采取相应的处理措施。

### 申请音频焦点

**当应用开始播放或录制音频时，系统将自动为相应的音频流申请音频焦点。**

例如，应用[使用AudioRenderer开发音频播放功能](./cj-using-audiorenderer-for-playback.md)，当调用AudioRenderer的[start](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#func-start-1)时，系统会自动为应用请求音频焦点。

若音频焦点请求成功，音频流将正常启动；反之，若音频焦点请求被拒绝，音频流将无法开始播放或录制。

建议应用主动[监听音频焦点事件](#处理音频焦点变化)，一旦音频焦点请求被拒绝，应用将接收到[音频焦点事件（InterruptEvent）](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#class-interruptevent)。

**特殊场景：**

1. **短音播放：** 若应用[使用SoundPool开发音频播放功能](../media/cj-media-kit-using-soundpool-for-playback.md)，且[StreamUsage](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-streamusage)指定为Music、Movie、AudioBook等类型，播放短音，则其申请焦点时默认为并发模式，不会影响其他音频。

2. **静音播放：** 若应用以静音状态开始播放音频（或视频），并且希望静音阶段不影响其他音频，当后续解除静音的时候，再以正常策略申请音频焦点，则可以调用静音并发播放模式的相关接口。具体请参见：

    - [使用AVPlayer开发音频播放功能](../media/cj-media-kit-using-avplayer-for-playback.md)，可以调用[setMediaMuted](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#func-setmediamutedmediatype-bool)函数。
    - [使用AudioRenderer开发音频播放功能](./cj-using-audiorenderer-for-playback.md)，可调用[setSilentModeAndMixWithOthers](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#func-setsilentmodeandmixwithothersbool)函数。

### 释放音频焦点

**当应用结束播放或录制音频时，系统会自动为相应的音频流释放音频焦点。**

例如，应用[使用AudioRenderer开发音频播放功能](./cj-using-audiorenderer-for-playback.md)，当调用AudioRenderer的[pause](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#func-pause)、[stop](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#func-stop)等时，系统会为其释放音频焦点。

当音频流释放音频焦点时，若存在受其影响的其他音频流（如音量被调低或被暂停的流），将触发恢复操作。