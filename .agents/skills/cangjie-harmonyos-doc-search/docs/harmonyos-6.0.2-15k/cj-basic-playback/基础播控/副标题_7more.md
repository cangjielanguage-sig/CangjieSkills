## 副标题

> **注意：**
>
> 自验证关注点：播放过程中查看播控中心是否显示副标题，显示是否正确。

副标题用于显示媒体内容的辅助信息，如歌曲的歌手名、影片的发布者信息、剧集/综艺节目的选集信息等。可通过[AVMetadata.subtitle](../../../API_Reference/source_zh_cn/apis/AVSessionKit/cj-apis-multimedia_avsession.md#class-avmetadata)或者[AVMetadata.artist](../../../API_Reference/source_zh_cn/apis/AVSessionKit/cj-apis-multimedia_avsession.md#class-avmetadata)，选其一设置。

![playback subtitle](./figures/playback-subtitle.png)

## 滚动歌词

> **注意：**
>
> 自验证关注点：播放过程中查看播控中心是否显示歌词，显示是否正确，是否随进度正确刷新显示。

歌曲类媒体内容如有歌词信息，可以选择在副标题区域显示歌词。将当前播放歌曲的全曲歌词内容，按照标准lyric格式拼接为字符串，如[00:25.44]xxx\r\n[00:26.44]xxx\r\n，通过[AVMetadata.lyric](../../../API_Reference/source_zh_cn/apis/AVSessionKit/cj-apis-multimedia_avsession.md#class-avmetadata)设置给播控中心。播控中心会自动按照进度，在副标题位置刷新显示，应用不需要实现其余功能。

![playback lyric](./figures/playback-lyric.png)

## 媒体音源特殊标识

> **注意：**
>
> 自验证关注点：播放过程中查看播控中心是否显示“AudioVivid”等标识。

应用可以提供当前播放的媒体内容的资源标签信息（[AVMetadata.displayTags](../../../API_Reference/source_zh_cn/apis/AVSessionKit/cj-apis-multimedia_avsession.md#class-avmetadata)）。根据媒体资源的属性，应用可用提供标签信息以体现该媒体内容的特殊性，如：AudioVivid

![playback displayTags](./figures/playback-displayTags.png)

## 播放/暂停

> **注意：**
>
> 自验证关注点：播放过程中，进入播控中心，点击播放暂停查看是否生效，状态是否与应用内对应。

应用需支持播控中心播放暂停，在接收到播控的播放/暂停回调，或者用户在应用内播放暂停，需上报当前的播放状态与进度。

![playback play pause](./figures/playback-play-pause.png)

## 上下一首/集

> **注意：**
>
> 自验证关注点：播放过程中，进入播控中心，点击上一首、下一首查看是否生效，播放内容是否与应用内对应。

应用按照内部实现，接入上下一首/集，在接收到播控的上下一首/集回调，或者用户在应用切歌切集时，需上报切换后新的媒体信息，播放状态、进度。

![playback previous next](./figures/playback-previous-next.png)

## 按钮置灰

> **注意：**
>
> 自验证关注点：播放过程中，进入播控中心，查看不支持的功能按钮是否已置灰。请按照自检表按应用类型接入必需的控制指令，以保障用户的体验。

![playback grey button](./figures/playback-grey-button.png)

应用按照内部实现，按需注册支持的播放控制指令。对于未注册的播放控制指令，在播控中心会显示为上图置灰样式，明确告知用户当前指令该应用不支持。具体实现可参考[应用接入AVSession-不支持命令的处理](./cj-avsession-access-scene.md)。

## 点击播控卡片跳转应用指定页面

> **注意：**
>
> 自验证关注点：播放过程中，进入播控中心，点击封面大图查看是否跳转至应用当前播放页面。

用户通过点击播控卡片，应跳转到应用的具体业务页，如：音乐/听书/视频的播放详情页，直播间页，新闻阅读播放页，浏览器具体tab页。具体实现可参考[媒体会话提供方-开发步骤](./cj-using-avsession-developer.md#开发步骤)的第3步。

![playback jump](./figures/playback-jump.png)