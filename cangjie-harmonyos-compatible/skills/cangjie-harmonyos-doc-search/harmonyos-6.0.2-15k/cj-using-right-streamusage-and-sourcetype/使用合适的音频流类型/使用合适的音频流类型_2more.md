# 使用合适的音频流类型

[音频流](./cj-audio-kit-intro.md#音频流介绍)类型是定义音频数据播放和录制方式的关键属性。对于播放流，其类型由[StreamUsage](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-streamusage)确定；对于录制流，则由[SourceType](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-sourcetype)决定。音频流类型对音量控制、音频焦点管理以及输入/输出设备的选择具有决定性影响。

为了确保音频行为符合预期并提供优质的用户体验，应用开发者应根据具体业务场景和实际需求，为音频选择适当的流类型。

接下来，文档将介绍[常用的音频流类型及其适用场景](#常用的音频流类型及其适用场景)，同时说明[不同流类型对音频业务的影响](#流类型对音频业务的影响)。最后，指导开发者在采用不同方法实现音频播放和音频录制时，应当如何[设置音频流类型](#设置音频流类型)。

## 常用的音频流类型及其适用场景

### 播放音频流类型

下表中列举常用的播放音频流类型，由[StreamUsage](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-streamusage)定义。

| 音频流使用类型（StreamUsage） | 适用场景 |
| ---------- | ---------- |
| STREAM_USAGE_MUSIC | 适用于播放音乐，同样适用于其他媒体场景，如[使用SoundPool](../media/cj-media-kit-using-soundpool-for-playback.md)播放简短音效等。 |
| STREAM_USAGE_MOVIE |  适用于播放短视频、电影、电视剧等各类视频内容。 |
| STREAM_USAGE_AUDIOBOOK | 适用于播放有声读物、新闻、播客等。|
| STREAM_USAGE_GAME | 适用于游戏内配乐、配音，后台音乐不会被打断；游戏内语音，建议使用STREAM_USAGE_VOICE_COMMUNICATION。 |
| STREAM_USAGE_NAVIGATION | 适用于导航场景的语音播报功能。 |
| STREAM_USAGE_VOICE_MESSAGE | 适用于播放语音短消息。 |
| STREAM_USAGE_VOICE_COMMUNICATION | 适用于VoIP语音通话。 |
| STREAM_USAGE_ALARM | 适用于播放闹铃。 |
| STREAM_USAGE_RINGTONE | 适用于VoIP来电响铃等。 |
| STREAM_USAGE_NOTIFICATION | 适用于播放通知音、提示音。 |

### 录制音频流类型

下表中列举常用的录制音频流类型，由[SourceType](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-sourcetype)定义。

| 音频流使用类型（StreamUsage） | 适用场景 |
| ---------- | ---------- |
| SOURCE_TYPE_MIC | 适用于普通录音。|
| SOURCE_TYPE_VOICE_RECOGNITION | 适用于语音识别。 |
| SOURCE_TYPE_VOICE_COMMUNICATION | 适用于VoIP语音通话。 |
| SOURCE_TYPE_VOICE_MESSAGE | 适用于录制语音短消息。 |
| SOURCE_TYPE_CAMCORDER | 适用于相机录像。 |