# 使用AVPlayer添加视频外挂字幕

当前仅支持视频播放前设置外挂字幕。

在进行应用开发的过程中，开发者可以通过AVPlayer的实例注册[on('subtitleUpdate')](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#func-onavplayercallbacktype-callback1argumentsubtitleinfo)方法监听字幕信息。

## 开发步骤及注意事项

详细的API说明请参见[AVPlayer](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#class-avplayer)。

1. 使用视频播放的AVPlayer实例设置外挂字幕资源。

    ```cangjie
    // 可以通过MainAbility获取AbilityContext实例, 参考完整示例部分
    var fileDescriptor = context.resourceManager.getRawFd("xxx.srt")

    avPlayer.addSubtitleFromFd(fileDescriptor.fd, offset: fileDescriptor.offset, length: fileDescriptor.length)

    // 或者使用addSubtitleFromUrl接口
    var fdUrl: String = "http://xxx.xxx.xxx.xxx:xx/xx/index.srt"
    avPlayer.addSubtitleFromUrl(fdUrl)
    ```

2. 使用视频播放的AVPlayer实例注册字幕回调函数。

    ```cangjie
    // 注册字幕回调函数，实现可参考完整示例
    avPlayer.on(AVPlayerCallbackType.subtitleUpdate, SubtitleUpdateCallback())
    ```

3. （可选）当需要不显示字幕时，使用视频播放的AVPlayer实例注销字幕回调函数。

    ```cangjie
    avPlayer.off(AVPlayerCallbackType.subtitleUpdate)
    ```