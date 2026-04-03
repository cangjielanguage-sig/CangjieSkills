### DASH设置视频起播策略

为了保证在弱网环境下的播放体验，AVPlayer会默认选择最低的视频分辨率开始播放，随后依据网络状况自动调整。开发者可根据实际需求，自定义DASH视频的起播策略，包括设定视频的宽度、高度以及色彩格式等参数。

以调节视频起播分辨率为例，下述示例代码描述了设置视频宽度1920px、高度1080px起播。此时，AVPlayer会选择MPD资源中一路分辨率为1920x1080的视频资源进行播放。

```cangjie
var avPlayer: AVPlayer = createAVPlayer()
var mediaSource: MediaSource = createMediaSourceWithUrl("http://test.cn/dash/aaa.mpd", headers: HashMap<String, String>([("User-Agent", "User-Agent-Value")]))
var playbackStrategy: PlaybackStrategy = PlaybackStrategy(preferredWidth: 1920, preferredHeight: 1080)
avPlayer.setMediaSource(mediaSource, strategy: playbackStrategy)
```

### DASH切换音视频轨道

DASH流媒体资源一般包含多路分辨率、码率、采样率、编码格式等参数各不相同的音频、视频和字幕资源。默认情况下，AVPlayer会依据网络状况自动切换不同码率的视频轨道。开发者可根据实际需求，自主选择指定的音视频轨道进行播放，此时自适应码率切换策略会失效。

1. 设置selectTrack生效的监听事件[trackChange](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#func-onavplayercallbacktype-ontrackchangehandler)。

    ```cangjie
    avPlayer.on(AVPlayerCallbackType.trackChange, TrackChangeCallback())

    // 切换音视频轨道回调函数类，用户可以按照实际情况自行实现回调函数功能
    class TrackChangeCallback <: OnTrackChangeHandler {
        public init() {}
        public open func invoke(index: Int32, isSelect: Bool) {
        AppLog.info("trackChange info, index: ${index}, isSelect: ${isSelect}")
        }
    }
    ```

2. 调用[getTrackDescription](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#func-gettrackdescription)获取所有音视频轨道列表。开发者可根据实际需求，基于[MediaDescription](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#type-mediadescription)各字段信息，确定目标轨道索引。

    ```cangjie
    // 以获取1080p视频轨道索引为例
    func value2String(vt: ValueType): String {
        match(vt) {
        case INT(v) => v.toString()
        case INT64(v) => v.toString()
        case DOUBLE(v) => v.toString()
        case STRING(v) => v.toString()
        }
    }
    var videoTrackIndex = 0
    var arrList: Array<MediaDescription> = avPlayer.getTrackDescription()
    for (i in 0..arrList.size) {
        var propertyIndex: ValueType = arrList[i][MediaDescriptionKey.MD_KEY_TRACK_INDEX]
        var propertyType: ValueType = arrList[i][MediaDescriptionKey.MD_KEY_TRACK_TYPE]
        var propertyWidth: ValueType = arrList[i][MediaDescriptionKey.MD_KEY_WIDTH]
        var propertyHeight: ValueType = arrList[i][MediaDescriptionKey.MD_KEY_HEIGHT]
        if (value2String(propertyType) == "MEDIA_TYPE_VID" && value2String(propertyWidth) == "1920" && value2String(propertyHeight) == "1080") {
        videoTrackIndex = Int32.parse(value2String(propertyIndex)) // 获取1080p视频轨道索引
        }
    }
    ```

3. 在音视频播放过程中调用[selectTrack](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#func-selecttrackint32-switchmode)选择对应的音视频轨道，或者调用[deselectTrack](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#func-deselecttrackint32)取消选择的音视频轨道。

    ```cangjie
    // 切换至目标视频轨道
    avPlayer.selectTrack(videoTrackIndex)
    // 取消选择目标视频轨道
    // avPlayer.deselectTrack(videoTrackIndex)
    ```