## AVRecorder

AVRecorder主要工作是捕获音频信号，接收视频信号，完成音视频编码并保存到文件中，帮助开发者轻松实现音视频录制功能，包括开始录制、暂停录制、恢复录制、停止录制、释放资源等功能控制。它允许调用者指定录制的编码格式、封装格式、文件路径等参数。

当使用AVRecorder开发应用录制视频时，AVRecorder与外部模块的交互关系如图所示。

![Video recording interaction diagram](./figures/video-recording-interaction-diagram.png)

- 音频录制：应用通过调用仓颉接口层提供的AVRecorder接口实现音频录制时，框架层会通过录制服务（Player Framework），调用音频服务（Audio Framework）通过音频HDI捕获音频数据，通过软件编码封装后保存至文件中，实现音频录制功能。

- 视频录制：应用通过调用仓颉接口层提供的AVRecorder接口实现视频录制时，先通过Camera接口调用相机服务（Camera Framework）通过视频HDI捕获图像数据送至框架层的录制服务，录制服务将图像数据通过视频编码HDI编码，再将编码后的图像数据封装至文件中，实现视频录制功能。

通过音视频录制组合，可分别实现纯音频录制、纯视频录制、音视频录制。

图中的数字标注表示需要数据与外部模块的传递。

1. 应用通过AVRecorder接口从录制服务获取SurfaceID。

2. 应用将SurfaceID设置给相机服务，相机服务可以通过SurfaceID获取到Surface。相机服务通过视频HDI捕获图像数据送至框架层的录制服务。

3. 相机服务通过Surface将视频数据传递给录制服务。

4. 录制服务通过视频编码HDI模块将视频数据编码。

5. 录制服务将音频参数设置给音频服务，并从音频服务获取到音频数据。

### 支持的格式

支持的音频源如下：

| 音频源类型 | 说明 |
| -------- | -------- |
| mic | 系统麦克风作为音频源输入。 |

支持的视频源如下：

| 视频源类型 | 说明 |
| -------- | -------- |
| surface_yuv | 输入surface中携带的是raw data。 |
| surface_es | 输入surface中携带的是ES data。 |

支持的音视频编码格式如下：

| 音视频编码格式 | 说明 |
| -------- | -------- |
| audio/mp4a-latm | 音频/mp4a-latm类型 |
| video/hevc | 视频/hevc类型 |
| video/avc | 视频/avc类型 |
| audio/mpeg | 音频/mpeg类型 |
| audio/g711mu | 音频/g711-mulaw类型 |

支持的输出文件格式如下：

| 输出文件格式 | 说明 |
| -------- | -------- |
| mp4 | 视频的容器格式，MP4。 |
| m4a | 音频的容器格式，M4A。 |
| mp3 | 音频的容器格式，MP3。 |
| wav | 音频的容器格式，wav。 |