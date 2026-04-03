# 使用AVPlayer播放视频

当前提供两种视频播放开发的方案：

- [AVPlayer](cj-media-kit-intro.md#avplayer)：功能较完善的音视频播放仓颉/JS API，集成了流媒体和本地资源解析，媒体资源解封装，视频解码和渲染功能，适用于对媒体资源进行端到端播放的场景，可直接播放mp4、mkv等格式的视频文件。
- Video组件：封装了视频播放的基础能力，需要设置数据源以及基础信息即可播放视频，但相对扩展能力较弱。Video组件由ArkUI提供能力，相关指导请参考UI开发文档-[Video组件](../../arkui-cj/cj-common-components-video-player.md)。

本开发指导将介绍如何使用AVPlayer开发视频播放功能，以完整地播放一个视频作为示例，实现端到端播放原始媒体资源。

播放的全流程包含：创建AVPlayer，设置播放资源和窗口，设置播放参数（音量/倍速/缩放模式），播放控制（播放/暂停/跳转/停止），重置，销毁资源。在进行应用开发的过程中，开发者可以通过AVPlayer的state属性主动获取当前状态或使用on('stateChange')方法监听状态变化。如果应用在视频播放器处于错误状态时执行操作，系统可能会抛出异常或生成其他未定义的行为。播放状态变化示意图如下所示。

![Playback status change](./figures/playback-status-change.png)

状态的详细说明请参见[AVPlayerState](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#enum-avplayerstate)。当播放处于prepared / playing / paused / completed状态时，播放引擎处于工作状态，这需要占用系统较多的运行内存。当客户端暂时不使用播放器时，调用reset()或release()回收内存资源，做好资源利用。

## 开发建议

当前指导仅介绍如何实现媒体资源播放，在应用开发过程中可能会涉及后台播放、播放冲突等情况，请根据实际需要参考以下说明。

- 当前暂不支持暂不支持后台播放或息屏播放。
- 应用在播放过程中，若播放的媒体数据涉及音频，根据系统音频管理策略（参考[处理音频焦点事件](../audio/cj-audio-playback-concurrency.md)），可能会被其他应用打断，建议应用主动监听音频打断事件，根据其内容提示，做出相应的处理，避免出现应用状态与预期效果不一致的问题。
- 面对设备同时连接多个音频输出设备的情况，应用可以通过[on('audioOutputDeviceChangeWithInfo')](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#func-onavplayercallbacktype-callback1argumentaudiostreamdevicechangeinfo)监听音频输出设备的变化，从而做出相应处理。
- 如果需要访问在线媒体资源，需要申请 ohos.permission.INTERNET 权限。