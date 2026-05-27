### class VideoController

```cangjie
public class VideoController {
    public init()
}
```

**功能：** VideoController对象可以控制一个或多个video，可用视频播放实例请参考[ohos.multimedia_media](../apis/MediaKit/cj-apis-multimedia_media.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init()

```cangjie
public init()
```

**功能：** 创建一个 VideoController 对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func start()

```cangjie
public func start(): Unit
```

**功能：** 开始播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func pause()

```cangjie
public func pause(): Unit
```

**功能：** 暂停播放，显示当前帧，再次播放时从当前位置继续播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func stop()

```cangjie
public func stop(): Unit
```

**功能：** 停止播放，显示当前帧，再次播放时从头开始播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func reset()

```cangjie
public func reset(): Unit
```

**功能：** 显示当前帧，再次播放时从头开始播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### func setCurrentTime(Int32, SeekMode)

```cangjie
public func setCurrentTime(time: Int32, seekMode: SeekMode): Unit
```

**功能：** 指定视频播放的进度位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|time|Int32|是|-|视频播放进度位置。<br>单位：s。|
|seekMode|[SeekMode](#enum-seekmode)|是|-|跳转模式。|

#### func exitFullscreen()

```cangjie
public func exitFullscreen(): Unit
```

**功能：** 退出全屏播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func requestFullscreen(Bool)

```cangjie
public func requestFullscreen(fullScreen: Bool): Unit
```

**功能：** 请求全屏播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fullScreen|Bool|是|-|是否全屏（填充满应用窗口）播放。|