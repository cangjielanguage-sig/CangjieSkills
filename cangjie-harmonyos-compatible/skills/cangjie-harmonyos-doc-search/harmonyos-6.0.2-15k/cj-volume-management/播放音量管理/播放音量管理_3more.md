# 播放音量管理

本模块提供播放音量管理能力，包括对**系统音量**、**应用音量**和**音频流音量**的管理。

**系统音量**是由HarmonyOS系统全局管理的音量设置，适用于所有应用程序和设备。HarmonyOS系统将音频分为不同的流类型，每种流类型有独立的系统音量控制。

> **说明：**
>
> 系统音量可以通过物理音量按键或系统设置界面调节。在设置界面中，用户可以单独调整上述每种系统音量的大小。

常见的流类型以及对应的系统音量如下所示。

- 媒体音量：用于音乐、视频、游戏等媒体播放。
- 通话音量：用于语音通话。
- 铃声音量：用于来电铃声。
- 闹钟音量：用于闹钟提醒。

**应用音量**是HarmonyOS提供给三方应用用来控制该应用下所有音频流音量的一种音量类型。三方应用设置应用音量之后，该应用中起的所有音频流默认使用该音量大小。另外具有系统应用权限的应用可以通过UID单独调整指定应用的音量。

**音频流音量**是由应用独立控制的音量设置，仅影响该应用中指定的音频流输出音量大小。例如：媒体播放器可以独立控制其播放音量，而不影响系统音量以及该应用中的其他类型流音量。

系统音量、应用音量和音频流音量的关系如下所示。

- 层级关系：系统音量是全局的，应用音量和音频流音量是局部的。应用音量和音频流音量的调整范围受系统音量的限制。例如：系统媒体音量设置为50%，应用音量设置为100%，应用程序的最终输出音量只能达到50%。音频流音量是对应用音量的更精细化控制。设置了应用音量的三方应用，还可以继续通过音频流音量对指定的音频流进行更加精细化的控制。

- 协同关系：应用最终的输出音量是由系统音量、应用音量和音频流音量共同决定的。例如：系统媒体音量设置为50%，应用音量设置为50%，应用程序中对媒体音频流设置音频流音量为100%，则该音频流最终输出的音量为25%。

HarmonyOS通过系统音量，应用音量和音频流音量协同的方式实现应用对音量的精确控制。

## 系统音量

管理系统音量的接口由AudioVolumeManager提供，在使用之前，需要使用[getVolumeManager()](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#func-getvolumemanager)获取AudioVolumeManager实例。

通过AudioVolumeManager只能获取音量信息及监听音量变化，不能主动调节系统音量。

```cangjie
import kit.AudioKit.*

let audioManager = getAudioManager()
let audioVolumeManager = audioManager.getVolumeManager()
```

### 监听系统音量变化

通过设置监听事件，可以监听系统音量的变化：

```cangjie
import kit.AudioKit.*
import ohos.base.Callback1Argument

class VolumeEventCallback <: Callback1Argument<VolumeEvent> {
    public VolumeEventCallback(let f: (VolumeEvent) -> Unit) {}
    public func invoke(event: VolumeEvent): Unit {
        f(event)
    }
}

func subscribe() {
    let callback: (VolumeEvent) -> Unit = {
        volumeEvent: VolumeEvent =>
        AppLog.info("VolumeType of stream: ${volumeEvent.volumeType}")
        AppLog.info("Volume level: ${volumeEvent.volume}")
        AppLog.info("Whether to updateUI: ${volumeEvent.updateUi}")
    }
    audioVolumeManager.on(AudioVolumeManagerCallbackType.VOLUME_CHANGE, VolumeEventCallback(callback))
}
```

## 应用音量

目前不支持设置和查询应用音量。