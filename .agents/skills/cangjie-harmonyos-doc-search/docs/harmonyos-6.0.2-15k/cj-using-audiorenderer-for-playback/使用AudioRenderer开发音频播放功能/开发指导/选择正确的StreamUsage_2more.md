### 选择正确的StreamUsage

创建播放器时候，开发者需要根据应用场景指定播放器的`StreamUsage`，选择正确的`StreamUsage`可以避免用户遇到不符合预期的行为。

在音频API文档[StreamUsage](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-streamusage)介绍中，列举了每一种类型推荐的应用场景。例如音乐场景推荐使用`STREAM_USAGE_MUSIC`，电影或者视频场景推荐使用`STREAM_USAGE_MOVIE`，游戏场景推荐使用`STREAM_USAGE_GAME`，等等。

如果开发者配置了不正确的`StreamUsage`，可能带来一些不符合预期的行为。例如以下场景。

- 游戏场景错误使用`STREAM_USAGE_MUSIC`类型，游戏应用将无法和其他音乐应用并发播放，而游戏场景通常可以与其他音乐应用并发播放。
- 导航场景错误使用`STREAM_USAGE_MUSIC`类型，导航应用播报时候会导致正在播放的音乐停止播放，而导航场景通常期望正在播放的音乐仅仅降低音量播放。

### 配置合适的音频采样率

采样率：指音频每秒单个声道样点数，单位为Hz。

重采样：根据输入输出音频采样率的差异，进行上采样(通过插值增加样点数)或下采样(通过抽取减少样点数)。

AudioRenderer支持枚举类型AudioSamplingRate中定义的所有采样率。

若通过AudioRenderer设置的输入音频采样率与设备输出采样率不一致，系统会将输入音频重采样为设备输出采样率。

若为减少重采样功耗，可使用采样率与输出设备采样率一致的输入音频。推荐使用48k采样率。