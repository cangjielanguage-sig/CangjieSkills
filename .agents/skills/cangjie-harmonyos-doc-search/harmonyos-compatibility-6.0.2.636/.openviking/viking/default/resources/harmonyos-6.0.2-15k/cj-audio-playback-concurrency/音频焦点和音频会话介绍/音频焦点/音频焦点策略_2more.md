### 音频焦点策略

当音频流申请或释放音频焦点时，系统依据音频焦点策略，对所有音频流（包括播放和录制）实施焦点管理，决定哪些音频流可正常运行，哪些需被打断或执行其他操作。

系统预设的默认音频焦点策略，主要依据音频流类型（即播放流的[StreamUsage](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-streamusage)和录制流的[SourceType](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-sourcetype)）及音频流启动的顺序进行决策。

为防止焦点变化不符合预期，应用在启动播放或录制前，应根据音频流的用途，准确设置StreamUsage或SourceType。关于各类型的详细说明，请参考[使用合适的音频流类型](./cj-using-right-streamusage-and-sourcetype.md)。

常见的音频焦点场景示例如下：

- 开始播放Movie音频流时，将导致正在播放的Music音频流暂停，但Movie播放停止后，Music不会收到恢复播放的通知。
- 开始Navigation音频流时，会自动降低正在播放的Music音频流音量，Navigation停止后，Music音量将恢复至原样。
- Music音频流与Game音频流可并发混音播放，相互之间不会影响音量或播放状态。
- VoiceCommunication开始播放时，将暂停正在播放的Music音频流，VoiceCommunication停止后，Music将收到恢复播放的通知。
- 开始录制VoiceMessage时，Music音频流会被暂停，VoiceMessage录制停止后，Music将收到恢复播放的通知。

### 焦点模式

针对同一应用创建的多个音频流，应用可通过设置[焦点模式（InterruptMode）](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-interruptmode)，选择由应用自主管控，或由系统统一管理。

系统预设了两种焦点模式：

- 共享焦点模式（SHARE_MODE）：同一应用创建的多个音频流共享一个音频焦点。这些音频流之间的并发规则由应用自行决定，音频焦点策略不会介入。仅当其他应用创建的音频流与该应用的音频流同时播放时，才会触发音频焦点策略的管理。

- 独立焦点模式（INDEPENDENT_MODE）：应用创建的每个音频流均独立拥有一个音频焦点，多个音频流同时播放时，将触发音频焦点策略的管理。

应用可根据需求选择合适的焦点模式。在创建音频流时，系统默认采用共享焦点模式（SHARE_MODE），应用可主动设置所需模式。

设置焦点模式的方法：

- 若[使用AVPlayer开发音频播放功能](../media/cj-media-kit-using-avplayer-for-playback.md)，则可以通过修改AVPlayer的[audioInterruptMode](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#prop-audiointerruptmode)属性进行设置。

- 若[使用AudioRenderer开发音频播放功能](./cj-using-audiorenderer-for-playback.md)，则可以调用[setInterruptMode](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#func-setinterruptmodeinterruptmode)函数进行设置。