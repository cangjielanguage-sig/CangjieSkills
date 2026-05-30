### 快进快退

系统支持三种快进快退的时长，应用可以通过接口进行设置；同时注册快进快退的回调命令，以响应控制。

```cangjie
import kit.AVSessionKit.*
import ohos.base.*

class FastForwardCallback <: Callback1Argument<Int64> {
    FastForwardCallback(let f: (Int64) -> Unit) {}
    public func invoke(arg1: Int64): Unit {
        f(arg1)
    }
}

class RewindCallback <: Callback1Argument<Int64> {
    RewindCallback(let f: (Int64) -> Unit) {}
    public func invoke(arg1: Int64): Unit {
        f(arg1)
    }
}

let context = Global.getStageContext() // 获取Context应用上下文请参见 [API 参考] -> [API参考概述] -> [开发说明] -> [仓颉示例代码说明]

func setListener() {
    let `type`: AVSessionType = AVSessionType.SESSION_TYPE_AUDIO
    // 假设已经创建了一个session，如何创建session可以参考之前的案例。
    let session = createAVSession(context, 'SESSION_NAME', `type`)

    // 设置支持的快进快退的时长设置给AVSession。
    let metadata = AVMetadata("0")
    metadata.title = "TITLE"
    metadata.mediaImage = ValueType.STRING("IMAGE")
    metadata.skipIntervals = SkipIntervals.SECONDS_10
    try {
        session.setAVMetadata(metadata)
        AppLog.info("SetAVMetadata successfully")
    } catch (err: BusinessException) {
        AppLog.error("Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}")
    }

    session.on(
        AVSessionEventType.FastForward,
        FastForwardCallback({
            time => AppLog.info("on fastForward , do fastForward task")
        // do some tasks ···
        })
    )
    session.on(
        AVSessionEventType.Rewind,
        RewindCallback({
            time => AppLog.info("on rewind , do rewind task")
        // do some tasks ···
        })
    )
}
```

### 收藏

音乐类应用实现收藏功能，那么需要注册收藏的控制响应[on(AVSessionEventType, Callback0Argument)](../../../API_Reference/source_zh_cn/apis/AVSessionKit/cj-apis-multimedia_avsession.md#func-onavsessioneventtype-callback0argument)。

```cangjie
import kit.AVSessionKit.*
import ohos.base.*

class ToggleFavoriteCallback <: Callback1Argument<String> {
    ToggleFavoriteCallback(let f: (String) -> Unit) {}
    public func invoke(arg1: String): Unit {
        f(arg1)
    }
}

let context = Global.getStageContext() // 获取Context应用上下文请参见 [API 参考] -> [API参考概述] -> [开发说明] -> [仓颉示例代码说明]

func setListener() {
    let `type`: AVSessionType = AVSessionType.SESSION_TYPE_AUDIO
    // 假设已经创建了一个session，如何创建session可以参考之前的案例。
    let session = createAVSession(context, 'SESSION_NAME', `type`)
    session.on(
        AVSessionEventType.ToggleFavorite,
        ToggleFavoriteCallback(
            {
                assetId =>
                AppLog.info("on toggleFavorite")
                // 应用收到收藏命令，进行收藏处理。

                // 应用内完成或者取消收藏，把新的收藏状态设置给AVSession。
                let playbackState = AVPlaybackState()
                playbackState.isFavorite = true
                try {
                    session.setAVPlaybackState(playbackState)
                    AppLog.info("SetAVPlaybackState successfully")
                } catch (err: BusinessException) {
                    AppLog.error("SetAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}")
                }
            }
        )
    )
}
```