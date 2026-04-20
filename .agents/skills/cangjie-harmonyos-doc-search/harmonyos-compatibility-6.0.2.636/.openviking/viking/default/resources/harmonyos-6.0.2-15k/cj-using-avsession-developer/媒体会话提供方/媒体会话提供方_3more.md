# 媒体会话提供方

音视频应用在实现音视频功能的同时，需要作为媒体会话提供方接入媒体会话，在媒体会话控制方（例如播控中心）中展示媒体相关信息，及响应媒体会话控制方下发的播控命令。

## 基本概念

- 媒体会话元数据（AVMetadata）： 用于描述媒体数据相关属性，包含标识当前媒体的ID（assetId），上一首媒体的ID（previousAssetId），下一首媒体的ID（nextAssetId），标题（title），专辑作者（author），专辑名称（album），词作者（writer），媒体时长（duration）等属性。

- 媒体播放状态（AVPlaybackState）：用于描述媒体播放状态的相关属性，包含当前媒体的播放状态（state）、播放位置（position）、播放倍速（speed）、缓冲时间（bufferedTime）、循环模式（loopMode）、是否收藏（isFavorite）、正在播放的媒体Id（activeItemId）、自定义媒体数据（extras）等属性。

## 接口说明

媒体会话提供方使用的关键接口如下表所示。

| 接口名 | 说明 |
| -------- | -------- |
|  createAVSession(context: CPointer\<Unit>, tag: String, \`type\`: AVSessionType): AVSession|创建会话对象，一个Ability只能存在一个会话，重复创建会失败。 |
| setAVMetadata(data: AVMetadata): Unit|设置媒体会话元数据。 |
| setAVPlaybackState(state: AVPlaybackState): Unit|设置媒体会话播放状态。 |
| setLaunchAbility(ability: WantAgent): Unit|设置一个WantAgent用于拉起会话的Ability。 |
| getController(): AVSessionController|获取当前会话自身控制器。 |
|getOutputDevice(): OutputDeviceInfo|获取播放设备相关信息。 |
| activate(): Unit|激活媒体会话。 |
| deactivate(): Unit|禁用当前会话。 |
| destroy(): Unit|销毁媒体会话。 |
| setAVQueueItems(items: Array\<AVQueueItem>): Unit |设置媒体播放列表。 |
|setAVQueueTitle(title: String): Unit|设置媒体播放列表名称。|
| dispatchSessionEvent(event: String, args: HashMap\<String, ValueType>): Unit|设置会话内自定义事件。 |
| setExtras(extras: HashMap\<String, ValueType>): Unit|设置键值对形式的自定义媒体数据包。|
| getOutputDevice(): OutputDeviceInfo|获取当前输出设备信息。 |

更多API说明请参见[API文档](../../../API_Reference/source_zh_cn/apis/AVSessionKit/cj-apis-multimedia_avsession.md)。