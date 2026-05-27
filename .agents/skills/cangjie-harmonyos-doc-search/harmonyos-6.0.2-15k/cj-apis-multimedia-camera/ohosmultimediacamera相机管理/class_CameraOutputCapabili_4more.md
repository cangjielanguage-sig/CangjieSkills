## class CameraOutputCapability

```cangjie
public class CameraOutputCapability {
    public let previewProfiles: Array<Profile>
    public let photoProfiles: Array<Profile>
    public let videoProfiles: Array<VideoProfile>
    public let supportedMetadataObjectTypes: Array<MetadataObjectType>
}
```

**功能：** 相机输出能力项。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### let photoProfiles

```cangjie
public let photoProfiles: Array<Profile>
```

**功能：** 支持的拍照配置信息集合。

**类型：** Array\<[Profile](#class-profile)>

**读写能力：** 只读

**起始版本：** 19

### let previewProfiles

```cangjie
public let previewProfiles: Array<Profile>
```

**功能：** 支持的预览配置信息集合。

**类型：** Array\<[Profile](#class-profile)>

**读写能力：** 只读

**起始版本：** 19

### let supportedMetadataObjectTypes

```cangjie
public let supportedMetadataObjectTypes: Array<MetadataObjectType>
```

**功能：** 支持的metadata流类型信息集合。

**类型：** Array\<[MetadataObjectType](#enum-metadataobjecttype)>

**读写能力：** 只读

**起始版本：** 19

### let videoProfiles

```cangjie
public let videoProfiles: Array<VideoProfile>
```

**功能：** 支持的录像配置信息集合。

**类型：** Array\<[VideoProfile](#class-videoprofile)>

**读写能力：** 只读

**起始版本：** 19

## struct CameraStatusInfo

```cangjie
public struct CameraStatusInfo {
    public var camera: CameraDevice
    public var status: CameraStatus
    public init(camera: CameraDevice, status: CameraStatus)
}
```

**功能：** 相机管理器回调返回的接口实例，表示相机状态信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### var camera

```cangjie
public var camera: CameraDevice
```

**功能：** 相机信息。

**类型：** [CameraDevice](#class-cameradevice)

**读写能力：** 可读写

**起始版本：** 19

### var status

```cangjie
public var status: CameraStatus
```

**功能：** 相机状态。

**类型：** [CameraStatus](#enum-camerastatus)

**读写能力：** 可读写

**起始版本：** 19

### init(CameraDevice, CameraStatus)

```cangjie
public init(camera: CameraDevice, status: CameraStatus)
```

**功能：** 创建CameraStatusInfo对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|camera|[CameraDevice](#class-cameradevice)|是|-|相机信息。|
|status|[CameraStatus](#enum-camerastatus)|是|-|相机状态。|

## struct CaptureEndInfo

```cangjie
public struct CaptureEndInfo {
    public var captureId: Int32
    public var frameCount: Int32
}
```

**功能：** 拍照停止信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### var captureId

```cangjie
public var captureId: Int32
```

**功能：** 拍照的ID。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var frameCount

```cangjie
public var frameCount: Int32
```

**功能：** 帧数。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

## struct CaptureStartInfo

```cangjie
public struct CaptureStartInfo {
    public var captureId: Int32
    public var time: UInt32
}
```

**功能：** 拍照开始信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### var captureId

```cangjie
public var captureId: Int32
```

**功能：** 拍照的ID。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var time

```cangjie
public var time: UInt32
```

**功能：** 预估的单次拍照底层出sensor采集帧时间。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19