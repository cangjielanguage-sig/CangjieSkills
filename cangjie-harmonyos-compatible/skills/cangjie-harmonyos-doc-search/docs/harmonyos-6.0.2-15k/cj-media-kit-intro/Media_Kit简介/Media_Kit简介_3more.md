# Media Kit简介

Media Kit（媒体服务）用于开发音视频播放或录制的各类功能。在Media Kit的开发指导中，将详细介绍音视频多个模块的开发方式，指导开发者如何使用系统提供的音视频API实现对应功能。比如使用SoundPool实现简单的提示音，当设备接收到新消息时，会发出短促的“滴滴”声；使用AVPlayer实现音乐播放器，循环播放一首音乐。

Media Kit提供的模块有：

- [AVPlayer](#avplayer)：播放音视频
- [SoundPool](#soundpool)：播放短音频
- [AVRecorder](#avrecorder)：录制音视频
- [AVScreenCapture](#avscreencapture)：录制屏幕
- [AVMetadataExtractor](#avmetadataextractor)：获取音视频元数据
- [AVImageGenerator](#avimagegenerator)：获取视频缩略图

## 亮点/特征

- 使用轻量媒体引擎

   使用较少的系统资源（线程、内存），可支持音视频播放/录制，pipeline灵活拼装，以及插件化扩展source/demuxer/codec。

- 支持HDR视频

   系统原生数据结构与接口支持hdr vivid的采集与播放，方便第三方应用在业务中使用系统的HDR能力，为用户带来更绚丽的体验。

- 支持音频池

   针对开发中常用的短促音效播放场景，如相机快门音效、系统通知音效等，应用可调用SoundPool，实现一次加载，多次低时延播放。

## 开发说明

本开发指导仅针对音视频播放或录制本身，由media模块提供相关能力，不涉及UI界面、图形处理、媒体存储或其他相关领域功能。

在开发音乐、视频播放功能之前，建议了解流媒体播放的相关概念包括但不限于：

- 播放过程：网络协议 > 容器格式 > 音视频编解码 > 图形/音频渲染

- 网络协议：比如HLS、HTTP-FLV、HTTP/HTTPS

- 容器格式：比如mp4、mkv、mpeg-ts

- 编码格式：比如h264/h265

详细流媒体开发流程请参见[流媒体播放开发指导](./cj-media-kit-streaming-media-playback-development-guide.md)。