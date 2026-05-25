# 使用AVPlayer播放流媒体

本开发指导将介绍如何使用[AVPlayer](./cj-media-kit-intro.md#avplayer)开发流媒体播放功能，以完整地播放一个流媒体视频作为示例，实现端到端播放流媒体资源。

当前指导仅介绍如何实现流媒体播放功能，本地音视频播放等其他场景，请参见[视频播放](./cj-media-kit-using-avplayer-for-playback.md)。

## 流媒体支持的格式

| 流媒体协议类型 | 典型链接 | 网络点播 | 网络直播 |内容保护 |
| -------- | -------- | -------- | -------- | -------- |
| HLS | `https://xxxx/index.m3u8` | 支持 | 支持 | - |
| DASH | `https://xxxx.mpd` | 支持 | - | - |
| HTTP/HTTPS | `https://xxxx.mp4` | 支持 | - | - |
| HTTP-FLV | `https://xxxx.flv` | 支持 | 支持 | - |

## 开发步骤

创建AVPlayer，设置播放资源和窗口，设置播放参数（音量/倍速/缩放模式），播放控制（播放/暂停/跳转/停止），重置，销毁资源。在进行应用开发的过程中，开发者可以通过AVPlayer的state属性主动获取当前状态或使用on("stateChange")方法监听状态变化。如果应用在视频播放器处于错误状态时执行操作，系统可能会抛出异常或生成其他未定义的行为。状态的详细说明请参见[AVPlayerState](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#enum-avplayerstate)。具体的开发步骤如下：

1. 创建实例createAVPlayer()，AVPlayer初始化idle状态。

2. 设置业务需要的监听事件，搭配全流程场景使用。支持的监听事件包括：

   | 事件类型 | 说明 |
   | -------- | -------- |
   | stateChange | 必要事件，监听播放器的state属性改变。 |
   | error | 必要事件，监听播放器的错误信息。 |
   | durationUpdate | 用于进度条，监听进度条长度，刷新资源时长。 |
   | timeUpdate | 用于进度条，监听进度条当前位置，刷新当前时间。 |
   | seekDone | 响应API调用，监听seek()请求完成情况。<br/>当使用seek()跳转到指定播放位置后，如果seek操作成功，将上报该事件。 |
   | speedDone | 响应API调用，监听setSpeed()请求完成情况。<br/>当使用setSpeed()设置播放倍速后，如果setSpeed操作成功，将上报该事件。 |
   | volumeChange | 响应API调用，监听setVolume()请求完成情况。<br/>当使用setVolume()调节播放音量后，如果setVolume操作成功，将上报该事件。 |
   | bufferingUpdate | 用于网络播放，监听网络播放缓冲信息，用于上报缓冲百分比以及缓存播放进度。 |
   | audioInterrupt | 监听音频焦点切换信息，搭配属性audioInterruptMode使用。<br/>如果当前设备存在多个音频正在播放，音频焦点被切换（即播放其他媒体如通话等）时将上报该事件，应用可以及时处理。 |

3. 设置资源：[使用AVPlayer设置播放URL](./cj-media-kit-playback-url-setting-method.md)，AVPlayer进入initialized状态。

   > **说明：**
   >
   > 下面代码示例中的url仅作示意使用，开发者需根据实际情况，确认资源有效性并设置：
   >
   > - 使用网络播放路径，需声明权限：ohos.permission.INTERNET。
   > - 需要使用支持的播放格式与协议。

4. 设置窗口：获取并设置属性SurfaceID，用于设置显示画面。

   应用需要从XComponent组件获取surfaceID，获取方式请参见[XComponent](../../../API_Reference/source_zh_cn/arkui-cj/cj-rendering-drawing-xcomponent.md)。

5. 准备播放：调用prepare()，AVPlayer进入prepared状态，此时可以获取duration，设置缩放模式、音量等。

6. 视频播控：播放play()，暂停pause()，跳转seek()，停止stop()等操作。

7. （可选）更换资源：调用reset()重置资源，AVPlayer重新进入idle状态，允许更换资源url。

8. 退出播放：调用release()销毁实例，AVPlayer进入released状态，退出播放。