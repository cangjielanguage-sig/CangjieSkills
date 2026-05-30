public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        AppLog.info("MainAbility onWindowStageCreate.")
        windowStage.loadContent("EntryView")
        // declared in index.cj
        ctx = this.context
    }
}
```

**情况五：通过应用沙箱中的m3u8文件播放在线流媒体资源**

当应用需要通过解析应用沙箱中的的m3u8文件，播放在线流媒体资源时，可以通过[fs.open](../../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_fs.md#static-func-openstring-int64)获取文件句柄，将其拼接成fdUrl。

```cangjie
    import kit.CoreFileKit.*
    import kit.MediaKit.*

    //可以通过MainAbility获取AbilityContext实例, 参考情况四的示例
    var context = None<UIAbilityContext>
    // 创建avPlayer实例对象
    var avPlayer: AVPlayer = createAVPlayer()

    var mgr = context.getOrThrow().resourceManager
    // 设置本地m3u8文件名
    var m3u8FileName: String = "xxx.m3u8"
    // 设置本地m3u8沙箱路径
    var filePath = "/data/storage/el1/bundle/${m3u8FileName}"

    // 通过fs.openSync获取文件句柄
    var file = FileFs.open(filePath, mode: READ_ONLY.mode)
    var fd: String = file.fd.toString()
    // 用文件句柄构造本地m3u8的URL
    var fdUrl: String = "fd://" + fd + "?offset=" + "0" + "&size=" + "0"

    // 按需设置HTTP请求头
    var headers: HashMap<String,String> = HashMap<String, String>([("User-Agent", "User-Agent-Value"), ("Cookie", "Cookie-Value")])
    // 通过本地m3u8的URL和HTTP请求头构造mediaSource媒体来源
    var mediaSource: MediaSource = createMediaSourceWithUrl(fdUrl, headers: headers)

    // 设置播放策略，设置缓冲区数据量为20s
    var playbackStrategy: PlaybackStrategy = PlaybackStrategy(preferredBufferDuration: 20)
    // 为avPlayer设置媒体来源和播放策略
    avPlayer.setMediaSource(mediaSource, strategy: playbackStrategy)
  ```