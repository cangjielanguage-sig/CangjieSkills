# 音频播放开发概述

## 如何选择音频播放开发方式

系统提供了多样化的API，来帮助开发者完成音频播放的开发，不同的API适用于不同音频数据格式、音频资源来源、音频使用场景，甚至是不同开发语言。因此，选择合适的音频播放API，有助于降低开发工作量，实现更佳的音频播放效果。

- [AudioRenderer](./cj-using-audiorenderer-for-playback.md)：用于音频输出的仓颉 API，仅支持PCM格式，需要应用持续写入音频数据进行工作。应用可以在输入前添加数据预处理，如设定音频文件的采样率、位宽等，要求开发者具备音频处理的基础知识，适用于更专业、更多样化的媒体播放应用开发。

- [AudioHaptic](./cj-using-audiohaptic-for-playback.md)：用于音振协同播放的仓颉 API，适用于需要在播放音频时同步发起振动的场景，如来电铃声随振、键盘按键反馈、消息通知反馈等。

除上述方式外，也可以通过Media Kit中的AVPlayer和SoundPool实现音频播放。

- [AVPlayer](../media/cj-media-kit-using-avplayer-for-playback.md)：用于音频播放的仓颉 API，集成了流媒体和本地资源解析、媒体资源解封装、音频解码和音频输出功能。可用于直接播放mp3、m4a等格式的音频文件，不支持直接播放PCM格式文件。

- [SoundPool](../media/cj-media-kit-using-soundpool-for-playback.md)：低时延的短音播放仓颉 API，适用于播放急促简短的音效，如相机快门音效、按键音效、游戏射击音效等。

## 后台播放或熄屏播放开发须知

当前不支持应用后台播放或熄屏播放。
