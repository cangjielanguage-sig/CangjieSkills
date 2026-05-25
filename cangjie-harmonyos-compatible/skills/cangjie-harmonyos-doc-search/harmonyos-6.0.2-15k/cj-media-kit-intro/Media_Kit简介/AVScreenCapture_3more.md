## AVScreenCapture

AVScreenCapture主要工作是捕获音频信号、视频信号，并通过音视频编码将屏幕信息保存到文件中，帮助开发者轻松实现屏幕录制功能，主要包括录屏存文件和录屏取码流两套接口，它允许调用者指定屏幕录制的编码格式、封装格式和文件路径等参数。

当使用AVScreenCapture开发应用录制屏幕时，AVScreenCapture与外部模块的交互关系如图所示。

![AvScreenCapture interaction diagram](./figures/avscreencapture-interaction-diagram.png)

- 音频录制：应用通过调用JS/Native接口层提供的AVScreenCapture接口实现音频录制时，框架层会通过录屏框架，调用音频服务（Audio Framework）通过音频捕获音频数据，通过软件编码封装后保存至文件中，实现音频录制功能。
- 屏幕录制：应用通过调用JS/Native接口层提供的AVScreenCapture接口实现屏幕录制时，框架层会通过录屏框架，调用图形图像服务通过视频捕获屏幕数据，通过软件编码封装后保存至文件中，实现屏幕录制功能。

### 支持的格式

支持的音频源如下：

| 音频源类型 | 说明 |
| -------- | -------- |
| MIC | 系统麦克风作为音频源输入。 |
| ALL_PLAYBACK | 系统内录使用作为音频源输入。 |

支持的视频源如下：

| 视频源类型 | 说明 |
| -------- | -------- |
| SURFACE_RGBA | 输出Buffer是rgba data |

支持的音频编码格式如下：

| 音频编码格式 | 说明 |
| -------- | -------- |
| AAC_LC | AAC_LC类型 |

支持的视频编码格式如下：

| 视频编码格式 | 说明 |
| -------- | -------- |
| H264 | H264类型 |

支持的输出文件格式如下：

| 输出文件格式 | 说明 |
| -------- | -------- |
| mp4 | 视频的容器格式，MP4。 |
| m4a | 纯音频的容器格式，M4A。 |

## AVMetadataExtractor

AVMetadataExtractor 主要用于获取音视频元数据。通过使用 AVMetadataExtractor，开发者可以从原始媒体资源中提取出丰富的元数据信息。以音频资源为例，可以获取到关于该音频的标题、艺术家、专辑名称、时长等详细信息。视频资源的元数据获取流程与音频类似，由于视频没有专辑封面，所以无法获取视频资源的专辑封面。

获取音频资源的元数据的全流程包含：创建AVMetadataExtractor，设置资源，获取元数据，获取专辑封面（可选），销毁资源。

### 支持的格式

支持的音视频源请参见[媒体数据解析](./cj-avcodec-support-formats.md#媒体数据解析)。

## AVImageGenerator

AVImageGenerator 主要用于获取视频缩略图。通过使用 AVImageGenerator，开发者可以实现从原始媒体资源中获取视频指定时间的视频帧。

### 支持的格式

支持的视频源请参见[视频解码](./cj-avcodec-support-formats.md#视频解码)。