## SoundPool

SoundPool主要工作是将音频媒体资源（比如mp3/m4a/wav等）转码为音频模拟信号，并通过输出设备进行播放。

SoundPool提供短音频的播放能力，应用只需提供音频资源来源，不负责数据解析和解码即可实现播放效果。

当使用SoundPool开发应用播放音频时，SoundPool与外部模块的交互关系如图所示。

![SoundPool Interaction Diagram](./figures/soundpool-interaction-diagram.png)

音乐类应用通过调用仓颉接口层提供的SoundPool接口实现相应功能时，框架层会通过播放服务（Player Framework）将资源解析成音频数据流（PCM），音频数据流经过软件解码后输出至音频服务（Audio Framework），由音频服务输出至音频驱动渲染，实现音频播放功能。完整的音频播放需要应用、Player Framework、Audio Framework、音频HDI共同实现。

图中的数字标注表示需要数据与外部模块的传递。

1. 音乐应用将媒体资源传递给SoundPool接口。

2. Player Framework将音频PCM数据流输出给Audio Framework，再由Audio Framework输出给音频HDI。

### 支持的格式与协议

推荐使用以下主流的播放格式，音视容器、音频编码属于内容创作者所掌握的专业领域，不建议应用开发者自制码流进行测试，以免产生无法播放、卡顿等兼容性问题。若发生此类问题不会影响系统，退出播放即可。

支持的协议如下：

| 协议类型 | 协议描述 |
| -------- | -------- |
| 本地点播 | 协议格式：支持file descriptor，禁止file path |

支持的音频播放格式如下：

| 音频容器规格 | 规格描述 |
| -------- | -------- |
| m4a | 音频格式：AAC |
| aac | 音频格式：AAC |
| mp3 | 音频格式：MP3 |
| ogg | 音频格式：VORBIS |
| wav | 音频格式：PCM |