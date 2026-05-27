## class AVFileDescriptor

```cangjie
public class AVFileDescriptor {
    public AVFileDescriptor(
        public var fd: Int32,
        public var offset: ?Int64,
        public var length: ?Int64
    )
    public init(fd: Int32)
}
```

**功能：** 音视频文件资源描述，一种特殊资源的播放方式，使用场景：应用中的音频资源被连续存储在同一个文件中，需要根据偏移量和长度进行播放。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### var fd

```cangjie
public var fd: Int32
```

**功能：** 资源句柄。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var length

```cangjie
public var length: ?Int64
```

**功能：** 资源长度，默认值为文件中从偏移量开始的剩余字节，需要基于预置资源的信息输入，非法值会造成音视频资源解析错误。

**类型：** ?Int64

**读写能力：** 可读写

**起始版本：** 19

### var offset

```cangjie
public var offset: ?Int64
```

**功能：** 资源偏移量，默认值为0，需要基于预置资源的信息输入，非法值会造成音视频资源解析错误。

**类型：** ?Int64

**读写能力：** 可读写

**起始版本：** 19

### AVFileDescriptor(Int32, ?Int64, ?Int64)

```cangjie
public AVFileDescriptor(
    public var fd: Int32,
    public var offset: ?Int64,
    public var length: ?Int64
)
```

**功能：** 构造音视频文件资源描述类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|资源句柄，通过[resourceManager.getRawFd](../LocalizationKit/cj-apis-resource_manager.md#func-getrawfdstring)获取。|
|offset|?Int64|是|-|资源偏移量，需要基于预置资源的信息输入，非法值会造成字幕频资源解析错误。|
|length|?Int64|是|-|资源长度，默认值为文件中从偏移量开始的剩余字节，需要基于预置资源的信息输入，非法值会造成字幕频资源解析错误。|

### init(Int32)

```cangjie
public init(fd: Int32)
```

**功能：** 构造音视频文件资源描述类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|资源句柄，通过[resourceManager.getRawFd](../LocalizationKit/cj-apis-resource_manager.md#func-getrawfdstring)获取。|