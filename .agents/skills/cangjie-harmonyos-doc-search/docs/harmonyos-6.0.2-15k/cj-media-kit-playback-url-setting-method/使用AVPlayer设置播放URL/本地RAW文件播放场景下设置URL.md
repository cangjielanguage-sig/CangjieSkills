## 本地RAW文件播放场景下设置URL

**情况一：应用沙箱文件播放**

```cangjie
    // 创建avPlayer实例对象
    var avPlayer: AVPlayer = createAVPlayer()
    var fdPath = "fd://"
    // 通过AbilityContext获取沙箱地址filesDir, 可以通过MainAbility获取AbilityContext实例，此处假设已经获取到context
    var pathDir = context.filesDirectory
    var path = "/data/storage/el1/bundle/01.mp3"
    // 打开相应的资源文件地址获取fd，并为url赋值触发initialized状态机上报
    var file = FileFs.open(path)
    fdPath = fdPath + "" + file.fd
    avPlayer.url = fdPath
  ```

**情况二：本地文件播放**

```cangjie
    // 创建avPlayer实例对象
    var avPlayer: AVPlayer = createAVPlayer()
    // 通过AbilityContext的resourceManager成员的getRawFd接口获取媒体资源播放地址，可以通过MainAbility获取AbilityContext实例，此处假设已经获取到context
    var fileDescriptor = ctx.getOrThrow().resourceManager.getRawFd("01.mp3")
    // 返回类型为AVFileDescriptor, fd为HAP包fd地址，offset为媒体资源偏移量，length为播放长度
    var avFileDescriptor: AVFileDescriptor =
      AVFileDescriptor(fileDescriptor.fd, fileDescriptor.offset, fileDescriptor.length)
    // 为fdSrc赋值触发initialized状态机上报
    avPlayer.fdSrc = avFileDescriptor
  ```