# 使用AudioHaptic开发音振协同播放功能

AudioHaptic提供音频与振动协同播放及管理的方法，适用于需要在播放音频时同步发起振动的场景，如来电铃声随振、键盘按键反馈、消息通知反馈等。

## 开发指导

使用AudioHaptic播放音频并同步开启振动，涉及到音频及振动资源的管理、音频时延模式及音频流使用类型的配置、音振播放器的创建及管理等。本开发指导将以一次音振协同播放的过程为例，向开发者讲解如何使用AudioHaptic进行音振协同播放，建议配合[AudioHaptic的API说明](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio_haptic.md)阅读。

### 权限申请

如果应用创建的AudioHapticPlayer需要触发振动，必须校验应用是否拥有 `ohos.permission.VIBRATE` 权限。

1. [声明权限](../../security/AccessToken/cj-declare-permissions.md)。
2. [向用户申请授权](../../security/AccessToken/cj-request-user-authorization.md)。

### 开发步骤及注意事项

1. 获取音振管理器实例，并注册音频及振动资源，资源支持情况请参见[AudioHapticManager](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio_haptic.md#class-audiohapticmanager)。

    ```cangjie
    import kit.AudioKit.*
    import ohos.base.*

    let audioHapticManagerInstance = getAudioHapticManager()
    let audioUri = 'data/audioTest.wav' // 需更改为目标音频资源的Uri
    let hapticUri = 'data/hapticTest.json' // 需更改为目标振动资源的Uri
    let id = audioHapticManagerInstance.registerSource(audioUri, hapticUri)
    ```

2. 设置音振播放器参数，各参数作用请参见[AudioHapticManager](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio_haptic.md#class-audiohapticmanager)。

    ```cangjie
    let latencyMode = AudioLatencyMode.AUDIO_LATENCY_MODE_FAST
    audioHapticManagerInstance.setAudioLatencyMode(id, latencyMode)

    let usage = StreamUsage.STREAM_USAGE_NOTIFICATION
    audioHapticManagerInstance.setStreamUsage(id, usage)
    ```

3. 创建AudioHapticPlayer实例。

    ```cangjie
    let options = AudioHapticPlayerOptions(muteAudio: false, muteHaptics: false)
    let audioHapticPlayer = audioHapticManagerInstance.createPlayer(id, options)
    ```

4. 调用start()方法，开启音频播放并同步开启振动。

    ```cangjie
    audioHapticPlayer.start()
    ```

5. 调用stop()方法，停止音频播放并同步停止振动。

    ```cangjie
    audioHapticPlayer.stop()
    ```

6. 释放AudioHapticPlayer实例。

    ```cangjie
    audioHapticPlayer.release()
    ```

7. 将已注册的音频及振动资源移除注册。

    ```cangjie
    audioHapticManagerInstance.unregisterSource(id)
    ```
