## AVPlayer

AVPlayer主要工作是将Audio/Video媒体资源（比如mp4/mp3/mkv/mpeg-ts等）转码为可供渲染的图像和可听见的音频模拟信号，并通过输出设备进行播放。

AVPlayer具有功能完善一体化的播放能力，应用只需提供流媒体来源，无需负责数据解析和解码，即可实现播放效果。

### 音频播放

当使用AVPlayer开发音乐应用播放音频时，AVPlayer与外部模块的交互关系如图所示。

![Audio Playback Interaction Diagram](./figures/audio-playback-interaction-diagram.png)

音乐类应用通过调用仓颉接口层提供的AVPlayer接口实现相应功能时，框架层会通过播放服务（Player Framework）将资源解析成音频数据流（PCM），音频数据流经过软件解码后输出至音频服务（Audio Framework），由音频服务输出至音频驱动渲染，实现音频播放功能。完整的音频播放需要应用、Player Framework、Audio Framework、音频HDI共同实现。

上图中，数字标注表示需要数据与外部模块的传递。

1. 音乐应用将媒体资源传递给AVPlayer接口。

2. Player Framework将音频PCM数据流输出给Audio Framework，再由Audio Framework输出给音频HDI。

### 视频播放

当使用AVPlayer开发视频应用播放视频时，AVPlayer与外部模块的交互关系如图所示。

![Video playback interaction diagram](./figures/video-playback-interaction-diagram.png)

应用通过调用仓颉接口层提供的AVPlayer接口实现相应功能时，框架层会通过播放服务（Player Framework）解析成单独的音频数据流和视频数据流，音频数据流经过软件解码后输出至音频服务（Audio Framework），再至硬件接口层的音频HDI，实现音频播放功能。视频数据流经过硬件（推荐）/软件解码后输出至图形渲染服务（Graphic Framework），再输出至硬件接口层的显示HDI，完成图形渲染。

完整的视频播放需要：应用、XComponent、Player Framework、Graphic Framework、Audio Framework、显示HDI和音频HDI共同实现。

图中的数字标注表示需要数据与外部模块的传递。

1. 应用从XComponent组件获取窗口SurfaceID，获取方式请参见[XComponent](../../../API_Reference/source_zh_cn/arkui-cj/cj-rendering-drawing-xcomponent.md)。

2. 应用把媒体资源、SurfaceID传递给AVPlayer接口。

3. Player Framework 将视频ES数据流输出给解码HDI，解码获得视频帧（NV12/NV21/RGBA）。

4. Player Framework 将音频PCM数据流输出给Audio Framework，Audio Framework输出给音频HDI。

5. Player Framework 将视频帧（NV12/NV21/RGBA）输出给Graphic Framework，Graphic Framework输出给显示HDI。