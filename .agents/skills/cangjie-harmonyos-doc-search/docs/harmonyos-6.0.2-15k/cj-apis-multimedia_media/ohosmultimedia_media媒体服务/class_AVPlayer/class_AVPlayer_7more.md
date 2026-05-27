## class AVPlayer

```cangjie
public class AVPlayer {}
```

**功能：** 播放管理类，用于管理和播放媒体资源。在调用AVPlayer的方法前，需要先通过[createAVPlayer()](#func-createavplayer)构建一个AVPlayer实例。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

### prop audioEffectMode

```cangjie
public mut prop audioEffectMode: AudioEffectMode
```

**功能：** 设置音频音效模式，默认值为EFFECT_DEFAULT，动态属性。audioRendererInfo的usage变动时会恢复为默认值，只允许在prepared/playing/paused/completed状态下设置。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**类型：** [AudioEffectMode](../AudioKit/cj-apis-multimedia-audio.md#enum-audioeffectmode)

**读写能力：** 可读写

**起始版本：** 19

### prop audioInterruptMode

```cangjie
public mut prop audioInterruptMode: InterruptMode
```

**功能：** 音频焦点模型。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**类型：** [InterruptMode](../AudioKit/cj-apis-multimedia-audio.md#enum-interruptmode)

**读写能力：** 可读写

**起始版本：** 19

### prop audioRendererInfo

```cangjie
public mut prop audioRendererInfo: AudioRendererInfo
```

**功能：** 设置音频渲染信息。若媒体源包含视频，则usage默认值为STREAM_USAGE_MOVIE，否则usage默认值为STREAM_USAGE_MUSIC。rendererFlags默认值为0。若默认usage不满足需求，则须主动配置[audio.AudioRendererInfo](../AudioKit/cj-apis-multimedia-audio.md#class-audiorendererinfo)。<br/>只允许在**initialized**状态下设置。<br/>在第一次调用[prepare()](#func-prepare)之前设置，以便音频渲染器信息在之后生效。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**类型：** [AudioRendererInfo](../AudioKit/cj-apis-multimedia-audio.md#class-audiorendererinfo)

**读写能力：** 可读写

**起始版本：** 19

### prop currentTime

```cangjie
public prop currentTime: Int32
```

**功能：** 音频的当前播放位置，单位为毫秒（ms）。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### prop dataSrc

```cangjie
public mut prop dataSrc: AVDataSrcDescriptor
```

**功能：** 流式媒体资源描述，只允许在idle状态下设置。

使用场景：应用播放从远端下载到本地的文件，在应用未下载完整音视频资源时，提前播放已获取的资源文件。

支持的视频格式：mp4、mpeg-ts、mkv。

支持的音频格式：m4a、aac、mp3、ogg、wav、flac、amr。

使用示例：假设用户正在从远端服务器获取音视频媒体文件，希望下载到本地的同时，播放已经下载好的部分，步骤如下。

1.用户需要获取媒体文件的总大小size（单位为字节），获取不到时设置为-1。

2.用户需要实现回调函数用于填写数据，如果size = -1，播放器只会按照顺序获取数据；否则播放器会按需跳转并获取数据。

3.用户设置AVDataSrcDescriptor。

> **注意：**
> 如果播放的是mp4/m4a格式，用户需要保证moov字段（媒体信息字段）在mdat字段（媒体数据字段）之前，或者moov之前的字段小于10M，否则会导致解析失败无法播放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**类型：** [AVDataSrcDescriptor](#class-avdatasrcdescriptor)

**读写能力：** 可读写

**起始版本：** 19

### prop duration

```cangjie
public prop duration: Int32
```

**功能：** 视频时长，单位为毫秒（ms），可查询参数。<br/>返回为(-1)表示无效值，**prepared**/**playing**/**paused**/**completed**状态下有效。<br/>直播场景默认返回(-1)。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19