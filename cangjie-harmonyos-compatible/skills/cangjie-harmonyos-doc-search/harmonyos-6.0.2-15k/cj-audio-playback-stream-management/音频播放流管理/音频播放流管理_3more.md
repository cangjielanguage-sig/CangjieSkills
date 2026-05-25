# 音频播放流管理

对于播放音频类的应用，开发者需要关注该应用的音频流的状态以做出相应的操作，比如监听到状态为播放中/暂停时，及时改变播放按钮的UI显示。

## 读取或监听应用内音频流状态变化

参考[使用AudioRenderer开发音频播放功能](./cj-using-audiorenderer-for-playback.md)或[createAudioRenderer](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#func-createaudiorendereraudiorendereroptions)，完成AudioRenderer的创建，然后可以通过以下两种方式查看音频流状态的变化：

- 方法1：直接查看AudioRenderer的[state](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#prop-state-1)：

    ```cangjie
    import kit.AudioKit.*

    let audioRendererState: AudioState = audioRenderer.state
    AppLog.info("Current state is: ${audioRendererState }")
    ```

- 方法2：注册stateChange监听AudioRenderer的状态变化：

    ```cangjie
    import kit.AudioKit.*
    import ohos.base.Callback1Argument

    class StateChangeCallback <: Callback1Argument<AudioState> {
        public StateChangeCallback(let f: (AudioState) -> Unit) {}
        public func invoke(state: AudioState): Unit {
            f(state)
        }
    }

    func subscribe() {
        let callback: (AudioState) -> Unit = {
            state: AudioState => AppLog.info("State change to: ${state}")
        }
        audioRenderer.on(AudioRendererCallbackType.AR_STATE_CHANGE, StateChangeCallback(callback))
    }
    ```

获取state后可对照[AudioState](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-audiostate)来进行相应的操作，比如更改暂停播放按钮的显示等。

## 读取或监听所有音频流的变化

如果部分应用需要查询获取所有音频流的变化信息，可以通过AudioStreamManager读取或监听所有音频流的变化。

如下为音频流管理调用关系图：

![Audio stream management invoking relationship](figures/audio-stream-mgmt-invoking-relationship.png)<!-- ToBeReviewed -->

在进行应用开发的过程中，开发者需要使用getStreamManager()创建一个AudioStreamManager实例，进而通过该实例管理音频流。开发者可通过调用[on(AudioStreamManagerCallbackType, Callback1Argument\<AudioRendererChangeInfoArray>)](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#func-onaudiostreammanagercallbacktype-callback1argumentaudiocapturerchangeinfoarray)监听音频流的变化，在音频流状态变化、设备变化时获得通知。同时可通过off('audioRendererChange')取消相关事件的监听。另外，开发者可以主动调用getCurrentAudioRendererInfoArray()来查询播放流的唯一ID、播放流客户端的UID、音频流状态等信息。

详细API含义请参见[AudioStreamManager](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#class-audiostreammanager)。