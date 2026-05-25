## 注意事项

播放流媒体的标准流程如上述开发步骤所示，但使用不同的流媒体格式在实际开发的过程中还是会存在一定差异，本节将详细描述不同流媒体格式业务的差异，包括设置视频起播策略、切换音视频轨道等。

### 流媒体缓冲状态

当下载速率低于片源的码率时，可能会出现卡顿，此时播放器检测到缓冲区数据不足，会先缓冲一些数据再播放，避免连续卡顿。一次卡顿对应的缓冲事件上报过程为：BUFFERING_START-> BUFFERING_PERCENT 0 -> ... -> BUFFERING_PERCENT 100 -> BUFFERING_END。而CACHED_DURATION无论是卡顿过程中还是播放过程中，都会持续上报，直至下载至资源末尾。详情请参见[BufferingInfoType缓冲事件类型枚举](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#enum-bufferinginfotype)。

监听当前bufferingUpdate缓冲状态示例代码：

```cangjie
avPlayer.on(AVPlayerCallbackType.bufferingUpdate, BufferingUpdateCallback())

// 回调函数的实现示例
class BufferingUpdateCallback <: OnBufferingUpdateHandler {
    public init() {}
    public open func invoke(infoType: BufferingInfoType, value: Int32): Unit {
        AppLog.info("AVPlayer bufferingUpdate, infoType is ${infoType}, value is ${value}.")
    }
}
```

### HLS切换码率

当前流媒体HLS协议流支持多码率播放，默认情况下，播放器会根据网络下载速度选择合适的码率。

1. 通过[on("availableBitrates")](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#func-onavplayercallbacktype-callback1argumentarrayint32)监听当前HLS协议流可用的码率，若监听的码率列表长度为0，则不支持设置指定码率。

    ```cangjie
    // 创建avPlayer实例对象
    var avPlayer: AVPlayer = createAVPlayer()
    // 监听当前HLS协议流可用的码率
    avPlayer.on(AVPlayerCallbackType.availableBitrates, AvailableBitCallback)

    // 回调函数类示例，用户可以按照实际情况自行实现回调函数功能
    class AvailableBitCallback <: Callback1Argument<Array<Int32>> {
        public init() {}
        public open func invoke(bitrates: Array<Int32>): Unit {
        AppLog.info("availableBitrates called, and availableBitrates length is: ${bitrates.size}")
        }
    }
    ```

2. 通过[setBitrate](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#func-setbitrateint32)接口设置播放码率，若用户设置的码率不在可用码率中，播放器将从可用码率中选择最小且最接近的码率。该接口只能在prepared/playing/paused/completed状态下调用，可通过监听[bitrateDone](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#func-onavplayercallbacktype-callback1argumentint32)事件确认是否生效。

    ```cangjie
    // 创建avPlayer实例对象
    var avPlayer: AVPlayer = createAVPlayer()
    // 监听码率设置是否生效
    avPlayer.on(AVPlayerCallbackType.bitrateDone, BitrateDoneCallback())
    // 设置播放码率
    var bitrate: Int32 = 96000
    avPlayer.setBitrate(bitrate)

    // 回调函数类示例，用户可以按照实际情况自行实现回调函数功能
    class BitrateDoneCallback <: Callback1Argument<Int32> {
        public init() {}
        public open class invoke(bitrate: Int32): Unit {
        AppLog.info("bitrateDone called, and bitrate value is: ${bitrate}")
        }
    }
    ```