### prop fdSrc

```cangjie
public mut prop fdSrc: AVFileDescriptor
```

**功能：** 媒体文件描述，只允许在**idle**状态下设置。

使用场景：应用中的媒体资源被连续存储在同一个文件中。

支持的视频格式(mp4、mpeg-ts、mkv)。

支持的音频格式(m4a、aac、mp3、ogg、wav、flac、amr)。

**使用示例**：

假设一个连续存储的媒体文件:

视频1(地址偏移:0，字节长度:100)；

视频2(地址偏移:101，字节长度:50)；

视频3(地址偏移:151，字节长度:150)；

1.播放视频1：AVFileDescriptor(资源句柄, offset: 0, length: 100)。

2.播放视频2：AVFileDescriptor(资源句柄, offset: 101, length: 50)。

3.播放视频3：AVFileDescriptor(资源句柄, offset: 151, length: 150)。

假设是一个独立的媒体文件: 请使用src=fd://xx。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**类型：** [AVFileDescriptor](#class-avfiledescriptor)

**读写能力：** 可读写

**起始版本：** 19

### prop height

```cangjie
public prop height: Int32
```

**功能：** 视频高，单位为像素（px），可查询参数。<br/>返回为(0)表示无效值，**prepared**/**playing**/**paused**/**completed**状态下有效。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### prop loop

```cangjie
public mut prop loop: Bool
```

**功能：** 视频循环播放属性，默认'false'，设置为'true'表示循环播放，动态属性。<br/>只允许在**prepared**/**playing**/**paused**/**completed**状态下设置。<br/>直播场景不支持loop设置。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### prop state

```cangjie
public prop state: AVPlayerState
```

**功能：** 音视频播放的状态，全状态有效，可查询参数。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**类型：** [AVPlayerState](#enum-avplayerstate)

**读写能力：** 只读

**起始版本：** 19

### prop surfaceId

```cangjie
public mut prop surfaceId: String
```

**功能：** 视频窗口ID，默认无窗口。

支持在**initialized**状态下设置。

支持在**prepared**/**playing**/**paused**/**completed**/**stopped**状态下重新设置，重新设置时确保已经在**initialized**状态下进行设置，否则重新设置失败，重新设置后视频播放在新的窗口渲染。

使用场景：视频播放的窗口渲染，纯音频播放不用设置。

**使用示例**：通过XComponent创建surfaceId。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### prop url

```cangjie
public mut prop url: String
```

**功能：** 媒体URL，只允许在**idle**状态下设置。

支持的视频格式：mp4、mpeg-ts、mkv。

支持的音频格式：m4a、aac、mp3、ogg、wav、flac、amr。

**支持路径示例：**

1.fd类型播放：`fd://xx`。

2.http网络播放: `http://xx`。

3.https网络播放: `https://xx`。

4.hls网络播放路径：`http://xx`或者`https://xx`。

> **说明：**
>
> - 设置网络播放路径，需声明权限：[ohos.permission.INTERNET](../../../../Dev_Guide/security/AccessToken/cj-permissions-for-all.md#ohospermissioninternet)，相关错误码: [201](../../errorcodes/cj-errorcode-universal.md)。
> - 从API version 11开始不支持webm。
> - 将资源句柄（fd）传递给AVPlayer 实例之后，请不要通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer / AVMetadataExtractor / AVImageGenerator / AVTranscoder。同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致媒体播放器数据获取异常。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**类型：** String

**读写能力：** 可读写

**起始版本：** 19