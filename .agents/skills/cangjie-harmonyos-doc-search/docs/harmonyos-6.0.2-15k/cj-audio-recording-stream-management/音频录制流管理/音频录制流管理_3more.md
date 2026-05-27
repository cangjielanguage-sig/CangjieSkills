# 音频录制流管理

对于录制音频类的应用，开发者需要关注该应用的音频流的状态以做出相应的操作，比如监听到状态为结束时，及时提示用户录制已结束。

## 读取或监听应用内音频流状态变化

请参见[使用AudioCapturer开发音频录制功能](./cj-using-audiocapturer-for-recording.md)或[createAudioCapturer](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#func-createaudiocaptureraudiocaptureroptions)，完成AudioCapturer的创建，然后可以通过以下两种方式查看音频流状态的变化：

- 方法1：直接查看AudioCapturer的[state](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#prop-state)：

    ```cangjie
    let audioCapturerState: AudioState = audioCapturer.state
    AppLog.info("audioCapturerState: ${audioCapturerState}")
    ```

- 方法2：注册stateChange监听AudioCapturer的状态变化：

    ```cangjie
    class AudioStateCallback <: Callback1Argument<AudioState> {
        public func invoke(arg: AudioState) {
            AppLog.info("callback: ${arg}")
        }
    }

    audioCapturer.on(AudioCapturerCallbackType.STATE_CHANGE, AudioStateCallback())
    ```

获取state后可对照[AudioState](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#enum-audiostate)来进行相应的操作，比如显示录制结束的提示等。

## 读取或监听所有录制流的变化

如果部分应用需要查询获取所有音频流的变化信息，可以通过AudioStreamManager读取或监听所有音频流的变化。

如下为音频流管理调用关系图：

![Invoking relationship of recording stream management](figures/invoking-relationship-recording-stream-mgmt.png) <!-- ToBeReviewed -->

在进行应用开发的过程中，开发者需要使用[getStreamManager()](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#func-getstreammanager)创建一个AudioStreamManager实例，进而通过该实例管理音频流。开发者可通过调用[on(AudioStreamManagerCallbackType.CAPTURER_CHANGE)](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#func-onaudiostreammanagercallbacktype-callback1argumentaudiocapturerchangeinfoarray)监听音频流的变化，在音频流状态变化、设备变化时获得通知，同时可通过[off(AudioStreamManagerCallbackType.CAPTURER_CHANGE)](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#func-offaudiostreammanagercallbacktype-callbackobject)取消相关事件的监听。另外，开发者可以通过主动调用[getCurrentAudioCapturerInfoArray()](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#func-getcurrentaudiocapturerinfoarray)查询录制流的唯一ID、录制流客户端的UID、以及流状态等信息。

详细API含义请参见[AudioStreamManager](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#class-audiostreammanager)。