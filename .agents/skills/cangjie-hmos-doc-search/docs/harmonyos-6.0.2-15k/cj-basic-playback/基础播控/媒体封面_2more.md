## 媒体封面

> **注意：**
>
> 自验证关注点：播放过程中查看播控中心是否显示媒体封面，封面图是否清晰。

应用提供媒体内容的封面图片（[AVMetadata.mediaImage](../../../API_Reference/source_zh_cn/apis/AVSessionKit/cj-apis-multimedia_avsession.md#class-avmetadata)），如音乐专辑封面、视频海报等。如果应用提供的媒体封面比例或分辨率不满足要求，将会被自动缩放、裁切到合适大小。这可能导致封面图片内的信息损失或模糊，体验下降。mediaImage设置PixelMap性能更优。

音乐类媒体内容应提供比例为 1:1 的方形封面图片，建议分辨率为 800px * 800px（如果应用提供的图片分辨率更大，将被压缩到 800px * 800px 显示），最小分辨率是 300px * 300px。

![playback mediaImage music](./figures/playback-mediaImage-music.png)

视频及其他类型的媒体内容除了上述建议分辨率的方形模板外，还支持纵向及横向的矩形封面模板。

纵向矩形模板的宽高比为13:18，如小于此比例，将会被自动缩放、裁切到该比例。

横向矩形模板的宽高比为16:9，如大于此比例，将会被自动缩放、裁切到该比例。

![playback mediaImage other](./figures/playback-mediaImage-other.png)

## 主标题

> **注意：**
>
> 自验证关注点：播放过程中查看播控中心是否显示主标题，显示是否正确。

主标题（[AVMetadata.title](../../../API_Reference/source_zh_cn/apis/AVSessionKit/cj-apis-multimedia_avsession.md#class-avmetadata)）用于显示歌曲名、影片名等内容名称，直播应用也可设置直播间名等，用于向用户展示当前正在播放的媒体内容，建议采用简短的字符串。字符串超长时会从右向左滚动显示。

![playback title](./figures/playback-title.png)