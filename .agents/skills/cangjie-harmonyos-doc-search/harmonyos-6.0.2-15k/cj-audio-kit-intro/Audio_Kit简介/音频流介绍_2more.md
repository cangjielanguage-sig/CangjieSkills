## 音频流介绍

在开发音频应用之前，还需要了解什么是音频流，它是HarmonyOS音频系统中的关键概念，在之后的章节中会多次提及。

音频流，是指音频系统中一个具备音频格式和音频使用场景信息的独立音频数据处理单元。可以表示播放，也可以表示录制，并且具备独立音量调节和音频设备路由切换能力。

音频流基础信息通过[AudioStreamInfo](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#class-audiostreaminfo)表示，包含采样、声道、位宽、编码信息，是创建音频播放或录制流的必要参数，描述了音频数据的基本属性。在配置时开发者需要保证基础信息与传输的音频数据相匹配，音频系统才能正确处理数据。

### 音频流使用场景信息

除了基本属性，音频流还需要具备使用场景信息。基础信息只能对音频数据进行描述，但在实际的使用过程中，不同的音频流，在音量大小、设备路由、并发策略上是有区别的。系统就是通过音频流所附带的使用场景信息，为不同的音频流制定合适的处理策略，以达到更好的音频用户体验。

- 播放场景

    音频播放场景的信息，通过[StreamUsage](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-streamusage)进行描述。

    StreamUsage指音频流本身的用途类型，包括媒体、语音通信、语音播报、通知、铃声等。

- 录制场景

    音频流录制场景的信息，通过[SourceType](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-sourcetype)进行描述。

    SourceType指音频流中录音源的类型，包括麦克风音频源、语音识别音频源、语音通话音频源等。

请参见[使用合适的音频流类型](./cj-using-right-streamusage-and-sourcetype.md)进行设置。

## 支持的音频格式

audio模块下的接口支持PCM编码，包括AudioRenderer、AudioCapturer、TonePlayer、OpenSL ES等。

音频格式说明：

- 支持的常用的音频采样率（Hz）：8000、11025、12000、16000、22050、24000、32000、44100、48000、64000、88200、96000、176400、192000， 具体参考枚举[AudioSamplingRate](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-audiosamplingrate)。

    不同设备支持的采样率规格会存在差异。

- 支持单声道、双声道，具体参考[AudioChannel](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-audiochannel)。

- 支持的采样格式：U8（无符号8位整数）、S16LE（带符号的16位整数，小尾数）、S24LE（带符号的24位整数，小尾数）、S32LE（带符号的32位整数，小尾数）、F32LE（带符号的32位浮点数，小尾数），具体参考[AudioSampleFormat](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-audiosampleformat)。

    由于系统限制，S24LE、S32LE、F32LE仅部分设备支持，请根据实际情况使用。

    小尾数指的是小端模式，即数据的高字节保存在内存的高地址中，而数据的低字节保存在内存的低地址中。这种存储模式将地址的高低和数据的位权有效结合起来，高地址部分权值高，低地址部分权值低。