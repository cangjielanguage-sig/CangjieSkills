## 流媒体播放场景下设置URL

**情况一：播放HTTP/HTTPS媒体资源**

```cangjie
    // 创建avPlayer实例对象
    var avPlayer: AVPlayer = createAVPlayer()
    // 设置对应的播放url
    avPlayer.url = "https://xxx.xxx.xxx.mp4"
  ```

**情况二：HLS媒体资源播放(点播/直播)**

```cangjie
    // 创建avPlayer实例对象
    var avPlayer: AVPlayer = createAVPlayer()
    // 设置对应的播放url
    avPlayer.url = "https://xxx.xxx.xxx.xxx:xx/xx/index.m3u8"
  ```

**情况三：设置HTTP请求头信息播放**

当服务器需要校验HTTP请求头信息时，可通过[createMediaSourceWithUrl](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#func-createmediasourcewithurlstring-hashmapstringstring)设置HTTP请求头信息。

```cangjie
    // 创建avPlayer实例对象
    var avPlayer: AVPlayer = createAVPlayer()
    // 创建mediaSource实例对象，设置媒体来源，定制HTTP请求，如需要，可以键值对的形式设置User-Agent、Cookie、Referer等字段
    var mediaSource: MediaSource = createMediaSourceWithUrl("https://xxx.xxx.xxx.xxx:xx/xx/index.m3u8",  HashMap<String, String>([("User-Agent", "User-Agent-Value"), ("Cookie", "Cookie-Value"), ("Referer", "Referer-Value")]))
    // 设置播放策略，设置缓冲区数据量为20s
    var playbackStrategy: PlaybackStrategy = PlaybackStrategy(preferredBufferDuration: 20)
    // 为avPlayer设置媒体来源和播放策略
    avPlayer.setMediaSource(mediaSource, playbackStrategy)
  ```

**情况四：通过本地RAW文件中的m3u8文件播放在线流媒体资源**

当应用需要通过解析本地RAW文件中的m3u8文件，播放在线流媒体资源时，可以通过[resourceManager.getRawFd](../../../API_Reference/source_zh_cn/apis/LocalizationKit/cj-apis-resource_manager.md#func-getrawfdstring)获取文件描述符，将其拼接成url的形式。

```cangjie
    import kit.CoreFileKit.*
    import kit.MediaKit.*

    //此处先初始化context，可以通过MainAbility获取AbilityContext, 示例代码见下方
    var ctx = None<UIAbilityContext>
    // 创建avPlayer实例对象
    var avPlayer: AVPlayer = createAVPlayer()
    // 获取context实例
    var mgr = ctx.getOrThrow().resourceManager
    // 设置本地m3u8文件名
    var m3u8FileName: String = "xxx.m3u8"
    // 通过本地m3u8文件名，获取文件描述符
    var fileDescriptor = mgr.getRawFd(m3u8FileName)

    // 用文件描述符构造本地m3u8的URL
    var fd: String = fileDescriptor.fd.toString()
    var offset: String = fileDescriptor.offset.toString()
    var length: String = fileDescriptor.length.toString()
    var fdUrl: String = "fd://" + fd + "?offset=" + offset + "&size=" + length

    // 按需设置HTTP请求头
    var headers: HashMap<String, String> = HashMap<String, String>([("User-Agent", "User-Agent-Value"), ("Cookie", "Cookie-Value")])
    // 通过本地m3u8的URL和HTTP请求头构造mediaSource媒体来源
    var mediaSource: MediaSource = createMediaSourceWithUrl(fdUrl, headers: headers)

    // 设置播放策略，设置缓冲区数据量为20s
    var playbackStrategy: PlaybackStrategy = PlaybackStrategy(preferredBufferDuration: 20)
    // 为avPlayer设置媒体来源和播放策略
    avPlayer.setMediaSource(mediaSource, strategy:playbackStrategy)
  ```

获取AbilityContext的示例代码如下：

```cangjie
// main_ability.cj
import kit.AbilityKit.{LaunchReason, LaunchParam, Want, UIAbility}
import kit.ArkUI.WindowStage
import kit.UIKit.AppLog

class MainAbility <: UIAbility {
    public init() {
        super()
        registerSelf()
    }

    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility OnCreated.${want.abilityName}")
        match (launchParam.launchReason) {
            case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
            case _ => ()
        }
    }