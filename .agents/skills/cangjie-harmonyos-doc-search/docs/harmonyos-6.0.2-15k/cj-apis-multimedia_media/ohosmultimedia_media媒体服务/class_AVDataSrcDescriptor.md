## class AVDataSrcDescriptor

```cangjie
public class AVDataSrcDescriptor {
    public AVDataSrcDescriptor(
        public var fileSize: Int64,
        public var callback: Callback3ArgumentWithReturn<Array<UInt8>, UInt32, Int64, Int32>
    )
}
```

**功能：** 音视频文件资源描述，用于DataSource播放方式。使用场景：应用在未获取完整音视频资源时，允许用户创建播放实例并开始播放，达到提前播放的目的。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

### var callback

```cangjie
public var callback: Callback3ArgumentWithReturn<Array<UInt8>, UInt32, Int64, Int32>
```

**功能：** 用户设置的回调函数，用于填写数据。

**类型：** [Callback3ArgumentWithReturn](../BasicServicesKit/cj-apis-base.md#class-callback3argumentwithreturn)\<Array\<UInt8>, UInt32, Int64, Int32>

**读写能力：** 可读写

**起始版本：** 19

### var fileSize

```cangjie
public var fileSize: Int64
```

**功能：** 待播放文件大小（字节），-1代表大小未知。如果fileSize设置为-1, 播放模式类似于直播，不能进行seek及setSpeed操作，不能设置loop属性，因此不能重新播放。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### AVDataSrcDescriptor(Int64, Callback3ArgumentWithReturn\<Array\<UInt8>, UInt32, Int64, Int32>)

```cangjie
public AVDataSrcDescriptor(
    public var fileSize: Int64,
    public var callback: Callback3ArgumentWithReturn<Array<UInt8>, UInt32, Int64, Int32>
)
```

**功能：** 创建AVDataSrcDescriptor对象。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fileSize|Int64|是|-|待播放文件大小（字节），-1代表大小未知。如果fileSize设置为-1, 播放模式类似于直播，不能进行seek及setSpeed操作，不能设置loop属性，因此不能重新播放。|
|callback|[Callback3ArgumentWithReturn](../BasicServicesKit/cj-apis-base.md#class-callback3argumentwithreturn)\<Array\<UInt8>, UInt32, Int64, Int32>|是|-|用户设置的回调函数，用于填写数据。|