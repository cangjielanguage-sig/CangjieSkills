## class AVTranscoder

```cangjie
public class AVTranscoder {}
```

**功能：** 视频转码管理类，用于视频转码。在调用AVTranscoder的方法前，需要先通过[createAVTranscoder()](#func-createavtranscoder)创建一个AVTranscoder实例。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

### prop fdSrc

```cangjie
public mut prop fdSrc: AVFileDescriptor
```

**功能：** 源媒体文件描述，通过该属性设置数据源，必须在调用[prepare()](#func-prepare)方法前设置。

> **说明：**
>
> - 假设一个连续存储的媒体文件，地址偏移:0，字节长度:100。其文件描述为AVFileDescriptor{ fd = 资源句柄; offset = 0; length = 100; }。
> - 将资源句柄（fd）传递给AVTranscoder实例之后，请不要通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer/AVMetadataExtractor/AVImageGenerator/AVTranscoder。同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致视频转码数据获取异常。

**类型：** [AVFileDescriptor](#class-avfiledescriptor)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400101|No memory.|
  |5400102|Operation not allowed.|

### prop fdDst

```cangjie
public mut prop fdDst: Int32
```

**功能：** 目标媒体文件描述，通过该属性设置数据输出，必须在调用[prepare()](#func-prepare)方法前设置。

> **说明：**
>
> - 创建AVTranscoder实例后，必须设置fdSrc和fdDst属性。
> - 将资源句柄（fd）传递给AVTranscoder实例之后，请不要通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer/AVMetadataExtractor/AVImageGenerator/AVTranscoder。同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致视频转码数据获取异常。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400101|No memory.|
  |5400102|Operation not allowed.|